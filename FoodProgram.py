import FoodClass as fc

# this dictionary represents transactions. The key of the dictionary is the transaction identifier.
# The Value of the dictionary is a list. The elements in each list are -
# ['Date', 'Name of item', 'Cost', 'customerid' ]

dict = {'trans1':['2/15/2023','The Lone Patty',17,569],
                'trans2':['2/15/2023','The Octobreakfast',18,569],
                'trans3':['2/15/2023','The Octoveg',16,570],
                'trans4':['2/15/2023','The Octoburger',20,570],
}

order_total = 0

customer1 = fc.Customer(570,'Danni Sellyar', '97 Mitchell Way Hewitt Texas 76712','dseyllyarft@gmpg.org', '254-555-9362', 'False')
#customer1 = fc.Customer(569,'Aubree Himsworth','1172 Moulton Hill Waco Texas 76710', 'ahimsworthfs@list-manage.com','254-555-2273','True')

print(f'Customer Name: {customer1.get_name()}')
print(f'Phone:{customer1.get_phone()}')

for rec in dict:
    trans = fc.Transaction(dict[rec][0],dict[rec][1],dict[rec][2],dict[rec][3])
    if customer1.get_customerid() == trans.get_customerid():
        order_total += int(trans.get_cost())
        print(f'Order Item: {trans.get_item_name()} Price: ${trans.get_cost():.2f}')
        
    
if customer1.get_member_status() == 'True':
    discount = order_total*.2
    member_disc = order_total-discount
    print(f'Total Cost: ${order_total:.2f}')
    print(f'Member Discount: ${discount:.2f}')
    print(f'Total Cost After Discount: ${member_disc:.2f}')

else:
    print(f'Total Cost: {order_total:.2f}')

