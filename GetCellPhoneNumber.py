import os

f = open("CellPhoneList.txt","w")

for number in range(100000000):
    password = "09"+str(number).zfill(8)+"\n"
    f.write(password)

f.close()