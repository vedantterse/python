def generate_table():
    x = int(input('Enter the number for the required table: '))
    for i in range(1, 11):
        print(f'{x} X {i} = {x * i}')

def perform_operation(operation):
    numbers = list(map(int, input(f"Enter the numbers for {operation} (separated by spaces): ").split()))
    result = sum(numbers) if operation == 'addition' else numbers[0] - sum(numbers[1:]) if operation == 'subtraction' else 1

    print(f"The {operation} result is: {result}")

def main():
    print('SIMPLE CALCULATOR')
    print('1. Table Generator')
    print('2. Addition')
    print('3. Subtraction')
    print('4. Multiplication')
    print('5. Division')

    while True:
        choice = input('Enter the number for the corresponding action (Press "exit" to end): ')
        if choice.lower() == 'exit':
            break

        if choice == '1':
            generate_table()
        elif choice in ['2', '3', '4', '5']:
            operations = ['addition', 'subtraction', 'multiplication', 'division']
            perform_operation(operations[int(choice) - 2])
        else:
            print('Enter a valid value')

if __name__ == "__main__":
    main()


                print("The division result is:", dividend)

            except ValueError:
                print('Invalid input')
