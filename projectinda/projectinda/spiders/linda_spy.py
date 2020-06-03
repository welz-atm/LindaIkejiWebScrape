# -*- coding: utf-8 -*-
import scrapy


class LindaSpySpider(scrapy.Spider):
    name = 'linda_spy'
    page_number = 2
    start_urls = ['http://lindaikejisblog.com/']


    def parse(self, response):

        linda_container = response.css('.story_block')

        for article in linda_container:

            title = article.css('.story_title a::text').extract()
            news_url = article.css('.story_title a::attr(href)').extract()
            date_posted = article.css('.post_age::text').extract()


            #zipped_data =zip(title,news_url,date_posted)

            #for item in zipped_data:

            scraped_data = {
                'Title' : title,
                'news_url' : news_url,
                'date_posted' : date_posted
            }

            yield scraped_data


        next_page  = 'https://www.lindaikejisblog.com/page/' + str(LindaSpySpider.page_number)
        if LindaSpySpider.page_number <= 200:
            LindaSpySpider.page_number += 1
            yield response.follow(next_page , callback= self.parse)


        #pass
