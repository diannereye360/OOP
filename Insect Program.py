import InsectClass as i

mosquito = i.Insect("mosquito",2,4)
housefly = i.Insect("housefly",4,8)

mosquito.calc_flight()
housefly.calc_flight()

print(f"The {mosquito.get_name()} can fly up to {mosquito.get_flight()} miles")
print(f"The {housefly.get_name()} can fly up to {housefly.get_flight()} miles")