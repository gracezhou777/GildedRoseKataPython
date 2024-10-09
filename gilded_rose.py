# -*- coding: utf-8 -*-


class Item:
    """ DO NOT CHANGE THIS CLASS!!!"""
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


class GildedRose(object):

    def __init__(self, items: list[Item]):
        # DO NOT CHANGE THIS ATTRIBUTE!!!
        self.items = items

    def update_quality(self):
        for item in self.items:
            if item.name == "Sulfuras, Hand of Ragnaros":
                continue
            if item.name == "Aged Brie":
                self._update_aged_brie(item)
            elif item.name == "Backstage passes to a TAFKAL80ETC concert":
                self._update_backstage_pass(item)
            elif item.name == "Conjured":
                self._update_conjured_item(item)
            else:
                self._update_normal_item(item)
            self._ensure_quality_limits(item)

    def _update_aged_brie(self, item):
        item.sell_in -= 1
        if item.quality < 50:
            item.quality += 1
        if item.sell_in < 0 and item.quality < 50:
            item.quality += 1

    def _update_backstage_pass(self, item):
        item.sell_in -= 1
        if item.sell_in < 0:
            item.quality = 0
        else:
            if item.quality < 50:
                item.quality += 1
            if item.sell_in < 10 and item.quality < 50:
                item.quality += 1
            if item.sell_in < 5 and item.quality < 50:
                item.quality += 1

    def _update_conjured_item(self, item):
        item.sell_in -= 1
        item.quality -= 2 if item.sell_in >= 0 else 4

    def _update_normal_item(self, item):
        item.sell_in -= 1
        item.quality -= 1 if item.sell_in >= 0 else 2

    def _ensure_quality_limits(self, item):
        if item.quality < 0:
            item.quality = 0
        elif item.quality > 50 and item.name != "Sulfuras, Hand of Ragnaros":
            item.quality = 50