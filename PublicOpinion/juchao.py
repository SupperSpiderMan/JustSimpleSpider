import json
import logging
import math
import pprint
import time

import pymysql
import requests as req

from PublicOpinion.configs import MYSQL_HOST, MYSQL_PORT, MYSQL_USER, MYSQL_PASSWORD, MYSQL_DB, LOCAL_MYSQL_DB, \
    LOCAL_MYSQL_HOST, LOCAL_MYSQL_USER, LOCAL_MYSQL_PORT, LOCAL_MYSQL_PASSWORD, LOCAL
from PublicOpinion.sql_pool import PyMysqlPoolBase

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


class JuChaoInfo(object):
    def __init__(self):
        self.zuixin_url = "http://webapi.cninfo.com.cn//api/sysapi/p_sysapi1128"
        self.stock_url = "http://webapi.cninfo.com.cn//api/sysapi/p_sysapi1078"
        self.fund_url = "http://webapi.cninfo.com.cn//api/sysapi/p_sysapi1126"
        self.datas_url = "http://webapi.cninfo.com.cn//api/sysapi/p_sysapi1127"

        self.mcode = self._generate_mcode()
        self.headers = {
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
            'Cache-Control': 'no-cache',
            'Connection': 'keep-alive',
            'Content-Length': '0',
            'Cookie': '__qc_wId=726; pgv_pvid=6020356972; Hm_lvt_489bd07e99fbfc5f12cbb4145adb0a9b=1581945588; codeKey=ce7a9a719b; Hm_lpvt_489bd07e99fbfc5f12cbb4145adb0a9b=1582016401',
            'Host': 'webapi.cninfo.com.cn',
            'mcode': '{}'.format(self.mcode),
            'Origin': 'http://webapi.cninfo.com.cn',
            'Pragma': 'no-cache',
            'Referer': 'http://webapi.cninfo.com.cn/',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest',

        }
        self.local = LOCAL
        if self.local:
            conf = {
                "host": LOCAL_MYSQL_HOST,
                "port": LOCAL_MYSQL_PORT,
                "user": LOCAL_MYSQL_USER,
                "password": LOCAL_MYSQL_PASSWORD,
                "db": LOCAL_MYSQL_DB,

            }
            self.db = LOCAL_MYSQL_DB
        else:
            conf = {
                "host": MYSQL_HOST,
                "port": MYSQL_PORT,
                "user": MYSQL_USER,
                "password": MYSQL_PASSWORD,
                "db": MYSQL_DB,
            }
            self.db = MYSQL_DB
        self.sql_pool = PyMysqlPoolBase(**conf)
        self.table = "juchao_info"
        self.error_detail = []

    def _generate_mcode(self):
        dt = str(math.floor(time.time()))
        keyStr = "ABCDEFGHIJKLMNOP" + "QRSTUVWXYZabcdef" + "ghijklmnopqrstuv" + "wxyz0123456789+/" + "="
        output = ""
        i = 0
        while i < len(dt):
            try:
                chr1 = ord(dt[i])
            except IndexError:
                chr1 = 0
            i += 1

            try:
                chr2 = ord(dt[i])
            except IndexError:
                chr2 = 0
            i += 1

            try:
                chr3 = ord(dt[i])
            except:
                chr3 = 0
            i += 1

            enc1 = chr1 >> 2
            enc2 = ((chr1 & 3) << 4) | (chr2 >> 4)
            enc3 = ((chr2 & 15) << 2) | (chr3 >> 6)
            enc4 = chr3 & 63
            if not chr2:
                enc3 = enc4 = 64
            elif not chr3:
                enc4 = 64
            output = output + keyStr[enc1] + keyStr[enc2] + keyStr[enc3] + keyStr[enc4]
        return output

    def _get(self, url):
        resp = req.post(url, headers=self.headers)
        # print(resp)
        if resp.status_code == 200:
            return resp.text

    def _contract_sql(self, to_insert):
        ks = []
        vs = []
        for k in to_insert:
            ks.append(k)
            vs.append(to_insert.get(k))
        fields_str = "(" + ",".join(ks) + ")"
        values_str = "(" + "%s," * (len(vs) - 1) + "%s" + ")"
        base_sql = '''INSERT INTO `{}`.`{}` '''.format(
            self.db, self.table) + fields_str + ''' values ''' + values_str + ''';'''
        return base_sql, tuple(vs)

    def _save(self, to_insert):
        try:
            insert_sql, values = self._contract_sql(to_insert)
            count = self.sql_pool.insert(insert_sql, values)
        except pymysql.err.IntegrityError:
            logger.info("重复 {}".format(to_insert))
            return 1
        except:
            logger.warning("失败")
        else:
            logger.info("保存成功 {}".format(to_insert))
            return count

    def get_list(self, url):
        body = self._get(url)
        # print(body)
        py_data = json.loads(body)
        result_code = py_data.get("resultcode")
        if result_code == 200:
            records = py_data.get("records")   # list
            for record in records:
                yield record

    def __del__(self):
        try:
            self.sql_pool.dispose()
        except:
            pass

    def _create_table(self):
        sql = '''
         CREATE TABLE IF NOT EXISTS `juchao_info` (
          `id` int(11) NOT NULL AUTO_INCREMENT,
          `code` varchar(8) NOT NULL COMMENT '证券代码',
          `pub_date` datetime NOT NULL COMMENT '发布时间',
          `title` varchar(128) CHARACTER SET utf8 COLLATE utf8_bin DEFAULT NULL COMMENT '资讯标题',
          `category` varchar(64) CHARACTER SET utf8 COLLATE utf8_bin DEFAULT NULL COMMENT '资讯类别',
          `summary` text CHARACTER SET utf8 COLLATE utf8_bin COMMENT '资讯摘要',
          `CREATETIMEJZ` datetime DEFAULT CURRENT_TIMESTAMP,
          `UPDATETIMEJZ` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
          PRIMARY KEY (`id`),
          UNIQUE KEY `code_title` (`code`,`title`),
          KEY `pub_date` (`pub_date`),
          KEY `update_time` (`UPDATETIMEJZ`)
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='巨潮AI资讯'; 
        '''
        self.sql_pool.insert(sql)
        self.sql_pool.end()

    def start(self):
        self._create_table()

        zuixin_records = self.get_list(self.zuixin_url)
        self.process_records(zuixin_records, 1128)

        stock_records = self.get_list(self.stock_url)
        self.process_records(stock_records, 1078)

        fund_records = self.get_list(self.fund_url)
        self.process_records(fund_records, 1126)

        datas_records = self.get_list(self.datas_url)
        self.process_records(datas_records, 1127)

    def process_records(self, records, type_code):
        num = 0
        for record in records:
            item = dict()
            pub_date = record.get("DECLAREDATE")
            if not pub_date:
                pub_date = record.get("RECTIME")
            item['pub_date'] = pub_date  # 发布时间
            item['code'] = record.get("SECCODE")  # 证券代码
            item['title'] = record.get("F001V")  # 资讯标题
            item['category'] = record.get("F003V")   # 资讯类别
            item['summary'] = record.get("F002V")   # 资讯摘要
            # item['pdf_link'] = record.get("F004V")    # pdf 链接
            # code = record.get("SECCODE")    # 文章编号
            # link = "http://webapi.cninfo.com.cn/#/aidetail?type=sysapi/p_sysapi{}&scode={}".format(type_code, code)
            # item['link'] = link
            count = self._save(item)
            self.sql_pool.connection.commit()
            if not count:
                self.error_detail.append(item)
            num += 1
            if num >= 10:
                # print("commit")
                num = 0
                self.sql_pool.connection.commit()


if __name__ == "__main__":
    runner = JuChaoInfo()
    runner.start()
