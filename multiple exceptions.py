try:
    num1, num=eval(input("enter two numbers, separated by a comma:"))
    result=num1/num2
    print("result is",result)
except zerodivisionerror:
 print("division by zero is error!!")
except syntaxerror:
 print("comma is missing. Enter numbers separated by a comma like this 1, 2")
except:
 print("wrong input")
else:
 print("no exceptions")
finally:
 print("this will execute no matter what")