"""
-> Create a food log file for each client.
-> Create an exercise log file for each client.
-> Ask the user whether they want to log or retrieve client data.
-> Write a function that takes the user input of the client's name.
-> After the client name is entered , a message should be display "What you want to log, diet or exercise"
-> Write a function to retrieve exercise or food file records for any client.
"""

# 3 clients - Client_1 , Client_2 and Client_3
# Total 6 files

import datetime
def getdate() :
    return datetime.datetime.now()

def gettime() :
    return datetime.datetime.now()

def logvalue(k) :
    if k==1 :
        c = int(input("Enter '1' for Excersise and '2' for Food : "))
        if (c==1) :
            value = input("Type Here\n")
            with open("Client_1_exercise.txt","a") as op:
                op.write(str([str(gettime())])+" : "+value+"\n")
            print("Successfully Written...")
        elif (c==2) :
            value = input("Type Here :-\n")
            with open("Client_1_food.txt", "a") as op:
                op.write(str([str(gettime())]) + " : " + value + "\n")
            print("Successfully Written...")
        else :
            print("Invalid Input..!!")

    elif(k==2) :
        c = int(input("Enter '1' for Excersise and '2' for Food : "))
        if (c == 1) :
            value = input("Type Here :-\n")
            with open("Client_2_exercise.txt", "a") as op:
                op.write(str([str(gettime())]) + " : " + value + "\n")
            print("Successfully Written...")
        elif (c == 2) :
            value = input("Type Here :-\n")
            with open("Client_2_food.txt", "a") as op:
                op.write(str([str(gettime())]) + " : " + value + "\n")
            print("Successfully Written...")
        else :
            print("Invalid Input..!!")

    elif(k==3) :
        c = int(input("Enter '1' for Excersise and '2' for Food : "))
        if (c == 1) :
            value = input("Type Here :-\n")
            with open("Client_3_exercise.txt", "a") as op:
                op.write(str([str(gettime())]) + " : " + value + "\n")
            print("Successfully Written...")
        elif (c == 2) :
            value = input("Type Here :-\n")
            with open("Client_3_food.txt", "a") as op:
                op.write(str([str(gettime())]) + " : " + value + "\n")
            print("Successfully Written...")
        else :
            print("Invalid Input..!!")
        
    else :
        print("Invalid Input..!!")

def retrieve(k) :
    if k==1 :
        c = int(input("Enter '1' for Excersise and '2' for Food : "))
        if (c==1) :
            with open("Client_1_exercise.txt") as op:
                for i in op:
                    print(i,end="")
        elif (c==2) :
            with open("Client_1_food.txt") as op:
                for i in op:
                    print(i, end="")
        else :
            print("Invalid Input..!!")

    elif (k==2) :
        c = int(input("Enter '1' for Excersise and '2' for Food : "))
        if (c == 1) :
            with open("Client_2_exercise.txt") as op:
                for i in op:
                    print(i, end="")
        elif (c == 2) :
            with open("Client_2_food.txt") as op:
                for i in op:
                    print(i, end="")
        else :
            print("Invalid Input..!!")

    elif(k==3) :
        c = int(input("Enter '1' for Excersise and '2' for Food : "))
        if (c == 1) :
            with open("Client_3_exercise.txt") as op:
                for i in op:
                    print(i, end="")
        elif (c == 2) :
            with open("Client_3_food.txt") as op:
                for i in op:
                    print(i, end="")
        else :
            print("Invalid Input..!!")

    else:
        print("Invalid Input..!!")

print("* * * * * * * * * * Health Management System * * * * * * * * * *\n")
a = int(input("Press '1' for Log The Value and '2' for Retrieve : "))
if a==1 :
    b = int(input("Press '1' for Client_1 , '2' for Client_2 , '3' for Client_3 : "))
    logvalue(b)
elif a==2 :
    b = int(input("Press '1' for Client_1 , '2' for Client_2 , '3' for Client_3 : "))
    retrieve(b)
else :
    print("Invalid Input..!!")