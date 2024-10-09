# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals("fixme", items[0].name)

#Example
    def test_vest_item_should_decrease_after_one_day(self):

        vest = "+5 Dexterity Vest"
        items = [Item(vest, 1, 2), Item(vest, 9, 19), Item(vest, 4, 6), ]
        gr = GildedRose(items)
        gr.update_quality()

        assert gr.get_items_by_name(vest) == [Item(vest, 0, 1), Item(vest, 8, 18), Item(vest, 3, 5)]

#Three failed tests
#1. "Aged Brie" actually increases in Quality the older it gets
    def test_aged_brie_increases_in_quality(self):
        brie = "Aged Brie"
        items = [Item(brie, 2, 0), Item(brie, 1, 10), Item(brie, 5, 49)]
        gr = GildedRose(items)

        gr.update_quality()

        expected_items = [
            Item(brie, 1, 1),
            Item(brie, 0, 11),
            Item(brie, 4, 50)
        ]
        for expected, actual in zip(expected_items, gr.items):
            self.assertEqual(expected.name, actual.name)
            self.assertEqual(expected.sell_in, actual.sell_in)
            self.assertEqual(expected.quality, actual.quality)

#2. The Quality of an item is never more than 50
    def test_quality_never_more_than_50(self):
        brie = "Aged Brie"
        items = [
            Item(brie, 2, 55)
        ]

        gr = GildedRose(items)

        gr.update_quality()

        assert gr.items[0].quality <= 50

#3. "Sulfuras", being a legendary item, never has to be sold or decreases in Quality
    def test_sulfuras_does_not_change(self):
        sulfuras = "Sulfuras, Hand of Ragnaros"
        items = [Item(sulfuras, 0, 80), Item(sulfuras, -1, 80)]
        gr = GildedRose(items)

        gr.update_quality()

        expected_items = [
            Item(sulfuras, 0, 80),
            Item(sulfuras, -1, 80)
        ]
        for expected, actual in zip(expected_items, gr.items):
            self.assertEqual(expected.name, actual.name)
            self.assertEqual(expected.sell_in, actual.sell_in)
            self.assertEqual(expected.quality, actual.quality)

if __name__ == '__main__':
    unittest.main()
