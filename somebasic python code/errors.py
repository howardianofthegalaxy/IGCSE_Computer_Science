#age = int(input(input("enter your age:"))


try:
    age = int(input("enter your age:"))
    calculation = 10/age
except (ValueError, ZeroDivisionError) as error:
    print("please enter a valid")
    print(error)

print("if this is executed the pgrom didn't stop running")