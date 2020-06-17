import pymongo
import dns
 
from pymongo import MongoClient

myclient = pymongo.MongoClient("mongodb+srv://vue11:vue11@cluster0-s21uc.mongodb.net/test?retryWrites=true&w=majority")
mydb = myclient["eBookHouse_test"]
mycol = mydb["temp2"]
mail=input("Please Enter Your E-mail ID ")
#x = ''  
#for x in mycol.find({"ISBN13":isbn}, {"Author":1 ,"_id":0}):
    #print (x)   
mydict = { "e_mail": mail , "points": 0 , "ctitle": "bronze" , "com_rate": 0.2 , "earnings": 0 , "tot_earnings": 0}

x = mycol.insert_one(mydict)