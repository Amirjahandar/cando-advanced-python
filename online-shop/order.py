from typing import List, Optional
from datetime import date
from product import *
from order import *


class Cart:
    def __init__(self):
        self.products: List[Product] = []
        self.total_price = 0.0
        self.date = date.today()

    @property
    def total_price(self):
        return self.total_price
    @total_price.setter
    def total_price(self):
        self.total_price = sum([p.price for p in self.products])


    def add_voucher(self, offer_code: str) -> None:
        self.total_price -= (self.total_price * 30) / 100

    def add_product(self, product: Product) -> None:
        self.products.append(product)
        self.total_price += product.price

    def remove_product(self, product: Product) -> None:
        if product in self.products:
            self.products.remove(product)
            self.total_price -= product.price


class Order:
    def __init__(self, order_id: int, products: List[Product], status: str):
        self.order_id = order_id
        self.order_date = date.today()
        self.products = products
        self.status = status

    def place_order(self) -> None:
        # Logic for placing an order
        pass
