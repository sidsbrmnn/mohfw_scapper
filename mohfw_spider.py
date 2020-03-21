import scrapy
import csv


class MohfwSpider(scrapy.Spider):
    name = 'mohfw'
    allowed_domains = ['mohfw.gov.in']
    start_urls = ['https://www.mohfw.gov.in/']

    def parse(self, response):
        trs = response.xpath('//table/tbody/tr')
        states = []
        for tr in trs[:-1]:
            item = dict()
            item['state'] = tr.xpath('td[2]//text()').extract_first()
            item['confirmed_local'] = tr.xpath('td[3]//text()').extract_first()
            item['confirmed_intl'] = tr.xpath('td[4]//text()').extract_first()
            item['cured'] = tr.xpath('td[5]//text()').extract_first()
            item['death'] = tr.xpath('td[6]//text()').extract_first()
            states.append(item)

        with open('covid_data.csv', 'w') as myfile:
            wr = csv.DictWriter(myfile, states[0].keys())
            wr.writeheader()
            wr.writerows(states)
