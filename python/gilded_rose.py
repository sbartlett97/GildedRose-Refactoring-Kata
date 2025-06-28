# -*- coding: utf-8 -*-
from typing import Literal

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            if item.type == "standard":
                if item.sell_in > 0 and item.quality > 0:
                    item.quality -= 1
                elif item.sell_in <= 0 and item.quality > 0:
                    item.quality -= 2
            elif item.type == "maturing":
                if item.sell_in > 0 and item.quality < 50:
                    item.quality += 1
            elif item.type == "backstage_passes":
                if item.sell_in < 11 and item.quality < 50:
                    item.quality += 2
                if item.sell_in < 6 and item.quality < 50:
                    item.quality += 3
                elif item.quality < 50:
                    item.quality += 1
                else:
                    item.quality = 0
            elif item.type == "legendary":
                pass


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
    

class ExtendedItem(Item):
    def __init__(self, name: str, sell_in: int, quality: int, type: Literal["standard", "maturing", "backstage_passes", "legendary", "conjured"]):
        super().__init__(name, sell_in, quality)
        self.type = type

    def __repr__(self):
        return "%s, %s, %s, %s" % (self.name, self.sell_in, self.quality, self.type)
    