import os

f = open("TelephoneList.txt","w")

for number in range(10000000):
    password = "2"+str(number).zfill(8)+"\n"
    f.write(password)

f.close()