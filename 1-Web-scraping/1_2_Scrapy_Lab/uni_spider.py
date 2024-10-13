import scrapy


class UniSpiderSpider(scrapy.Spider):
    name = "uni_spider"
    allowed_domains = ["www.uc3m.es"]
    start_urls = ["https://www.uc3m.es/bachelor-degree/data-science"]

    def parse(self, response):
      #1c print(response.xpath("//*[@id='program']").get())
      print(response.xpath("//*[@id='content']/div[2]/div[3]/div[2]/div/div[1]/div[1]/div[1]/table").get())
      #2a print(response.xpath('//a[span[text()="Web Analytics"]]/@href').get())
      #3b
      #yield{
      #  'url': response.xpath('//a[span[text()="Web Analytics"]]/@href').get()
      #}