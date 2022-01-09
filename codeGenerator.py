#Devs:
#Muhammed Hassan
#Muhammed Galal Qassas
#Kareem Ahmed Abdelfatah
#submitted to : Dr.Hatem

import random
import datetime
import json

codeLength = 4
codeOrig = "1234567890"
final = ""

a_file = open("myDataBase.json", "r")
database =json.load(a_file)
a_file.close()

exDate = datetime.datetime.today()+datetime.timedelta(days=365*2)

while True:
    numCo = int(input ("please enter the number of codes you wish to generate \n"))
    val = input ("please enter the value 10,20,50 or 100 EGP\n")
    def makePromoteCode(count):
        promotecode=""
        for i in range(count):
            for x in range(codeLength):
                promotecode += random.choice(codeOrig)
            promotecode +="-"
        return promotecode
    for z in range(numCo):
        final = makePromoteCode(4)
        prom={
            "code":final[:-1],
            "state":"valid",
            "expire":exDate.strftime("%d/%m/%Y"),
            "value":val+"EGP"
        }
        database.append(prom)

    j = json.dumps(database,indent=5,sort_keys=False)
    with open('myDataBase.json', 'w') as f:
        f.write(j)
        f.close()

    def checkV():
        isVAL=input ("check validity\n")
        for obj in list(database):
            if(isVAL == obj["code"]):
                return "VALID"
        else:
            return "NOT VALID!"
                
    print (checkV())

    def used():
        useC = input ("Enter the code you wish to use\n")
        for obj in list(database):
            if(obj["code"] == useC and obj["state"] == "used"):
                print("this code has been used")
            elif(obj["code"] == useC):
                obj["state"]="used"
    used()

    def dela():
        a_in = input("Delete used codes? y/n \n")
        if(a_in =="y"):
            for obj in list(database):
                if(obj["state"] == "used"):
                    database.remove(obj)
        elif(a_in =="n"):
            return
    a_file = open("myDataBase.json", "w")
    json.dump(database,a_file,indent=5,sort_keys=False)
    a_file.close()
    dela()
    a_file = open("myDataBase.json", "w")
    json.dump(database,a_file,indent=5,sort_keys=False)
    a_file.close()

