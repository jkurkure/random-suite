# versions of the generators that use the standard library
import random
from geopy.geocoders import Nominatim

prompt = "⚙️  > "
moveUp = lambda:print('\033[1A', end="")
clear = lambda n:print(("\b" * n) + (" " * n) + ("\b" * n), end="")

dice = lambda:["⚄", "⚁", "⚃", "⚀", "⚅", "⚂"][int(random.random()*6)]
card = lambda:f"{random.choice(["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"])}{random.choice(["♠", "♣", "♥", "♦"])}"
ipv4 = lambda:"{}.{}.{}.{}".format(*[int(random.randint(1234567, 891011121314))*x % 256 for x in range(1, 5)])

def place():
    while True:
        location = Nominatim(user_agent='GetLoc').reverse((random.randint(-90, 90), random.randint(0, 180)))
        if location != None:
            return location.address

while True:
    cmd = input(prompt)
    moveUp()
    clear(len(prompt) + len(cmd))

    try:
        print(eval(f"{cmd}()"))
    except NameError:
        print("Command not found!")