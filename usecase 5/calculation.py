import pymongo
import dns
 
from pymongo import MongoClient

myclient = pymongo.MongoClient("mongodb+srv://vue11:vue11@cluster0-s21uc.mongodb.net/test?retryWrites=true&w=majority")
mydb = myclient["eBookHouse_test"]
mycol = mydb["temp2"]
mycol2 = mydb["eBooks"]
mail = input("ENTER YOUT E-MAIL ID")
isbn = input("Enter Your ISBN Number")
rate = 0
for x in mycol.find({"e_mail":mail}, {"com_rate":1 ,"_id":0}):
     rate = x["com_rate"]
for x in mycol2.find({"ISBN13":isbn}, {"Price":1 ,"_id":0}):
    amt = int(x["Price"])
earng = (rate*amt) /100
print ("Your Earn:" , earng)
myquery = { "e_mail": mail }
newvalues = { "$inc": { "earnings":earng , "tot_earnings":earng } }
mycol.update_one(myquery, newvalues)