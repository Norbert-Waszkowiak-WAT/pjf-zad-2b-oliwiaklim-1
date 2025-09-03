import sys
import unittest
from io import StringIO

from solution import Shop, Supplier, Notebook, Bread, Pen, MineralWater

class TestShop(unittest.TestCase):
    def setUp(self):
        self.shop = Shop()
        self.supplier = Supplier(self.shop)
        self.notebook = Notebook()
        self.bread = Bread()
        self.pen = Pen()
        self.mineral_water = MineralWater()

    def test_add_product(self):
        self.supplier.deliver_product(self.notebook)
        self.assertIn(self.notebook, self.shop.paper_products)

    def test_add_product_again(self):
        self.supplier.deliver_product(self.bread)
        self.assertIn(self.bread, self.shop.food_products)

    def test_check_availability(self):
        self.supplier.deliver_product(self.pen)
        self.assertTrue(self.shop.check_availability("Pen"))

    def test_check_availability_again(self):
        self.assertFalse(self.shop.check_availability("NotExistingProduct"))

    def test_sell_food_product(self):
        self.supplier.deliver_product(self.bread)
        self.shop.sell_food_product("Bread")
        self.assertNotIn(self.bread, self.shop.food_products)

    def test_sell_food_product_again(self):
        self.shop.sell_food_product("NotExistingProduct")
        self.assertNotIn("NotExistingProduct", [product.name for product in self.shop.food_products])

    def test_sell_paper_product(self):
        self.supplier.deliver_product(self.notebook)
        self.shop.sell_paper_product("Notebook")
        self.assertNotIn(self.notebook, self.shop.paper_products)

    def test_sell_paper_product_again(self):
        self.shop.sell_paper_product("NotExistingProduct")
        self.assertNotIn("NotExistingProduct", [product.name for product in self.shop.paper_products])

    def test_print_product_list(self):
        self.supplier.deliver_product(self.notebook)
        self.supplier.deliver_product(self.bread)
        self.supplier.deliver_product(self.pen)
        self.supplier.deliver_product(self.mineral_water)

        # Przechwycenie standardowego wyjścia
        captured_output = StringIO()
        sys.stdout = captured_output

        # Wywołanie metody print_product_list
        self.shop.print_product_list()

        # Przywrócenie standardowego wyjścia
        sys.stdout = sys.__stdout__

        # Sprawdzenie, czy wydrukowano poprawną listę produktów
        expected_output = "Notebook\nPen\nBread\nMineralWater"
        self.assertEqual(captured_output.getvalue().strip(), expected_output)


if __name__ == '__main__':
    unittest.main()
