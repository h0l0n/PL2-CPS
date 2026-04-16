# -*- coding: utf-8 -*-
import pytest

from first_gilded_rose import Item, GildedRose


def test_non_specified_item():
    """
    Tests that normal items quality decays 1 each day and 2 after sell_in <= 0
    """
    gilded_rose = GildedRose([Item("+5 Dexterity Vest", 10, 20)])
    item = Item("+5 Dexterity Vest", 10, 20)

    for _ in range(20):
        # calidad baja 1 (o 2 si sell_in <= 0). Nunca baja de 0.
        item.quality = item.quality - (1 if item.sell_in > 0 else 2)
        item.quality = max(0, item.quality)

        # sell_in siempre baja 1
        item.sell_in = item.sell_in - 1

        # logica real de la clase
        gilded_rose.update_quality()

    expected_values = (item.quality, item.sell_in)

    actual_values = (gilded_rose.items[0].quality, gilded_rose.items[0].sell_in)

    assert actual_values == expected_values


def test_sulfuras_hand_of_ragnaros():
    sulfuras = Item("Sulfuras, Hand of Ragnaros", 0, 80)
    gilded_rose = GildedRose([sulfuras])
    for _ in range(20):
        gilded_rose.update_quality()

    assert sulfuras.sell_in == 0
    assert sulfuras.quality == 80


def tests_aged_brie_quality_increases():
    aged_brie = Item("Aged Brie", 5, 7)
    gilded_rose = GildedRose([Item("Aged Brie", 5, 7)])

    for _ in range(20):
        # manual update
        aged_brie.quality += 1 if aged_brie.sell_in > 0 else 2
        aged_brie.sell_in -= 1

        # actual logic
        gilded_rose.update_quality()

    aged_brie.quality = min(50, aged_brie.quality)  # nunca mayor de 50

    expected_values = (aged_brie.quality, aged_brie.sell_in)
    actual_values = (gilded_rose.items[0].quality, gilded_rose.items[0].sell_in)

    assert actual_values == expected_values


def tests_backstage_passes_increases_quality_then_drops():
    backstage_passes = Item("Backstage passes to a TAFKAL80ETC concert", 5, 7)
    gilded_rose = GildedRose([Item("Backstage passes to a TAFKAL80ETC concert", 5, 7)])

    for _ in range(20):
        # manual update
        backstage_passes.sell_in -= 1
        if backstage_passes.sell_in > 0:
            backstage_passes.quality += 1
        else:
            backstage_passes.quality = 0

        # actual logic
        gilded_rose.update_quality()

    expected_values = (backstage_passes.quality, backstage_passes.sell_in)
    actual_values = (gilded_rose.items[0].quality, gilded_rose.items[0].sell_in)

    assert actual_values == expected_values


def tests_conjured_items_degrade_twice_as_fast():
    conjured = Item("Conjured Mana Cake", 3, 6)
    gilded_rose = GildedRose([Item("Conjured Mana Cake", 3, 6)])

    for _ in range(20):
        # manual update
        conjured.quality = conjured.quality - (1 if conjured.sell_in > 0 else 2)
        conjured.quality = max(0, conjured.quality)

        # sell_in siempre baja 1
        conjured.sell_in = conjured.sell_in - 1

        # actual logic
        gilded_rose.update_quality()

    expected_values = (conjured.quality, conjured.sell_in)
    actual_values = (gilded_rose.items[0].quality, gilded_rose.items[0].sell_in)

    assert actual_values == expected_values


def tests_no_item_quality_is_negative():
    gilded_rose = GildedRose(
        [
            Item(name="+5 Dexterity Vest", sell_in=10, quality=20),
            Item(name="Aged Brie", sell_in=2, quality=0),
            Item(name="Elixir of the Mongoose", sell_in=5, quality=7),
            Item(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80),
            Item(name="Sulfuras, Hand of Ragnaros", sell_in=-1, quality=80),
            Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=15, quality=20),
            Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=49),
            Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=49),
            Item(name="Conjured Mana Cake", sell_in=3, quality=6),
        ]
    )

    for _ in range(100):
        gilded_rose.update_quality()

    for item in gilded_rose.items:
        assert item.quality >= 0


def tests_no_item_quality_is_greater_than_50():  # except sulfuras
    gilded_rose = GildedRose(
        [
            Item(name="+5 Dexterity Vest", sell_in=10, quality=1000),
            Item(name="Aged Brie", sell_in=2, quality=100),
            Item(name="Elixir of the Mongoose", sell_in=5, quality=200),
            Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=15, quality=20),
            Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=60),
            Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=49),
            Item(name="Conjured Mana Cake", sell_in=3, quality=6),
        ]
    )

    for _ in range(50):
        gilded_rose.update_quality()

    for item in gilded_rose.items:
        assert item.quality <= 50
