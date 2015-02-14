#coding=utf-8
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.selector import HtmlXPathSelector,Selector
from lagou.items import LagouItem
from scrapy.http import Request

class lagouSpider(CrawlSpider):
    name = "lagouSpider"
    download_delay = 2
    allowed_domains = ["lagou.com"]
    start_urls=['http://www.lagou.com/']
    #翻页函数
    def parse(self, response):

        content = HtmlXPathSelector(response)
        start_url = content.xpath("//div[@class='menu_sub dn']/dl/dd/a/@href").extract()
        print start_url
        if start_url:
         for i in start_url:
            print '-------------------------------------------------------------------'
            print i
            urls = [i+'&pn='+str(n) for n in range(1,30)]
            for url in urls:
                yield  Request(url,callback=self.parse1)

    #一级页面
    def parse1(self, response):

        content = HtmlXPathSelector(response)
        jobs = content.xpath("//div[@class='hot_pos_l']//div[@class='mb10']/a/@href").extract()
        print jobs
        for job in jobs:
                 yield  Request(job, callback=self.parse2)
    #二级页面
    def parse2(self, response):

        content = HtmlXPathSelector(response)
        item = LagouItem()
        title = content.xpath("//dt[@class='clearfix']/h1/@title").extract()
        item['title'] = [t.encode('utf-8') for t in title]

        line = content.xpath("//dd[@class='job_request']/span/text()").extract()
        item['salary'] = [s.encode('utf-8') for s in line[0]]
        item['location'] = [l.encode('utf-8') for l in line[1]]
        item['founded'] = [f.encode('utf-8') for f in line[2]]
        item['degree_require'] = [d.encode('utf-8') for d in line[3]]

        item['tag'] = content.xpath("//dd[@class='job_request']/text()").extract()[5].split(":")[1].strip(' \n\t\r')

        company = content.xpath("//dl[@class='job_company']/dt/a/img/@alt").extract()[0]
        item['company'] = [c.encode('utf-8') for c in company]

        business_field = content.xpath("//dl[@class='job_company']//ul[@class='c_feature reset']/li/text()").extract()[0]
        item['business_field'] = [b.encode('utf-8') for b in business_field]
        item['size'] = content.xpath("//dl[@class='job_company']//ul[@class='c_feature reset']/li/text()").extract()[1]
        stage = content.xpath("//dl[@class='job_company']//ul[@class='c_feature reset']/li/text()").extract()[5]
        item['stage'] = [s.encode('utf-8') for s in stage]
        detail = content.xpath("//dd[@class='job_bt']/p/text()").extract()
        item['job_detail'] = [d.encode('utf-8') for d in detail]

        item['url'] = response.url

        yield item

