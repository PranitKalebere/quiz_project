import re
import os

class Student:
    def __init__(self):
        self.student_Details = []
        self.login = False

    def Register(self,Firstname, Lastname, Id, Username,Passwd):
        self.register_condition = True
        self.firstname = Firstname
        self.lastname = Lastname
        self.id = Id
        self.username = Username
        self.passwd = Passwd

        
        
        file_check_condition = os.path.isfile(f"D:\python_quiz_project\{Username}.txt") and os.path.getsize(f"D:\python_quiz_project\{Username}.txt") > 0
        if file_check_condition == True:
            print("User Already Registerd..!")
            self.register_condition = False
        else:
                while (True):
                    flag = 0

                    if not re.search('[0-9]', self.passwd):
                        flag = 1
                    if not re.search('[a-z]', self.passwd):
                        flag = 1
                    if not re.search('[A-Z]', self.passwd):
                        flag = 1
                    if not re.search('[#$!@]', self.passwd):
                        flag = 1

                    if flag == 0:
                        self.passwd = self.passwd
                        break
                    else:
                        print("Password Should Contain Capital Letters,Numbers And Symbols ")
                        self.passwd = input(" Please Enter Correct Password :")

                self.student_Details = [Firstname, Lastname, Id, Username, self.passwd]
                with open(f"{Username}.txt", "w") as f:
                    for Details in self.student_Details:
                        f.write(str(Details) + '\n')    
            

    def Login(self,Username, Password):
        with open(f"{Username}.txt","r") as f:
            Details = f.read()
            self.student_Details = Details.split("\n")
            if str(Username) in str(self.student_Details):
                if str(Password) in str(self.student_Details):
                    self.login = True
                else:
                    print("Wrong Password..!")
            else:
                print("Username is Invalid..!")

            if self.login == True:

                firstName = str(self.student_Details[0])
                lastName = str(self.student_Details[1])
                studentId = str(self.student_Details[2])

                file_check_condition = os.path.isfile(f"D:\python_quiz_project\{firstName}{lastName}.txt") and os.path.getsize(f"D:\python_quiz_project\{firstName}{lastName}.txt") > 0
                if file_check_condition == False:
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
                        print("\n", question[i])
                        ans = input("\nEnter Your Answer :")
                        ans = ans.lower().strip()
                        useranswers.append(ans)
                    print("\nYour Score is being Processed..")

                    for i in range(0, 10):
                        if answers[i] == useranswers[i]:
                            counter += 1
                            report.append(i)

                    print(f"NAME :{self.student_Details[0]} {self.student_Details[1]}\n")
                    print(f"STUDENT ID/ROLL NUMBER :{self.student_Details[2]}\n")
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


                    fp = open(f"{firstName}{lastName}.txt", "a")
                    fp.write(
                        "Name is :" + firstName + lastName + '\n' + 'Your STUDENT ID is :' + studentId + '\n' + "YOUR SCORE IS :" + str(
                            counter) + "\n")
                    fp.close()

                else:
                    print("You Already Given This Test..!\nthank you ..!")


student = Student()

def MainMenu():
    print('''1. Register
2. Login
Press 1 for Register and 2 for Login''')

    UserInput = int(input("Please Enter Your Choice: "))

    if UserInput == 1:
        firstname = input("Please Enter Your Firstname: ")
        lastname = input("Please Enter Your Lastname: ")
        id = input("Please Enter Your Student Roll No/ Id: ")
        username = input("Enter A Username You Want To Put: ")
        password = input("Please Enter Your Password: ")
        student.Register(firstname, lastname, id, username, password)
        if student.register_condition == True:
            print("Press 1 for go to Login Page And 2 for Exit this program")
            userinput = int(input("Please Enter Your Choice: "))

            if userinput == 1:
                username = input("Enter Your Username: ")
                password = input("Please Enter Your Password: ")
                student.Login(username, password)
        else:
            return False

            
    if UserInput == 2:
        username = input("Enter Your Username: ")
        password = input("Please Enter Your Password: ")
        student.Login(username,password)

MainMenu()