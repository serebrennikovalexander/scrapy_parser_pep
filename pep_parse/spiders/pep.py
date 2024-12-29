import scrapy

from pep_parse.items import PepParseItem
from pep_parse.settings import ALLOWED_DOMAINS, SPIDER_NAME, START_URLS


class PepSpider(scrapy.Spider):
    name = SPIDER_NAME
    allowed_domains = [ALLOWED_DOMAINS]
    start_urls = [START_URLS]

    def parse(self, response):
        all_peps = response.xpath('//a[starts-with(@href, "pep")]')
        for pep_link in all_peps:
            yield response.follow(pep_link, callback=self.parse_pep)

    def parse_pep(self, response):
        number, name = (
            response.xpath('//h1[@class="page-title"]/text()')
            .get()
            .split(' – ')
        )
        number = number.replace('PEP ', '')
        data = {
            'number': int(number),
            'name': name,
            'status': response.css('dt:contains("Status") + dd')
            .css('abbr::text')
            .get(),
        }
        yield PepParseItem(data)
