# #swap 1
# a = 5
# b = 10

# print(f"a = {a} before")
# print(f"b = {b} before")

# c = a
# a = b
# b = c

# print(f"a = {a} after")
# print(f"b = {b} after")



# ## Swap 2 
# a = 15
# b = 30

# print(f"a = {a} before")
# print(f"b = {b} before")

# a = a+b
# b = a-b
# a = a-b

# print(f"a = {a} after")
# print(f"b = {b} after")


# # Swap 3

# a = 'B'
# b = 'a'

# print(f"a = {a} before")
# print(f"b = {b} before")

# a = ord(a)
# b = ord(b)

# a = a+b
# b = a-b
# a = a-b

# a = chr(a)
# b = chr(b)

# print(f"a = {a} after")
# print(f"b = {b} after")



#SWAP 4 - String
def uni_num(a):
    uninum = []
    for i in a:
        uninum.append(ord(i))
    return uninum


def num_uni(a):
    numuni = []
    for i in a:
        numuni.append(chr(i))
    return "".join(numuni)

a = "Alucard"
b = "BELMONT"

print(f"a = {a} before")
print(f"b = {b} before")

Aa = uni_num(a)
Bb = uni_num(b)

tempA =[]
tempB = []
if len(Aa)==len(Bb):
    for j in range(len(Aa)):
        a = Aa[j]
        b = Bb[j]
        a = a+b
        b = a-b
        a = a-b
        tempA.append(a)
        tempB.append(b)

        # print(f"a = {a} after")
        # print(f"b = {b} after")



Aa =num_uni(tempA)
Bb = num_uni(tempB)

a = Aa
b= Bb




print(f"a = {a} after")
print(f"b = {b} after")




