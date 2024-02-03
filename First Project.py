import random

num = "qwertyuiopasdfghjklzxcvbnm1234567890"
a = ""
for i in range(9):
    a = a + random.choice(num)
print(a)



