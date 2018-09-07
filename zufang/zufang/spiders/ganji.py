import scrapy
import sqlite3

from ..items import ZufangItem


class GanjiSpyder(scrapy.Spider):
    name = "zufang"
    start_urls = ['file:///tmp/tmp9cgcb85n.html']

    def parse(self, response):
        print(response)
        zf = ZufangItem()
        title_list = response.xpath(".//div[@class='f-list-item ershoufang-list']/dl/dd[1]/a/text()").extract()
        money_list = response.xpath(
            ".//div[@class='f-list-item ershoufang-list']/dl/dd[5]/div[1]/span[1]/text()").extract()
        for i, j in zip(title_list, money_list):
            # print(i, ':', j)
            zf['title'] = i
            zf['money'] = j
            yield zf
