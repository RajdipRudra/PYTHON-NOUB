import os
logo = r"""
┏━╸┏━┓┏━╸┏━┓┏━┓┏━┓   ┏━╸╻┏━┓╻ ╻┏━╸┏━┓
┃  ┣━┫┣╸ ┗━┓┣━┫┣┳┛   ┃  ┃┣━┛┣━┫┣╸ ┣┳┛
┗━╸╹ ╹┗━╸┗━┛╹ ╹╹┗╸   ┗━╸╹╹  ╹ ╹┗━╸╹┗╸                                    
                                     
"""


Letter_library = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9','!','#','$','%','&','(',')','*','+',',','-','.','/','<','>','?','@','[','\\',']','^','_','`','{','|','}','~','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
          'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','0', '1', '2', '3', '4', '5', '6', '7', '8', '9','!','#','$','%','&','(',')','*','+',',','-','.','/','<','>','?','@','[','\\',']','^','_','`','{','|','}','~',
          'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']



def encode(msg,s_num,LL):
    encoded_msg = []
    for i in range(len(msg)):
        letter = msg[i]
        if letter in LL:
            encoded_msg.append(LL[(LL.index(letter))+s_num])
        else:
            encoded_msg.append(letter)
    return "".join(encoded_msg)

def decode(msg,s_num,LL):
    decoded_msg = []
    for i in range(len(msg)):
        letter = msg[i]
        if letter in LL:
            decoded_msg.append(LL[(LL.index(letter))-s_num])
        else:
            decoded_msg.append(letter)
    return "".join(decoded_msg)



while True:
    os.system("cls")
    print(logo)
    operation = input("Type 'encode' to encrypt, type 'decode' to decrypt ->\n").lower()
    message = input("Type your message -> ")
    shift_num = int(input("Type your Shift Number:\n"))

    if operation == "en" or operation=="encode" or operation=="e":
        output = encode(message,shift_num,Letter_library)
        print(f"Here's the encoded result:\n{output}")
    elif operation == "de" or operation=="decode" or operation=="d":
        output = decode(message,shift_num,Letter_library)
        print(f"Here's the decoded result:\n{output}")
    else:
        print("Enter a valid input.")
    
    run_again = input("Type 'yes' if you want to go again Otherwise type 'no'\n").lower()
    if run_again=='n' or run_again=="no" or run_again=='nah':
        input('loading...')
        break