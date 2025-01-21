print("\033c")

def hotelCost(nights):
    return 140 * nights

def planeRideCost(city):
    if city == "Dhaka":
        return 222
    
    elif city == "Chattogram":
        return 475
    
    elif city == "Jashore":
        return 183
    
    elif city == "Feni":
        return 220

def rentalCarCost(days):
    if days >= 7:
        return (40 * days) - 50
    
    elif days >= 3:
        return (40 * days) - 20
    
    else:
        return (40 * days)

def tripCost(city, days):
    hC = hotelCost(days)
    rC = rentalCarCost(days)
    pC = planeRideCost(city)
    
    sum = hC + rC + pC
    
    return sum

d = int(input("Enter the amount of days you will stay(in digit) : "))
c = input("Enter the city you are going to : ")

print()

print(f"Hotel cost : ${hotelCost(d)}")
print(f"Car cost : ${rentalCarCost(d)}")
print(f"Plane cost : ${planeRideCost(c)}")
print(f"Total cost : ${tripCost(c, d)}")