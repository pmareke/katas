from app.domain.item import Item


class GildedRose:

    @staticmethod
    def update_quality(items: list[Item]) -> None:
        for item in items:
            item.update()
