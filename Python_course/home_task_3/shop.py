from Python_course.home_task_3.basket import Basket

source_product_list = str(input("Enter your list of products: "))
product_list = source_product_list.split()

basket = Basket(product_list)
print("Your list of products consist of: " + str(basket))

while not basket.is_empty():
    additional_product_list = str(input("Enter additional products: "))
    new_product_list = additional_product_list.split()

    for product in new_product_list:
        if product.startswith("-"):
            product = product[1:]
            basket.remove_product(product)
        else:
            basket.add_product(product)

    print("Your list of products consist of: " + str(basket))
print("Your list of products is empty. Program is finished.")