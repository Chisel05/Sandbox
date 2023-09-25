"""
Program for replicating TIS-100 'Signal Patter Detector' problem & solution
"""

from random import randint


def main():
    """Replicate Signal Pattern Detector problem & solution"""
    zeros = []
    number = randint(0, 4)
    while len(zeros) < 4:
        if number == 0:
            while number == 0 or len(zeros) != 4:
                zeros.append(0)
                print(number)
                number = randint(0, 4)
        else:
            zeros = []
            number = randint(0, 4)
            print(number)
    print(f"WOW! You got FOUR zeros in a row?\n"
          f"List: {zeros}")


main()
