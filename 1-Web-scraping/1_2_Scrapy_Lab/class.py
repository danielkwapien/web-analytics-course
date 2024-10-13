import scrapy


class ClassSpider(scrapy.Spider):
    name = "class"
    allowed_domains = ["aplicaciones.uc3m.es"]
    start_urls = ["https://aplicaciones.uc3m.es/cpa/generaFicha?&est=350&plan=392&asig=16507&idioma=2"]

    def parse(self, response):
      #2c 
      print(response.xpath('//div[@class="panel panel-primary apartado"]//div[@class="panel-heading degradado" and contains(text(),"Description of contents")]/following-sibling::div[@class="panel-body"]//div[@class="tarea"]/text()').getall())
      #3b
      #yield{'text':response.xpath('//div[@class="panel panel-primary apartado"]//div[@class="panel-heading degradado" and contains(text(),"Description of contents")]/following-sibling::div[@class="panel-body"]//div[@class="tarea"]/text()').getall()}
