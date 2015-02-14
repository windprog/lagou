import scrapy
from scrapy.contrib.spiders import CrawlSpider, Rule 
from scrapy.contrib.linkextractors import LinkExtractor
from lagou.items import JobItem

class LagouSpider(CrawlSpider):
    name = "lagouJob"

    download_delay = 2

    allowed_domains = ["lagou.com"]
    start_urls = [
        "http://www.lagou.com/"
    ]
    rules = [Rule(LinkExtractor(allow=['/jobs/\d+\.html']), 'parse_job')]

#    def start_requests(self):
#        return [scrapy.FormRequest("http://passport.lagou.com/login/login.html",
#                                    formdata={'email':'lintan49@aliyun.com', 'password':'testtest'},
#                                    callback=self.logged_in)]
#    def logged_in(self, response):
#        return response.url

    def parse_job(self, response):
        job = JobItem()
        job['title'] = response.xpath("//head/title/text()").extract()
        job['company'] = response.xpath("//head/meta/text()").extract()
        job['request'] = response.xpath("//body/div[@id='container']/div/div/dl/dd/text()").extract()
        job['desc'] =  "empty"
        job['respon'] = "empty"
        job['link'] = response.url
        return job

#    def parse(self, response):
#        self.log('current url is: %s' % response.url)
#        for sel in response.xpath('//ul/li'):
#            title = sel.xpath('a/text()').extract()
#            link = sel.xpath('a/@href').extract()
#            desc = sel.xpath('text()').extract()
#            print title, link, desc
#
