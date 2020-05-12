"""post 公告接口"""
import datetime
from urllib.parse import urljoin

import requests
from lxml import html


class MarginBroadcast(object):
    def __init__(self):
        self.sh_url = 'http://www.sse.com.cn/disclosure/magin/announcement/s_index.htm'
        self.sh_base_url = 'http://www.sse.com.cn/disclosure/magin/announcement/s_index_{}.htm'
        self.dt_format = "%Y-%m-%d"

    def start(self):
        for page in range(1, 23):
            if page == 1:
                url = self.sh_url
            else:
                url = self.sh_base_url.format(page)
            self.post_sh(url)

    def post_sh(self, url):
        resp = requests.post(url)
        if resp.status_code == 200:
            body = resp.text
            body = body.encode("ISO-8859-1").decode("utf-8")
            doc = html.fromstring(body)
            '''
            <dd>
                 <span>2020-04-30</span>
                 <a href="/disclosure/magin/announcement/ssereport/c/c_20200430_5085195.shtml" title="关于融资融券标的证券调整的公告" target="_blank">关于融资融券标的证券调整的公告 </a>
            </dd>
            '''
            broadcasts = doc.xpath(".//div[@class='sse_list_1 js_createPage']/dl/dd")
            for b in broadcasts:
                item = dict()
                show_dt_str = b.xpath("./span")[0].text_content()
                show_dt = datetime.datetime.strptime(show_dt_str, self.dt_format)
                href = b.xpath("./a/@href")[0]
                # http://www.sse.com.cn/   disclosure/magin/announcement/ssereport/c/c_20200430_5085195.shtml
                href = urljoin("http://www.sse.com.cn/", href)
                ret = self.parse_sh_detail(href)
                content = ret.get("content")
                keyword = ret.get("keyword")
                item['time'] = show_dt
                item['link'] = href
                item['content'] = content
                item['keyword'] = keyword
                print(item)

    def parse_sh_detail(self, url):
        """
        eg. http://www.sse.com.cn/disclosure/magin/announcement/ssereport/c/c_20200430_5085195.shtml
        :param url:
        :return:
        """
        resp = requests.get(url)
        if resp.status_code == 200:
            body = resp.text
            body = body.encode("ISO-8859-1").decode("utf-8")

            # print(body)

            # 文章正文
            '''
            <div class="allZoom">  
                <p style="text-align: center;">上证公告（交易）〔2020〕007号</p>
                <p>　　2020年5月6日，美都能源（600175）、六国化工（600470）、飞乐音响（600651）、安信信托（600816）和宜华生活（600978）被实施退市风险警示。根据《上海证券交易所融资融券交易实施细则》第三十一条规定，本所于2020年5月6日起将以上证券调出融资融券标的证券名单。</p>
                <p>　　特此公告。<br />&nbsp;</p>
                <p>　　上海证券交易所</p>
                <p>　　2020年4月30日</p>
            </div> 
            '''
            doc = html.fromstring(body)
            content = doc.xpath("//div[@class='allZoom']")[0].text_content()

            # 提取本篇的关键词
            '''
            <p style="display:none">
                <fjtignoreurl>
                    <span  id="searchTitle">
                        关于融资融券标的证券调整的公告
                    </span>
                    <span  id="keywords">
                            600978,
                            600816,
                            600651,
                            600470,
                            600175,
                            融资融券标的证券调整,
                    </span>
                </fjtignoreurl>
            </p>
            '''
            key_words = doc.xpath("//span[@id='keywords']")[0].text_content().split()
            words = []
            for word in key_words:
                word = word.strip(",")
                words.append(word)
            words_str = ','.join(words)
            return {"content": content, "keyword": words_str}


if __name__ == "__main__":
    m = MarginBroadcast()
    m.start()