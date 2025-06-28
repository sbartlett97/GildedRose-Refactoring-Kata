# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose, ExtendedItem


class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [ExtendedItem("foo", 0, 0, "standard")]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("foo", items[0].name)

        
if __name__ == '__main__':
    unittest.main()
