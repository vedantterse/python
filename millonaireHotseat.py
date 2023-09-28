

questions = [
    [
        "Which language was used to create Facebook?", "Python", "French", "JavaScript",
        "PHP", "None",
    ],
    [
        "Who is the founder of Microsoft?", "Bill Gates", "Steve Jobs", "Mark Zuckerberg",
        "Elon Musk", "None", 'a'
    ],
    [
        "What does HTML stand for?", "Hypertext Markup Language", "Hyperlink and Text Markup Language",
        "Home Tool Markup Language", "Hyper Tool Markup Language", "None", 'a'
    ],
    [
        "Which programming language is known as the 'mother of all languages'?", "C", "Java", "Assembly",
        "Fortran", "None", 'c'
    ],
    [
        "Which company developed the Android operating system?", "Google", "Apple", "Microsoft",
        "Samsung", "None", 'a'
    ],
    [
        "What is the largest planet in our solar system?", "Jupiter", "Saturn", "Earth",
        "Mars", "None", 'a'
    ],
    [
        "What is the chemical symbol for gold?", "Au", "Ag", "Fe", "Cu", "None", 1
    ],
    [
        "Who painted the Mona Lisa?", "Leonardo da Vinci", "Pablo Picasso", "Vincent van Gogh",
        "Michelangelo", "None", 'a'
    ],
    [
        "Which country is famous for the Taj Mahal?", "India", "China", "Egypt", "Italy", "None", 'a'
    ],
    [
        "What is the capital city of Australia?", "Canberra", "Sydney", "Melbourne", "Perth", "None", 'a'
    ],
    [
        "Who wrote the play 'Romeo and Juliet'?", "William Shakespeare", "Jane Austen", "Charles Dickens",
        "Mark Twain", "None", 'a'
    ],
    [
        "Which country won the FIFA World Cup in 2018?", "France", "Germany", "Brazil", "Spain", "None", 'a'
    ],
    [
        "What is the largest ocean on Earth?", "Pacific Ocean", "Atlantic Ocean", "Indian Ocean",
        "Arctic Ocean", "None", 'a'
    ],
    [
        "Who is the lead vocalist of the band 'Queen'?", "Freddie Mercury", "John Lennon", "Michael Jackson",
        "Elvis Presley", "None", 'a'
    ],
    [
        "What is the national animal of Canada?", "Beaver", "Moose", "Polar Bear", "Bald Eagle", "None", 'a'
    ],

]






levels = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000, 640000, 1250000, 250000, 500000, 1000000]
l = input('Enter your name: ')
while True:
    print("Welcome to Kaun Banega Carorpati" + '   ' + l + '!!!')
    print("Let's begin the game!")

    money = 0   
    correct = True   

    for i in range(len(questions)):
        print(f'Your question for ${levels[i]} is:')
        print(f'QUESTION {i + 1}')
        print(f'{questions[i][0]}')
        print(f'a. {questions[i][1]}     b. {questions[i][2]}')
        print(f'c. {questions[i][3]}   d. {questions[i][4]}')

        ans = ['d', 'a', 'a', 'c', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a']

        while True:
            x = input('Your answer: ').lower()

            if x in ['a', 'b', 'c', 'd']:
                break
            else:
                print('Invalid input. Please enter a, b, c, or d.')

        if x == ans[i]:
            print(f'Correct answer! You won ${levels[i]}')
            money = levels[i]  
        else:
            print('SORRY, WRONG ANSWER')
            correct = False
            break

    if not correct:
        print(f'\nYou won ${money}! Well played.')
    else:
        print(f'\nYou won $0. Better luck next time.')

    play = input('Do you want to play again? (yes/no): ')
    if play.lower() != 'yes':
        break
