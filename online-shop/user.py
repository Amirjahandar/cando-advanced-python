from typing import List, Optional
from datetime import date
from product import *
from order import *
import re

class User:
    def __init__(self, name: str, family: str, phone: str, email: str, username: str, password: str, address:str):
        self.__name = name
        self.__family = family
        self.__phone = phone
        self.__email = email
        self.username = username
        self.password = password
        self.isadmin = False
        self.permissions: List[str] = []
        self.address = address
        self.cart = Cart()
        self.orders: List[Order] = []

    @property
    def __name(self):
        return self.__name
    @__name.setter
    def __name(self, name):
        if name.isalpha():
            self.__name = name
        else:
            return "name must be alphabet!!"

    @property
    def __family(self):
        return self.__family
    @__family.setter
    def __family(self, family):
        if family.isalpha():
            self.__family = family
        else:
            return "family must be alphabet!!!"

    @property
    def __phone(self):
        return self.__phone
    @__phone.setter
    def __phone(self, phone):
        if phone.isdigit() and len(phone) == 11:
            self.__phone = phone
        else:
            return "phone number is invalid!!!"

    @property
    def __email(self):
        return self.__email
    @__email.setter
    def __email(self, email):
        valid = re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email)
        if valid:
            self.__email = email
        else:
            return "email is invalid!!!"


    def login(self) -> bool:
        # Logic for login
        return True

    def logout(self) -> None:
        # Logic for logout
        pass
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

    def remove_product(self, product: 'Product') -> None:
        # Logic for removing a product
        pass

    def manage_orders(self) -> None:
        # Logic for managing orders
        pass

    def view_orders(self) -> None:
        # Logic for viewing orders
        pass



"""
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
"""