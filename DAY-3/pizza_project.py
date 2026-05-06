logo = rf'''
        _....._
    _.:`.--|--.`:._
  .: .'\o  | o /'. '.
 // '.  \ o|  /  o '.\
//'._o'. \ |o/ o_.-'o\\
|| o '-.'.\|/.-' o   ||
||--o--o-->|<o-----o-||
\\  o _.-'/|\'-._o  o//
 \\.-'  o/ |o\ o '-.//
  '.'.o / o|  \ o.'.'
    `-:/.__|__o\:-'
       `"--=--"`

'''

print(logo)
print("Welcome to Pizza Vendor")

size = input("What size pizza do you want? s($15), m($20) or l($25)").lower()
add_pepperoni = input("Do you want pepperoni? y or n ").lower()
extra_cheese = input("Do you want extra cheese? y or n ").lower() 

Price = 0


if size=="s" or size=="small":
    price = 15
elif size=="m" or size=="mid":
    price = 20
elif size=="l" or size=="large":
    price = 25

if add_pepperoni=="y" or add_pepperoni=="yes":
    if size=="s" or size=="small":
        price+=2
    elif (size=="m" or size=="mid")or(size=="l" or size=="large"):
        price+=3

if extra_cheese=='y' or extra_cheese=='yes':
    price+=1

print(f"Your Final Bill is: ${price}")



