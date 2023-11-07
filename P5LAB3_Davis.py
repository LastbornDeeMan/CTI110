# CTI 110
# P5HW1 - Math Quiz
# Davisc
# 11/7/23

question_set = {
    "question1": {
        "question": "What is the name of the protagonist in Berserk?",
        "options": ["Guts", "Griffith", "Casca", "Zodd"],
        "answer": "Guts"
    },
    "question2": {
        "question": "Who is the main antagonist in Berserk?",
        "options": ["Griffith", "Farnese", "Serpico", "Isidro"],
        "answer": "Griffith"
    },
    "question3": {
        "question": "What is the name of Guts' sword in Berserk?",
        "options": ["Dragonslayer", "Eclipse", "Behelit", "Beherit"],
        "answer": "Dragonslayer"
    },
    "question4": {
        "question": "Who is Guts' closest companion in Berserk?",
        "options": ["Casca", "Puck", "Schierke", "Judeau"],
        "answer": "Casca"
    },
    "question5": {
        "question": "What is the name of the mercenary band that Guts joins",
        "options": ["Band of the Hawk", "Band of the Falcon", "Band of the Sword", "Band of the Rose"],
        "answer": "Band of the Hawk"
    }
}

def main():
    print("Welcome to the Math Quiz!")
    print("Test your knowledge and see how well you can do.\n")
  
    score = 0

    for question_number, question in question_set.items():
        print(question['question'])
        print("Options:")
        for option in question['options']:
            print(option)
        user_answer = input("Your answer: ")
        if user_answer == question['answer']:
            print("Correct!")
            score += 1
        else:
            print("Incorrect!")

    print("\nQuiz completed!")
    print("Your total score is: ", score, " out of ", len(question_set))

# Call the main function to start the quiz
main()