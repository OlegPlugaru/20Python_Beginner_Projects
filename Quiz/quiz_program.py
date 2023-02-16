# a dictionary that stores question and answers

quiz = {
    "question1": {
        "question": "What is the capital of France?",
        "answer": "Paris"
    },
    "question2": {
        "question": "What is the capital of Germany?",
        "answer": "Berlin"
    },
    "question3": {
        "question": "What is the capital of Italy?",
        "answer": "Rome"
    },
    "question11": {
        "question": "What is the capital of the United States?",
        "answer": "Washington, D.C."
    },
    "question12": {
        "question": "What is the capital of the United Kingdom?",
        "answer": "London"
    },
    "question4": {
        "question": "What is the capital of Japan?",
        "answer": "Tokyo"
    },
    "question5": {
        "question": "What is the capital of Canada?",
        "answer": "Ottawa"
    },
    "question6": {
        "question": "What is the capital of China?",
        "answer": "Beijing"
    },
    "question7": {
        "question": "What is the capital of Australia?",
        "answer": "Canberra"
    },
    "question8": {
        "question": "What is the capital of Brazil?",
        "answer": "Brasilia"
    },
    "question9": {
        "question": "What is the capital of Russia?",
        "answer": "Moscow"
    },
    "question10": {
        "question": "What is the capital of India?",
        "answer": "New Delhi"
    }
}

#  have a variable that tracks the score of the player
score = 0

# loop through the dictionary using the key value pairs

for key, value in quiz.items():
    # display each question to the user and allow them to answer
    print(value['question'])
    answer = input("Answer => ")

    if answer.lower() == value['answer'].lower():
        # tell them if they are right or wrong
        print('Correct!!!')
        score = score + 1
        print("Your score is: " + str(score))
        print()
        print()
    elif answer.lower() == "exit":
        print("See you later!!!")
        exit()
    else:
        print("Wrong!")
        print("The answer is: " + value['answer'])
        print("Your score is: " + str(score))
        print()
        print()

# show the final result when quiz is completed
print("You got " + str(score) + " out of 12 questions correctly")
print("Your percentage is " + str(int(score/12 * 100)) + "%")
