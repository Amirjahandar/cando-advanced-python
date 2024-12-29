
class Product:
    def __init__(self, id: int, name: str, aspect_ratio: int, weight: float, price: float, brand: str, description: str):
        self.id = id
        self.name = name
        self.aspect_ratio = aspect_ratio
        self.weight = weight
        self.price = price
        self.brand = brand
        self.description = description

    def get_details(self) -> str:
        return f"{self.name} by {self.brand} - ${self.price}"

    def delete_product(self) -> str:
        # Logic for deleting a product
        return "Product deleted"


class Phone(Product):
    def __init__(self, id: int, name: str, aspect_ratio: int, weight: float, price: float, brand: str, description: str, storage: int, camera: str, battery_capacity: int, sim_cart: bool):
        super().__init__(id, name, aspect_ratio, weight, price, brand, description)
        self.storage = storage
        self.camera = camera
        self.battery_capacity = battery_capacity
        self.sim_cart = sim_cart

    def get_camera_specs(self) -> str:
        return f"Camera: {self.camera}"

    def show_storage_details(self) -> str:
        return f"Storage: {self.storage}GB"

    def is_5g_supported(self) -> bool:
        return self.sim_cart


class Laptop(Product):
    def __init__(self, id: int, name: str, aspect_ratio: int, weight: float, price: float, brand: str, description: str, ram: int, processor: str, gpu: str):
        super().__init__(id, name, aspect_ratio, weight, price, brand, description)
        self.ram = ram
        self.processor = processor
        self.gpu = gpu

    def get_performance_details(self) -> str:
        return f"Processor: {self.processor}, RAM: {self.ram}GB, GPU: {self.gpu}"

    def get_performance_score(self) -> int:
        # Logic for calculating performance score
        return 85

    def show_hardware_details(self) -> str:
        return f"Processor: {self.processor}, RAM: {self.ram}GB, GPU: {self.gpu}"

    def is_gaming_compatible(self) -> bool:
        return "GTX" in self.gpu or "RTX" in self.gpu

    def battery_health_check(self) -> str:
        # Logic for checking battery health
        return "Battery health is good"


class Tablet(Product):
    def __init__(self, id: int, name: str, aspect_ratio: int, weight: float, price: float, brand: str, description: str, screen_size: float, stylus_support: bool):
        super().__init__(id, name, aspect_ratio, weight, price, brand, description)
        self.screen_size = screen_size
        self.stylus_support = stylus_support

    def get_screen_details(self) -> str:
        return f"Screen size: {self.screen_size} inches"

    def supports_stylus(self) -> bool:
        return self.stylus_support

    def calculate_portability(self) -> str:
        return "Highly portable" if self.weight < 1.0 else "Less portable"

    def show_screen_details(self) -> str:
        return self.get_screen_details()
