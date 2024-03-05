import UserDefinedFirstModule

def main():
    name = input("Enter your name: ")
    UserDefinedFirstModule.say_hello(name)
    
    num1 = float(input("Enter Your Mark: "))
    num2 = float(input("Enter Your Mark: "))
    
    sum_result =  UserDefinedFirstModule.add(num1, num2)
    print("Sum of {} and {} is: {}".format(num1, num2, sum_result))
    
    diff_result =  UserDefinedFirstModule.subtract(num1, num2)
    print("Difference of {} and {} is: {}".format(num1, num2, diff_result))

if __name__ == "__main__":
    main()
