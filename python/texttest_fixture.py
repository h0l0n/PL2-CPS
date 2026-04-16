# -*- coding: utf-8 -*-
from __future__ import print_function

from gilded_rose import *


def main():
    print("OMGHAI!")
    items = [
        Item(name="+5 Dexterity Vest", sell_in=10, quality=20),
        Item(name="Aged Brie", sell_in=2, quality=0),
        Item(name="Elixir of the Mongoose", sell_in=5, quality=7),
        Item(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80),
        Item(name="Sulfuras, Hand of Ragnaros", sell_in=-1, quality=80),
        Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=15, quality=20),
        Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=49),
        Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=49),
        Item(name="Conjured Mana Cake", sell_in=3, quality=6),  # <-- :O
    ]
    days = 2
    import sys

    if len(sys.argv) > 1:
        days = int(sys.argv[1]) + 1
    for day in range(days):
        print("=" * 25 + f"{f"day {day}":^10}" + "=" * 25)
        print(f"{"name":41} | {"sellIn":6} | {"quality":7}")
        print("=" * 60)
        for item in items:
            print(f"{item.name:41} | {item.sell_in:6} | {item.quality:7}")
        print("")
        GildedRose(items).update_quality()


if __name__ == "__main__":
    main()
