from datetime import date

class Student:
    def __init__(self,studentid,name,dob,classification):
        self.__studentid = studentid
        self.__name = name

        self.__dob = dob
        self.__classification = classification
        self.__age = 0
        self.__register = ''

    def calc_age(self):
        today = date.today()
        dob = self.__dob.split('/')
        dob_year = int(dob[2])
        age = today.year - dob_year
        self.__age = age

    def register(self):
        if self.__classification == 'senior':
            self.__register = '11/01 thru 11/03'
        elif self.__classification == 'junior':
            self.__register = '11/04 thru 11/06'
        elif self.__classification == 'sophomore':
            self.__register = '11/07 thru 11/09'
        elif self.__classification == 'senior':
            self.__register = '11/10 thru 11/12'
        else:
            self.__register = 'classification not found'
    
    def return_age(self):
        return self.__age
    
    def return_registration(self):
        return self.__register

