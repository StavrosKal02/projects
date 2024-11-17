print("______Welcome to my Calculator without GUI!_______")
while 1:
    print("What would you like to do?")
    print("1. Addition")
    print("2. Substraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")
    choice= int(input("Please enter your choice: "))
    if choice==1:
        number1=int(input("Enter your first number: "))
        number2=int(input("Enter your second number: "))
        print("Output: ", number1+number2)

    elif choice==2:
        number1=int(input("Enter your first number: "))
        number2=int(input("Enter your second number: "))
        print("Output: ", number1-number2)
    elif choice==3:
        number1=int(input("Enter your first number: "))
        number2=int(input("Enter your second number: "))
        print("Output: ", number1*number2)
    elif choice==4:
        number1=int(input("Enter your first number: "))
        number2=int(input("Enter your second number: "))
        while 1:
            if number2==0:
                print("Give a valid number for Substraction")
                number2=int(input("Enter your second number: "))
            else:
                break
            
        print("Output: ", number1/number2)
    elif choice==5:
        print("Exiting...")
        break
