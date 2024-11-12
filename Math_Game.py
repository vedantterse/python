import random
import time
import easygui

score = 0
start_time = time.time()

for i in range(1, 6):
    first_number = random.randint(1, 10)
    second_number = random.randint(1, 10)
    operators = ['+', '-', '/', '%', '*']
    selected_operator = random.choice(operators)

    message = f"Problem {i} -> {first_number} {selected_operator} {second_number}"

    while True:
        user_answer = easygui.enterbox(message, "Enter your answer:")

        if user_answer is None or user_answer.strip() == "":
            easygui.msgbox("You must enter a number. Please try again.")
            continue

        try:
            user_answer = float(user_answer)  
            break  
        except ValueError:
            easygui.msgbox("Please enter a valid number!")  
            continue

    if selected_operator == '+':
        result = first_number + second_number
    elif selected_operator == '-':
        result = first_number - second_number
    elif selected_operator == '/':
        result = round(first_number / second_number, 1)
    elif selected_operator == '%':
        result = first_number % second_number
    elif selected_operator == '*':
        result = first_number * second_number

    if result == user_answer:
        score += 1
    else:
        explanation = f"The correct answer is: {first_number} {selected_operator} {second_number} = {result}"
        easygui.msgbox(explanation)

end_time = time.time()
final_time = round(end_time - start_time, 2)
result_message = f"You have scored {score} points in {final_time} seconds."
easygui.msgbox(result_message, "Result")
