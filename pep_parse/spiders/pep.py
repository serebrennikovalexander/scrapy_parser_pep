import scrapy
import re
from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = "pep"
    allowed_domains = ["peps.python.org"]
    start_urls = ["https://peps.python.org/"]

    def parse(self, response):
        all_peps = response.xpath('//a[starts-with(@href, "pep")]')
        for pep_link in all_peps:
            yield response.follow(pep_link, callback=self.parse_pep)

    def parse_pep(self, response):
        title = response.xpath('//h1[@class="page-title"]/text()').get()
        data = {
            "name": re.search(r"– (?P<name>.+)", title).group("name"),
            "number": re.search(r"(?P<number>\d+)", title).group("number"),
            "status": response.css('dt:contains("Status") + dd')
            .css("abbr::text")
            .get(),
        }
        yield PepParseItem(data)
