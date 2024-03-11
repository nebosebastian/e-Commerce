class Order:
    id: int
    customer_id: int
    items: list[int]

orders : list[Order]  = [
    Order(id=1, customer_id=1, items=[1,2])
]
ids = []
current_order = None
for order in orders:
    ids.append(order.id)
if order.id == 1:
    current_order = order
    print (current_order)