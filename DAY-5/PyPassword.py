import random as rn


    
logo = fr'''                                                                                                  
 ▄▄▄▄▄         ▄▄▄▄▄                                                █           ▄▄▄               
 █   ▀█ ▄   ▄  █   ▀█  ▄▄▄    ▄▄▄    ▄▄▄  ▄     ▄  ▄▄▄    ▄ ▄▄   ▄▄▄█         ▄▀   ▀  ▄▄▄   ▄ ▄▄  
 █▄▄▄█▀ ▀▄ ▄▀  █▄▄▄█▀ ▀   █  █   ▀  █   ▀ ▀▄ ▄ ▄▀ █▀ ▀█   █▀  ▀ █▀ ▀█         █   ▄▄ █▀  █  █▀  █ 
 █       █▄█   █      ▄▀▀▀█   ▀▀▀▄   ▀▀▀▄  █▄█▄█  █   █   █     █   █         █    █ █▀▀▀▀  █   █ 
 █       ▀█    █      ▀▄▄▀█  ▀▄▄▄▀  ▀▄▄▄▀   █ █   ▀█▄█▀   █     ▀█▄██          ▀▄▄▄▀ ▀█▄▄▀  █   █ 
         ▄▀                                                                                       
        ▀▀                                                                                        '''

def  gen_random(need,thing):
    output_list = []
    for i in range(need):
        output_list.append(rn.choice(thing))
    return output_list

SYMBOL = ['!','#','$','%','&','(',')','*','+',',','-','.','/','<','>','?','@','[','\\',']','^','_','`','{','|','}','~']
LETTER = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
NUMBER = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

print(logo)
print("Welcome to the PyPassword Generator!")
letter_need = int(input("How many aletters would you like in your password?"))
symbol_need = int(input("How many symbols would you like in your password?"))
num_nedd = int(input("How many NUMbers would you like in your password?"))


letter_gen = gen_random(letter_need,LETTER)
symbol_gen = gen_random(symbol_need,SYMBOL)
number_gen = gen_random(num_nedd,NUMBER)

gen_pass = [letter_gen,symbol_gen,number_gen]
pass_gen = []
for i in gen_pass:
    for j in i:
        pass_gen.append(j)


rn.shuffle(pass_gen)
print(f"Here is your Password: {"".join(pass_gen)}")






