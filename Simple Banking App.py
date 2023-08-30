## Remember this is just a Simulation not a real banking app 
# Generate Random Numbers for Account no. and Balance
import random
tasks = ["1","2","3","4"]
AC_no1 = random.randint(10, 19)
AC_no2 = random.randint(1234 , 9999)
AC_no3 = random.randint(1234 , 9999)
AC_no4 = random.randint(1234 , 9999)
total = random.randint(100000 , 99999999)
# Greets the user
print("Hello!, Welcome to Khan Bank Limited.")
# Card Number
card = input("> Please Enter your Card Number: ")
task = ""
while task != "4":
    while True:
        if card.isnumeric() and len(card) == 15 or len(card) == 16 or len(card) == 14:
            print(f"Your Acccount number is 10{AC_no1} {AC_no2} {AC_no3} {AC_no4}")
            break
        else:
            print("Your Card Number must be from 14 to 16 digits only.")
            card = input("> Please enter a Valid number : ")
    # Menu
    print('''What would you like to do Please type the number for the task you wish to proceed with:
    > 1 - Withdraw
    > 2 - Show Balance
    > 3 - Transfer
    > 4 - Exit''')
    task = input("> ")
    while task not in tasks:
        print("> Please Type the number next to the tasks")
        task =input("> ")
    # Exit (Option)
    if task == "4":
        input("Thanks for banking with us!")
        exit()
    # Withdraw (Option)
    elif task == "1":
        draw = input("> How much would you like to withdraw?: Rs.")
        while True:
            if draw.isnumeric():
                draw = int(draw)
                while draw <= 0:
                    draw = int(input("> Please Enter a Valid Amount to Withdraw: "))
                last = total - draw
                if last < 0 :
                    draw = input( f"> Sorry!, you only have Rs.{total} in your bank account.Please enter a Valid ammount : Rs.")
                else:
                    print(f"> Your amount of Rs.{draw} has been withdrawn")
                    print(f"> Your remaining balance is Rs.{last}  ")
                    input("Thanks for banking with us!")
                    total = last
                    break
    # Show Balance (Option)
    if task == "2":
        print( f"> Your balance is Rs.{total}")
        input("Thanks for banking with us!")
    # Transfer (Option)
    if task == "3":
        while True:
            AC = input("Please Enter the Account no. you wish to transfer to: ")
            if AC.isnumeric() and len(AC) == 16:
                transfered =int(input(( f"> What's the Amount you wish to transfer: Rs.")))
                print(f"> The amount Rs.{transfered} has been transfered to Account no.{AC}")
                total = total - transfered
                print(f"Your remaining balance is {total}")
                input("Thanks for banking with us!")
                break
            else:
                print("The Account no. must be 16 digits (e.g 1023 1823 6612 9937) :")
                AC = input("> Please enter a Valid Account no. : ")




















