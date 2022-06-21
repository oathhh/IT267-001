from cusorder.customer import Customer
from cusorder.order import Order

#cerate object customer
cus1 = Customer("Jame","Nonthaburi")

#
order1 = Order("15-06-2002","packed")

#display info
print(f'Order of {cus1.name} on {order1.date} is {order1.status}')