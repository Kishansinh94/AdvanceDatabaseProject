from py2neo import Graph, Node, Relationship
from neo4j import GraphDatabase 
import pandas as pd
from pandas import DataFrame

i=1
print ("Enter name")
mail=input()
graph = Graph(password="Temp")

while i !='0':
    print("1. To view your list")
    print("2. To view Finished list")
    print("3. To read new book")
    print("0. To Exit")
    choice1=input()
    array1= []
    ar_id=[]
    if choice1 == '1':
        j=''
        x= ''
      
        tx = graph.run('''Match (:Person{Name:"'''+mail+'''"})-[R:READING]->(b:Book) return b.Title as Title, ID(b) as ID'''  ).to_data_frame()
        if tx.empty:
            print("Surf book and start reading")
        else:
            for j in tx['Title'].values:
                array1.append(j)
            cnt=1
            for x in array1:
                print(str(cnt)+". "+x)
                cnt=cnt+1  
            
            for j in tx['ID'].values:
              ar_id.append(j)
            arsize=len(ar_id)

            temp = input("Do you want to mark it as finished ? Press 1 for yes")
            
            if temp=='1':
                num= int(input("Enter book number to mark it as finished "))
                print("You select "+str(tx['Title'].values[num-1]))
                if num <=arsize:
                    tx2= graph.run ('''match (p:Person{Name:"'''+mail+'''"})-[r:READING]->(b:Book{Title:"'''+tx['Title'].values[num-1]+'''"}) delete r ''').data()
                    tx3= graph.run ('''match (p:Person{Name:"'''+mail+'''"}) match (b:Book{Title:"'''+tx['Title'].values[num-1]+'''"}) create (p)-[:FINISHED_READING]->(b) ''').data()
    #to check your finished reading list book
        wait=input("press any key to continue...")
    elif choice1 =='2':
        tx = pd.DataFrame()
        tx = graph.run('''Match (:Person{Name:"'''+mail+'''"})-[R:FINISHED_READING]->(b:Book) return b.Title as Title'''  ).to_data_frame()
        if tx.empty:
            print("You haven't finish book yet")
            print("Books Build Stairway to your imagination, Finish your first book to add in this  ")
        else:
            for j in tx['Title'].values:
             array1.append(j)
            cnt=1
            for x in array1:
                print(str(cnt)+". "+x)
                cnt=cnt+1 
        wait=input("press any key to continue...")

    #Code for read new book comment and rating    
    elif choice1 =='3':
       
        tx = graph.run('''Match (b:Book) return b.Title as Title, ID(b) as ID LIMIT 5'''  ).to_data_frame()
        for j in tx['Title'].values:
              print(j)
        for j in tx['ID'].values:
              ar_id.append(j)
        arsize=len(ar_id)
    
        num= int(input("Select book number : "))
        print(tx['Title'].values[num-1])
        if num <=arsize:
            tx3 = graph.run('''merge (p:Person{Name:"'''+mail+'''"}) merge (b:Book{Title:"'''+tx['Title'].values[num-1]+'''"}) Merge (p)-[:READING]->(b) ''')
            print("\n\n Book content will be  here..............")

            tx4 = graph.run('''Match (p:Person{Name:"'''+mail+'''"})-[R:Rate]->(B:Book{Title:"'''+tx['Title'].values[num-1]+'''"}) Return R.starts as starts ''').to_data_frame()
            tx5 = graph.run('''Match (p:Person{Name:"'''+mail+'''"})-[C:COMMENT]->(B:Book{Title:"'''+tx['Title'].values[num-1]+'''"}) Return C.Text as Text''').to_data_frame()

            ip=input("Enter 1 to check Ratings section : ")
            if ip=='1':
                if tx4.empty:
                    rtng= int(input("No rating given by you yet \nEnter New Rating here (only value between 1-5  "))
                    tx = graph.run('''merge (p:Person{Name:"'''+mail+'''"}) merge (b:Book{Title:"'''+tx['Title'].values[num-1]+'''"}) Merge (p)-[:Rate{starts:'''+str(rtng)+'''}]->(b) ''').data()
                else:
                    print("Your Ratings is "+ str(tx4['starts'].values[0]))  

            ip=input("Enter 1 to check comments section : ")
            if ip=='1':
               
                if tx5.empty:
                    cmnt= input("No comments yet Enter New Comments here ")
                    tx = graph.run('''merge (p:Person{Name:"'''+mail+'''"}) merge (b:Book{Title:"'''+tx['Title'].values[num-1]+'''"}) Merge (p)-[:COMMENT{Text:"'''+cmnt+'''"}]->(b) ''').data()
                else:
                    print("Your Comments on book is "+ str(tx5['Text'].values[0]))
            wait=input("press any key to continue...")

        else:
            print("Wrong choice Please select number in range ")
            wait=input("press any key to continue...")

     
    elif choice1 == '0':
        break;

    else:
        print("wrong choice")
       
#cypher query
#tx = graph.run('''Match (p:Person) return p.Name as Name'''  ).to_data_frame()

#use .data() upside when want to count relarionships number 
#down below for loop is  to get all data one by one
#for i in tx['Name'].values:
#imported panda liabrary and storing value in data frame formate 
  

#getting value of only single record 
#tx=tx['Name'].values[0]
#tx2 = graph.run('''Match (p:Person {Name:"'''+str(tx)+'''"} ) return p.Name as Name''' ).data()
#print(tx2)

tx3 = graph.run('''Match (p:Person{Name:"Kishan"})-[R:READING]->(B:Book{Title:"Titanic"}) Return p.Name, B.Title ''').data()
if tx3 ==[]:
    print("No record")
else:
    print(tx3)