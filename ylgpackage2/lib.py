from termcolor import colored
from random import randint
from time import sleep

def try_me():
    for i in range(100):
        line = ""
        for j in range(100):
            line += str(randint(0, 1))
        print(colored(line,'green'))
        sleep(0.01)
    print(colored("THANKS! You have successfully been hacked!", "red"))
    sleep(0.5)
    print(colored("Your computer is going to shutdown in ...", "red"))
    sleep(1)
    print(colored("3", "red"))
    sleep(1)
    print(colored("2", "red"))
    sleep(1)
    print(colored("1", "red"))
    sleep(1)
    print(colored("BOOOM", "red"))
