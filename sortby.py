def sort_by_piece(item: tuple):
    return item[2]

   

def sort_by_remaining_stock(items: list):
    return sorted(items, key=sort_by_piece)


products = [("banana", 5.95, 12), ("apple", 3.95, 3), ("orange", 4.50, 2), ("watermelon", 4.95, 22)]

for product in sort_by_remaining_stock(products):
    print(f"{product[0]} {product[2]} pcs")