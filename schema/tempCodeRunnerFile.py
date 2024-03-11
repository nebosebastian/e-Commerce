products : list[Product] | dict = {
    1: Product(id=1, name="Milo", price=Decimal('50.00'), quantity_available=1),
    2: Product(id=2, name="Pepsi", price=Decimal('150.00'), quantity_available=15),
    3: Product(id=3, name="Coffee", price=Decimal('10.50'), quantity_available=5),
}

items = []
for _, product in products.items():
    items.append(product)
    print(items) 