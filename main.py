'''
Sweetly composed by Alex Ruger
11th October, Two Thousandth, Twentieth, plus Two, 
Year of Our Lord Theo the Cat-o.
'''


def say_something():
    print('What do you want to say?')
    to_print = input()
    print('How many times do you want to say this?')
    goal = input()

    count = 0
    while (count < int(goal)):
        print(str(count + 1) + f': {to_print}')
        count += 1

    print(f'Congratulations, you just said {to_print} {goal} times!')


def main():
    say_something()


if __name__ == '__main__':
    main()
