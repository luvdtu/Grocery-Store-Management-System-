import mysql.connector as sq
import datetime
d_day=datetime.date.today()
d_time=datetime.datetime.now()
conn=sq.connect(host='localhost', user = 'root', password ='luv@dec4',database ='account')
c1=conn.cursor()
print("                               ","GROCERY STORE MANAGEMENT SYSTEM")
print(d_day.day,"/",d_day.month,"/",d_day.year,"    ",d_time.hour,":",d_time.minute,)
while 5>1:
                print("             ","1.LOGIN")
                print("             ","2.REGISTER")
                print("             ","3.VIEW ALL USERS")
                print("             ","4.CHANGE PASSWORD")
                print("             ","5.EXIT")
                choice=int(input('ENTER THE CHOICE:'))
                print("===========================================================================================================================================================================")
                if choice == 1:
                                us=input('USERNAME:')
                                ps=input('PASSWORD:')
                                c1.execute("select * from user where username = '{}' and passwd = '{}'".format(us , ps))
                                
                                data = c1.fetchall()
                                
                                if any(data) :
                                                import mains
                                
                                else:
                                                print("                      ",'''.............SORRY............
            ............WRONG USERNAME OR PASSWORD...............''')


                elif choice == 2:
                                print("===========================================================================================================================================================================")
                                li=input('ENTER THE NEW USERNAME:')
                                while 8>1:
                                                li2=input('ENTER YOUR PASSWORD:')
                                                li3=input('ENTER YOUR PASSWORD AGAIN(to confirm):')
                                                if li2== li3:
                                                                c1.execute("insert into user values("+'"'+li+'",'+'"'+li3+'")')
                                                                print("ID has been successfully created:")
                                                                conn.commit()
                                                                break
                                                else:
                                                                print("INCORRECT PASSWORD") 
                elif choice ==3:
                                c1.execute("select username from user")
                                data = c1.fetchall()
                                for row in data : print(row)
                elif choice == 4:
                                print("===========================================================================================================================================================================")
                                a=input('USERNAME:')
                                b=input('EXISTING PASSWORD:')
                                c1.execute("select * from user where username = '{}' and passwd = '{}'".format(a , b))
                                data = c1.fetchall()
                                
                                if any(data) :
                                                c=input("ENTER NEW PASSWORD:")
                                                c1.execute("update user set passwd=" + str(c) + " where username="+str(a))
                                
                                else:
                                                print('''..SORRY..
WRONG.......USERNAME OR PASSWORD''')

                                
                                
                    
                    
                elif choice == 5:
                                print(".......................LOGGING...........OUT................")
                                break
                                        
                else:
                                print('please enter the right option')

