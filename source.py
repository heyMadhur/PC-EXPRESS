print("--------------------              PC EXPRESS            ---------------------")
print('\n')
print("--------------------             DATABASE 2020          ---------------------")
print("\n")

c='y'
while(c=='y'):
    print('1.PC Component')
    print('2.Sales Detail')
    print('3.Exit')
    print('\n')
    choice=int(input('Enter the number:'))
    print('\n')
    if choice==1:
            print('1.Motherboard')
            print('2.Processor')
            print('3.Ram')
            print('4.Storage')
            print('5.Graphic card')
            print('6.Power Supply')
            print('7.Cabinet')
            print('8.EXIT')
            print('\n')
            a=int(input('Enter the number:'))
            print('\n')
            if a==1:
                def mob():            
                    c='y'
                    while c=='y':
                        print('1.Add Motherboard Record')
                        print('2.Update Motherboard Record')
                        print('3.Display Motherboard Record')
                        print('4.Search Motherboard Record')
                        print('5.Delete Motherboard Record')
                        print('6.Main Menu')
                        print('\n')
                        x=int(input('Enter the number:'))
                        print('\n')
                        if x==1:
                            addmb()
                        elif x==2:
                            upmb()
                        elif x==3:
                            dismb()
                        elif x==4:
                            sermb()
                        elif x==5:
                            delmb()
                        else :
                            print('Returning to main menu')
                            print('\n')
                            break
                       
                def addmb():
                    import mysql.connector
                    try:
                        mydb=mysql.connector.connect(host='localhost',user='root',passwd="",db="pc_express")
                        mycursor=mydb.cursor()
                        name=input('Model Name:')
                        company=input('Company Name:')
                        soctype=input("socket_type Name:")
                        chip=input('Chipset Name:')
                        qty=input('QUANTITY:')
                        price=input('Enter Price:')
                        mycursor.execute("""INSERT INTO motherboard(Name,Company,Socket_type,Chipset,Qty,Price)VALUES(%s,%s,%s,%s,%s,%s)""",(name,company,soctype,chip,qty,price))
                        mydb.commit()
                        print('\n')
                        print("Record Inserted")
                        print('\n')
                    except Exception as e:
                        print("Unable to insert record")
                        print(e)
                        print('\n')
                def upmb():
                    import mysql.connector
                    try:
                        mydb=mysql.connector.connect(host='localhost',user='root',passwd="",db="pc_express")
                        mycursor=mydb.cursor()
                        name=input('Model Name:')
                        company=input('Company Name:')
                        soctype=input("socket_type Name:")
                        chip=input('Chipset Name:')
                        qty=input('QUANTITY:')
                        price=input('Enter Price:')
                        mycursor.execute("""UPDATE motherboard SET Company=%s,Socket_type=%s,Chipset=%s,Qty=%s,Price=%s WHERE Name=%s""",(company,soctype,chip,qty,price,name))
                        mydb.commit()
                        print('Record Updated')
                        print('\n')
                    except Exception as e:
                        print(e)
                        print("Unable to update record")
                        print('\n')
                def dismb():
                    import mysql.connector
                    from tabulate import tabulate
                    try:
                        mydb=mysql.connector.connect(host='localhost',user='root',passwd="",db="pc_express")
                        mycursor=mydb.cursor()
                        mycursor.execute('select * from motherboard')
                        results=mycursor.fetchall()
                        print(tabulate(results,headers=['Name','Company','Socket_type','Chipset','Qty','Price'],tablefmt='grid'))
                        print("Record Displayed")
                        print('\n')
                        mydb.commit()
                    except Exception as e:
                        print("Error:unable to fetch data.Please try again")
                        print(e)
                        print('\n')
                def sermb():
                    import mysql.connector
                    from tabulate import tabulate
                    try:
                        mydb=mysql.connector.connect(host='localhost',user='root',passwd="",db="pc_express")
                        mycursor=mydb.cursor()
                        name=input('Enter name to be searched:')
                        mycursor.execute("""SELECT * FROM motherboard WHERE Name=%s""",(name,))
                        result=mycursor.fetchall()
                        print(tabulate(result,headers=['Name','Company','Socket_type','Chipset','Qty','Price'],tablefmt='grid'))
                        mydb.commit()
                        print("Record Displayed")
                        print('\n')
                    except Exception as e:
                        print(e)
                        print("Unable to display")
                        print('\n')
                def delmb():
                    import mysql.connector
                    try:
                        mydb=mysql.connector.connect(host='localhost',user='root',passwd="",db="pc_express")
                        mycursor=mydb.cursor()
                        name=input('Enter name to delete record for:')
                        mycursor.execute("""DELETE FROM motherboard WHERE Name=%s""",(name,))
                        mydb.commit()
                        print("Record Deleted")
                        print('\n')
                    except Exception as e:
                        print(e)
                        print("Unable to delete")
                        print('\n')
                mob()
            if a==2:
                def pro():
                    c='l'
                    while c=='l':
                        print("1.Add Processsor Records")
                        print("2.Update Processor Records")
                        print('3.Display Proecessor Records')
                        print("4.Search Processor Records")
                        print("5.Delete Processor Records")
                        print('6.Exit')
                        print('\n')
                        t=int(input("Enter Your Choice:"))
                        print('\n')
                        if t==1:
                            addpro()
                        elif t==2:
                            uppro()
                        elif t==3:
                            dispro()
                        elif t==4:
                            serpro()
                        elif t==5:
                            delpro()
                        else:
                            ('Returning to main menu...')
                            print('\n')
                            break
                def addpro():
                    import mysql.connector
                    try:
                        mydb=mysql.connector.connect(host='localhost',user='root',passwd="",db='pc_express')
                        mycursor=mydb.cursor()
                        company=input('Enter company name:')
                        name=input('Enter Product name:')
                        cores=int(input('Enter No of cores:'))
                        soctype=input("Enter soctype:")
                        basecl=input('Enter base clock:')
                        boostcl=input("Enter Boost clock:")
                        qty=input('Enter Quantity:')
                        price=input('Enter price:')
                        mycursor.execute("""INSERT INTO processor(Company,Name,Cores,Socket_type,Base_clock,Boost_clock,Qty,Price)VALUES(%s,%s,%s,%s,%s,%s,%s,%s)""",(company,name,cores,soctype,basecl,boostcl,qty,price))
                        mydb.commit()
                        print('Records Inserted')
                        print('\n')
                    except Exception as e:
                        print("Unable to insert record")
                        print(e)
                        print('\n')
                
                def uppro():
                    import mysql.connector
                    try:
                        mydb=mysql.connector.connect(host='localhost',user='root',passwd="",db='pc_express')
                        mycursor=mydb.cursor()
                        name=input('Enter Product name:')
                        company=input('Enter company name:')
                        cores=int(input('Enter No of cores:'))
                        soctype=input("Enter soctype:")
                        basecl=input('Enter base clock:')
                        boostcl=input("Enter Boost clock:")
                        qty=input('Enter Quantity:')
                        price=input('Enter price:')
                        mycursor.execute("""UPDATE processor SET Company=%s,Cores=%s,Socket_type=%s,Base_clock=%s,Boost_clock=%s,Qty=%s,Price=%s WHERE Name=%s""",(company,cores,soctype,basecl,boostcl,qty,price,name))
                        print("Record updated")
                        print('\n')
                        mydb.commit()
                    except Exception as e:
                        print(e)
                        print('Unable to Update record')
                        print('\n')

                def dispro():
                    import mysql.connector
                    from tabulate import tabulate
                    try:
                        mydb=mysql.connector.connect(host='localhost',user='root',passwd="",db='pc_express')
                        mycursor=mydb.cursor()
                        mycursor.execute('select * from processor')
                        result=mycursor.fetchall()
                        print(tabulate(result,headers=['Company','Name','Cores','Socket_type','Base_clock','Boost_clock','Qty','Price'], tablefmt='grid'))
                        print("Displaying Record...")
                        print('\n')
                        mydb.commit()
                    except Exception as e:
                        print(e)
                        print('Unable to display record')
                        print('\n')               
                def serpro():
                    import mysql.connector
                    from tabulate import tabulate
                    try:
                        mydb=mysql.connector.connect(host='localhost',user='root',passwd="",db='pc_express')
                        mycursor=mydb.cursor()
                        name=input('Enter name to search record:')
                        mycursor.execute("""SELECT * FROM processor WHERE Name=%s""",(name,))
                        result=mycursor.fetchall()
                        print(tabulate(result,headers=['Company','Name','Cores','Socket_type','Base_clock','Boost_clock','Qty','Price'], tablefmt='grid'))
                        print("Record Searched")
                        print('\n')
                        mydb.commit()
                    except Exception as e:
                        print(e)
                        print("Unable to search record")
                        print('\n')

                def delpro():
                    import mysql.connector
                    try:
                        mydb=mysql.connector.connect(host='localhost',user='root',pssswd="",db='pc_express')
                        mycursor=mydb.cursor()
                        name=input('Enter name for deleting record')
                        mycursor.execute("""DELETE FROM processor WHERE Name=%s""",(name,))
                        print('Record deleted')
                        print('\n')
                        mydb.commit()
                    except Exception as e:
                        print('Unable to delete Record')
                        print('\n')
                        print(e)                        
                pro()
            if a==3:
                def ram():
                    c='u'
                    while c=='u':
                        print("1.Add Ram Records")
                        print("2.Update Ram Records")
                        print("3.Display Ram Records")
                        print("4.Search Ram Records")
                        print("5.Delete Ram Records")
                        print("6.Exit")
                        print("\n")
                        x=int(input("Enter Your choice:"))
                        print('\n')
                        if x==1:
                            addram()
                        elif x==2:
                            upram()
                        elif x==3:
                            disram()
                        elif x==4:
                            serram()
                        elif x==5:
                            delram()
                        else:
                            print("Returing to main menu...")
                            print('\n')
                            break

                def addram():
                    import mysql.connector
                    try:
                        mydb=mysql.connector.connect(host='localhost',user='root',passwd="",db='pc_express')
                        mycursor=mydb.cursor()
                        company=input("Enter Company name:")
                        name=input('Enter Name:')
                        size=input("Enter Size:")
                        speed=input('Enter Speed:')
                        ramtype=input("Enter Ramtype:")
                        qty=input('Enter Quantity:')
                        price=input('Enter Price:')
                        mycursor.execute("""INSERT INTO rams(Company,Name,Size,Speed,Ram_type,Qty,Price)VALUES(%s,%s,%s,%s,%s,%s,%s)""",(company,name,size,speed,ramtype,qty,price))
                        print('Record Inserted')
                        print('\n')
                        mydb.commit()
                    except Exception as e:
                        print("Unable to insert Record")
                        print(e)
                        print('\n')
                
                def upram():
                    import mysql.connector
                    try:
                        mydb=mysql.connector.connect(host='localhost',user='root',passwd="",db='pc_express')
                        mycursor=mydb.cursor()
                        name=input('Enter Name:')
                        company=input("Enter Company name:") 
                        size=input("Enter Size:")
                        speed=input('Enter Speed:')
                        ramtype=input("Enter Ramtype:")
                        qty=input('Enter Quantity:')
                        price=input('Enter Price:')
                        mycursor.execute("""UPDATE rams SET Company=%s,Size=%s,Speed=%s,Ram_type=%s,Qty=%s,Price=%s WHERE Name=%s""",(company,size,speed,ramtype,qty,price,name))
                        print('Record updated')
                        print('\n')
                        mydb.commit()
                    except Exception as e:
                        print("Unable to update record")
                        print(e)
                        print('\n')
                def disram():
                    import mysql.connector
                    from tabulate import tabulate
                    try:
                        mydb=mysql.connector.connect(host='localhost',user='root',passwd="",db='pc_express')
                        mycursor=mydb.cursor()
                        mycursor.execute('select * from rams')
                        results=mycursor.fetchall()
                        print(tabulate(results,headers=['Company','Name','Size','Speed','Ram_type','Qty','Price'], tablefmt='grid'))
                        print('Record Displayed')
                        print('\n')
                        mydb.commit()
                    except Exception as e:
                        print("Unable to display record")
                        print(e)
                        print('\n')
                def serram():
                    import mysql.connector
                    from tabulate import tabulate
                    try:
                        mydb=mysql.connector.connect(host='localhost',user='root',passwd="",db='pc_express')
                        mycursor=mydb.cursor()
                        name=input('Enter name you want to search for:')
                        mycursor.execute("""SELECT * FROM rams WHERE Name=%s""",(name,))
                        result=mycursor.fetchall()
                        print(tabulate(result,headers=['Company','Name','Size','Speed','Ram_type','Qty','Price'], tablefmt='grid'))
                        print('Record displayed')
                        print('\n')
                        mydb.commit()
                    except Exception as e:
                        print("Unable to search record")
                        print(e)
                        print('\n')
                def delram():
                    import mysql.connector
                    try:
                        mydb=mysql.connector.connect(host='localhost',user='root',passwd="",db='pc_express')
                        mycursor=mydb.cursor()
                        name=input('Enter the name for deleting record:')
                        mycursor.execute("""DELETE FROM rams WHERE Name=%s""",(name,))
                        print('Record deleted')
                        print('\n')
                        mydb.commit()
                    except Exception as e:
                        print("Unable to delete")
                        print(e)
                        print('\n')
                ram()
            if a==4:
                def storage():
                    b='g'
                    while b=='g':
                        print("1.Add Storage Records")
                        print("2.Update Storage Records")
                        print("3.Display Storage Records")
                        print("4.Search Storage Records")
                        print("5.Delete Storage Records")
                        print("6.Exit")
                        print("\n")
                        c=int(input("Enter Your Choice:"))
                        print('\n')
                        if c==1:
                            addsto()
                        elif c==2:
                            upsto()
                        elif c==3:
                            dissto()
                        elif c==4:
                            sersto()
                        elif c==5:
                            delsto()
                        else:
                            print("Returing to main menu...")
                            print('\n')
                            break
                def addsto():
                    import mysql.connector
                    try:
                        mydb=mysql.connector.connect(host='localhost',user='root',passwd="",db='pc_express')
                        mycursor=mydb.cursor()
                        company=input('Enter Company name:')
                        name=input('Enter product name:')
                        type=input('Enter storage type:')
                        speed=input('Enter speed:')
                        size=input("Enter Storage size:")
                        qty=input('Enter Quantity')
                        price=input('Enter price:')
                        mycursor.execute("""INSERT INTO storage(Company,Name,Type,Speed,Size,Qty,Price)VALUES(%s,%s,%s,%s,%s,%s,%s)""",(company,name,type,speed,size,qty,price))
                        print('Record Inserted')
                        print('\n')
                        mydb.commit()
                    except Exception as e:
                        print("Unable to insert record ")
                        print(e)
                        print('\n')
                def upsto():
                    import mysql.connector
                    try:
                        mydb=mysql.connector.connect(host='localhost',user='root',passwd="",db="pc_express")
                        mycursor=mydb.cursor()
                        name=input('Enter product name:')
                        company=input('Enter Company name:')
                        type=input('Enter storage type:')
                        speed=input('Enter speed:')
                        size=input("Enter Storage size:")
                        qty=input('Enter Quantity')
                        price=input('Enter price:')                        
                        mycursor.execute("""UPDATE storage SET Company=%s,Type=%s,Speed=%s,Size=%s,Qty=%s,Price=%s WHERE Name=%s""",(company,type,speed,size,qty,price,name))
                        print('Record Updated')
                        print('\n')
                        mydb.commit()
                    except Exception as e:
                        print("Unable to update the record")
                        print(e)
                        print('\n')
                def dissto():
                    import mysql.connector
                    from tabulate import tabulate
                    try:
                        mydb=mysql.connector.connect(host='localhost',user='root',passwd="",db="pc_express")
                        mycursor=mydb.cursor()
                        mycursor.execute("select * from storage")
                        results=mycursor.fetchall()
                        print(tabulate(results,headers=['Company','Name','Type','Speed','Size','Qty','Price'], tablefmt='grid'))
                        print('Record Displayed')
                        print('\n')
                        mydb.commit()
                    except Exception as e:
                        print("Unable to display record")
                        print(e)
                        print('\n')
                def sersto():
                    import mysql.connector
                    from tabulate import tabulate
                    try:
                        mydb=mysql.connector.connect(host='localhost',user='root',passwd="",db='pc_express')
                        mycursor=mydb.cursor()
                        name=input('Enter name you want to want to search for:')
                        mycursor.execute("""SELECT * FROM storage WHERE Name=%s""",(name,))
                        result=mycursor.fetchall()
                        print(tabulate(result,headers=['Company','Name','Type','Speed','Size','Qty','Price'], tablefmt='grid'))
                        print('Record displayed')
                        print('\n')
                        mydb.commit()
                    except Exception as e:
                        print("Unable to search record")
                        print(e)
                        print('\n')
                def delsto():
                    import mysql.connector
                    try:
                        mydb=mysql.connector.connect(host='localhost',user='root',passwd="",db='pc_express')
                        mycursor=mydb.cursor()
                        name=input('Enter name to delete record:')
                        mycursor.execute("""DELETE FROM storage WHERE Name=%s""",(name,))
                        print("Records Deleted")
                        mydb.commit()
                        print('\n')
                    except Exception as e:
                        print("Unable to Delete record")
                        print(e)
                        print('\n')
                storage()
            if a==5:
                def gfx():
                    o='p'
                    while o=='p':
                        print("1.Add Graphic card Records")
                        print("2.Update Graphic card Records")
                        print("3.Display Graphic card Records")
                        print("4.Search Graphic card Records")
                        print("5.Delete Graphic card Records")
                        print("6.Exit")
                        print('\n')
                        y=int(input('Enter Your Choice:'))
                        print('\n')
                        if y==1:
                            addgfx()
                        elif y==2:
                            upgfx()
                        elif y==3:
                            disgfx()
                        elif y==4:
                            sergfx()
                        elif y==5:
                            delgfx()
                        else:
                            print('Returing to main menu...')
                            print('\n')
                            break

                def addgfx():
                    import mysql.connector
                    try:
                        mydb=mysql.connector.connect(host='localhost',user='root',passwd="",db='pc_express')
                        mycursor=mydb.cursor()
                        company=input("Enter company name:")
                        name=input("Enter product name:")
                        memtype=input("Enter Memory Type:")
                        vram=input("Enter Amount of vram:")
                        qty=input('Enter Quantity')
                        price=input("Enter price of graphic card")
                        mycursor.execute("""INSERT INTO graphic_cards(Company,Name,Memory_Type,Vram,Qty,Price)VALUES(%s,%s,%s,%s,%s,%s)""",(company,name,memtype,vram,qty,price))
                        print("Record Inserted")
                        print('\n')
                        mydb.commit()
                    except Exception as e:
                        print("Unable to insert record")
                        print(e)
                        print('\n')
                def upgfx():
                    import mysql.connector
                    try:
                        mydb=mysql.connector.connect(host='localhost',user='root',passwd="",db='pc_express')
                        mycursor=mydb.cursor()
                        name=input("Enter product name:")
                        company=input("Enter company name:")
                        memtype=input("Enter Memory Type:")
                        vram=input("Enter Amount of vram:")
                        qty=input('Enter Quantity:')
                        price=input("Enter price of graphic card:")
                        mycursor.execute("""UPDATE graphic_cards SET Company=%s,Memory_Type=%s,Vram=%s,Qty=%s,Price=%s WHERE Name=%s""",(company,memtype,vram,qty,price,name))
                        print("Record Updated")
                        print('\n')
                        mydb.commit()
                    except Exception as e:
                        print("Unable to update records")
                        print(e)
                        print('\n')
                def disgfx():
                    import mysql.connector
                    from tabulate import tabulate
                    try:
                        mydb=mysql.connector.connect(host='localhost',user='root',passwd="",db='pc_express')
                        mycursor=mydb.cursor()
                        mycursor.execute("select * from graphic_cards")
                        results=mycursor.fetchall()
                        print(tabulate(results,headers=['Company','Name','Memory_Type','Vram','Qty','Price'], tablefmt='grid'))
                        print('Record Displayed')
                        print('\n')
                        mydb.commit()
                    except Exception as e:
                        print("Unable to display records")
                        print(e)
                        print('\n')
                def sergfx():
                    import mysql.connector
                    from tabulate import tabulate
                    try:
                        mydb=mysql.connector.connect(host='localhost',user='root',passwd="",db='pc_express')
                        mycursor=mydb.cursor()
                        name=input("Enter the name to search for:")
                        mycursor.execute("""SELECT * FROM graphic_cards WHERE Name=%s""",(name,))
                        result=mycursor.fetchall()
                        print(tabulate(result,headers=['Company','Name','Memory_Type','Vram','Qty','Price'], tablefmt='grid'))
                        print("Record displayed")
                        print('\n')
                        mydb.commit()
                    except Exception as e:
                        print("Unable to search record")
                        print(e)
                        print('\n')
                def delgfx():
                    import mysql.connector
                    try:
                        mydb=mysql.connector.connect(host='localhost',user='root',passwd="",db='pc_express')
                        mycursor=mydb.cursor()
                        name=input('Enter to name to delete record:')
                        mycursor.execute("""DELETE FROM graphic_cards WHERE Name=%s""",(name,))
                        print("Record deleted")
                        print('\n')
                        mydb.commit()
                    except Exception as e:
                        print("Unable to delete record")
                        print(e)
                        print('\n')
                gfx()
            if a==6:
                def psu():
                    g='f'
                    while g=='f':
                        print("1.Add Power Supply Records")
                        print("2.Update Power Supply Records")
                        print("3.Display Power Supply Records")
                        print("4.Search Power Supply Records")
                        print("5.Delete Power Supply Records")
                        print('\n')
                        e=int(input('Enter Your Choice:'))
                        print('\n')
                        if e==1:
                            addpsu()
                        elif e==2:
                            uppsu()
                        elif e==3:
                            dispsu()
                        elif e==4:
                            serpsu()
                        elif e==5:
                            delpsu()
                        else:
                            print("Returing to main menu...")
                            print('\n')
                            break
                def addpsu():
                    import mysql.connector
                    try:
                        mydb=mysql.connector.connect(host='localhost',user='root',passwd="",db='pc_express')
                        mycursor=mydb.cursor()
                        company=input('Enter Company name:')
                        name=input('Enter Product name:')
                        psutype=input('Enter the psu type:')
                        watts=input('Enter Watts: ')
                        qty=input('Enter Quantity:')
                        price=input('Enter price:')
                        mycursor.execute("""INSERT INTO power_supply(Company,Name,Type,Watts,Qty,Price)VALUES(%s,%s,%s,%s,%s,%s)""",(company,name,psutype,watts,qty,price))
                        print("Record Inserted")
                        print('\n')
                        mydb.commit()
                    except Exception as e:
                        print('Unable to insert record')
                        print(e)
                        print('\n')
                def uppsu():
                    import mysql.connector
                    try:
                        mydb=mysql.connector.connect(host='localhost',user='root',passwd="",db='pc_express')
                        mycursor=mydb.cursor()
                        name=input('Enter Product name:')
                        company=input('Enter Company name:')
                        psutype=input('Enter the psu type:')
                        watts=input('Enter Watts: ')
                        qty=input('Enter Quantity:')
                        price=input('Enter price:')
                        mycursor.execute("""UPDATE power_supply SET Company=%s,Name=%s,Type=%s,Watts=%s,Qty=%s,Price=%s WHERE Name=%s""",(company,psutype,watts,qty,price,name))
                        print("Record updates")
                        print('\n')
                        mydb.commit()
                    except Exception as e:
                        print('Unable to insert record')
                        print(e)
                        print('\n')
                def dispsu():
                    import mysql.connector
                    from tabulate import tabulate
                    try:
                        mydb=mysql.connector.connect(host='localhost',user='root',passwd="",db='pc_express')
                        mycursor=mydb.cursor()
                        mycursor.execute('select * from power_supply')
                        results=mycursor.fetchall()
                        print(tabulate(results,headers=['Company','Name','Type','Watts','Qty','Price'], tablefmt='grid'))
                        print("Records Displayed")
                        print('\n')
                        mydb.commit()
                    except Exception as e:
                        print("Unable to display records")
                        print(e)
                        print('\n')
                def serpsu():
                    import mysql.connector
                    from tabulate import tabulate
                    try:
                        mydb=mysql.connector.connect(host='localhost',user='root',passwd="",db='pc_express')
                        mycursor=mydb.cursor()
                        name=input('Enter the name you want to search for:')
                        mycursor.execute("""SELECT * FROM power_supply WHERE Name=%s""",(name,))
                        result=mycursor.fetchall()
                        print(tabulate(result,headers=['Company','Name','Type','Watts','Qty','Price'], tablefmt='grid'))
                        print("Records displayed")
                        print('\n')
                        mydb.commit()
                    except Exception as e:
                        print("Unable to search record")
                        print(e)
                        print('\n')
                def delpsu():
                    import mysql.connector
                    try:
                        mydb=mysql.connector.connect(host='localhost',user='root',passwd="",db='pc_express')
                        mycursor=mydb.cursor()
                        name=input('Enter name to delete record for:')
                        mycursor.execute("""DELETE FROM power_supply WHERE Name=%s""",(name,))
                        print('Record Deleted')
                        print('\n')
                        mydb.commit()
                    except Exception as e:
                        print('Unable to delete record')
                        print(e)
                        print('\n')
                psu()
            if a==7:
                def case():
                    h='g'
                    while h=='g':
                        print('1.Add cabinet records')
                        print('2.Update cabinet records')
                        print('3.Display cabinet records')
                        print("4.Search cabinet records")
                        print('5.Delete cabinet records')
                        print('6.Exit')
                        print('\n')
                        v=int(input("Enter Your Choice"))
                        print("\n")
                        if v==1:
                            addcase()
                        elif v==2:
                            upcase()
                        elif v==3:
                            discase()
                        elif v==4:
                            sercase()
                        elif v==5:
                            delcase()
                        else:
                            ("Returning to main menu...")
                            print('\n')
                            break
                def addcase():
                    import mysql.connector
                    try:
                        mydb=mysql.connector.connect(host='localhost',user='root',passwd="",db='pc_express')
                        mycursor=mydb.cursor()
                        company=input("Enter Company name:")
                        name=input("Enter Product name:")
                        size=input("Enter the Form Factor:")
                        qty=input('Enter Quantity:')
                        price=input('Enter Price:')
                        mycursor.execute("""INSERT INTO cabinet(Company,Name,Form_Factor,Qty,Price)VALUES(%s,%s,%s,%s,%s)""",(company,name,size,qty,price))
                        print('Record Inserted')
                        print('\n')
                        mydb.commit()
                    except Exception as e:
                        print('Unable to insert record')
                        print(e)
                        print('\n')
                def upcase():
                    import mysql.connector
                    try:
                        mydb=mysql.connector.connect(host='localhost',user='root',passwd="",db='pc_express')
                        mycursor=mydb.cursor()
                        name=input("Enter Product name:")
                        company=input("Enter Company name:")         
                        size=input("Enter the Form Factor:")
                        qty=input('Enter Quantity:')
                        price=input('Enter Price:')
                        mycursor.execute("""UPDATE cabinet SET Company=%s,Form_Factor=%s,Qty=%s,Price=%s WHERE Name=%s""",(company,size,qty,price,name) )
                        print("Record Updated")
                        print('\n')
                        mydb.commit()
                    except Exception as e:
                        print("Unable to update record")
                        print(e)
                        print('\n')
                def discase():
                    import mysql.connector
                    from tabulate import tabulate
                    try:
                        mydb=mysql.connector.connect(host='localhost',user='root',passwd="",db='pc_express')
                        mycursor=mydb.cursor()
                        mycursor.execute("select * from cabinet")
                        results=mycursor.fetchall()
                        print(tabulate(results,headers=['Company','Name','Form_Factor','Qty','Price'], tablefmt='grid'))
                        print('Record Displayed')
                        print('\n')
                        mydb.commit()
                    except Exception as e:
                        print('Unable to display record')
                        print(e)
                        print('\n')
                def sercase():
                    import mysql.connector
                    from tabulate import tabulate
                    try:
                        mydb=mysql.connector.connect(host='localhost',user='root',passwd="",db='pc_express')
                        mycursor=mydb.cursor()
                        name=input('Enter the name to search for:')
                        mycursor.execute(""""SELECT * FROM cabinet WHERE Name=%s""",(name,))
                        result=mycursor.fetchall()
                        print(tabulate(result,headers=['Company','Name','Form_Factor','Qty','Price'], tablefmt='grid'))
                        print('Record displayed')
                        print('\n')
                        mydb.commit()
                    except Exception as e:
                        print("Unable to search record")
                        print(e)
                        print('\n')
                def delcase():
                    import mysql.connector
                    try:
                        mydb=mysql.connector.connect(host='localhost',user='root',passwd="",db='pc_express')
                        mycursor=mydb.cursor()
                        name=input('Enter the name to delete record:')
                        mycursor.execute("""DELETE FROM cabinet WHERE Name=%s""",(name,))
                        print("Record Deleted")
                        print('\n')
                        mydb.commit()
                    except Exception as e:
                        print('Unable to delete record')
                        print(e)     
                        print('\n')               
                case() 
            else:
                print('Returning to main menu...')
                print('\n')       


    if choice==2:
        def sale():
            f='i'
            while f=='i':
                print('1.Add Sales Details records')
                print("2.Update Sales Details records")
                print('3.Display Sales Details records')
                print('4.Search Sales Details records')
                print('5.Delete Sales Details records')
                print('6.Exit')
                print('\n')
                f=int(input("Enter Your Choice:"))
                print('\n')
                if f==1:
                    addsale()
                elif f==2:
                    upsale()
                elif f==3:
                    dissale()
                elif f==4:
                    sersale()
                elif f==5:
                    delsale()
                else:
                    ('Returing to main menu...')
                    print('\n')
                    break
        def addsale():
            import mysql.connector
            try:
                mydb=mysql.connector.connect(host='localhost',user='root',passwd="",db='pc_express')
                mycursor=mydb.cursor()
                cname=input('Enter Customer name:')
                phno=input('Enter Phone number:')
                dog=input("Enter Description_of_Goods:")
                dop=input('Enter the Date_of_purchase:')
                qty=input('Enter Quantity:')
                price=input('Enter price:')
                mycursor.execute("""INSERT INTO sales_details(C_name,Phone_No,Description_of_Goods,Date_of_purchase,Qty,Price)VALUES(%s,%s,%s,%s,%s,%s)""",(cname,phno,dog,dop,qty,price))
                print('Record Updated')
                print('\n')
                mydb.commit()
            except Exception as e:
                print('Unable to insert record')
                print(e)
                print('\n')
        def upsale():
            import mysql.connector
            try:
                mydb=mysql.connector.connect(host='localhost',user='root',passwd="",db='pc_express')
                mycursor=mydb.cursor()
                cname=input('Enter Customer name:')
                phno=input('Enter Phone number:')
                dog=input("Enter Description_of_Goods:")
                dop=input('Enter the Date_of_purchase:')
                qty=input('Enter Quantity:')
                price=input('Enter price:')
                mycursor.execute("""UPDATE sales_details SET Phone_No=%s,Description_of_Goods=%s,Date_of_purchase=%s,Qty=%s,Price=%s WHERE C_name=%s""",(phno,dog,dop,qty,price,cname))
                print("Record Updates")
                print('\n')
                mydb.commit()
            except Exception as e:
                print("Unable to update record")
                print(e)
                print('\n')
        def dissale():
            import mysql.connector
            from tabulate import tabulate
            try:
                mydb=mysql.connector.connect(host='localhost',user='root',passwd="",db='pc_express')
                mycursor=mydb.cursor()
                mycursor.execute('select * from sales_details')
                results=mycursor.fetchall()
                print(tabulate(results,headers=['C_name','Phone_No','Description_of_Goods','Date_of_purchase','Qty','Price'], tablefmt='grid'))
                print('Record Displayed')
                print('\n')
                mydb.commit()
            except Exception as e:
                print("Unable to display record")
                print(e)
                print('\n')
        def sersale():
            import mysql.connector
            from tabulate import tabulate
            try:
                mydb=mysql.connector.connect(host='localhost',user='root',passwd="",db='pc_express')
                mycursor=mydb.cursor()
                cname=input('Enter name to search for:')
                mycursor.execute("""SELECT * FROM sales_details WHERE C_name=%s""",(cname,))
                result=mycursor.fetchall()
                print(tabulate(result,headers=['C_name','Phone_No','Description_of_Goods','Date_of_purchase','Qty','Price'], tablefmt='grid'))
                print('Record Displayed')
                print('\n')
                mydb.commit()
            except Exception as e:
                print('Unable to search record')
                print(e)
                print('\n')
        def delsale():
            import mysql.connector
            try:
                mydb=mysql.connector.connect(host='localhost',user='root',passwd="",db='pc_express')
                mycursor=mydb.cursor()
                cname=input("Enter the name to delete record:")
                mycursor.execute("""DELETE FROM sales_details WHERE C_name=%s""",(cname,))
                print('Record deleted')
                print('\n')
                mydb.commit()
            except Exception as e:
                print('Unable to delete Record')
                print(e)
                print('\n')
        sale()
        
    if choice==3:
        exit()
