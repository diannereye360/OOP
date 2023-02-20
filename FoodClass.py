class Food:
    def __init__(self,customerid,name,address,email,phone,member_status):
        self.__customerid = customerid
        self.__name = name
        self.__address = address
        self.__email = email
        self.__phone = phone
        self.__member_status = ''



class Transaction:
    def __init__(self, date, item_name, cost, customerid):
        self.__date = date
        self.__item_name = item_name
        self.__cost = cost
        self.__customerid = customerid


