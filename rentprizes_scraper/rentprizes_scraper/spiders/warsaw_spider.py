import scrapy


class WarszawaSpider(scrapy.Spider):

    def __init__(self):
        self.target_offers = 0
        self.all_offers = 0
        self.rooms = 0
        self.urls = [
            'https://www.olx.pl/d/nieruchomosci/mieszkania/wynajem/warszawa/?search%5Bfilter_enum_rooms%5D%5B0%5D=two',
            'https://www.olx.pl/d/nieruchomosci/mieszkania/wynajem/warszawa/?search%5Bfilter_enum_rooms%5D%5B0%5D=three',
            'https://www.olx.pl/d/nieruchomosci/mieszkania/wynajem/warszawa/?search%5Bfilter_enum_rooms%5D%5B0%5D=four'
            ]

    name = 'warszawa'
    start_urls = [
        'https://www.olx.pl/d/nieruchomosci/mieszkania/wynajem/warszawa/?search%5Bfilter_enum_rooms%5D%5B0%5D=one',
    ]


    def parse(self, response):
        
        offers_number = "".join(response.css('div[data-testid="total-count"]::text').extract())

        self.all_offers = int(''.join([x for x in offers_number if x.isdigit()]))

        if self.all_offers == 1000:
            self.all_offers = 100000
        
        for offers in response.css('a.css-rc5s2u'):
            if self.target_offers <= self.all_offers:
                yield {
                    'name': offers.css('h6.css-16v5mdi::text').get(),
                    'price': offers.css('p[data-testid="ad-price"]::text').get(),
                    'location': offers.css('p[data-testid="location-date"]::text').extract()[0],
                    'm2': offers.css('span.css-643j0o::text').get(),
                    'link': 'https://www.olx.pl' + offers.css('a.css-rc5s2u').attrib['href'],
                    'date': offers.css('p[data-testid="location-date"]::text').extract()[2],
                    'rooms': self.rooms + 1
                }
                self.target_offers += 1
        
        np_button = response.css('a[data-testid="pagination-forward"]')

        print(self.target_offers)
        print(self.all_offers)
        if np_button != [] and self.target_offers <= self.all_offers:
            next_page = 'https://www.olx.pl' + np_button.attrib['href']
            yield response.follow(next_page, callback=self.parse)
        elif self.rooms < 3:
            self.target_offers = 0
            self.rooms += 1
            yield response.follow(self.urls[self.rooms - 1], callback=self.parse)
