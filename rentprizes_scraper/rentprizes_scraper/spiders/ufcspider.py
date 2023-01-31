import scrapy


class RentSpider(scrapy.Spider):
    name = 'ufc'
    start_urls = ['http://ufcstats.com/statistics/events/completed?page=all']

    def parse(self, response):

        counter = 0
        for offer in response.css('a.b-link_style_black'):
            if counter == 5:
                break
            fight_link = offer.attrib['href']
            request = scrapy.Request(fight_link, callback=self.parseEventInfo)
            counter += 1
            yield request
    
    def parseEventInfo(self, response):
        fight_links = response.css('tbody.b-fight-details__table-body').css('tr.b-fight-details__table-row::attr(onclick)').extract()

        counter = 0
        for row in fight_links:
            if counter == 5:
                break
            next_page = row.replace("doNav('", '').replace("')", '')
            request = scrapy.Request(next_page, callback=self.parseFightInfo)
            counter += 1

            yield request


    def parseFightInfo(self, response):
        fight_details = response.css('div.b-fight-details__content')
        fight_columns = response.css('td.b-fight-details__table-col')
        win_lose = response.css('i.b-fight-details__person-status::text').getall()
        win_lose = [x.strip() for x in win_lose] 

        table_detail = 'p.b-fight-details__table-text::text'

        figter_1_points = 'K/O'
        figter_2_points = 'K/O'

        if fight_details.css('p.b-fight-details__text')[-1].css('i.b-fight-details__text-item::text'):
            figter_1_points = 0
            figter_2_points = 0
            for index in range(1, 6, 2):
                points = fight_details.css('p.b-fight-details__text')[-1].css('i.b-fight-details__text-item::text')[index].get().strip().replace(' ', '').replace('.','').split('-')
                figter_1_points += int(points[0])
                figter_2_points += int(points[1])

        yield {
            'fighter1': {
                'name': fight_columns[0].css('a.b-link.b-link_style_black::text')[0].get(),
                'fight_status': win_lose[0],
                'kd': fight_columns[1].css(table_detail)[0].get().strip(),
                'sig_str': fight_columns[2].css(table_detail)[0].get().strip(),
                'sig_str_%': fight_columns[3].css(table_detail)[0].get().strip(),
                'total_str': fight_columns[4].css(table_detail)[0].get().strip(),
                'td': fight_columns[5].css(table_detail)[0].get().strip(),
                'td_%': fight_columns[6].css(table_detail)[0].get().strip(),
                'sub_att': fight_columns[7].css(table_detail)[0].get().strip(),
                'rev': fight_columns[8].css(table_detail)[0].get().strip(),
                'ctrl': fight_columns[9].css(table_detail)[0].get().strip(),
                'points': figter_1_points
            },
            'fighter2': {
                'name': fight_columns[0].css('a.b-link.b-link_style_black::text')[1].get(),
                'fight_status': win_lose[1],
                'kd': fight_columns[1].css(table_detail)[1].get().strip(),
                'sig_str': fight_columns[2].css(table_detail)[1].get().strip(),
                'sig_str_%': fight_columns[3].css(table_detail)[1].get().strip(),
                'total_str': fight_columns[4].css(table_detail)[1].get().strip(),
                'td': fight_columns[5].css(table_detail)[1].get().strip(),
                'td_%': fight_columns[6].css(table_detail)[1].get().strip(),
                'sub_att': fight_columns[7].css(table_detail)[1].get().strip(),
                'rev': fight_columns[8].css(table_detail)[1].get().strip(),
                'ctrl': fight_columns[9].css(table_detail)[1].get().strip(),
                'points': figter_2_points
            },
            'method': fight_details.css('i.b-fight-details__text-item_first')[0].css('i::text')[3].get(),
            'round': fight_details.css('i.b-fight-details__text-item::text')[1].get().strip(),
            'time_format': fight_details.css('i.b-fight-details__text-item::text')[5].get().strip(),
            'k/o_details':  fight_details.css('p.b-fight-details__text::text')[-1].get().strip()  
        }






