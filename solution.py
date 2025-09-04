# solution.py
from typing import List, Optional, Union


# === Produkty ===
class PaperProduct:
    def __init__(self, product_type: str = "PaperProduct") -> None:
        self.product_type: str = product_type
        # konkretne klasy ustawiają self.name

    def get_name(self) -> str:
        return "PaperProduct"

    def get_product_type(self) -> str:
        return self.product_type


class FoodProduct:
    def __init__(self, product_type: str = "FoodProduct") -> None:
        self.product_type: str = product_type
        # konkretne klasy ustawiają self.name

    def get_name(self) -> str:
        return "FoodProduct"

    def get_product_type(self) -> str:
        return self.product_type


# --- Konkrety papiernicze ---
class Pen(PaperProduct):
    def __init__(self) -> None:
        super().__init__("PaperProduct")
        self.name = "Pen"

    def get_name(self) -> str:
        return "Pen"


class Notebook(PaperProduct):
    def __init__(self) -> None:
        super().__init__("PaperProduct")
        self.name = "Notebook"

    def get_name(self) -> str:
        return "Notebook"


# --- Konkrety spożywcze ---
class Bread(FoodProduct):
    def __init__(self) -> None:
        super().__init__("FoodProduct")
        self.name = "Bread"

    def get_name(self) -> str:
        return "Bread"


class MineralWater(FoodProduct):
    def __init__(self) -> None:
        super().__init__("FoodProduct")
        self.name = "MineralWater"

    def get_name(self) -> str:
        return "MineralWater"


# === Sklep ===
class Shop:
    def __init__(self) -> None:
        self.food_products: List[FoodProduct] = []
        self.paper_products: List[PaperProduct] = []

    def add_to_store(self, product: Union[FoodProduct, PaperProduct]) -> None:
        if isinstance(product, FoodProduct) and not isinstance(product, PaperProduct):
            self.food_products.append(product)
        elif isinstance(product, PaperProduct) and not isinstance(product, FoodProduct):
            self.paper_products.append(product)
        else:
            # awaryjnie – wrzuć według dostępnej bazy
            if isinstance(product, FoodProduct):
                self.food_products.append(product)
            elif isinstance(product, PaperProduct):
                self.paper_products.append(product)

    def check_availability(self, item: Union[str, FoodProduct, PaperProduct]) -> bool:
        if isinstance(item, str):
            return any(p.get_name() == item for p in self.food_products) or \
                   any(p.get_name() == item for p in self.paper_products)
        if isinstance(item, FoodProduct) and not isinstance(item, PaperProduct):
            return any(p.get_name() == item.get_name() for p in self.food_products)
        if isinstance(item, PaperProduct) and not isinstance(item, FoodProduct):
            return any(p.get_name() == item.get_name() for p in self.paper_products)
        return False

    def sell_food_product(self, name: str) -> Optional[FoodProduct]:
        for i, p in enumerate(self.food_products):
            if p.get_name() == name:
                return self.food_products.pop(i)
        return None

    def sell_paper_product(self, name: str) -> Optional[PaperProduct]:
        for i, p in enumerate(self.paper_products):
            if p.get_name() == name:
                return self.paper_products.pop(i)
        return None

    def print_product_list(self) -> None:
        # Dokładnie taki format, jakiego oczekuje test:
        # najpierw papierowe, potem spożywcze; jedna nazwa na linię.
        lines = [p.get_name() for p in self.paper_products] + \
                [p.get_name() for p in self.food_products]
        print("\n".join(lines))


# === Dostawca ===
class Supplier:
    def __init__(self, shop: Shop) -> None:
        self.shop: Shop = shop

    def deliver_product(self, product: Union[FoodProduct, PaperProduct]) -> None:
        self.shop.add_to_store(product)

