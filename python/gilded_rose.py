# -*- coding: utf-8 -*-
from typing import Literal

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            item.update_quality()


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
    

class StandardItem(Item):
    def __init__(self, name: str, sell_in: int, quality: int):
        super().__init__(name, sell_in, quality)

    def update_quality(self):
        if self.sell_in > 0 and self.quality > 0:
            self.quality -= 1
        elif self.sell_in <= 0 and self.quality > 0:
            self.quality -= 2
        self.sell_in -= 1
    
class MaturingItem(StandardItem):

    def update_quality(self):
        if self.sell_in > 0 and self.quality < 50:
            self.quality += 1
        self.sell_in -= 1


class BackstagePassesItem(StandardItem):

    def update_quality(self):
        if self.sell_in < 11 and self.quality < 50:
            self.quality += 2
        if self.sell_in < 6 and self.quality < 50:
            self.quality += 3
        elif self.quality < 50:
            self.quality += 1
        else:
            self.quality = 0
        self.sell_in -= 1

class LegendaryItem(StandardItem):

    def __init__(self, name: str, sell_in: int, quality: int):
        super().__init__(name, 0, 80)

    def update_quality(self):
        pass
    
class ConjuredItem(StandardItem):

    def update_quality(self):
        if self.sell_in > 0 and self.quality > 0:
            self.quality -= 2
        elif self.sell_in <= 0 and self.quality > 0:
            self.quality -= 4
        self.sell_in -= 1