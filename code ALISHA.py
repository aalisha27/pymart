def list12(s,e):
        print()
        cursor.execute("select * from item")
        print("Sno |Item Name                           |Price")
        item=cursor.fetchall()
        for i in range(s-101,e-100):
                print("_____________________________________________________")
                print(item[i][0],"|",item[i][1],"|",item[i][2])
        print()
def cartin(c):
        quan=str(input("Enter the quantity of the thing-:"))
        cursor.execute("select * from item")
        a=cursor.fetchall()
        b=c-101
        try:
                cursor.execute("insert into cart values({},'{}','{}     ',{})".format(a[b][0],a[b][1],quan,a[b][2]))
                mycon.commit
        except:
                choice123=int(input('''The item is already in cart whether you want to change quantity or exit
Press 1 to change quantity
Press 2 to exit-:'''))
                if choice123==1:
                        quan=str(input("Please enter the quantity-:"))
                        cursor.execute("update cart set quantity = '{}     ' where sno = {}".format(quan,a[b][0]))
                        mycon.commit
                else:
                        print("The item with quantity has not been changed")
        cursor.execute("select * from cart")
        data=cursor.fetchall()
        print()
        print("Sno |Item Name                           |Quantity|Price")
        i=0
        while True:
                try:
                     print("_______________________________________________________")
                     print(data[i][0],"|",data[i][1],"|",data[i][2],"|",data[i][3])
                except:
                        break
                i+=1
        print()
        choicecart=int(input('''Whether you want to modify cart ??
Press 1 to remove item
Press 2 to modify quantity
Press 3 to exit-:'''))
        if choicecart==1:
                remove=int(input("Please enter the sno of the item to be removed-:"))
                cursor.execute("delete from cart where sno = {}".format(remove))
                mycon.commit
                print("Your updated cart is here")
                cursor.execute("select * from cart")
                data=cursor.fetchall()
                print()
                print("Sno |Item Name                           |Quantity|Price")
                i=0
                while True:
                        try:
                                print("_______________________________________________________")
                                print(data[i][0],"|",data[i][1],"|",data[i][2],"|",data[i][3])
                        except:
                                break
                        i+=1

        elif choicecart==2:
                sno=int(input("Please enter the sno of the item to modify quantity-:"))
                quan=str(input("Please enter the quantity of the selected item to change-:"))
                cursor.execute("update cart set quantity='{}     ' where sno = {}".format(quan,sno))
                mycon.commit
                print("Your updated cart is here")
                cursor.execute("select * from cart")
                data=cursor.fetchall()
                print()
                print("Sno |Item Name                           |Quantity|Price")
                i=0
                while True:
                        try:
                                print("_______________________________________________________")
                                print(data[i][0],"|",data[i][1],"|",data[i][2],"|",data[i][3])
                        except:
                                break
                        i+=1
        else:
               print("Exited sucessfully")
def admin_login():
        login=input('''Are you admin or user
Type 1 for admin
Type 2 for user-:''')
        while True:
                if login=='1':
                        password=input("Enter the password for admin login-:")
                        if password=='root':
                                while True:
                                        choice=input('''Enter what you want to change
Type 1 to insert item
Type 2 to update
Type 3 to remove item
Type 4 to exit-:''')
                                        print("List of items is here")
                                        print()
                                        cursor.execute("select * from item")
                                        print("Sno |Item Name                           |Price")
                                        item=cursor.fetchall()
                                        row=cursor.rowcount
                                        for i in item:
                                                print(i[0],"|",i[1],"|",i[2])
                                        print()
                                        if choice=="1":
                                                name_item=input("Enter the name of the item to be inserted-:")
                                                price_item=int(input("Enter the price of the item to be inserted-:"))
                                                while len(name_item)<34:
                                                        name_item+=" "
                                                cursor.execute("insert into item values({},'{}',{})".format(row+101,name_item,price_item))
                                                mycon.commit
                                                print("Item inserted successfully")
                                        elif choice=="2":
                                                sno_item=int(input("Enter the sno of the item to update-:"))
                                                price_update=int(input("Enter the price to update-:"))
                                                try:
                                                        cursor.execute("update item set price={} where Sno={}".format(price_update,sno_item))
                                                        mycon.commit
                                                except:
                                                        print("Invalid sno entered, please try again")
                                        elif choice=="3":
                                                sno_item=int(input("Enter the sno of the item to remove-:"))
                                                try:
                                                        cursor.execute("delete from item where Sno={}".format(sno_item))
                                                        mycon.commit
                                                except:
                                                        print("Invalid sno entered, please try again")
                                        elif choice=="4":
                                                print("Program ended successfully")
                                                mycon.close()
                                                sys.exit()
                                        else:
                                                print("Invalid operation selected, please try again")
                                                continue
                        else:
                                print("Invalid password, please try again")
                elif login=="2":
                        break
                else:
                        print("Invalid choice, please try again")
import random
import sys
from datetime import datetime
import mysql.connector as mysql
mycon=mysql.connect(host="localhost",user="root",passwd="root")
cursor=mycon.cursor()
try:
        cursor.execute("create database Gift_mart")
except:
        pass
try:
        cursor.execute("use Gift_mart")
except:
        pass
try:  
        cursor.execute("create table item(Sno int primary key,Item_name varchar(50),price int)")
except:
        pass
try:
        cursor.execute("insert into item values (101 ,'Toy Train set                         ',450)")
        cursor.execute("insert into item values (102 ,'Kitchen set                       ',460)")
        cursor.execute("insert into item values (103 ,'Colouring set                     ',250)")
        cursor.execute("insert into item values (104 ,'Barbie home set                  ',600)")
        cursor.execute("insert into item values (105 ,'Dumpy animals set                 ',400)")
        cursor.execute("insert into item values (106 ,'Cartoon backpacks                 ',700)")
        cursor.execute("insert into item values (107 ,'Mind puzzle game                  ',289)")
        cursor.execute("insert into item values (108 ,' super drone            ',1200)")
        cursor.execute("insert into item values (109 ,'Rubix cube crystal version        ',277)")
        cursor.execute("insert into item values (110 ,'Widget crystal spinner            ',300)")
        cursor.execute("insert into item values (111 ,'Cricket kit of ss                 ',14000)")
        cursor.execute("insert into item values (112 ,'Video games                         ',700)")
        cursor.execute("insert into item values (113 ,'Pubg trigger                         ',300)")
        cursor.execute("insert into item values (114 ,'airdopes boat                      ',1500)")
        cursor.execute("insert into item values (115 ,' IQOO z5 5G                       ',24999)")
        cursor.execute("insert into item values (116 ,'Redmi Note 5 pro                   ',15590)")
        cursor.execute("insert into item values (117 ,'Redmi fit bit band                ',7000)")
        cursor.execute("insert into item values (118 ,'Mivi duopods                       ',999)")
        cursor.execute("insert into item values (119 ,'skating board                     ',4400)")
        cursor.execute("insert into item values (120 ,'T-rex cart                        ',1850)")
        cursor.execute("insert into item values (121 ,'portrait photo frame              ',250)")
        cursor.execute("insert into item values (122 ,'Cannon dslr camera                ',50000)")
        cursor.execute("insert into item values (123 ,'Flower vase (exclusive)          ',600)")
        cursor.execute("insert into item values (124 ,'Dinner set                       ',6500)")
        cursor.execute("insert into item values (125 ,'Teaset Laopala                 ',2000)")
        cursor.execute("insert into item values (126 ,'Lg web ios smart tv         ',46000)")
        cursor.execute("insert into item values (127 ,'Nayasa plasticware container set  ',999)")
        cursor.execute("insert into item values (128 ,'Repairing toolkit                 ',600)")
        cursor.execute("insert into item values (129 ,'G-shock watch                     ',1300)")
        cursor.execute("insert into item values (130 ,'Axe perfume set (GOLD EDITION)               ',400)")
        cursor.execute("insert into item values (131 ,' Boxing bag with gloves                   ',2000)")
        cursor.execute("insert into item values (132 ,'Echo dot 5th gen                      ',2000)")
        cursor.execute("insert into item values (133 ,'Women's kit                        ',2000)")
        cursor.execute("insert into item values (134 ,'Travel humsafar kit               ',4500)")
        cursor.execute("insert into item values (135 ,'Fiddlys lcd writing tablet        ',1600)")
        cursor.execute("insert into item values (136 ,'Led bottle lamp                   ',695)")
        cursor.execute("insert into item values (137 ,'Ullo wine purifier                ',1350)")
        cursor.execute("insert into item values (138 ,'Karavan audiocase                 ',1160)")
        cursor.execute("insert into item values (139 ,'Custom portraits                    ',560)")
        cursor.execute("insert into item values (140 ,'Nightware set                     ',1500)")
        cursor.execute("insert into item values (141 ,'Rocky talking watch               ',700)")
        cursor.execute("insert into item values (142 ,' MI Powerbank                      ',999)")
        cursor.execute("insert into item values (143 ,'Oreo biscuit                          ',100)")
        mycon.commit
except:
        pass
try:
        cursor.execute("create table cart(Sno int primary key,Item_Name varchar(50),Quantity varchar(10),Price int)")
except:
        pass
admin_login()
print("$$$$$$$$$$$$$$ welcome to SHOP_HUB gift mart $$$$$$$$$$$$$")
print("******************welcome to our shop**************")
print("*****************we provides every customer 20% discount************")
print("hope you will enjoy our site/////")
price=0
a=(input("press enter for viewing the gift category:"))
print("loading the gift category....")
done=True
while done:
        b=int(input('''-> press 1 to select gifts for age group 1-6 
-> press 2 to select gifts for age group 7-13 
-> press 3 to select gifts for age group 14-25 
-> press 4 to select gifts for age group 26-40 
-> press 5 to select gifts for 40+ age group-:'''))
        if b==1:
            list12(101,106)
            while True:
                    c=int(input("enter your gift choice:"))
                    if c==101:
                            cartin(c)
                            print("Your item is added to cart sucessfully!!")
                            
                            
                    elif c==102:
                            cartin(c)
                            print("Your item is added to cart sucessfully!!")
                            
                            
                    elif c==103:
                            cartin(c)
                            print("Your item is added to cart sucessfully!!")
                            
                            
                    elif c==104:
                            cartin(c)
                            print("Your item is added to cart sucessfully!!")
                            
                            
                    elif c==105:
                            cartin(c)
                            print("Your item is added to cart sucessfully!!")
                            
                            
                    elif c==106:
                            cartin(c)
                            print("Your item is added to cart sucessfully!!")
                    choice=int(input('''Whether you want to add more items to cart from this category or proceed to payment ??
Press 1 to continue
Press 2 to exit and see other categories
Press 3 to proceed to payment'''))
                    if choice==1:
                                    continue
                    elif choice==3:
                                  done=False
                                  break
                    elif choice==2:
                                  break
        
                    
        elif b==2:
                list12(107,113)
                while True:
                        c=int(input("enter your gift choice:"))
                        if c==107:
                            cartin(c)
                            print("Your item is added to cart sucessfully!!")
                            
                            
                        elif c==108:
                            cartin(c)
                            print("Your item is added to cart sucessfully!!")
                            
                            
                        elif c==109:
                            cartin(c)    
                            print("Your item is added to cart sucessfully!!")
                            
                            
                        elif c==110:
                            cartin(c)
                            print("Your item is added to cart sucessfully!!")
                            
                            
                        elif c==111:
                            cartin(c)
                            print("Your item is added to cart sucessfully!!")
                            
                            
                        elif c==112:
                            print("Your item is added to cart sucessfully!!")
                            
                            
                        elif c==113:
                            cartin(c)    
                            print("Your item is added to cart sucessfully!!")
                        choice=int(input('''Whether you want to add more items to cart from this category or proceed to payment ??
Press 1 to continue
Press 2 to exit and see other categories
Press 3 to proceed to payment'''))
                        if choice==1:
                                            continue
                        elif choice==3:
                                          done=False
                                          break
                        elif choice==2:
                                          break

                    
        elif b==3:
            list12(114,120)
            while True:
                    c=int(input("enter gift choice"))
                    if c==114:
                            cartin(c)
                            print("Your item is added to cart sucessfully!!")
                    elif c==115:
                            cartin(c)
                            print("Your item is added to cart sucessfully!!")
                    elif c==116:
                            cartin(c)
                            print("Your item is added to cart sucessfully!!")
                            
                    elif c==117:
                            cartin(c)
                            print("Your item is added to cart sucessfully!!")
                    elif c==118:
                            cartin(c)
                            print("Your item is added to cart sucessfully!!")
                    elif c==119:
                            cartin(c)
                            print("Your item is added to cart sucessfully!!")
                    elif c==120:
                            cartin(c)
                            print("Your item is added to cart sucessfully!!")
                    choice=int(input('''Whether you want to add more items to cart from this category or proceed to payment ??
Press 1 to continue
Press 2 to exit and see other categories
Press 3 to proceed to payment'''))
                    if choice==1:
                                    continue
                    elif choice==3:
                                  done=False
                                  break
                    elif choice==2:
                                  break
        elif b==4:
            list12(121,128)
            while True:
                    c=int(input("enter your gift choice:"))
                    if c==121:
                        cartin(c)    
                        print("Your item is added to cart sucessfully!!")
                        
                        
                    elif c==122:
                        cartin(c)    
                        print("Your item is added to cart sucessfully!!")
                        
                        
                    elif c==123:
                        cartin(c)    
                        print("Your item is added to cart sucessfully!!")
                        
                        
                    elif c==124:
                        print("Your item is added to cart sucessfully!!")
                        
                        
                    elif c==125:
                        cartin(c)
                        print("Your item is added to cart sucessfully!!")
                        
                        
                    elif c==126:
                        cartin(c)
                        print("Your item is added to cart sucessfully!!")
                        
                        
                    elif c==127:
                        cartin(c)
                        print("Your item is added to cart sucessfully!!")
                        
                        
                    elif c==128:
                        cartin(c)
                        print("Your item is added to cart sucessfully!!")
                    choice=int(input('''Whether you want to add more items to cart from this category or proceed to payment ??
Press 1 to continue
Press 2 to exit and see other categories
Press 3 to proceed to payment'''))
                    if choice==1:
                                    continue
                    elif choice==3:
                                  done=False
                                  break
                    elif choice==2:
                                  break
    
                
        elif b==5:
            list12(129,143)
            while True:
                    c=int(input("enter your gift choice:"))
                    if c==129:
                        cartin(c)
                        print("Your item is added to cart sucessfully!!")
                        
                        
                    elif c==130:
                        cartin(c)
                        print("Your item is added to cart sucessfully!!")
                        
                        
                    elif c==131:
                        cartin(c)
                        print("Your item is added to cart sucessfully!!")
                        
                        
                    elif c==132:
                        cartin(c)
                        print("Your item is added to cart sucessfully!!")
                        
                        
                    elif c==133:
                        cartin(c)
                        print("Your item is added to cart sucessfully!!")
                        
                        
                    elif c==134:
                        cartin(c)
                        print("Your item is added to cart sucessfully!!")
                        
                        
                    elif c==135:
                        cartin(c)
                        print("Your item is added to cart sucessfully!!")
                        
                        
                    elif c==136:
                        cartin(c)
                        print("Your item is added to cart sucessfully!!")
                        
                        
                    elif c==137:
                        cartin(c)
                        print("Your item is added to cart sucessfully!!")
                        
                        
                    elif c==138:
                        cartin(c)
                        print("Your item is added to cart sucessfully!!")
                        
                        
                    elif c==139:
                        cartin(c)
                        print("Your item is added to cart sucessfully!!")
                        
                        
                    elif c==140:
                        cartin(c)
                        print("Your item is added to cart sucessfully!!")
                        
                        
                    elif c==141:
                        cartin(c)
                        print("Your item is added to cart sucessfully!!")
                        
                        
                    elif c==142:
                        cartin(c)
                        print("Your item is added to cart sucessfully!!")
                        
                        
                    elif c==143:
                        cartin(c)
                        print("Your item is added to cart sucessfully!!")
                        
                        
                    else:
                            print("Please enter available no.s only to select gifts")
                            continue
                    choice=int(input('''Whether you want to add more items to cart from this category or proceed to payment or see cart??
Press 1 to continue
Press 2 to exit and see other categories
Press 3 to proceed to payment-:'''))
                    if choice==1:
                                    continue
                    elif choice==3:
                                  done=False
                                  break
                    elif choice==2:
                                  break
print("please pay by the following choice:")
print("cash on delivery press 1001 ")
print("for upi press 1002")
print("card payment press 1003")
print("Your cart is here")
cursor.execute("select * from cart")
data=cursor.fetchall()
print()
print("Sno |Item Name                           |Quantity|Price")
i=0
while True:
        try:
                print("_______________________________________________________")
                print(data[i][0],"|",data[i][1],"|",data[i][2],"|",data[i][3])
                quan=int(data[i][2])
                price+=(quan*data[i][3])
        except:
                break
        i+=1
print()
print("You have to pay",price*80/100)
p=int(input("enter a method to pay your bill:"))
if p==1001:
    name_of_customer=input("enter your name:")
    phone_number=int(input("enter your mob. no."))
    address=str(input("enter delievery address:"))
    city=str(input("enter your city name:"))
    print("your total payment is",price*80/100)
if p==1002:
    print("be ready with ur online account money...u can send us or can pay the delievery boy")
    print("your total payment is",price*80/100)
if p==1003:
    print("enter the following details:")
    card_holder_name=input("enter the holder name:")
    card_number=int(input("enter your card number:"))
    validity_date=input("enter the validity date of the card(dd/mm/yyyy):")
    registered_phone_no=int(input("enter the no. registered with the bank account:"))
    print("an otp has sent to your mobile number please check it out and then enter the password!")
    password=input("enter the password:")
    print("your total payment is",price*80/100)
print("Your order placed at",datetime.now())
print("thanks for placing your order")
print("your item is expected to be delievered within",random.randint(2,5),"days keep shopping on ***shop_hub online mart***")
print("Developer of site Subrat kumar sahu")
mycon.close()
