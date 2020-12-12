import time
import random


def validation(question, dict1, chances, username):
    print("hint is :", question)
    answer = dict1[question]
    guesses = ''
    while chances > 0:
        flag = 0
        for char in answer:                             # for printing
            if char in guesses:
                print(char, end=" ")
            else:
                print("_", end=" ")
                flag += 1
        print("")
        if flag == 0:
            print(f"{username} won the game .")
            print("the word is : ", answer)
            break

        t1 = time.time()
        while True:                                     # if same letter guessed multiple time
            print("enter the letter : ", end=" ")
            guess = input()
            if guess in guesses:
                print("letter is already guessed \n enter another guess\n")
            else:
                break
        t2 = time.time()
        if t2-t1 <= 5:                                  # to check time out
            guesses += guess
            if guess not in answer:                     # checking if guess in correct or not
                chances = chances - 1
                print("wrong \n ", chances, " chances remaining.")
                if chances == 0:
                    print(f"{username} lost the game ")
        else:                                           # if time out occured
            chances -= 1
            if chances == 0:
                print(f"{username} lost the game ")
                break
            print("TIME OUT \n", chances, " chances remaining.")


def user_info():
    user_name = input("enter user name: ")
    return user_name


def game():
    # here keys are hints and values are their answers
    dict1 = {'has seven colors': 'rainbow', 'device': 'computer', 'study of motion': 'physics',
             'writing codes': 'programming'}
    chances = 4

    question = random.choice(list(dict1))

    print('Welcome to the game HangMan ')

    username = user_info()
    validation(question, dict1, chances, username)


if __name__ == '__main__':
    game()
