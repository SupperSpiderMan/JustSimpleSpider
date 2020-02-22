# -*- coding: utf-8 -*-

import pymysql

from .configs import DC_HOST, DC_PORT, DC_USER, DC_PASSWD, DC_DB, MYSQL_HOST, MYSQL_PORT, MYSQL_USER, MYSQL_DB, \
    MYSQL_PASSWORD, LOCAL_MYSQL_HOST, LOCAL_MYSQL_PORT, LOCAL_MYSQL_USER, LOCAL_MYSQL_PASSWORD, LOCAL_MYSQL_DB


def select_link_404():
    try:
        conn = pymysql.connect(host=MYSQL_HOST, port=MYSQL_PORT, user=MYSQL_USER,
                               passwd=MYSQL_PASSWORD, db=MYSQL_DB)
        # conn = pymysql.connect(host=LOCAL_MYSQL_HOST, port=LOCAL_MYSQL_PORT, user=LOCAL_MYSQL_USER,
        #                        passwd=LOCAL_MYSQL_PASSWORD, db=LOCAL_MYSQL_DB)
    except Exception as e:
        raise

    cur = conn.cursor()
    cur.execute(f"select id, link  from eastmoney_carticle where article is NULL;")
    ret = cur.fetchall()
    # print(ret)
    # print(type(ret))
    # print(len(ret))
    '''
    ((157713, 'http://caifuhao.eastmoney.com/news/20180412124813481311540'),
     (167885, 'http://caifuhao.eastmoney.com/news/20180404183514351416660'),
     (170371, 'http://caifuhao.eastmoney.com/news/20191209182152396012550'),
    '''
    return ret



# def main():
#     # keys = sorted(dc_info().values())
#     # print(keys)
#
#     ret = select_link_404()
#     for (id, link) in ret:
#         if link_test(link):
#             delete_link_404()


main()

# ['GQY视讯',
# 'TCL科技',
# 'TCL通讯',
# '一品红',
# '一心堂',
# '一拖股份',
# '一汽富维',
# '一汽轿车',
# '七一二', '七匹狼', '七彩化学', '万业企业', '万东医疗', '万丰奥威', '万兴科技', '万华化学', '万向德农', '万向钱潮', '万和电气', '万孚生物', '万安科技', '万德斯', '万方发展', '万林股份', '万泽股份', '万润科技', '万润股份', '万盛股份', '万科', '万讯自控', '万达信息', '万达电影', '万通地产', '万通智控', '万邦德', '万邦达', '万里扬', '万里石', '万里股份', '万里马', '万隆光电', '万集科技', '万顺新材', '万马科技', '万马股份', '三一重工', '三七互娱', '三丰智能', '三五互联', '三元股份', '三全食品', '三六五网', '三六零', '三利谱', '三力士', '三友化工', '三变科技', '三只松鼠', '三圣股份', '三夫户外', '三孚股份', '三安光电', '三峡新材', '三峡水利', '三峡油漆', '三川智慧', '三德科技', '三房巷', '三星医疗', '三星新材', '三晖电气', '三木集团', '三棵树', '三江购物', '三泰控股', '三湘印象', '三特索道', '三环股份', '三盛教育', '三祥新材', '三维工程', '三维橡胶', '三维通信', '三美股份', '三联虹普', '三聚环保', '三花智控', '三角轮胎', '三角防务', '三诺生物', '三超新材', '三达膜', '三鑫医疗', '三钢闽光', '三雄极光', '上实医药', '上实发展', '上峰水泥', '上工申贝', '上机数控', '上柴股份', '上汽集团', '上海三毛', '上海临港', '上海九百', '上海亚虹', '上海凤凰', '上海凯宝', '上海医药', '上海天洋', '上海家化', '上海建工', '上海新阳', '上海机场', '上海机电', '上海梅林', '上海沪工', '上海洗霸', '上海瀚讯', '上海爱旭', '上海物贸', '上海电力', '上海电影', '上海电气', '上海石化', '上海科技', '上海能源', '上海航空', '上海莱士', '上海贝岭', '上海钢联', '上海银行', '上海雅仕', '上港集团', '上港集箱', '上电股份', '世名科技', '世嘉科技', '世纪华通', '世纪天鸿', '世纪星源', '世纪瑞尔', '世纪鼎利', '世联行', '世茂股份', '世荣兆业', '世运电路', '世龙实业', '东信和平', '东兴证券', '东凌国际', '东北制药', '东北电气', '东北证券', '东北高速', '东华测试', '东华科技', '东华能源', '东华软件', '东南网架', '东吴证券', '东土科技', '东安动力', '东宏股份', '东宝生物', '东富龙', '东尼电子', '东山精密', '东方中科', '东方创业', '东方嘉盛', '东方园林', '东方国信', '东方日升', '东方时尚', '东方明珠', '东方材料', '东方海洋', '东方环宇', '东方生物', '东方电子', '东方电气', '东方电热', '东方电缆', '东方盛虹', '东方精工', '东方网力', '东方网络', '东方能源', '东方航空', '东方证券', '东方财富', '东方通', '东方通信', '东方金钰', '东方钽业', '东方铁塔', '东方银星', '东方锅炉', '东方锆业', '东方集团', '东方雨虹', '东旭光电', '东旭蓝天', '东易日盛', '东晶电子', '东材科技', '东杰智能', '东江环保', '东港股份', '东湖高新', '东珠生态', '东百集团', '东睦股份', '东莞控股', '东诚药业', '东软载波', '东软集团', '东阳光科', '东阿阿胶', '东音股份', '东风汽车', '东风科技', '东风股份', '丝路视觉', '两面针', '中亚股份', '中交地产', '中京电子', '中体产业', '中信出版', '中信国安', '中信建投', '中信海直', '中信特钢', '中信证券', '中信重工', '中信银行', '中储股份', '中元股份', '中光学', '中光防雷', '中公教育', '中公高科', '中关村', '中兴商业', '中兴通讯', '中兵红箭', '中再资环', '中农立华', '中创物流', '中创环保', '中利集团', '中化国际', '中化岩土', '中华企业', '中南传媒', '中南建设', '中南文化', '中原传媒', '中原内配', '中原油气', '中原环保', '中原证券', '中原高速', '中嘉博创', '中国一重', '中国中冶', '中国中期', '中国中车', '中国中铁', '中国交建', '中国人保', '中国人寿', '中国出版', '中国动力', '中国化学', '中国北车', '中国医药', '中国卫星', '中国卫通', '中国国旅', '中国国航', '中国国贸', '中国外运', '中国天楹', '中国太保', '中国宝安', '中国巨石', '中国平安', '中国广核', '中国应急', '中国建筑', '中国核建', '中国核电', '中国武夷', '中国汽研', '中国海诚', '中国海防', '中国电建', '中国电影', '中国电研', '中国石化', '中国石油', '中国神华', '中国科传', '中国联通', '中国船舶', '中国西电', '中国软件', '中国通号', '中国重工', '中国重汽', '中国铁建', '中国铝业', '中国银河', '中国银行', '中国长城', '中国高科', '中坚科技', '中基健康', '中大力德', '中天科技', '中天能源', '中天金融', '中威电子', '中孚信息', '中孚实业', '中安科', '中宠股份', '中密控股', '中富通', '中山公用', '中山金马', '中川国际', '中工国际', '中广天择', '中广核技', '中建环能', '中弘股份', '中微公司', '中恒电气', '中恒集团', '中成股份', '中房股份', '中持股份', '中捷资源', '中文传媒', '中文在线', '中新科技', '中新药业', '中新赛克', '中新集团', '中旗股份', '中昌数据', '中曼石油', '中材国际', '中材科技', '中材节能', '中来股份', '中核苏阀', '中核钛白', '中欣氟材', '中毅达', '中水渔业', '中油工程', '中油资本', '中油龙昌', '中泰化学', '中泰股份', '中洲控股', '中海油服', '中海达', '中润资源', '中源协和', '中源家居', '中潜股份', '中炬高新', '中煤能源', '中牧股份', '中环环保', '中环股份', '中环装备', '中珠医疗', '中电兴发', '中电环保', '中电电机', '中百集团', '中直股份', '中石科技', '中矿资源', '中科三环', '中科云网', '中科信息', '中科创达', '中科新材', '中科曙光', '中科海讯', '中科电气', '中科软', '中科金财', '中简科技', '中粮控股', '中粮科技', '中粮糖业', '中联重科', '中能电气', '中航三鑫', '中航光电', '中航机电', '中航沈飞', '中航电子', '中航电测', '中航资本', '中航重机', '中航飞机', '中航高科', '中船科技', '中船防务', '中色股份', '中葡股份', '中衡设计', '中装建设', '中西药业', '中视传媒', '中设集团', '中超控股', '中路股份', '中远海发', '中远海控', '中远海特', '中远海科', '中远海能', '中迪投资', '中通国脉', '中通客车', '中金岭南', '中金环境', '中金黄金', '中钢国际', '中钢天源', '中钨高新', '中铁工业', '中铝国际', '中银绒业', '中银证券', '中闽能源', '中际旭创', '中集集团', '中青宝', '中青旅', '中顺洁柔', '中颖电子', '中飞股份', '中马传动', '中鼎股份', '丰乐种业', '丰元股份', '丰华股份', '丰原药业', '丰山集团', '丰林集团', '丸美股份', '丹化科技', '丹邦科技', '丽岛新材', '丽江旅游', '丽珠集团', '丽鹏股份', '久之洋', '久其软件', '久吾高科', '久日新材', '久立特材', '久远银海', '久量股份', '乐凯新材', '乐凯胶片', '乐山电力', '乐心医疗', '乐惠国际', '乐普医疗', '乐歌股份', '乐视网', '乐通股份', '乐鑫科技', '乔治白', '九典制药', '九华旅游', '九安医疗', '九州通', '九强生物', '九有股份', '九洲电气', '九洲药业', '九牧王', '九芝堂', '九阳股份', '九鼎新材', '乾景园林', '乾照光电', '二三四五', '二六三', '二局股份', '二重重装', '云内动力', '云南城投', '云南旅游', '云南白药', '云南能投', '云南铜业', '云南锗业', '云图控股', '云大科技', '云天化', '云意电气', '云投生态', '云海金属', '云煤能源', '云维股份', '云赛智联', '云铝股份', '五方光电', '五洋停车', '五洲交通', '五洲新春', '五矿发展', '五矿稀土', '五矿资本', '五粮液', '亚世光电', '亚光股份', '亚厦股份', '亚士创能', '亚太实业', '亚太科技', '亚太股份', '亚太药业', '亚威股份', '亚宝药业', '亚振家居', '亚星化学', '亚星客车', '亚星锚链', '亚普股份', '亚泰国际', '亚泰集团', '亚玛顿', '亚盛集团', '亚翔集成', '亚联发展', '亚通股份', '亚邦股份', '交大昂立', '交建股份', '交控科技', '交运股份', '交通银行', '亨通光电', '京东方', '京华激光', '京城股份', '京天利', '京威股份', '京山轻机', '京投发展', '京新药业', '京汉股份', '京沪高铁', '京泉华', '京粮控股', '京能电力', '京能置业', '京蓝科技', '京运通', '人人乐', '人民同泰', '人民网', '人福医药', '亿利洁能', '亿利达', '亿嘉和', '亿帆医药', '亿晶光电', '亿纬锂能', '亿联网络', '亿通科技', '亿阳信通', '仁东控股', '仁和药业', '仁智股份', '今世缘', '今创集团', '今天国际', '今飞凯达', '仙乐健康', '仙坛股份', '仙琚制药', '仙鹤股份', '仟源医药', '以岭药业', '仰帆控股', '任子行', '伊之密', '伊利股份', '伊力特', '伊戈尔', '众业达', '众信旅游', '众兴菌业', '众合科技', '众和股份', '众应互联', '众泰汽车', '众源新材', '众生药业', '优刻得', '优博讯', '优德精密', '会畅通讯', '会稽山', '伟明环保', '伟星新材', '伟星股份', '伟隆股份', '传化智联', '传艺科技', '传音控股', '伯特利', '佐力药业', '佛塑科技', '佛山照明', '佛慈制药', '佛燃股份', '佩蒂股份', '佰仁医疗', '佳云科技', '佳创视讯', '佳力图', '佳发教育', '佳士科技', '佳沃股份', '佳电股份', '佳禾智能', '佳纸股份', '佳讯飞鸿', '佳通轮胎', '佳都科技', '佳隆股份', '供销大集', '依米康', '依顿电子', '侨源气体', '侨银环保', '保利发展', '保利联合', '保千里', '保变电气', '保税科技', '保隆科技', '保龄宝', '信威集团', '信息发展', '信捷电气', '信立泰', '信维通信', '信达地产', '信邦制药', '信隆健康', '信雅达', '倍加洁', '值得买', '健友股份', '健帆生物', '健康元', '健民集团', '健盛集团', '傲农生物', '元利科技', '元力股份', '元成股份', '元祖股份', '元隆雅图', '兄弟科技', '兆丰股份', '兆新股份', '兆日科技', '兆易创新', '兆驰股份', '先导智能', '先河环保', '先达股份', '先进数通', '先锋新材', '先锋电子', '光一科技', '光力科技', '光华科技', '光启技术', '光大嘉宝', '光大证券', '光大银行', '光威复材', '光峰科技', '光库科技', '光弘科技', '光明乳业', '光明地产', '光正集团', '光洋股份', '光环新网', '光电股份', '光线传媒', '光莆股份', '光迅科技', '光韵达', '克劳斯', '克明面业', '克来机电', '兔宝宝', '兖州煤业', '全信股份', '全志科技', '全新好', '全柴动力', '全筑股份', '全聚德', '全通教育', '八一钢铁', '八亿时空', '八方股份', '八菱科技', '公牛集团', '六国化工', '兰太实业', '兰州民百', '兰州铝业', '兰州黄河', '兰生股份', '兰石重装', '兰花科创', '共达电声', '共进股份', '兴业矿业', '兴业科技', '兴业股份', '兴业证券', '兴业银行', '兴化股份', '兴发集团', '兴图新科', '兴森快捷', '兴民智通', '兴源环境', '兴瑞科技', '兴蓉环境', '兴齐眼药', '养元饮品', '冀东水泥', '冀东装备', '冀中能源', '冀凯股份', '内蒙一机', '内蒙华电', '再升科技', '农业银行', '农产品', '农发种业', '农尚环境', '冠农股份', '冠城大通', '冠昊生物', '冠福股份', '冠豪高新', '冰川网络', '冰轮环境', '准油股份', '凌云股份', '凌钢股份', '凌霄泵业', '凤凰传媒', '凤凰光学', '凤凰股份', '凤形股份', '凤竹纺织', '凯中精密', '凯乐科技', '凯众股份', '凯伦股份', '凯利泰', '凯发电气', '凯恩股份', '凯撒文化', '凯撒股份', '凯文教育', '凯普生物', '凯瑞德', '凯盛科技', '凯美特气', '凯莱英', '凯迪生态', '凯龙股份', '出版传媒', '分众传媒', '刚泰控股', '创业慧康', '创业环保', '创业黑马', '创元科技', '创兴资源', '创力集团', '创意信息', '创新医疗', '创智信息', '创源文化', '创维数字', '初灵信息', '利亚德', '利君股份', '利安隆', '利尔化学', '利德曼', '利欧股份', '利民股份', '利源精制', '利群股份', '利通电子', '剑桥科技', '力合科技', '力帆股份', '力星股份', '力源信息', '力生制药', '力盛赛车', '加加食品', '动力源', '劲嘉股份', '劲拓股份', '劲胜智能', '勘设股份', '勤上股份', '包头铝业', '包钢股份', '北京利尔', '北京君正', '北京城乡', '北京城建', '北京文化', '北京科锐', '北京银行', '北信源', '北化股份', '北大医药', '北大科技', '北大荒', '北巴传媒', '北斗星通', '北新建材', '北新路桥', '北方五环', '北方华创', '北方国际', '北方导航', '北方稀土', '北方股份', '北特科技', '北玻股份', '北矿科技', '北纬科技', '北讯集团', '北辰实业', '北部湾港', '北陆药业', '千山药机', '千方科技', '千禾味业', '千红制药', '千金药业', '升达林业', '华业资本', '华东医药', '华东数控', '华东电脑', '华东科技', '华东重机', '华中数控', '华丽家族', '华仁药业', '华仪电气', '华伍股份', '华体科技', '华侨城', '华信国际', '华信新材', '华信股份', '华光股份', '华兰生物', '华兴源创', '华凯创意', '华创阳安', '华力创通', '华北制药', '华北高速', '华升股份', '华友钴业', '华发股份', '华圣科技', '华域汽车', '华培动力', '华塑控股', '华夏幸福', '华夏航空', '华夏银行', '华大基因', '华天科技', '华天酒店', '华媒控股', '华孚时尚', '华宇软件', '华安证券', '华宏科技', '华宝香精', '华峰氨纶', '华峰测控', '华峰超纤', '华工科技', '华帝股份', '华平股份', '华建集团', '华录百纳', '华微电子', '华懋科技', '华扬联众', '华控赛格', '华数传媒', '华斯股份', '华新水泥', '华昌化工', '华昌达', '华明装备', '华星创业', '华映科技', '华林证券', '华森制药', '华正新材', '华泰股份', '华泰证券', '华泽钴镍', '华测导航', '华测检测', '华海药业', '华润三九', '华润双鹤', '华润微', '华源控股', '华灿光电', '华熙生物', '华特气体', '华瑞股份', '华电国际', '华电能源', '华电重工', '华立股份', '华策影视', '华纺股份', '华统股份', '华联商厦', '华联控股', '华联综超', '华联股份', '华胜天成', '华能国际', '华能水电', '华脉科技', '华自科技', '华致酒行', '华英农业', '华茂股份', '华荣股份', '华菱星马', '华菱精工', '华菱钢铁', '华虹计通', '华西股份', '华西能源', '华西证券', '华讯方舟', '华谊兄弟', '华谊嘉信', '华谊集团', '华贸物流', '华资实业', '华软科技', '华辰装备', '华达科技', '华远地产', '华通医药', '华通热力', '华邦健康', '华金资本', '华鑫股份', '华钰矿业', '华铁应急', '华铁股份', '华铭智能', '华银电力', '华锋股份', '华锐风电', '华锦股份', '华闻传媒', '华阳国际', '华阳集团', '华鲁恒升', '华鹏飞', '华鼎锦纶', '协鑫能科', '协鑫集成', '卓易信息', '卓翼科技', '卓胜微', '卓越新能', '卓郎智能', '南京中商', '南京公用', '南京化纤', '南京医药', '南京新百', '南京油运', '南京港', '南京熊猫', '南京聚隆', '南京证券', '南京银行', '南京高科', '南兴股份', '南化股份', '南华仪器', '南华期货', '南华生物', '南华西', '南卫股份', '南国置业', '南大光电', '南天信息', '南威软件', '南宁百货', '南宁糖业', '南山控股', '南山铝业', '南岭民爆', '南微医学', '南方传媒', '南方汇通', '南方航空', '南方轴承', '南极电商', '南洋股份', '南洋航运', '南玻股份', '南纺股份', '南都物业', '南都电源', '南钢股份', '南风化工', '南风股份', '博世科', '博云新材', '博信股份', '博元投资', '博创科技', '博士眼镜', '博天环境', '博威合金', '博实股份', '博彦科技', '博思软件', '博敏电子', '博晖创新', '博杰股份', '博汇纸业', '博济医药', '博深股份', '博瑞传播', '博瑞医药', '博腾股份', '博迈科', '博通股份', '博通集成', '博闻科技', '博雅生物', '卧龙地产', '卧龙电气', '卫信康', '卫光生物', '卫士通', '卫宁健康', '卫星石化', '印纪传媒', '厚普股份', '原尚股份', '厦华电子', '厦工股份', '厦门信达', '厦门国贸', '厦门海洋', '厦门港务', '厦门空港', '厦门钨业', '友好集团', '友讯达', '友邦吊顶', '友阿股份', '双一科技', '双塔食品', '双成药业', '双星新材', '双杰电气', '双林生物', '双林股份', '双汇发展', '双环传动', '双环科技', '双箭股份', '双良节能', '双象股份', '双飞股份', '双鹭药业', '口子窖', '古井贡酒', '古越龙山', '古鳌科技', '可立克', '台华新材', '台基股份', '台海核电', '史丹利', '号百控股', '司太立', '司尔特', '合众思壮', '合兴包装', '合力泰', '合力科技', '合康新能', '合盛硅业', '合纵科技', '合肥城建', '合肥百货', '合诚股份', '合金投资', '合锻智能', '吉华集团', '吉大通信', '吉宏股份', '吉峰科技', '吉恩镍业', '吉林化工', '吉林化纤', '吉林敖东', '吉林森工', '吉林高速', '吉比特', '吉电股份', '吉祥航空', '吉翔股份', '吉艾科技', '吉药控股', '吉视传媒', '吉鑫科技', '同为股份', '同仁堂', '同兴达', '同和药业', '同大股份', '同德化工', '同方股份', '同有科技', '同洲电子', '同济堂', '同济科技', '同益实业', '同花顺', '同达创业', '名家汇', '名臣健康', '名雕股份', '向日葵', '君正集团', '君禾股份', '启明信息', '启明星辰', '启迪古汉', '启迪环境', '启迪设计', '吴通控股', '周大生', '和仁科技', '和佳股份', '和晶科技', '和科达', '和而泰', '和胜股份', '和远气体', '和邦生物', '和顺电气', '哈三联', '哈尔斯', '哈工智能', '哈慈股份', '哈投股份', '哈森股份', '哈空调', '哈药股份', '哈高科', '唐人神', '唐山港', '唐德影视', '唐源电气', '商业城', '商赢环球', '喜临门', '嘉事堂', '嘉元科技', '嘉凯城', '嘉化能源', '嘉友国际', '嘉寓股份', '嘉应制药', '嘉必优', '嘉欣丝绸', '嘉泽新能', '嘉澳环保', '嘉美包装', '嘉诚国际', '嘉麟杰', '四创电子', '四川九洲', '四川双马', '四川成渝', '四川托普', '四川美丰', '四川路桥', '四川金顶', '四川银山', '四川长虹', '四方科技', '四方精创', '四方股份', '四方达', '四环生物', '四维图新', '四通新材', '四通股份', '回天新材', '因赛集团', '园城黄金', '围海股份', '国中水务', '国信证券', '国元证券', '国光电器', '国光股份', '国农科技', '国创高新', '国发股份', '国嘉实业', '国城矿业', '国恒铁路', '国恩股份', '国投中鲁', '国投电力', '国投资本', '国新健康', '国新文化', '国新能源', '国旅联合', '国星光电', '国机汽车', '国机通用', '国林科技', '国检集团', '国民技术', '国泰君安', '国泰集团', '国海证券', '国瓷材料', '国电南瑞', '国电南自', '国电电力', '国盛金控', '国睿科技', '国祯环保', '国科微', '国立科技', '国统股份', '国美通讯', '国联水产', '国联股份', '国脉科技', '国芳集团', '国茂股份', '国药一致', '国药股份', '国轩高科', '国金证券', '国际医学', '国际实业', '国风塑业', '圆通速递', '圣农发展', '圣济堂', '圣莱达', '圣达生物', '圣邦股份', '圣阳电源', '圣龙股份', '地素时尚', '均胜电子', '坚朗五金', '坚瑞沃能', '坤彩科技', '垒知集团', '埃斯顿', '城发环境', '城地股份', '城市传媒', '城投控股', '基蛋生物', '塔牌集团', '塞力斯', '士兰微', '壹网壹创', '复旦复华', '复星医药', '外运发展', '外高桥', '多伦科技', '多喜爱', '多氟多', '大业股份', '大东南', '大东海', '大丰实业', '大亚圣象', '大众交通', '大众公用', '大元泵业', '大冷股份', '大北农', '大千生态', '大华农', '大华股份', '大博医疗', '大厦股份', '大参林', '大同煤业', '大名城', '大唐发电', '大唐电信', '大商股份', '大富科技', '大庆华科', '大庆联谊', '大康农业', '大恒科技', '大悦城', '大族激光', '大晟文化', '大智慧', '大有能源', '大洋电机', '大洲控股', '大港股份', '大湖股份', '大烨智能', '大理药业', '大禹节水', '大秦铁路', '大立科技', '大胜达', '大西洋', '大豪科技', '大连友谊', '大连圣亚', '大连控股', '大连港', '大连热电', '大连电瓷', '大连重工', '大通燃气', '大金重工', '大龙地产', '天业股份', '天保基建', '天健集团', '天准科技', '天创时尚', '天华超净', '天原集团', '天味食品', '天和防务', '天喻信息', '天圣制药', '天地数码', '天地源', '天地科技', '天坛生物', '天域生态', '天壕环境', '天士力', '天夏智慧', '天奇股份', '天奈科技', '天奥电子', '天威视讯', '天孚通信', '天宇股份', '天安新材', '天宜上佳', '天宝食品', '天宸股份', '天富能源', '天山生物', '天山股份', '天常股份', '天广中茂', '天康生物', '天成控股', '天成自控', '天房发展', '天方药业', '天晟新材', '天桥起重', '天永智能', '天汽模', '天沃科技', '天泽信息', '天津一汽', '天津普林', '天津松江', '天津港', '天津磁卡', '天海防务', '天润乳业', '天润数娱', '天润曲轴', '天源迪科', '天玑科技', '天瑞仪器', '天目湖', '天目药业', '天神娱乐', '天翔环境', '天能重工', '天舟文化', '天茂集团', '天药股份', '天虹股份', '天赐材料', '天迈科技', '天通股份', '天邑股份', '天邦股份', '天铁股份', '天银机电', '天际股份', '天音控股', '天顺股份', '天顺风能', '天风证券', '天首发展', '天马微电', '天马科技', '天马股份', '天鹅股份', '天齐锂业', '天龙光电', '天龙股份', '天龙集团', '太化股份', '太原重工', '太安堂', '太平洋', '太平鸟', '太极实业', '太极股份', '太极集团', '太空智造', '太行水泥', '太辰光', '太钢不锈', '太阳电缆', '太阳纸业', '太阳能', '太龙照明', '太龙药业', '奇信股份', '奇正藏药', '奇精机械', '奋达科技', '奥佳华', '奥克股份', '奥士康', '奥康国际', '奥拓电子', '奥普光电', '奥普家居', '奥特佳', '奥特迅', '奥瑞德', '奥瑞金', '奥福环保', '奥维通信', '奥美医疗', '奥翔药业', '奥联电子', '奥赛康', '奥赛康', '奥飞娱乐', '奥飞数据', '奥马电器', '好利来', '好太太', '好当家', '好想你', '好莱客', '如意集团', '如通股份', '妙可蓝多', '姚记科技', '威创股份', '威华股份', '威唐工业', '威孚高科', '威尔泰', '威尔药业', '威帝股份', '威星智能', '威派格', '威海广泰', '威胜信息', '威龙股份', '孚日股份', '宁夏建材', '宁德时代', '宁沪高速', '宁波东力', '宁波中百', '宁波华翔', '宁波富达', '宁波富邦', '宁波建工', '宁波水表', '宁波海运', '宁波港', '宁波热电', '宁波精达', '宁波联合', '宁波银行', '宁波韵升', '宁波高发', '宇信科技', '宇晶股份', '宇环数控', '宇瞳光学', '宇通客车', '宇顺电子', '安井食品', '安信信托', '安凯客车', '安利股份', '安博通', '安图生物', '安奈儿', '安妮股份', '安居宝', '安彩高科', '安德利', '安徽合力', '安徽建工', '安恒信息', '安控科技', '安正时尚', '安泰科技', '安泰集团', '安洁科技', '安源煤业', '安琪酵母', '安硕信息', '安科瑞', '安科生物', '安纳达', '安记食品', '安诺其', '安车检测', '安达维尔', '安迪苏', '安通控股', '安道麦', '安阳钢铁', '安集科技', '安靠智电', '宋城演艺', '宋都股份', '完美世界', '宏创控股', '宏发股份', '宏和科技', '宏图高科', '宏大爆破', '宏川智慧', '宏昌电子', '宏润建设', '宏源证券', '宏盛科技', '宏盛股份', '宏良股份', '宏辉果蔬', '宏达新材', '宏达电子', '宏达矿业', '宏达股份', '宏达高科', '宗申动力', '宜华健康', '宜华生活', '宜安科技', '宜宾纸业', '宜昌交运', '宜通世纪', '宝丰能源', '宝信软件', '宝光股份', '宝兰德', '宝利国际', '宝塔实业', '宝德股份', '宝新能源', '宝泰隆', '宝胜股份', '宝色股份', '宝莫股份', '宝莱特', '宝通科技', '宝钛股份', '宝钢包装', '宝钢股份', '宝馨科技', '宝鹰股份', '宝鼎科技', '实丰文化', '实达集团', '宣亚国际', '家家悦', '容大感光', '容百科技', '密尔克卫', '富临精工', '富临运业', '富奥股份', '富安娜', '富控互动', '富春环保', '富春股份', '富森美', '富满电子', '富瀚微', '富煌钢构', '富瑞特装', '富祥股份', '富通鑫茂', '富邦股份', '寒锐钴业', '寿仙谷', '小商品城', '小天鹅', '小康股份', '小熊电器', '尔康制药', '尖峰集团', '尚品宅配', '尚纬股份', '尚荣医疗', '尤夫股份', '居然之家', '展鹏科技', '山东出版', '山东华鹏', '山东地矿', '山东墨龙', '山东威达', '山东海化', '山东矿机', '山东章鼓', '山东药玻', '山东赫达', '山东路桥', '山东钢铁', '山东铝业', '山东高速', '山东黄金', '山大华特', '山推股份', '山水文化', '山河智能', '山河药辅', '山煤国际', '山石网科', '山西汾酒', '山西焦化', '山西证券', '山西路桥', '山鹰控股', '山鼎设计', '岭南控股', '岭南股份', '岱勒新材', '岱美股份', '岳阳兴长', '岳阳林纸', '岷江水电', '峨眉旅游', '崇达技术', '川仪股份', '川大智胜', '川恒股份', '川投能源', '川润股份', '川环科技', '川能动力', '川金诺', '工业富联', '工商银行', '工大高新', '左江科技', '巨人网络', '巨力索具', '巨化股份', '巨星科技', '巨轮智能', '巴士在线', '巴安水务', '市北高新', '希努尔', '帝尔激光', '帝欧家居', '常宝股份', '常山北明', '常山药业', '常柴股份', '常熟汽饰', '常熟银行', '常铝股份', '常青股份', '平安银行', '平庄能源', '平治信息', '平潭发展', '平煤股份', '平高电气', '幸福蓝海', '广东明珠', '广东榕泰', '广东甘化', '广东金曼', '广东骏亚', '广东鸿图', '广信材料', '广信股份', '广博股份', '广发证券', '广和通', '广哈通信', '广大特材', '广宇发展', '广宇集团', '广安爱众', '广州发展', '广州浪奇', '广州港', '广州酒家', '广弘控股', '广日股份', '广晟有色', '广汇汽车', '广汇物流', '广汇能源', '广汽长丰', '广汽集团', '广济药业', '广深铁路', '广生堂', '广田集团', '广电电气', '广电网络', '广电计量', '广电运通', '广百股份', '广联达', '广聚能源', '广西广电', '广誉远', '庄园牧场', '应流股份', '庞大集团', '康佳集团', '康力电梯', '康尼机电', '康弘药业', '康强电子', '康得新', '康德莱', '康恩贝', '康惠制药', '康拓红外', '康斯特', '康普顿', '康欣新材', '康泰生物', '康盛股份', '康缘药业', '康美药业', '康芝药业', '康跃科技', '康辰药业', '康达尔', '康达新材', '康隆达', '康龙化成', '廊坊发展', '延华智能', '延安必康', '延江股份', '延长化建', '建业股份', '建发股份', '建投能源', '建新股份', '建研院', '建科院', '建艺集团', '建设机械', '建设银行', '建龙微纳', '开元仪器', '开创国际', '开尔新材', '开山股份', '开开实业', '开润股份', '开滦股份', '开立医疗', '开能健康', '引力传媒', '弘业股份', '弘亚数控', '弘信电子', '弘宇股份', '弘讯科技', '弘高创意', '张家港行', '张旅集团', '张江高科', '张裕', '强力新材', '强生控股', '当代东方', '当代明诚', '当升科技', '当虹科技', '彤程新材', '彩虹股份', '彩讯股份', '徐家汇', '徐工机械', '徕木股份', '得利斯', '得润电子', '得邦照明', '御家汇', '御银股份', '微光股份', '微芯生物', '德创环保', '德力股份', '德奥通航', '德威新材', '德宏股份', '德尔未来', '德尔股份', '德展健康', '德恩精工', '德新交运', '德方纳米', '德生科技', '德美化工', '德联集团', '德艺文创', '德豪润达', '德赛电池', '德赛西威', '德邦股份', '心脉医疗', '必创科技', '志邦股份', '快克股份', '快意电梯', '思创医惠', '思源电气', '思特奇', '思维列控', '思美传媒', '怡亚通', '怡球资源', '怡达股份', '恒丰纸业', '恒为科技', '恒久科技', '恒信东方', '恒力股份', '恒华科技', '恒基达鑫', '恒大高新', '恒天海龙', '恒宝股份', '恒实科技', '恒康医疗', '恒星科技', '恒林股份', '恒泰艾普', '恒润重工', '恒源煤电', '恒瑞医药', '恒生电子', '恒立实业', '恒立液压', '恒运集团', '恒通物流', '恒通科技', '恒逸石化', '恒邦股份', '恒铭达', '恒银金融', '恒锋信息', '恒锋工具', '恒顺醋业', '恩华药业', '恩捷股份', '恺英网络', '悦心健康', '悦达投资', '惠伦晶体', '惠博普', '惠发股份', '惠城环保', '惠天热电', '惠威科技', '惠泉啤酒', '惠程科技', '惠而浦', '惠达卫浴', '意华股份', '慈文传媒', '慈星股份', '慈铭体检', '慧金科技', '成城股份', '成都燃气', '成都路桥', '成都银行', '成飞集成', '我乐家居', '我武生物', '我爱我家', '戴维医疗', '扬农化工', '扬子新材', '扬子石化', '扬帆新材', '扬杰科技', '承德钒钛', '承德露露', '抚顺特钢', '报喜鸟', '拉卡拉', '拉夏贝尔', '拉芳家化', '拓尔思', '拓斯达', '拓日新能', '拓普集团', '拓维信息', '拓邦股份', '招商公路', '招商南油', '招商地产', '招商港口', '招商积余', '招商蛇口', '招商证券', '招商轮船', '招商银行', '指南针', '振东制药', '振华化学', '振华科技', '振华重工', '振德医疗', '振江股份', '振芯科技', '振静股份', '捷佳伟创', '捷成世纪', '捷捷微电', '捷昌驱动', '捷荣技术', '捷顺科技', '掌趣科技', '掌阅科技', '探路者', '搜于特', '摩恩电气', '摩登大道', '攀渝钛业', '攀钢钒钛', '敦煌种业', '数字政通', '数字认证', '数据港', '数源科技', '数知科技', '数码测绘', '数码科技', '文一科技', '文化长城', '文山电力', '文峰股份', '文投控股', '文灿股份', '文科园林', '斯太尔', '斯莱克', '斯达半导', '斯迪克', '新世界', '新乡化纤', '新乳业', '新五丰', '新亚制程', '新亿股份', '新余国科', '新元科技', '新光光电', '新光圆成', '新光药业', '新兴装备', '新兴铸管', '新农开发', '新农股份', '新凤鸣', '新力金融', '新劲刚', '新化股份', '新北洋', '新华传媒', '新华保险', '新华制药', '新华医疗', '新华文轩', '新华百货', '新华网', '新华联', '新华都', '新华锦', '新和成', '新国都', '新坐标', '新城市', '新城控股', '新大正', '新大陆', '新天然气', '新天科技', '新天药业', '新奥股份', '新媒股份', '新宁物流', '新安股份', '新宏泰', '新宏泽', '新宙邦', '新宝股份', '新希望', '新开普', '新开源', '新文化', '新日恒力', '新日股份', '新时达', '新易盛', '新晨科技', '新智认知', '新朋股份', '新泉股份', '新洋丰', '新海宜', '新湖中宝', '新湖创业', '新潮能源', '新澳股份', '新界泵业', '新疆交建', '新疆众和', '新疆天业', '新疆浩源', '新疆火炬', '新研股份', '新筑股份', '新纶科技', '新经典', '新美星', '新联电子', '新能泰山', '新莱应材', '新诺威', '新赛股份', '新通联', '新都酒店', '新野纺织', '新金路', '新钢股份', '新集能源', '新雷能', '新黄浦', '方大炭素', '方大特钢', '方大集团', '方正电机', '方正科技', '方正证券', '方盛制药', '方直科技', '方邦股份', '旋极信息', '旗天科技', '旗滨集团', '无锡银行', '日上集团', '日丰股份', '日出东方', '日发精机', '日播时尚', '日月股份', '日海智能', '日照港', '日盈电子', '日科化学', '日辰股份', '旭光股份', '旭升股份', '时代万恒', '时代出版', '时代新材', '旷达科技', '旺能环境', '昂利康', '昂立教育', '昆仑万维', '昆吾九鼎', '昆明机床', '昆药集团', '昇兴股份', '昊华科技', '昊华能源', '昊志机电', '昊海生科', '昌九生化', '昌红科技', '明天科技', '明德生物', '明星电力', '明泰铝业', '明牌珠宝', '明珠集团', '明阳智能', '明阳电路', '易世达', '易事特', '易华录', '易天股份', '易尚展示', '易德龙', '易成新能', '易明医药', '易联众', '易见股份', '星云股份', '星光农机', '星宇股份', '星帅尔', '星徽精密', '星星科技', '星期六', '星湖科技', '星源材质', '星网宇达', '星网锐捷', '星辉娱乐', '映翰通', '春光科技', '春兰股份', '春兴精工', '春秋电子', '春秋航空', '春风动力', '昭衍新药', '晋亿实业', '晋西车轴', '晓程科技', '晨丰科技', '晨光文具', '晨光生物', '晨化股份', '晨曦航空', '晨鑫科技', '晨鸣纸业', '普丽盛', '普元信息', '普利制药', '普利特', '普天邮通', '普洛药业', '普莱柯', '普路通', '普邦股份', '普门科技', '景兴纸业', '景嘉微', '景峰医药', '景旺电子', '景津环保', '景谷林业', '晶丰明源', '晶华新材', '晶方科技', '晶晨股份', '晶澳科技', '晶瑞股份', '晶盛机电', '智云股份', '智光电气', '智动力', '智宇未来', '智度股份', '智慧农业', '智慧能源', '智能自控', '智莱科技', '智飞生物', '暴风集团', '曙光股份', '曲江文旅', '曲美家居', '有友食品', '有方科技', '有研新材', '朗博科技', '朗姿股份', '朗新科技', '朗源股份', '朗玛信息', '朗科智能', '朗科科技', '朗进科技', '朗迪集团', '木林森', '未名医药', '本钢板材', '机器人', '杉杉股份', '来伊份', '杭叉集团', '杭可科技', '杭州园林', '杭州解百', '杭州银行', '杭州高新', '杭氧股份', '杭电股份', '杭萧钢构', '杭钢股份', '杭锅股份', '杭齿前进', '杰克股份', '杰恩设计', '杰普特', '杰瑞股份', '杰赛科技', '松发股份', '松德智慧', '松炀资源', '松芝股份', '松霖科技', '林州重机', '林洋能源', '林海股份', '柏堡龙', '柏楚电子', '柘中股份', '柯利达', '柯力传感', '柳化股份', '柳工', '柳药股份', '柳钢股份', '标准股份', '栖霞建设', '株冶集团', '格力地产', '格力电器', '格尔软件', '格林美', '桂东电力', '桂冠电力', '桂发祥', '桂林三金', '桂林旅游', '桃李面包', '桐昆股份', '梅安森', '梅花集团', '梅轮电梯', '梅雁吉祥', '梦洁股份', '梦百合', '梦网集团', '梦舟股份', '棒杰股份', '棕榈股份', '森源电气', '森特股份', '森远股份', '森霸传感', '森马服饰', '楚天科技', '楚天高速', '楚江新材', '榕基软件', '模塑科技', '横店东磁', '横店影视', '横河模具', '欢瑞世纪', '欣天科技', '欣旺达', '欣泰电气', '欣锐科技', '欣龙控股', '欧亚集团', '欧普康视', '欧普照明', '欧比特', '欧派家居', '欧浦智网', '欧菲光', '歌力思', '歌华有线', '歌尔股份', '正业科技', '正丹股份', '正元智慧', '正川股份', '正平股份', '正泰电器', '正海生物', '正海磁材', '正源股份', '正虹科技', '正裕工业', '正邦科技', '步森股份', '步步高', '步长制药', '武商集团', '武昌鱼', '武汉凡谷', '武汉控股', '武进不锈', '武钢股份', '毅昌股份', '每日互动', '比亚迪', '比特科技', '比音勒芬', '民丰特纸', '民和股份', '民德电子', '民生控股', '民生银行', '氯碱化工', '水井坊', '水仙电器', '水星家纺', '水晶光电', '永东股份', '永兴材料', '永冠新材', '永创智能', '永利股份', '永吉股份', '永和智控', '永太科技', '永安林业', '永安药业', '永安行', '永悦科技', '永新光学', '永新股份', '永泰能源', '永清环保', '永福股份', '永艺股份', '永贵电器', '永辉超市', '永高股份', '永鼎股份', '汇中股份', '汇嘉时代', '汇川技术', '汇得科技', '汇洁股份', '汇源通信', '汇纳科技', '汇通能源', '汇金科技', '汇金股份', '汇金通', '汇顶科技', '汇鸿国际', '汉商集团', '汉嘉设计', '汉威科技', '汉宇集团', '汉得信息', '汉森制药', '汉王科技', '汉缆股份', '汉邦高科', '汉钟精机', '汉鼎宇佑', '汕头宏业', '江中药业', '江丰电子', '江化微', '江南化工', '江南水务', '江南高纤', '江山欧派', '江山股份', '江河集团', '江泉实业', '江海股份', '江淮汽车', '江特电机', '江苏中设', '江苏北人', '江苏吴中', '江苏国信', '江苏国泰', '江苏新能', '江苏有线', '江苏神通', '江苏租赁', '江苏索普', '江苏舜天', '江苏银行', '江苏阳光', '江苏雷利', '江西水泥', '江西铜业', '江西长运', '江铃汽车', '江阴银行', '江龙船艇', '汤臣倍健', '沃华医药', '沃尔德', '沃尔核材', '沃施股份', '沃格光电', '沃森生物', '沃特股份', '沈阳化工', '沈阳机床', '沙河股份', '沙钢股份', '沧州大化', '沧州明珠', '沪宁股份', '沪电股份', '河池化工', '河钢股份', '河钢资源', '泉峰汽车', '法兰泰克', '法尔胜', '法拉电子', '泛微网络', '泛海控股', '波导股份', '泰合健康', '泰和新材', '泰和科技', '泰嘉股份', '泰尔重工', '泰山石油', '泰晶科技', '泰林生物', '泰格医药', '泰永长征', '泰瑞机器', '泰禾光电', '泰禾集团', '泰胜风能', '泰豪科技', '泰达股份', '泸天化', '泸州老窖', '泽璟制药', '洁特生物', '洁美科技', '洋河股份', '洛凯股份', '洛阳玻璃', '洛阳钼业', '津劝业', '津滨发展', '津膜科技', '洪城水业', '洪汇新材', '洪涛股份', '洪都航空', '洲明科技', '洲际油气', '洽洽食品', '派思股份', '派生科技', '济川药业', '济民制药', '浔兴股份', '浙商中拓', '浙商证券', '浙商银行', '浙大网新', '浙富控股', '浙数文化', '浙江世宝', '浙江东方', '浙江东日', '浙江交科', '浙江仙通', '浙江众成', '浙江信联', '浙江医药', '浙江富润', '浙江广厦', '浙江永强', '浙江美大', '浙江震元', '浙江鼎力', '浙江龙盛', '浙能电力', '浦东建设', '浦东金桥', '浦发银行', '浩丰科技', '浩云科技', '浩物股份', '浪潮信息', '浪潮软件', '浪莎股份', '海亮股份', '海伦哲', '海伦钢琴', '海信家电', '海信视像', '海兰信', '海兴电力', '海利尔', '海利得', '海利生物', '海南椰岛', '海南橡胶', '海南海药', '海南瑞泽', '海南矿业', '海南高速', '海印股份', '海大集团', '海天味业', '海天精工', '海宁皮城', '海容冷链', '海尔施', '海尔智家', '海尔生物', '海峡环保', '海峡股份', '海川智能', '海康威视', '海得控制', '海德股份', '海思科', '海星股份', '海普瑞', '海格通信', '海欣股份', '海欣食品', '海正药业', '海汽集团', '海油发展', '海油工程', '海波重科', '海泰发展', '海洋王', '海润光伏', '海源复材', '海澜之家', '海特生物', '海特高新', '海王生物', '海立股份', '海翔药业', '海联讯', '海联金汇', '海能实业', '海能达', '海航创新', '海航基础', '海航投资', '海航控股', '海航科技', '海螺型材', '海螺水泥', '海越股份', '海辰药业', '海达股份', '海通证券', '海量数据', '海陆重工', '海顺新材', '海马汽车', '海鸥住工', '海鸥股份', '海默科技', '润和软件', '润建股份', '润欣科技', '润禾材料', '润达医疗', '润邦股份', '润都股份', '涪陵榨菜', '涪陵电力', '淮北矿业', '淮河能源', '深中华', '深信服', '深冷股份', '深华发', '深南电', '深南电路', '深南股份', '深圳中侨', '深圳中浩', '深圳华强', '深圳新星', '深圳机场', '深圳燃气', '深圳石化', '深圳能源', '深大通', '深天地', '深房集团', '深振业', '深桑达', '深物业', '深特力', '深科技', '深粮控股', '深纺织', '深赛格', '深高速', '淳中科技', '清新环境', '清水源', '清源股份', '清溢光电', '渝农商行', '渝开发', '渤海活塞', '渤海租赁', '渤海股份', '渤海轮渡', '温州宏丰', '温氏股份', '游久游戏', '游族网络', '湖北宜化', '湖北广电', '湖北能源', '湖南发展', '湖南天雁', '湖南投资', '湖南海利', '湖南盐业', '湖南黄金', '湘油泵', '湘潭电化', '湘火炬Ａ', '湘电股份', '湘邮科技', '溢多利', '滨化股份', '滨江集团', '滨海能源', '漫步者', '漳州发展', '漳泽电力', '潍柴动力', '潍柴重机', '潜能恒信', '潞安环能', '潮宏基', '澄天伟业', '澄星股份', '澜起科技', '澳柯玛', '澳洋健康', '澳洋顺昌', '激智科技', '濮耐股份', '濮阳惠成', '瀚叶股份', '瀚川智能', '瀚蓝环境', '瀛通通讯', '火炬电子', '灵康药业', '炬华科技', '炼石航空', '热景生物', '烯碳新材', '烽火电子', '烽火通信', '焦作万方', '焦点科技', '煌上煌', '熊猫金控', '熙菱信息', '燕京啤酒', '燕塘乳业', '爱乐达', '爱仕达', '爱司凯', '爱婴室', '爱尔眼科', '爱康科技', '爱建集团', '爱施德', '爱普股份', '爱朋医疗', '爱柯迪', '爱迪尔', '片仔癀', '牧原股份', '牧高笛', '物产中大', '特一药业', '特发信息', '特变电工', '特宝生物', '特尔佳', '特锐德', '狮头股份', '猛狮科技', '猴王股份', '獐子岛', '玉禾田', '玉龙股份', '王子新材', '王府井', '环保股份', '环境集团', '环旭电子', '环球印务', '现代制药', '现代投资', '玲珑轮胎', '珀莱雅', '珈伟新能', '珍宝岛', '珠江啤酒', '珠江实业', '珠江钢琴', '珠海中富', '珠海港', '珠海鑫光', '理工光科', '理工环科', '理邦仪器', '琼民源Ａ', '瑞丰光电', '瑞丰高材', '瑞凌股份', '瑞和股份', '瑞尔特', '瑞康医药', '瑞斯康达', '瑞普生物', '瑞松科技', '瑞泰科技', '瑞特股份', '瑞玛工业', '瑞芯微', '瑞茂通', '瑞贝卡', '瑞达期货', '璞泰来', '甘咨询', '甘肃电投', '生态农业', '生意宝', '生物股份', '生益科技', '用友网络', '甬金股份', '田中精机', '申万宏源', '申华控股', '申科股份', '申联生物', '申能股份', '申达股份', '申通地铁', '申通快递', '电光科技', '电声股份', '电子城', '电工合金', '电广传媒', '电科能源', '电科院', '电连技术', '电魂网络', '畅联股份', '界龙实业', '登云股份', '登海种业', '白云制药', '白云山', '白云机场', '白云电器', '白银有色', '百傲化学', '百利电气', '百利科技', '百合花', '百大集团', '百奥泰', '百川股份', '百川能源', '百洋股份', '百润股份', '百联股份', '百联股份(合并前)', '百花村', '百达精工', '百邦科技', '百隆东方', '皇台酒业', '皇庭国际', '皇氏集团', '皇马科技', '皖天然气', '皖新传媒', '皖维高新', '皖能电力', '皖通科技', '皖通高速', '皮阿诺', '盈峰环境', '盈康生命', '盈方微', '盈趣科技', '益丰药房', '益佰制药', '益民集团', '益生股份', '益盛药业', '盐津铺子', '盐湖股份', '盐湖集团', '盐田港', '盘江股份', '盘龙药业', '盛和资源', '盛天网络', '盛屯矿业', '盛弘股份', '盛洋科技', '盛讯达', '盛路通信', '盛达资源', '盛运环保', '盛通股份', '盾安环境', '省广股份', '真视通', '睿创微纳', '睿能科技', '矩子科技', '石化机械', '石化油服', '石基信息', '石大胜华', '石头科技', '石油大明', '石英股份', '硅宝科技', '硕世生物', '硕贝德', '碧水源', '碳元科技', '祁连山', '神农科技', '神剑股份', '神力股份', '神奇制药', '神宇股份', '神州信息', '神州数码', '神州泰岳', '神州长城', '神州高铁', '神工股份', '神开股份', '神思电子', '神火煤电', '神雾环保', '神雾节能', '神马电力', '神马股份', '神驰机电', '祥和实业', '祥源文化', '祥生医疗', '祥鑫科技', '祥龙电业', '福光股份', '福安药业', '福建九州', '福建水泥', '福建金森', '福建高速', '福成股份', '福斯特', '福日电子', '福星股份', '福晶科技', '福瑞股份', '福田汽车', '福耀玻璃', '福能股份', '福莱特', '福蓉科技', '福达合金', '福达股份', '福鞍股份', '禾丰牧业', '禾望电气', '秀强股份', '秋林集团', '科伦药业', '科信技术', '科创信息', '科创新源', '科力尔', '科力远', '科华恒盛', '科华控股', '科华生物', '科博达', '科士达', '科大国创', '科大智能', '科大讯飞', '科安达', '科恒股份', '科斯伍德', '科新机电', '科林环保', '科林电气', '科森科技', '科沃斯', '科泰电源', '科瑞技术', '科蓝软件', '科融环境', '科达利', '科达洁能', '科达股份', '科远智慧', '科迪乳业', '科锐国际', '科陆电子', '科隆股份', '科顺股份', '秦安股份', '秦川机床', '秦港股份', '积成电子', '移为通信', '移远通信', '空港股份', '立华股份', '立思辰', '立昂技术', '立立电子', '立讯精密', '立霸股份', '章源钨业', '第一创业', '第一医药', '筑博设计', '米奥兰特', '粤传媒', '粤宏远', '粤桂股份', '粤泰股份', '粤电力', '粤高速', '精伦电子', '精准信息', '精功科技', '精华制药', '精密股份', '精工钢构', '精测电子', '精研科技', '精艺股份', '精达股份', '精锻科技', '索菱股份', '索菲亚', '索通发展', '紫光国微', '紫光学大', '紫光股份', '紫天科技', '紫晶存储', '紫江企业', '紫金矿业', '紫金银行', '紫鑫药业', '红塔证券', '红墙股份', '红太阳', '红宇新材', '红宝丽', '红旗连锁', '红日药业', '红星发展', '红相股份', '红蜻蜓', '红豆股份', '红阳能源', '纳尔股份', '纳川股份', '纳思达', '纵横通信', '纽威股份', '经纬纺机', '经纬辉开', '绝味食品', '继峰股份', '维业股份', '维信诺', '维力医疗', '维宏股份', '维尔利', '维科技术', '维维股份', '综艺股份', '绿地控股', '绿城水务', '绿庭投资', '绿康生化', '绿景控股', '绿盟科技', '绿色动力', '绿茵生态', '网宿科技', '网达软件', '罗博特科', '罗平锌电', '罗普斯金', '罗牛山', '罗莱生活', '罗顿发展', '置信电气', '美丽生态', '美亚光电', '美亚柏科', '美克家居', '美凯龙', '美利云', '美力科技', '美吉姆', '美好置业', '美尔雅', '美尚生态', '美年健康', '美康生物', '美思德', '美晨生态', '美格智能', '美的电器', '美的集团', '美盈森', '美盛文化', '美联新材', '美芝股份', '美诺华', '美达股份', '美迪西', '美邦服饰', '美都能源', '美锦能源', '羚锐制药', '群兴玩具', '翔港科技', '翔鹭钨业', '翠微股份', '翰宇药业', '耀皮玻璃', '老凤祥', '老板电器', '老白干酒', '老百姓', '耐威科技', '耐普矿机', '联创光电', '联创电子', '联创股份', '联化科技', '联发股份', '联合光电', '联建光电', '联得装备', '联明股份', '联泰环保', '联环药业', '联瑞新材', '联络互动', '联美控股', '联诚精密', '聚光科技', '聚力文化', '聚杰微纤', '聚灿光电', '聚辰股份', '聚隆科技', '聚飞光电', '聚龙股份', '胜利精密', '胜利股份', '胜宏科技', '胜景山河', '能科股份', '腾信股份', '腾达建设', '腾邦国际', '腾龙股份', '至正股份', '至纯科技', '致远互联', '舍得酒业', '舒泰神', '航发动力', '航发控制', '航发科技', '航天信息', '航天动力', '航天发展', '航天宏图', '航天工程', '航天彩虹', '航天晨光', '航天机电', '航天电器', '航天电子', '航天科技', '航天通信', '航天长峰', '航新科技', '航民股份', '航锦科技', '良信电器', '良品铺子', '艾华集团', '艾可蓝', '艾德生物', '艾格拉斯', '艾比森', '艾艾精工', '艾迪精密', '节能风电', '芒果超媒', '芭田股份', '芯源微', '芯能科技', '花园生物', '花王股份', '苏交科', '苏农银行', '苏利股份', '苏博特', '苏垦农发', '苏大维格', '苏奥传感', '苏宁易购', '苏宁环球', '苏州固锝', '苏州科达', '苏州银行', '苏州高新', '苏州龙杰', '苏泊尔', '苏盐井神', '苏美达', '苏试试验', '英力特', '英可瑞', '英唐智控', '英威腾', '英搏尔', '英杰电气', '英洛华', '英派斯', '英特集团', '英科医疗', '英维克', '英联股份', '英飞拓', '英飞特', '茂业商业', '茂化实华', '茂硕电源', '茶花股份', '荃银高科', '荣丰控股', '荣之联', '荣华实业', '荣安地产', '荣晟环保', '荣泰健康', '荣盛发展', '荣盛石化', '荣科科技', '药明康德', '药石科技', '莎普爱思', '莫高股份', '莱克电气', '莱宝高科', '莱绅通灵', '莱美药业', '莱茵体育', '莱茵生物', '莱钢股份', '莲花健康', '菲利华', '菲林格尔', '菲菲澳家', '菲达环保', '萃华股份', '营口港', '葛洲坝', '葵花股份', '蒙娜丽莎', '蒙草生态', '蓝丰生化', '蓝光发展', '蓝帆医疗', '蓝思科技', '蓝晓科技', '蓝海华腾', '蓝焰控股', '蓝盾股份', '蓝科高新', '蓝色光标', '蓝英装备', '蓝谷新能', '蓝黛传动', '蔚蓝生物', '藏格控股', '虹软科技', '融捷健康', '融捷股份', '融钰集团', '蠡湖股份', '裕兴股份', '裕同科技', '襄阳轴承', '西仪股份', '西南证券', '西宁特钢', '西安旅游', '西安银行', '西安饮食', '西山煤电', '西昌电力', '西水股份', '西王食品', '西菱动力', '西藏发展', '西藏城投', '西藏天路', '西藏旅游', '西藏珠峰', '西藏矿业', '西藏药业', '西部创业', '西部建设', '西部材料', '西部牧业', '西部矿业', '西部证券', '西部资源', '西部超导', '西部黄金', '西陇科学', '西麦食品', '视源股份', '视觉中国', '览海投资', '誉衡药业', '许继电气', '设研院', '设计总院', '证通电子', '诚志股份', '诚意药业', '诚益通', '诚迈科技', '诚邦股份', '诺力股份', '诺德股份', '诺普信', '诺邦股份', '读者传媒', '象屿股份', '豪尔赛', '豪能股份', '豪迈科技', '豫光金铅', '豫园股份', '豫能控股', '豫金刚石', '贝因美', '贝斯特', '贝斯美', '贝瑞基因', '贝肯能源', '贝达药业', '贝通信', '财信发展', '财通证券', '贤丰控股', '贵人鸟', '贵州燃气', '贵州百灵', '贵州茅台', '贵州轮胎', '贵广网络', '贵研铂业', '贵绳股份', '贵航股份', '贵酒股份', '贵阳银行', '赛为智能', '赛升药业', '赛意信息', '赛托生物', '赛摩电气', '赛特新材', '赛福天', '赛腾股份', '赛诺医疗', '赛象科技', '赛轮股份', '赛隆药业', '赞宇科技', '赢合科技', '赢时胜', '赣粤高速', '赣能股份', '赣锋锂业', '赤峰黄金', '赫美集团', '起步股份', '超华科技', '超图软件', '超声电子', '超讯通信', '超频三', '越博动力', '越秀金控', '跃岭股份', '跨境通', '路桥建设', '路畅科技', '路通视信', '软控股份', '轴研科技', '轻纺城', '辅仁药业', '辉丰股份', '辉煌科技', '辉隆股份', '辰安科技', '辰欣药业', '辽宁成大', '辽河油田', '达刚控股', '达华智能', '达威股份', '达安基因', '达安股份', '达实智能', '达尔曼', '达志科技', '达意隆', '迅游科技', '迈为股份', '迈克生物', '迈得医疗', '迈瑞医疗', '迎驾贡酒', '运盛实业', '运达科技', '运达股份', '远东传动', '远光软件', '远兴能源', '远大控股', '远大智能', '远方信息', '远望谷', '远程股份', '远达环保', '连云港', '迦南科技', '迪威迅', '迪安诊断', '迪普科技', '迪森股份', '迪瑞医疗', '迪生力', '迪贝电气', '迪马股份', '透景生命', '通产丽星', '通光线缆', '通化东宝', '通化金马', '通合科技', '通威股份', '通宇通讯', '通宝能源', '通富微电', '通润装备', '通源石油', '通用股份', '通程控股', '通策医疗', '通葡股份', '通裕重工', '通达动力', '通达电气', '通达股份', '通鼎互联', '道恩股份', '道明光学', '道森股份', '道氏技术', '道通科技', '道道全', '邦宝益智', '邦讯技术', '邮储银行', '邯郸钢铁', '郑州煤电', '郑州银行', '郑煤机', '郴电国际', '鄂尔多斯', '酒钢宏兴', '酒鬼酒', '醋化股份', '重庆啤酒', '重庆建工', '重庆水务', '重庆港九', '重庆燃气', '重庆百货', '重庆路桥', '重庆钢铁', '重药控股', '量子生物', '金一文化', '金亚科技', '金信诺', '金健米业', '金冠电气', '金刚玻璃', '金利华电', '金力永磁', '金力泰', '金卡智能', '金发拉比', '金发科技', '金固股份', '金圆股份', '金地集团', '金城医药', '金域医学', '金太阳', '金奥博', '金字火腿', '金宇车城', '金安国纪', '金山办公', '金山股份', '金岭矿业', '金徽酒', '金新农', '金时科技', '金明精机', '金晶科技', '金智科技', '金杯汽车', '金杯电工', '金枫酒业', '金桥信息', '金正大', '金河生物', '金泰集团', '金洲慈航', '金洲管道', '金浦钛业', '金海环境', '金溢科技', '金牌厨柜', '金牛化工', '金瑞矿业', '金田实业', '金盾股份', '金石亚药', '金石资源', '金禾实业', '金种子酒', '金科文化', '金科股份', '金能科技', '金自天正', '金花股份', '金荔科技', '金莱特', '金融街', '金螳螂', '金证股份', '金诚信', '金财互联', '金贵银业', '金轮股份', '金辰股份', '金达威', '金运激光', '金通灵', '金逸影视', '金钼股份', '金银河', '金陵体育', '金陵药业', '金陵饭店', '金隅集团', '金雷股份', '金风科技', '金马集团', '金鸿控股', '金鸿顺', '金鹰股份', '金麒麟', '金龙机电', '金龙汽车', '金龙羽', '鑫广绿环', '钢研纳克', '钢研高纳', '钧达股份', '钱江摩托', '钱江水利', '钱江生化', '铁岭新城', '铁汉生态', '铁流股份', '铁龙物流', '铂力特', '铂科新材', '铜峰电子', '铜陵有色', '铭普光磁', '银之杰', '银亿股份', '银信科技', '银宝山新', '银座股份', '银星能源', '银江股份', '银河生物', '银河电子', '银河磁体', '银泰黄金', '银禧科技', '银轮股份', '银邦股份', '银都股份', '银鸽投资', '银龙股份', '锋龙股份', '锌业股份', '锐奇股份', '锐明技术', '锐科激光', '锡业股份', '锦富技术', '锦州港', '锦州石化', '锦江投资', '锦江股份', '锦泓集团', '锦浪科技', '锦鸡股份', '锦龙股份', '镇海股份', '长久物流', '长亮科技', '长信科技', '长兴实业', '长园集团', '长城信息', '长城军工', '长城动漫', '长城影视', '长城汽车', '长城电工', '长城科技', '长城股份', '长城证券', '长安汽车', '长川科技', '长方集团', '长春一东', '长春燃气', '长春经开', '长春高新', '长江传媒', '长江健康', '长江投资', '长江电力', '长江证券', '长江通信', '长沙银行', '长海股份', '长源电力', '长生生物', '长电科技', '长白山', '长盈精密', '长盛轴承', '长缆科技', '长航凤凰', '长荣股份', '长虹华意', '长虹美菱', '长阳科技', '长青股份', '长青集团', '长飞光纤', '长高集团', '长鹰信质', '闰土股份', '闻泰科技', '闽东电力', '闽发铝业', '闽越花雕', '阳光城', '阳光新业', '阳光照明', '阳光电源', '阳普医疗', '阳泉煤业', '阳煤化工', '阳谷华泰', '阿石创', '阿科力', '际华集团', '陆家嘴', '陇神戎发', '陕国信托', '陕天然气', '陕西煤业', '陕西金叶', '陕西黑猫', '陕鼓动力', '隆利科技', '隆华科技', '隆基机械', '隆基股份', '隆平高科', '隆盛科技', '隆鑫通用', '隧道股份', '雄塑科技', '雄帝科技', '雄韬股份', '雅克科技', '雅化集团', '雅戈尔', '雅本化学', '雅百特', '雅运股份', '集友股份', '集智股份', '集泰股份', '雏鹰农牧', '雪人股份', '雪峰科技', '雪榕生物', '雪浪环境', '雪莱特', '雪迪龙', '雪龙集团', '雷曼光电', '雷柏科技', '雷科防务', '雷迪克', '震安科技', '露天煤业', '露笑科技', '青农商行', '青山纸业', '青岛中程', '青岛双星', '青岛啤酒', '青岛港', '青岛金王', '青岛银行', '青松建化', '青松股份', '青海华鼎', '青海春天', '青青稞酒', '青鸟消防', '青龙管业', '靖远煤电', '鞍山一工', '鞍山合成', '鞍重股份', '鞍钢股份', '韦尔股份', '韩建河山', '音飞储存', '韵达股份', '韶能股份', '韶钢松山', '顶固集创', '顶点软件', '顺丰控股', '顺利办', '顺发恒业', '顺威股份', '顺灏股份', '顺络电子', '顺网科技', '顺鑫农业', '顺钠股份', '顾地科技', '顾家家居', '领益智造', '风华高科', '风神股份', '风范股份', '风语筑', '飞乐音响', '飞亚达', '飞凯材料', '飞利信', '飞力达', '飞天诚信', '飞科电器', '飞荣达', '飞马国际', '飞鹿股份', '飞龙股份', '首创股份', '首商股份', '首开股份', '首旅酒店', '首航高科', '首钢股份', '香山股份', '香梨股份', '香江控股', '香溢融通', '香雪制药', '香飘飘', '马应龙', '马钢股份', '驰宏锌锗', '骆驼股份', '高乐股份', '高争民爆', '高伟达', '高升控股', '高德红外', '高斯贝尔', '高斯达', '高新兴', '高新发展', '高澜股份', '高盟新材', '高科石化', '高能在线', '高能环境', '高鸿股份', '鱼跃医疗', '鲁亿通', '鲁信创投', '鲁北化工', '鲁商健康', '鲁抗医药', '鲁泰纺织', '鲁西化工', '鲁银投资', '鲁阳节能', '鲍斯股份', '鸣志电器', '鸿利智汇', '鸿博股份', '鸿合科技', '鸿泉物联', '鸿路钢构', '鸿达兴业', '鸿远电子', '鹏博士', '鹏欣资源', '鹏翎股份', '鹏起科技', '鹏辉能源', '鹏鹞环保', '鹏鼎控股', '鹭燕医药', '鹿港文化', '麒盛科技', '麦克奥迪', '麦捷科技', '麦格米特', '麦趣尔', '麦达数字', '麦迪科技', '黄山旅游', '黄山胶囊', '黄河旋风', '黑牡丹', '黑猫股份', '黑芝麻', '黔源电力', '鼎信通讯', '鼎捷软件', '鼎汉技术', '鼎胜新材', '鼎龙文化', '鼎龙股份', '齐峰新材', '齐心集团', '齐翔腾达', '齐鲁石化', '龙元建设', '龙净环保', '龙力生物', '龙大肉食', '龙头股份', '龙宇燃油', '龙建股份', '龙星化工', '龙江交通', '龙泉股份', '龙津药业', '龙洲股份', '龙涤股份', '龙源技术', '龙溪股份', '龙科利华', '龙蟒佰利', '龙蟠科技', '龙软科技', '龙韵股份', '龙马环卫']


'''
select id, link  from eastmoney_carticle where article is NULL limit 10;
'''


'''
delete from eastmoney_carticle where id in (78495, 84221, 113661, 119975, 134031, 136221, 137839, 146381, 150199, 152565);
'''