from scrapy import Selector
from scrapy.loader import  ItemLoader
from itemloaders.processors import TakeFirst, MapCompose

def get_characteritics(item) -> dict:
    selector = Selector(text=item)
    return {
        "name": selector.xpath(
            "//div[contains(@class, 'AdvertSpecs_label')]/text()"
        ).extract_first(),
        "value": selector.xpath(
            "//div[contains(@class, 'AdvertSpecs_data')]//text()"
        ).extract_first(),
    }

def some(data:dict):
    data["new_key"] = "hello"
    return data

class AutoyoulaLoader(ItemLoader):
    default_item_class = dict
    # url_out = TakeFirst()
    # title_out = TakeFirst()
    characteristics_in = MapCompose(get_characteritics, some)