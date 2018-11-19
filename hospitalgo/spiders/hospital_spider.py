# -*- coding: utf-8 -*-
import scrapy
import re
from hospitalgo.items import HospitalgoItem
from scrapy.selector import Selector
from scrapy.http import HtmlResponse

##过滤HTML中的标签
# 将HTML中标签等信息去掉
# @param htmlstr HTML字符串.
def filter_tags(htmlstr):
    # 先过滤CDATA
    re_cdata = re.compile("//<!\[CDATA\[[^>]*//\]\]>", re.I)  # 匹配CDATA
    re_script = re.compile('<\s*script[^>]*>[^<]*<\s*/\s*script\s*>', re.I)  # Script
    re_style = re.compile('<\s*style[^>]*>[^<]*<\s*/\s*style\s*>', re.I)  # style
    re_br = re.compile('<br\s*?/?>')  # 处理换行
    re_h = re.compile('</?\w+[^>]*>')  # HTML标签
    re_comment = re.compile('<!--[^>]*-->')  # HTML注释
    s = re_cdata.sub('', htmlstr)  # 去掉CDATA
    s = re_script.sub('', s)  # 去掉SCRIPT
    s = re_style.sub('', s)  # 去掉style
    s = re_br.sub('\n', s)  # 将br转换为换行
    s = re_h.sub('', s)  # 去掉HTML 标签
    s = re_comment.sub('', s)  # 去掉HTML注释
    # 去掉多余的空行
    blank_line = re.compile('\n+')
    s = blank_line.sub('\n', s)
    s = replaceCharEntity(s)  # 替换实体
    return s

##替换常用HTML字符实体.
#使用正常的字符替换HTML中特殊的字符实体.
#你可以添加新的实体字符到CHAR_ENTITIES中,处理更多HTML字符实体.
#@param htmlstr HTML字符串.
def replaceCharEntity(htmlstr):
    CHAR_ENTITIES={'nbsp':' ','160':' ',
                'lt':'<','60':'<',
                'gt':'>','62':'>',
                'amp':'&','38':'&',
                'quot':'"','34':'"',}

    re_charEntity=re.compile(r'&#?(?P<name>\w+);')
    sz=re_charEntity.search(htmlstr)
    while sz:
        entity=sz.group()#entity全称，如&gt;
        key=sz.group('name')#去除&;后entity,如&gt;为gt
        try:
            htmlstr=re_charEntity.sub(CHAR_ENTITIES[key],htmlstr,1)
            sz=re_charEntity.search(htmlstr)
        except KeyError:
            #以空串代替
            htmlstr=re_charEntity.sub('',htmlstr,1)
            sz=re_charEntity.search(htmlstr)
    return htmlstr

def repalce(s,re_exp,repl_string):
    return re_exp.sub(repl_string,s)

class HospitalSpiderSpider(scrapy.Spider):
    name = 'hospital_spider'
    allowed_domains = ['http://www.tjmugh.com.cn/']
    start_urls = ['http://www.tjmugh.com.cn/ehibition/ehibition_default.asp?pro_id='+ str(x) for x in range(1, 999, 1)]



    def parse(self, response):
        # 实例化
        expert = HospitalgoItem()
        # 姓名
        expert['name'] = response.xpath('//*[@id="Table5"]/tr[1]/td[2]/text()').extract_first()
        #print(name)
        # 部门
        expert['department'] = response.xpath('//*[@id="Table5"]/tr[2]/td[2]/text()').extract_first()
        #print(department)
        # 职称
        expert['pro_title'] = response.xpath('//*[@id="Table5"]/tr[3]/td[2]/text()').extract_first()
        #print(pro_title)
        # 简历
        resume = response.xpath('//*[@id="Table5"]/tr[4]/td[2]').extract_first()
        # 清洗数据
        resume = filter_tags(str(resume))
        expert['resume'] = resume
        # print(resume)
        # print(expert)
        yield expert
        # for j in range(200,999):
        #     yield scrapy.Request('http://www.tjmugh.com.cn/ehibition/ehibition_default.asp?pro_id=' + str(j), callback=self.parse)

        # print(response.text)
        # pass
