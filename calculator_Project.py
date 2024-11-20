###I. Creating a simple calculator
'''
I am gonna create a calculator which will be able to perform
the following operations:
1.add, sub, div, mul, exp,root  
'''
def add(a,b):
    result= a+b
    print(num1,'+',num2,'=',result)
def sub(a,b):
    result= a-b
    print(num1,'-',num2,'=',result)
def div(a,b):
    result= a/b
    print(num1,'/',num2,'=',result)
def mul(a,b):
    result= a*b
    print(num1,'x',num2,'=',result)
def exp(a,b):
    result= a**b
    print(num1,'^',num2,'=',result)



def first():
    global num1
    num1=float(input("Enter the first number: "))
    global operators 
    operators=['+','-','/','x','^']
    global x 
    x =input("Enter the operator: ")
    while x not in operators:
        print("Only +, -, /, x, ^ operations are allowed \nTry again.")
        x =input("Enter the operator: ")
    inp()
def inp():
    global num2
    num2=float(input("Enter the second number: "))
    operation()

def operation():
    if x=="+":
        add(num1,num2)
    elif x=="-":
        sub(num1,num2)
    elif x=="/":
        div(num1,num2)
    elif x=="x":
        mul(num1,num2)
    elif x=="^":
        exp(num1,num2)
    again()

def again():
    again=input("Wanna try again?(yes or no): ")
    while again!="yes" and again!="no":
        again=input("Reply by either yes or no: ")
    if again=="yes":
        first()
    elif again=="no":
        print("Thank you!")
        exit()

       

    
       
print("Welcome!\nThis is a calculator that can help you perform the basic operations.\n \n")
print("+ is for addition \n- is for substraction \n/ is for division ")
print("x is for multiplication \n^ is for exponentiation \n\n\n")
print("Let's get started. \nYou just need to enter two numbers and the opertion you'd like to perform.")
first()



