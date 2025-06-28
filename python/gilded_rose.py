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
            self.quality = self.quality - 1 if self.quality > 1 else 0
        elif self.sell_in <= 0 and self.quality > 0:
            self.quality = self.quality - 2 if self.quality > 2 else 0
        else:
            self.quality = 0
        self.sell_in -= 1
    
class MaturingItem(StandardItem):

    def update_quality(self):
        if self.sell_in >= 0 and self.quality < 50:
            self.quality = self.quality + 1 if self.quality < 49 else 50
        self.sell_in -= 1


class BackstagePassesItem(StandardItem):

    def update_quality(self):
        if self.sell_in > 10 and self.quality < 50:
            self.quality = self.quality + 1 if self.quality < 49 else 50
        if self.sell_in < 11 and self.sell_in > 5 and self.quality < 50:
            self.quality = self.quality + 2 if self.quality < 49 else 50
        elif self.sell_in < 6 and self.sell_in > 0 and self.quality < 50:
            self.quality = self.quality + 3 if self.quality < 48 else 50
        elif self.sell_in <= 0:
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
            self.quality = self.quality - 2 if self.quality > 2 else 0
        elif self.sell_in <= 0 and self.quality > 0:
            self.quality = self.quality - 4 if self.quality > 4 else 0
        else:
            self.quality = 0
        self.sell_in -= 1