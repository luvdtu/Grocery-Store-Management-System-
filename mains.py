import mysql.connector as sq
conn=sq.connect(host='localhost', user = 'root', password ='luv@dec4',database ='account')
c1=conn.cursor()
chpasswd='d'
import datetime
d_day=datetime.date.today()
d_time=datetime.datetime.now()
print("                                                            "," WELCOME    TO   WALMART      ")
it=0
bill=0
while 5>1:
                print("******************************************************************************************************************************************************************************************************************************************************************************************************************************************************")
                print("                         ","1.CUSTOMER")
                print("                         ","2.ADMIN")
                print("                         ","3.EXIT")
                loggin=int(input("Enter the choice:"))
                print("*******************************************************************************************************")
                
                if loggin==1:
                                    g=input("Enter your name")
                                    f=int(input("Enter your phone no."))
                                    while 3>1:
                                            
                                                print("*******************************************************************************************************")
                                                def showAll():
    
                                                         global conn
                                                         global c1
    
                                                         try:
                                                                 query="select * from stock"
                                                                 c1.execute(query)
                                                                 results = c1.fetchall()
                                                                 print("**************************************************")
                                                                 print('%5s'%"product_no",'%15s'%'product_name','%20s'%'cost_per_product')
                                                                 print("**************************************************")
                                                                 count=0
                                                                 for row in results:
                                                                         print('%5s'%row[0],'%15s'%row[1],'%12s'%row[2])
                                                                         count+=1
                                                                 print("*************** TOTAL RECORD : ",count,"************")
                                                         except:
                                                                 print("try again")
                                                                     
                
                                               
                                                print(showAll())
                                                                 

                                                print("**************************************************************************************")
                                                b=input('select product number from the above list which you wish to purchase: ')
                                                c1.execute('select product_name,cost_per_product from stock where product_no =' + b)
                                                data= c1.fetchall()
                                                data1=list(data[0])
                                                print('Product name :', data1[0])
                                                print('Cost of the product :', data1[1] )
                                                z=int(input("No. of units you wish to purchase"))         
                                                appr= input('Do you want to confirm the purchase (Y/N) :')
                                                if appr == 'y' or appr =='Y' :
                                                                c1.execute("update stock set stock=stock-" + str(z)+ " where product_no= " + b )
                                                                c1.execute("update stock set purchased=purchased+" + str(z)+ " where product_no= " + b )
                                                                bill+=int(data1[1])
                                                                it+=z
                                                                print("bought successfully!!!!")
                                                                opn = input("Do you want buy any other thing (Y/N) : ")
                                                                if opn == 'y' or opn == 'Y':
                                                                                       continue
                                                                                       just=input('MODE OF PAYMENT (Cash/Card):')
                                                                                       print("***************************************************************************************************************")
                                                                                       print("                  BILL","                                  ","DAY-",d_day.day,"/",d_day.month,"/",d_day.year," ","TIME-",d_time.hour,":",d_time.minute)
                                                                                       print('''              WALMART       
NUMBER OF ITEMS PURCHASED:''',it)
                                                                                       print('''GRAND TOTAL AMOUNT:''', bill*z)
                                                                                       print('''MODE OF PAYMENT:''',just)
                                                                                       print('''*******THANK YOU*******
*******PLEASE VIST AGAIN*******''')
                                                                                       break
                                                                                       
                                                                elif opn=='n' or opn=='N':
                                                                     just=input('MODE OF PAYMENT (Cash/Card):')
                                                                     print("                      BILL","                                  ","DAY-",d_day.day,"/",d_day.month,"/",d_day.year," ","TIME-",d_time.hour,":",d_time.minute)
                                                                     print('''                     WALMART
NUMBER OF ITEMS PURCHASED:''',it)
                                                                     print('''GRAND TOTAL AMOUNT:''', bill*z)
                                                                     print('''MODE OF PAYMENT:''',just)
                                                                     print('''*******THANK YOU*******
*******PLEASE VIST AGAIN*******''')
                                                                     break
                                                elif appr =='n' or appr =='N':
                                                                opn = input(" Do you want buy any other thing (Y/N) : ")
                                                                if opn == 'y' or opn == 'Y':
                                                                                       continue
                                                                elif opn == 'n' or opn =='N':
                                                                                 print('''*******THANK YOU*******
*******PLEASE VIST AGAIN*******''')
                                                                                 break
                                                else:
                                                     print('####invalid command####')
                                                     break
                                                     conn.commit()
                elif loggin==2:
                                               p=input("Enter administrative password")
                                               if p=="admin":
                                                print("*******************************************************************************************************")
                                                print("1. View stock")
                                                print("2. Add stock")
                                                print("3. Adding a new product")
                                                ch=int(input("Enter your choice :"))
                                                if ch==1:

                                                                print("*******************************************************************************************************")
                                                                def show():
    
                                                                               global conn
                                                                               global c1
    
                                                                               try:
                                                                                       query="select * from stock"
                                                                                       c1.execute(query)
                                                                                       results = c1.fetchall()
                                                                                       print("******************************************************************************************************")
                                                                                       print('%5s'%"product_no",'%15s'%'product_name','%20s'%'cost_per_product','%15s'%'stock','%15s'%'purchased')
                                                                                       print("******************************************************************************************************")
                                                                                       count=0
                                                                                       for row in results:
                                                                                            print('%5s'%row[0],'%15s'%row[1],'%12s'%row[2],'%25s'%row[3],'%15s'%row[4])
                                                                                            count+=1
                                                                                       print("*************** TOTAL RECORD : ",count,"**************************************************************")
                                                                               except:
                                                                                       print("error")
                
                                               
                                                                print(show())
                                                            
                                                                a=input('Enter the product number :')
                                                                c1.execute("select * from stock where product_no="+a)
                                                                dt=c1.fetchall()
                                                                dt1=list(dt[0])
                                                                print("product name :",dt1[1])
                                                                print("cost per product:",dt1[2])
                                                                print("stock available:",dt1[3])
                                                                print(" Number of items purchased :",dt1[4])
                                                elif ch==2:
                                                                prdno=input("Enter the product number of the product for which the stock is going to be updated:")
                                                                upd_value=int(input("enter the number of new stocks came:"))
                                                                c1.execute("update stock set stock=stock+" + str(upd_value) + " where product_no="+prdno)
                                                                conn.commit()
                                                                print("Stock Updated Successfully")
                                                elif ch==3:
                                                                pno1=input('Enter the product number of new product:')
                                                                pna=input('Enter the product name of the new product:')
                                                                cst=input('Enter the cost of the product:')
                                                                stock12=input('Enter the number of stocks of the new product arrived:')
                                                                pch='0'
                                                                c1.execute("insert into stock values(" + pno1 +','+'"'+pna+'"'+','+cst+','+stock12+','+pch+')')
                                                                print("Added sucessfully!!!!!!!")
                                                                conn.commit()
                                                                print("*******************************************************************************************************")

                                                                def showto():
                                                                               global conn
                                                                               global c1
    
                                                                               try:
                                                                                       query="select * from stock"
                                                                                       c1.execute(query)
                                                                                       results = c1.fetchall()
                                                                                       print("******************************************************************************************************")
                                                                                       print('%5s'%"product_no",'%15s'%'product_name','%20s'%'cost_per_product','%15s'%'stock','%15s'%'purchased')
                                                                                       print("******************************************************************************************************")
                                                                                       count=0
                                                                                       for row in results:
                                                                                            print('%5s'%row[0],'%15s'%row[1],'%12s'%row[2],'%25s'%row[3],'%15s'%row[4])
                                                                                            count+=1
                                                                                       print("*************** TOTAL RECORD : ",count,"**************************************************************")
                                                                               except:
                                                                                       print("error")
                                                                print(showto())
                                                                
                                                                 
                                                else:
                                                                print('####INVALID OPTION ####')
                                               else:
                                                               print("#####INCORRECT PASSWORD#####","                 ","You are not allowed to access that program")
                                                                

                elif loggin== 3:
                                print("...QUITING... ")
                                break                                                               
                                
                else:
                                print("###INVALID OPTION####")
                                
                                
                
                                

