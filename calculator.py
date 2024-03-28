print("SIMPLE CALCULATOR")
print("This is a basic calculator")
print(
    """ENTER THE NUMBERS ACCORDING TO THE ACTIONS YOU WANT TO PERFORM
          TABLE GENERATOR: 1
          ADDITION: 2
          SUBTRACTION: 3
          MULTIPLICATION: 4
          DIVISION: 5"""
)
print("!! PRESS exit WHEN YOU NO LONGER NEED THE LOOP!")
exit_p = False

def request_input():
    """request input and check valid before returning two arguments in a tuple"""
    while True:
        numbers = input("Enter your numbers (separated by spaces): ")
        if numbers.lower() == "exit":
            exit_p = True
            break
        try:
            return tuple(map(int, numbers.split()))
            
        except:
            continue

while True:
    while True:
        w = input("Enter the value for the corresponding action: ")
        if w.lower() == "exit":
            exit_p = True
            break
        if w in ["1", "2", "3", "4", "5"]:
            break
        else:
            print("Enter a valid value")
    if exit_p:
        break

    if w == "1":
        print("\nTABLE GENERATOR")
        while True:
            try:
                x = input("Enter the number for the required table: ")
                if x.lower() == "exit":
                    break
                x = int(x)
                for i in range(10):
                    print(f"{x} X {i + 1} = {x * (i + 1)}")
            except ValueError:
                print("Invalid input")
                break

    elif w == "2":
        print("\nADDITION")
        print(f"The sum of your inputted numbers is {sum(request_input())}.\n")

    elif w == "3":
        print("\nSUBTRACTION")
        number_list = request_input()
        result = number_list[0]
        for num in number_list[1:]:
            result -= num
        print(f"The subtraction of your inputted numbers is {result}.\n")

    elif w == "4":
        print("\nMULTIPLICATION")
        while True:
            number_list = request_input()

            product = 1
            for num in number_list:
                product *= num

            print("The product is:", product)


    elif w == "5":
        print("\nDIVISION")
        while True:
            try:
                number_list = request_input()

                dividend = int(number_list[0])
                for num_str in number_list[1:]:
                    divisor = int(num_str)
                    dividend /= divisor

                print("The division result is:", dividend)

            except ValueError:
                print("Invalid input")



