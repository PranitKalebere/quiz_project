import os
import re


def register():
    fp = open('database.txt', 'r')
    fp.flush()
    os.system("cls")

    first_name = input("Enter Your First Name :")
    last_name = input("Enter Your Last Name :")
    student_id = input("Enter Your Student id Or Roll Number :")
    UserName = input("Create Any Username :")
    PassWord2 = input("Create Password For New User Resistration :")
    PassWord = passwords(PassWord2)
    ConfPass2 = input("Renter Your Password :")
    ConfPass = passwords(ConfPass2)

    uname = []
    pwd = []
    for i in fp:
        firstname, lastname, studentid, username, password = i.split(",")
        password = password.strip()
        uname.append(username)
        pwd.append(password)
    data = dict(zip(uname, pwd))

    if PassWord != ConfPass:
        print("Password Donot Matches... ")
        print("Please Try Aganin..!")
        register()
    else:
        if len(ConfPass) <= 5:
            print("password is too short.. Please Enter Anathor Password")
            register()

        elif UserName in uname:
            print("Username is Already Exist..")
            register()
        else:
            fp = open('database.txt', 'a')
            fp.write(first_name + ',' + last_name + ',' + student_id + ',' + UserName + ',' + ConfPass + '\n')
            fp.flush()
            print("Successfully Created A Username and password...!")
            fp.close()
            os.system("cls")
            login()


def login():
    global unm
    unm = input("Enter Your Username :")
    psw = input("Enter Your Password :")



    fp = open('database.txt', 'r')

    if not len(unm or psw) <= 1:
        uname = []
        pwd = []
        fname = []
        lname = []
        stdid = []
        uname2 = []

        for i in fp:
            firstname, lastname, studentid, username, password = i.split(",")
            password = password.strip()
            fname.append(firstname)
            lname.append(lastname)
            stdid.append(studentid)
            uname2.append(username)
            uname.append(username)
            pwd.append(password)
        credentials = dict(zip(uname, pwd))
        info1 = dict(zip(uname,fname))
        info2 = dict(zip(uname,lname))
        info3 = dict(zip(uname,stdid))

        global FirstName
        global LastnaMe
        global StudentId
        FirstName = info1[unm]
        LastnaMe = info2[unm]
        StudentId = info3[unm]



        try:
            if credentials[unm]:
                try:
                    if psw == credentials[unm]:

                        print("Login Successfully...!")
                        print("\n")
                        os.system("cls")
                        print(f'\n\tHello, {FirstName} {LastnaMe}')
                        quiz()
                    else:
                        print("Password of Username is incorrect")
                        login()
                except:
                    pass
            else:
                print("user not found ")
                login()
        except:
            print("Login error")
            login()
    else:
        print("Please Enter Any value")
        login()


def menu():
    option = int(input('''\n1. Login
2. Signup
Please Enter Your Choise :'''))
    if option == 1:
        login()
    elif option == 2:
        register()

def passwords(passwd):

    while(True):
        
        flag = 0

        if not re.search('[0-9]', passwd):
            flag =1
        if not re.search('[a-z]', passwd):
            flag =1
        if not re.search('[A-Z]',passwd):
            flag =1
        if not re.search('[#$!@]', passwd):
            flag =1


        if flag ==0:
            return passwd
            break
        else:
            print("Password Should Contain Capital Letters,Numbers And Symbols ")
            passwd = input(" Please Enter Correct Password :")

def quiz():
    
    counter = 0
    report = []
    print('''\n\n\tINSTRUCTIONS.\n
        * ALL ANSWERS ARE COMPULSORY..
        * ANSWERS MUST BE (A,B,C,D) OTHERWISE THAT ANSWER TO BE CONSIDERED AS WRONG..
        * YOU HAVE TO JUST TYPE THE OPTION OF THAT GIVEN QUESTIONS EITHER IN CAPITAL LETTER OR IN SMALL LETTER..\n''')
    print('''\n\tNow You Can start Your Test...\n
        ....ALL THE BEST....\n\n''')

    question = ('''Q1.Who Developed Python Programming Language
    
                A). wick van rossum
                B) Rasmus Leodorf
                C). Guidio Van rossum
                D). Niene stom''',
                '''Q2.What will be the value of he following python expression
                
                4 + 3 % 5
                A). 7
                B). 2
                C). 4
                D). 1''',
                '''Q3.which of the following is used to define a block of code in python language
                
                A). indentation
                B). key
                C). brackets
                D). all of the mentioned''',
                '''Q4.Which keyword id used for funtion in python language
                
                A). function
                B). def
                C). fun
                D). define''',
                '''Q5. what will be the output of the following python code
                
                    x = 'abcd'
                    for i in range(len(x)):
                        print(i)
                    
                A). error
                B). 1 2 3 4
                C). a b c d
                D). 0 1 2 3''',
                '''Q6.which of the following is a python tuple
                
                A). {1,2,3}
                B). {}
                C). [1,2,3]
                D). (1,2,3)''',
                '''Q7.What is output of print(math.pow(3,2))
                
                A). 9.0
                B). none
                C). 9
                D). none of the mentioned''',
                '''Q8.Which of the following concepts is not a part of python?
                
                A) pointers
                B). loops
                C). dynaminc typing
                D). all of the above''',
                '''Q9.Which of the following is the correct extension of the python file
                
                A). .python
                B). .pl
                C). .py
                D). .p''',
                '''Q10. All keywords i python are in ____
                
                A). capotalized
                B). lower case
                C). upper case
                D). none of the mentioned
                ''')
    answers = ("c", "a", "a", "b", "d", "d", "a", "a", "c", "d")
    useranswers = []

    for i in range(0, 10):
        print("\n",question[i])
        ans = input("\nEnter Your Answer :")
        ans = ans.lower().strip()
        useranswers.append(ans)
    print("\nYour Score is being Processed..")

    for i in range(0,10):
        if answers[i] == useranswers[i]:
            counter += 1
            report.append(i)


    def result():

        print(f"NAME :{FirstName} {LastnaMe}\n")
        print(f"STUDENT ID/ROLL NUMBER :{StudentId}\n")
        print(f"YOUR SCORE IS :{counter}\n")
        print("--------------------")
        if counter != 10:
            print("\n\tAnswers of wrong attempets\n")
            for i in range(0, 10):
                if i not in report:
                    print(question[i], '\n Correct Answer is -->>', answers[i], '\n')
        elif counter == 10:
            print("Congratulation.. You Answered All Correct ")
        print("\n\t...Thanks for Attempting This Quiz...")




    result()
    firstName = str(FirstName)
    lastName = str(LastnaMe)
    studentId = str(StudentId)
    counterstr = str(counter)
    fp = open(f"{unm}.txt", "w")
    fp.write("Name is :" + firstName + lastName + '\n' + 'Your STUDENT ID is :' + studentId + '\n' + "YOUR SCORE IS :" + counterstr + "\n")

    fp.close()

menu()