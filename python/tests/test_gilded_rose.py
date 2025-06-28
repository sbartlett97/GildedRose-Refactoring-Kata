# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose, StandardItem, MaturingItem, BackstagePassesItem, LegendaryItem, ConjuredItem


class GildedRoseTest(unittest.TestCase):
    
    def test_standard_item_before_sell_date(self):
        """Test standard item quality decreases by 1 before sell date"""
        items = [StandardItem("Standard Item", 10, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        
        self.assertEqual(9, items[0].sell_in)
        self.assertEqual(19, items[0].quality)
    
    def test_standard_item_after_sell_date(self):
        """Test standard item quality decreases by 2 after sell date"""
        items = [StandardItem("Standard Item", 0, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        
        self.assertEqual(-1, items[0].sell_in)
        self.assertEqual(18, items[0].quality)
    
    def test_standard_item_quality_never_negative(self):
        """Test standard item quality never goes below 0"""
        items = [StandardItem("Standard Item", 5, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        
        self.assertEqual(4, items[0].sell_in)
        self.assertEqual(0, items[0].quality)
    
    def test_standard_item_quality_never_negative_after_sell_date(self):
        """Test standard item quality never goes below 0 even after sell date"""
        items = [StandardItem("Standard Item", 0, 1)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        
        self.assertEqual(-1, items[0].sell_in)
        self.assertEqual(0, items[0].quality)
    
    def test_maturing_item_increases_quality(self):
        """Test Aged Brie increases in quality as it gets older"""
        items = [MaturingItem("Aged Brie", 10, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        
        self.assertEqual(9, items[0].sell_in)
        self.assertEqual(21, items[0].quality)
    
    def test_maturing_item_quality_never_above_50(self):
        """Test Aged Brie quality never exceeds 50"""
        items = [MaturingItem("Aged Brie", 10, 50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        
        self.assertEqual(9, items[0].sell_in)
        self.assertEqual(50, items[0].quality)
    
    def test_maturing_item_after_sell_date(self):
        """Test Aged Brie continues to increase quality after sell date"""
        items = [MaturingItem("Aged Brie", 0, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        
        self.assertEqual(-1, items[0].sell_in)
        self.assertEqual(21, items[0].quality)
    
    def test_backstage_passes_more_than_10_days(self):
        """Test backstage passes increase quality by 1 when more than 10 days left"""
        items = [BackstagePassesItem("Backstage passes to a TAFKAL80ETC concert", 15, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        
        self.assertEqual(14, items[0].sell_in)
        self.assertEqual(21, items[0].quality)
    
    def test_backstage_passes_10_days_or_less(self):
        """Test backstage passes increase quality by 2 when 10 days or less"""
        items = [BackstagePassesItem("Backstage passes to a TAFKAL80ETC concert", 10, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        
        self.assertEqual(9, items[0].sell_in)
        self.assertEqual(22, items[0].quality)
    
    def test_backstage_passes_5_days_or_less(self):
        """Test backstage passes increase quality by 3 when 5 days or less"""
        items = [BackstagePassesItem("Backstage passes to a TAFKAL80ETC concert", 5, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        
        self.assertEqual(4, items[0].sell_in)
        self.assertEqual(23, items[0].quality)
    
    def test_backstage_passes_quality_never_above_50(self):
        """Test backstage passes quality never exceeds 50"""
        items = [BackstagePassesItem("Backstage passes to a TAFKAL80ETC concert", 5, 49)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        
        self.assertEqual(4, items[0].sell_in)
        self.assertEqual(50, items[0].quality)
    
    def test_backstage_passes_after_concert(self):
        """Test backstage passes quality drops to 0 after concert"""
        items = [BackstagePassesItem("Backstage passes to a TAFKAL80ETC concert", 0, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        
        self.assertEqual(-1, items[0].sell_in)
        self.assertEqual(0, items[0].quality)
    
    def test_legendary_item_never_changes(self):
        """Test Sulfuras never has to be sold or decreases in quality"""
        items = [LegendaryItem("Sulfuras, Hand of Ragnaros", 0, 80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        
        self.assertEqual(0, items[0].sell_in)  # Sulfuras sell_in is always 0
        self.assertEqual(80, items[0].quality)  # Sulfuras quality is always 80
    
    def test_legendary_item_initialization(self):
        """Test Sulfuras is initialized with correct values regardless of input"""
        items = [LegendaryItem("Sulfuras, Hand of Ragnaros", 10, 50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        
        self.assertEqual(0, items[0].sell_in)  # Sulfuras sell_in is always 0
        self.assertEqual(80, items[0].quality)  # Sulfuras quality is always 80
    
    def test_conjured_item_before_sell_date(self):
        """Test conjured items degrade twice as fast as normal items before sell date"""
        items = [ConjuredItem("Conjured Mana Cake", 10, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        
        self.assertEqual(9, items[0].sell_in)
        self.assertEqual(18, items[0].quality)  # Decreased by 2 instead of 1
    
    def test_conjured_item_after_sell_date(self):
        """Test conjured items degrade twice as fast as normal items after sell date"""
        items = [ConjuredItem("Conjured Mana Cake", 0, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        
        self.assertEqual(-1, items[0].sell_in)
        self.assertEqual(16, items[0].quality)  # Decreased by 4 instead of 2
    
    def test_conjured_item_quality_never_negative(self):
        """Test conjured item quality never goes below 0"""
        items = [ConjuredItem("Conjured Mana Cake", 5, 1)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        
        self.assertEqual(4, items[0].sell_in)
        self.assertEqual(0, items[0].quality)
    
    def test_conjured_item_quality_never_negative_after_sell_date(self):
        """Test conjured item quality never goes below 0 even after sell date"""
        items = [ConjuredItem("Conjured Mana Cake", 0, 3)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        
        self.assertEqual(-1, items[0].sell_in)
        self.assertEqual(0, items[0].quality)
    
    def test_multiple_items_update(self):
        """Test multiple items of different types update correctly"""
        items = [
            StandardItem("Standard Item", 10, 20),
            MaturingItem("Aged Brie", 10, 20),
            BackstagePassesItem("Backstage passes to a TAFKAL80ETC concert", 10, 20),
            LegendaryItem("Sulfuras, Hand of Ragnaros", 10, 50),
            ConjuredItem("Conjured Mana Cake", 10, 20)
        ]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        
        # Standard item: quality -1, sell_in -1
        self.assertEqual(9, items[0].sell_in)
        self.assertEqual(19, items[0].quality)
        
        # Aged Brie: quality +1, sell_in -1
        self.assertEqual(9, items[1].sell_in)
        self.assertEqual(21, items[1].quality)
        
        # Backstage passes: quality +2, sell_in -1
        self.assertEqual(9, items[2].sell_in)
        self.assertEqual(22, items[2].quality)
        
        # Sulfuras: no change
        self.assertEqual(0, items[3].sell_in)
        self.assertEqual(80, items[3].quality)
        
        # Conjured: quality -2, sell_in -1
        self.assertEqual(9, items[4].sell_in)
        self.assertEqual(18, items[4].quality)
    
    def test_edge_case_quality_at_50(self):
        """Test items at quality 50 behave correctly"""
        items = [
            StandardItem("Standard Item", 10, 50),
            MaturingItem("Aged Brie", 10, 50),
            BackstagePassesItem("Backstage passes to a TAFKAL80ETC concert", 10, 50)
        ]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        
        # Standard item can decrease from 50
        self.assertEqual(49, items[0].quality)
        
        # Aged Brie stays at 50
        self.assertEqual(50, items[1].quality)
        
        # Backstage passes stay at 50
        self.assertEqual(50, items[2].quality)
    
    def test_edge_case_quality_at_0(self):
        """Test items at quality 0 behave correctly"""
        items = [
            StandardItem("Standard Item", 10, 0),
            MaturingItem("Aged Brie", 10, 0),
            ConjuredItem("Conjured Mana Cake", 10, 0)
        ]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        
        # Standard item stays at 0
        self.assertEqual(0, items[0].quality)
        
        # Aged Brie can increase from 0
        self.assertEqual(1, items[1].quality)
        
        # Conjured item stays at 0
        self.assertEqual(0, items[2].quality)
    
    def test_backstage_passes_edge_cases(self):
        """Test backstage passes edge cases around day boundaries"""
        # Test exactly 10 days
        items = [BackstagePassesItem("Backstage passes to a TAFKAL80ETC concert", 10, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(22, items[0].quality)  # Should increase by 2
        
        # Test exactly 5 days
        items = [BackstagePassesItem("Backstage passes to a TAFKAL80ETC concert", 5, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(23, items[0].quality)  # Should increase by 3
        
        # Test exactly 0 days (concert day)
        items = [BackstagePassesItem("Backstage passes to a TAFKAL80ETC concert", 0, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].quality)  # Should drop to 0


if __name__ == '__main__':
    unittest.main()
