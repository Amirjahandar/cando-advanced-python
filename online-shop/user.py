from typing import List, Optional
from datetime import date
from product import *
from order import *

class User:
    def __init__(self, name: str, family: str, phone: str, email: str, username: str, password: str):
        self.name = name
        self.family = family
        self.phone = phone
        self.email = email
        self.username = username
        self.password = password

    def login(self) -> bool:
        # Logic for login
        return True

    def logout(self) -> None:
        # Logic for logout
        pass


class Customer(User):
    def __init__(self, name: str, family: str, phone: str, email: str, username: str, password: str, address: str):
        super().__init__(name, family, phone, email, username, password)
        self.address = address
        self.cart = Cart()
        self.orders: List[Order] = []

    def add_comment(self) -> None:
        # Logic for adding a comment
        pass

    def view_products(self) -> None:
        # Logic for viewing products
        pass

    def place_order(self) -> None:
        # Logic for placing an order
        pass

    def add_favorit(self) -> None:
        # Logic for adding a product to favorites
        pass

    def delete_account(self) -> None:
        # Logic for deleting account
        pass


# Admin class
class Admin(User):
    def __init__(self, name: str, family: str, phone: str, email: str, username: str, password: str, admin_level: int):
        super().__init__(name, family, phone, email, username, password)
        self.admin_level = admin_level
        self.permissions: List[str] = []

    def manage_users(self) -> None:
        # Logic for managing users
        pass

    def view_reports(self) -> None:
        # Logic for viewing reports
        pass


# StoreManager class
class StoreManager(Admin):
    def __init__(self, name: str, family: str, phone: str, email: str, username: str, password: str, admin_level: int, store_id: int):
        super().__init__(name, family, phone, email, username, password, admin_level)
        self.store_id = store_id

    def add_product(self, product: 'Product') -> None:
        # Logic for adding a product
        pass

    def remove_product(self, product: 'Product') -> None:
        # Logic for removing a product
        pass

    def manage_orders(self) -> None:
        # Logic for managing orders
        pass

    def view_orders(self) -> None:
        # Logic for viewing orders
        pass


# ContentManager class
class ContentManager(Admin):
    def __init__(self, name: str, family: str, phone: str, email: str, username: str, password: str, admin_level: int):
        super().__init__(name, family, phone, email, username, password, admin_level)
        self.moderated_categories: List[str] = []

    def create_content(self) -> None:
        # Logic for creating content
        pass

    def delete_content(self) -> None:
        # Logic for deleting content
        pass

    def check_comments(self) -> None:
        # Logic for checking comments
        pass

    def edit_product_description(self, product: 'Product', description: str) -> None:
        # Logic for editing product description
        product.description = description

    def upload_media(self, media: str) -> None:
        # Logic for uploading media
        pass
