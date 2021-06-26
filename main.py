import random
lower = []
upper = []
numbers = []
for i in range(97, 123):
    lower.append(chr(i))
    lower.append(chr(i).upper())
for i in range (0, 10):
    numbers.append(str(i))
password = ''
allSym = lower+upper+numbers
while len(password)<16:
    password+=allSym[random.randint(0,(len(allSym)-1))]
print(password)