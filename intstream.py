import time, math
from rich.console import Console
from nltk.corpus import brown
from geopy.geocoders import Nominatim

BIGNUM = 3**3**8 + eval(input("Enter any number: "))
intstream = (BIGNUM % int(math.pi*time.time()*math.e) for _ in range(BIGNUM))

moveUp = lambda:print('\033[1A', end="")
clear = lambda n:print(("\b" * n) + (" " * n) + ("\b" * n), end="")
console = Console()
colors = ["red", "green", "yellow", "blue", "magenta", "cyan", "white", "bright_red", "bright_yellow", "indian_red1", "hot_pink", "dark_olive_green3"]

isPrime = lambda n:n==2 or (n%2==1 and 0 not in (n%i for i in range(2, math.ceil(n/2) + 1)))
primes = (n for n in range(1, BIGNUM) if isPrime(n))
getPrime = lambda n: [next(primes) for _ in range(n)][-1]

out = set()
try:
    for chunk in intstream:
        oldLineLen = len(out)

        out.add(f"{chunk}")

        if len(out) > 3:
            moveUp()
            clear(oldLineLen)
            color = colors[chunk % len(colors)]
            console.print(f"[{color}]{''.join(out)}[/{color}]")

        if len(out) > 10:
            out = set()
except KeyboardInterrupt:
    print("\n")
    result = ''.join(out)

    console.print(f"Decimal between 0 and 1: [blue]{int(result)/(10**len(result))}[/blue]") 
    console.print(f"Coin toss: [blue]{'Heads' if int(result) % 2 == 0 else 'Tails'}[/blue]")

    dices = ["⚄", "⚁", "⚃", "⚀", "⚅", "⚂"]
    console.print(f"Dice roll: [blue]{dices[int(result) % 6]}[/blue]")

    suites = ["♠", "♣", "♥", "♦"]
    faces = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    card_colour = "black" if int(result) % 4 < 3 else "red"
    draw = f"{faces[int(result) % 13]}{suites[int(result) % 4]}"
    console.print(f"Card draw: [{card_colour}]{draw}[/{card_colour}]")

    console.print(f"Number between 0 and 100: [blue]{int(result) % 100}[/blue]")
    console.print(f"Number between 0 and 1000: [blue]{(int(result[2:9])*int(result)) % 1000}[/blue]")
    console.print("Random IP address: [green]{}.{}.{}.{}[/green]".format(*[int(result)*x % 256 for x in range(1, 5)]))

    console.print(f"Random English word: [yellow]{brown.words()[int(result) % len(brown.words())]}[/yellow]")
    console.print(f"Random prime number: [hot_pink]{getPrime(int(result[2:6]))}[/]")

    for i in range(int(result) % 10 + 1):
        while True:
            latitude = (int(result[2:4]) * time.time()) % 180 - 90
            longitude = (int(result[3:6]) * time.time()) % 360 - 180
            location = Nominatim(user_agent='GetLoc').reverse((latitude, longitude))
            if  location != None:
                console.print(f"Random Street Address #{i + 1}: {location.address}")
                break