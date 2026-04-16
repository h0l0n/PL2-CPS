class Item:
    """
    An available item inside the GildedRose.
    """
    def __init__(self, name: str, sell_in: int, quality: int):
        """
        Inicializa una instacia del objeto Item.

        Args:
            name: nombre del item
            sell_in: numero de dias restantes para venderlo
            quality: valor que denota como de valioso es el objeto
        """
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


class GildedRose:
    """
    Una tienda de items.
    """
    def __init__(self, items: list[Item]):
        """
        Crea una instancia de GildedRose que maneja el ciclo de vida de sus items.

        Args:
            items: conjunto de items a la venta
        """
        self.items = items
        self.max_quality = 50
        self.min_quality = 0

    def update_quality(self):
        """
        Actualiza el estado de cada uno de los items.
        """
        for item in self.items:

            if item.name == "Sulfuras, Hand of Ragnaros":  
                # no se modifica nada
                continue

            if item.name == "Aged Brie":
                # gana valor con el tiempo
                item.quality += 1

                # el doble de valor cuando ha pasado la fecha de venta
                if item.sell_in <= 0:
                    item.quality += 1

            elif item.name == "Backstage passes to a TAFKAL80ETC concert":
                # cuando ha pasado la fecha, no tiene valor
                if item.sell_in <= 0:
                    item.quality = 0
                # cuando se acerca mucho sube + 3
                elif item.sell_in <= 5:
                    item.quality += 3
                # cuando se acerca bastante sube +2
                elif item.sell_in <= 10:
                    item.quality += 2

            else:
                # items normales se degradan con el tiempo
                item.quality -= 1

                # los items se degradan el doble cuando se ha pasado la fecha de venta
                if item.sell_in <= 0:
                    item.quality -= 1

            # un dia menos
            item.sell_in -= 1
            item.quality = min(self.max_quality, max(self.min_quality, item.quality))
