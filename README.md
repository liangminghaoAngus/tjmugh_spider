# tjmugh_spider
a demo using scrapy for  tjmugh_spider

# 爬取天津医科大学总医院专家信息
## 运行环境

> * python 3.6.7
> * Scrapy 1.5.1
> * JetBrains PyCharm 2017.1 x64

## [安装](https://www.imooc.com/video/17514)（点我）
参考上述课程的链接

clone
```
git clone https://github.com/liangminghaoAngus/tjmugh_spider.git
```
进入项目文件夹
```
cd tjmugh_spider
```

## 项目结构
```
+-- README.md
+-- scrapy.cfg
+-- hospitalgo
|  +--  __init__.py
|  +-- items.py
|  +-- main.py
|  +-- middlewares.py
|  +-- pipelines.py
|  +-- settings.py
|  +-- spiders
    │  |  +-- hospital_spider.py
    │  |  +-- data0.csv
    │  |  +-- data0.json #这个 json 文件有点问题
    │  |  +--  __init__.py
``` 
## 运行
```
cd hospitalgo/spiders
scrapy crawl hospital_spider -o data0.csv
或者 scrapy crawl hospital_spider -o data0.json
```
MIT
联系方式：linagminghaoangus@163.com
## Rookie project
