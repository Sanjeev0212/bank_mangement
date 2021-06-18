import mysql.connector
mydb=mysql.connector.connect(host="localhost",port="3306", user="root", password="sanju123", database="bank_mangement")
def openAcc():
    n=input("Enter The Name: ")
    ac=input("Enter The Account No: ")
    db=input("Enter The Date Of Birth: ")
    add=input("Enter The Address: ")
    cn=input("Enter The Contact Number: ")
    b=ob=int(input("Enter The Opening Balance: "))
    data1=(n,ac,db,add,cn,ob)
    data2=(n,ac,b)
    sql1="insert into account values(%s,%s,%s,%s,%s,%s)"
    sql2="insert into amount values(%s,%s,%s)"
    x=mydb.cursor()
    x.execute(sql1,data1)
    x.execute(sql2,data2)
    mydb.commit() #save the changes
    print("Data Entered Succesfully")
    main()
def depoAmo():
    amo=int(input("Enter the amount you want to deposit: "))
    ac=input("Enter The Account No: ")
    a='select balance from amount where AccNo=%s'
    data=(ac,)
    x=mydb.cursor()
    x.execute(a,data)
    result=x.fetchone()
    t=result[0]+amo
    p=(t,ac)
    sql=('UPDATE amount SET balance=%s WHERE AccNo=%s')
    x.execute(sql,p)
    mydb.commit() #save the changes
    print("Deposit amount succesfully")
    main()
def withdrawAmount():
    amount=int(input("Enter the amount you want to withdraw: "))
    ac=input("Enter The Account No: ")
    a='select balance from amount where AccNo=%s'
    data=(ac,)
    x=mydb.cursor()
    x.execute(a,data)
    result=x.fetchone()
    t=result[0]-amount
    sql=('update amount set balance=%s where AccNo=%s')
    d=(t,ac)
    x.execute(sql,d)
    mydb.commit() #save the changes
    print("Withdraw succesfully")
    main() 
def balEnq():
    ac=input("Enter the account no: ")
    a='select * from amount where AccNo=%s'
    data=(ac,)
    x=mydb.cursor()
    x.execute(a,data)
    result=x.fetchone()
    print("Displaying balance:")
    print('Balance for account',ac,'is',result[-1])
    main()
def disDetails():
    ac=input("Enter the account no: ")
    a='select * from account where AccNo=%s'
    data=(ac,)
    x=mydb.cursor()
    x.execute(a,data)
    result=x.fetchone()
    print("Displaying customer details: ")
    co=1
    for i in result:
        if(co==1):
            print("Account Holder Name: ",i)
        elif(co==2):
            print("Account Number: ",i)
        elif(co==3):
            print("DOB: ",i)   
        elif(co==4):
            print("Address: ",i)
        elif(co==5):
            print("Phone Number: ",i) 
        else:
            print("Account Balance: ",i)
        co=co+1

    main()
def closeAcc():
    ac=input("Enter the account no: ")
    sql1='delete from account where AccNo=%s'
    sql2='delete from amount where AccNo=%s'
    data=(ac,)
    x=mydb.cursor()
    x.execute(sql1,data)
    x.execute(sql2,data)
    mydb.commit()
    print("Account closed succesfully")
    main()
def main():
    print("*"*150)
    print('''
             1.OPEN NEW ACCOUNT
             2.DEPOSIT AMOUNT
             3.WITHDRAW AMOUNT
             4.BALANCE ENQUIRY
             5.DISPLAY CUSTOMER DETAILS
             6.CLOSE AN ACCOUNT ''')
    choice=input("Enter The Number Of Task You Want To Perform:")
    if(choice=='1'):
        openAcc()
    elif(choice=='2'):
        depoAmo()
    elif(choice=='3'):
        withdrawAmount()
    elif(choice=='4'):
        balEnq()
    elif(choice=='5'):
        disDetails()
    elif(choice=='6'):
        closeAcc()
    else:
        print("Invalid Choice")
        main()
main()
