import os

logo = r''' 

                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\
                         `'-------'`
                       .-------------.
                   jgs/_______________\
'''

def winner(dicto):
    win = []
    price = []
    for i in dicto:
        price.append(dicto[i])
    maximum = max(price)
    # print(maximum)
    for j in dicto:
        if dicto[j]==maximum:
            win.extend([j,dicto[j]])
    return win


name_price = {}
print("Welcome to the secret auction Program.")

while True:
    print(logo)
    name = input("What is your name?-> ")
    bid_price = int(input("What's your bid? -> $"))
    name_price[name]= bid_price
    is_other = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    if is_other=="no" or is_other=="nah" or is_other=="na" or is_other=="n":
        winning_person = winner(name_price)
        print(f"The Highest bid is {winning_person[1]} and the winner is {winning_person[0]}")
        break
    os.system("clear")
# print(name_price)