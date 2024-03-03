# for i in range(10):
#     print(i)

# for i in range(3,10):
#     print(i)

# for i in range(3,10,2):
#     print(i)

# for i in range(10,5,-1):
#     print(i)

# name="Yasin Beken"
# for i in name:
#     print(i)
# print("--------------------")
# for i in range(len(name)):
#     print(name[i])

# Reverse the value entered from the keyboard.
# 1st METHOD (THE TEACHER'S IMPLEMENTATION)
# value=input("Please write the one things: ")
# otherText=""
# for i in range(len(value)-1,-1,-1):
#     otherText+=value[i]
     
# print(otherText)

# 2nd METHOD (IMPLEMENTED BY THE STUDENTS IN THE CLASS)

# value=input("Please write the one things: ")
# otherText=""

# for i in value:
#     otherText=i+otherText
# print(otherText)

# A code that prints a value taken from the keyboard by skipping 1.

# 1st METHOD (MY IMPLEMENTATION LINE BY LINE)
# value=input("Please write the one things: ")

# for i in range(0,len(value),2):
#     print(value[i])

# 2nd METHOD (MY IMPLEMENTATION SIDE BY SIDE)

# value=input("Please write the one things: ")
# result=""

# for i in range(0,len(value),2):
#    result+=value[i]
# print(result)

# choice="06"
# match choice:
#     case "06":
#         print("Ankara")
#     case "34":
#         print("İstanbul")

# i=0
# while i<10:
#     print(i)
#     i+=1

# Factorial calculation obtained by keyboard input.


# (MY IMPLEMENTATION)
# number=int(input("Please enter a number: "))
# result=1
# i=1
# while i<=number:
    
#     result*=i
#     i+=1
# print(f"{number}! = {result}")


# 2nd METHOD (IMPLEMENTED BY THE TEACHER)

# number=int(input("Please enter a number: "))
# result=1
# while number>0:
#     result*=number
#     number-=1
# print(result)


# Using Ternary İf: 
# number=6
# print("Merhaba") if number==5 else print("hello")

# Continue and Break statements

# for i in range(10):
#     if i==3:
#         continue
#     print(i)

# for i in range(3):
#     for j in range(5):
#         if j==2:
#             continue
#         print(f"İ: {i} J: {j}")

# for i in range(10):
#     if i==5:
#         break
#     print(i)

# for i in range(3):
#     for j in range(5):
#         if j==2:
#             break
#         print(f"İ: {i} J: {j}")

# Write a code that separates and prints the characters 'a' or 'A' from a value entered from the keyboard. 


# (MY IMPLEMENTATION)
# value=input("Please write a thing: ")
# newValue=""

# for i in value:
#     if i=="a" or i=="A":
#         continue
#     else:
#         newValue+=i

# print(newValue)

# 2nd METHOD (IMPLEMENTED BY THE TEACHER)


# value=input("Please write a thing: ")
# newValue=""
# for i in range(len(value)):
#     if value[i]=="a" or value[i]=="A":
#         continue
#     newValue+=value[i]
# print(newValue)


# QUESTION - BUILD YOUR BANK AN ATM WITH CASH WITHDRAWAL, DEPOSIT, PASSWORD OPERATIONS, BALANCE OF 20,000 TL.
# (MY IMPLEMENTATION)
# count=0
# balance=int(20000)
# password=input("Please Enter The Password: ")
# while True:
    
#     if password!="1234":
#         while count<=2:
#             if count<2:
#                 password=input("Your password is incorrect. Please enter it again: ")
#                 count+=1
#             if count==2:
#                 print("Your card has been blocked!")
#                 break
#         break
#     if password=="1234":
#         transaction=input(f"Your Balance: {balance} TL.\n1 - Balance Inquiry\n2 - Withdrawal\n3 - Deposit\n0 - Quit\nPlease select the operation you want to perform: ")
#         if transaction=="1":
#             print(f"Your Balance: {balance} TL.")
#         elif transaction=="2":
#             withdrawalOp=int(input("Please enter the amount you want to withdraw: "))
#             if withdrawalOp>balance:
#                 print("Insufficient balance!")
#             else:
#                 balance=balance-withdrawalOp
#                 print(f"The withdrawal has been completed. New balance: {balance} TL.")
#         elif transaction=="3":
#             depositOp=int(input("Please enter the amount you want to deposit: "))
#             balance=balance+depositOp
#             print(f"The deposit transaction has been completed. Your new balance is: {balance} TL.")
#         elif transaction=="0":
#             print("Logging out... Goodbye for now...")
#             break

# 2nd METHOD (IMPLEMENTED BY THE TEACHER)


# count=0
# balance=20000

# while True:
#     password=input("Please Enter The Password: ")
#     if count==2:
#         print("Your card has been blocked!")
#         break
#     if password!="1234":
#         print("Your password is incorrect. Please enter it again: ")
#         count+=1
#         continue
#     while True:
#         choice=input(f"\tMENU\nYour Balance: {balance} TL\n1-Withdrawal\n2-Deposit\n0-Quit")
#         if choice=="1":
#             input=int(input("Please enter the amount you want to withdraw: "))
#             if input>balance:
#                 print("Insufficient balance.")
#             else:
#                 balance-=input
#         elif choice=="2":
#             input=int(input("Please enter the amount you want to deposit: "))
#             balance+=input
#         elif choice=="0":
#             print("Until we meet again.")
#             break
#         else:
#             print("You made an incorrect selection.")

#     break
    

        

            



    

