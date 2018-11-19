from scrapy.cmdline import execute
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__))) #加入该模块
execute(["scrapy", "crawl", "hospital_spider"]) #相当于命令行 scrapy crawl jobbole(之前设置的爬虫名称)
