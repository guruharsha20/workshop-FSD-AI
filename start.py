item="fried rice"
#price=60
rating=4 
is_veg=True
#print(type(price))
#print(type(rating))
#print(type(is_veg))
#print(type(item))
menu=["Dosa","Idli","Vada","Pongal"]
print(type(menu))
print(menu[2])
#print(menu[6])
menu.append("Sambar")
print(menu)
menu[2]="Pani Puri"
#print(menu)
menu.remove("Dosa")
print(menu)
#print(f"The price of {item} is {price} rupees.") 



working_days=["Monday","Tuesday","Wednesday","Thursday","Friday"]
print(working_days[2])
working_days[0]="Sunday" 
print(working_days)

prices={
    "Dosa": 50,
    "Idli": 30,
    "Vada": 20,
    "Pongal": 40
}
#print(prices["Dosa"])
prices["Sambar"]=60
print(prices)
prices["Vada"]=25
print(prices)
print(type(prices))
prices.pop("Idli")
print(prices)


