
print('SIMPLE CALCULATOR')
print('This is a basic calculator')
print('''ENTER THE NUMBERS ACCORDING TO THE ACTIONS YOU WANT TO PERFORM
          TABLE GENERATOR: 1
          ADDITION: 2
          SUBTRACTION: 3
          MULTIPLICATION: 4
          DIVISION: 5''')
print('!! PRESS exit WHEN YOU NO LONGER NEED THE LOOP!')
exit_p=False

while True:
    while True:
        w = input('Enter the value for the corresponding action: ')
        if w.lower() == 'exit':
            exit_p= True
            break
        if w in ['1', '2', '3', '4', '5']:
            break
        else:
            print('Enter a valid value')
    if exit_p:
        break

    if w == '1':
        print('TABLE GENERATOR')
        while True:
            try:
                x = input('Enter the number for the required table: ')
                if x.lower() == 'exit':
                    break
                x = int(x)
                for i in range(10):
                    print(f'{x} X {i + 1} = {x * (i + 1)}')
            except ValueError:
                print('Invalid input')
                break

    elif w == '2':
        print('ADDITION')
        while True:
            try:
                numbers = input("Enter the numbers (separated by spaces): ")
                if numbers.lower() == 'exit':
                    break
                number_list = numbers.split()

                sum = 0
                for num_str in number_list:
                    num = int(num_str)
                    sum += num

                print("The sum is:", sum)
                continue
            except ValueError:
                print('Invalid input')
                continue

    elif w == '3':
        print('SUBTRACTION')
        while True:
            try:
                numbers = input("Enter the numbers (separated by spaces): ")
                if numbers.lower() == 'exit':
                    break

                number_list = numbers.split()

                subtraction = int(number_list[0])
                for num_str in number_list[1:]:
                    num = int(num_str)
                    subtraction -= num

                print("The subtraction result is:", subtraction)
                continue
            except ValueError:
                print('Invalid input. Please enter numbers only.')
                continue

    elif w == '4':
        print('MULTIPLICATION')
        while True:
            numbers = input("Enter the numbers (separated by spaces): ")
            if numbers.lower() == 'exit':
                break
            number_list = numbers.split()

            product = 1
            for num_str in number_list:
                num = int(num_str)
                product *= num

            print("The product is:", product)
            continue

    elif w == '5':
        print('DIVISION')
        while True:
            try:
                numbers = input("Enter the numbers (separated by spaces): ")
                if numbers.lower() == 'exit':
                    break
                number_list = numbers.split()

                dividend = int(number_list[0])
                for num_str in number_list[1:]:
                    divisor = int(num_str)
                    dividend /= divisor

                print("The division result is:", dividend)

            except ValueError:
                print('Invalid input')
