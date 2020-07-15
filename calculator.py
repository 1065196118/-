def fn(line,pole):
    for line in range(line):
        for i in range(1, pole):
            print('*',end='')
        print("\n")
x=input("enter (y) = ")
def vc():
    num1=int(input("enter first number = "))
    operator=input("enter the operator = ")
    num2=int(input("enter secand number = "))
    if operator=='*':
        print("the sum = ",num1*num2)
    elif operator=='+':
        print("the sum = ",num1+num2)
    elif operator=='-':
        print("the sum = ",num1-num2)
    elif operator=='/':
        print("the sum = ",num1/num2)
    elif operator=='%':
        print("the sum = ",num1%num2)
    else:
        print("not vaild") 
while x=='y':
    fn(2,90)
    vc()
    fn(1,90)
    x=input("Complete enter (y) to finsh enter (n) = ")

    