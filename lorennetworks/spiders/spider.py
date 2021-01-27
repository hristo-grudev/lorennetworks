import scrapy

from scrapy.loader import ItemLoader
from w3lib.html import remove_tags

from ..items import LorennetworksItem


class LorennetworksSpider(scrapy.Spider):
	name = 'lorennetworks'
	start_urls = ['https://lorennetworks.com/news/']

	def parse(self, response):
		posts = response.xpath('//div[@class="Wrap"]')
		for post in posts[2:]:
			title = post.xpath('.//div[@class="TitleBig"]').get()
			title = remove_tags(title).strip()
			description = post.xpath('.//div[@class="Content"]').get()
			description = remove_tags(description).strip()
			date = post.xpath('.//div[@class="PostDate"]/text()').get()
			print(description)

			item = ItemLoader(item=LorennetworksItem(), response=response)
			item.add_value('title', title)
			item.add_value('description', description)
			item.add_value('date', date)

			yield item.load_item()