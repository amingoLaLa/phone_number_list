import os

f = open("cellphone.txt","w")

for number in range(100000000):
    password = "09"+str(number).zfill(8)+"\n"
    f.write(password)

f.close()