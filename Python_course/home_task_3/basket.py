class Basket:
    def __init__(self, products_list: list):
        self.products_list = products_list

    def add_product(self, new_product: str):
        self.products_list.append(new_product)

    def remove_product(self, product_to_be_removed: str):
        if product_to_be_removed in self.products_list:
            self.products_list.remove(product_to_be_removed)

    def is_empty(self):
        return len(self.products_list) == 0

    def __str__(self):
        return str(self.products_list)
