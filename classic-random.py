# versions of the generators that use the standard library
import random, pyasn, types
from importlib.machinery import SourceFileLoader
from geopy.geocoders import Nominatim
from geoip import geolite2
graphics = SourceFileLoader("graphics", "lib/graphics.py").load_module()
hieros = SourceFileLoader("hiero", "lib/hiero.py").load_module()

asndb = pyasn.pyasn('lib/asn/ipasn_20240905.dat', as_names_file="lib/asn/asnames.json")

prompt = "⚙️  > "
moveUp = lambda:print('\033[1A', end="")
clear = lambda n:print(("\b" * n) + (" " * n) + ("\b" * n), end="")

quit = lambda:exit()
INTERNAL = ['moveUp', 'clear', 'ipv4_info', 'ipv4_full']
help = lambda:"\t".join([k for k in globals().keys() if "<function <lambda>" in str(globals()[k]) and k not in INTERNAL])


ipv4_info = lambda addr:f"\nAutonomous System:\t{asndb.get_as_name(asndb.lookup(addr)[0])}\nContinent:\t{geolite2.lookup(addr).continent}\nCountry:\t{geolite2.lookup(addr).country}\nRegion:\t{" ".join([r for r in geolite2.lookup(addr).subdivisions])}\nStreet Address:\t{Nominatim(user_agent='GetLoc').reverse((geolite2.lookup(addr).location[0], geolite2.lookup(addr).location[1])).address}"
ipv4_full = lambda addr:f"{addr}{"".join([ipv4_info(addr) for _ in [1] if geolite2.lookup(addr) is not None])}\n"

dice = lambda:graphics.DICE[int(random.random()*6)]
card = lambda:f"{random.choice(["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"])}{random.choice(["♠", "♣", "♥", "♦"])}"
coin = lambda:[graphics.HEADS, graphics.TAILS][random.random() < 0.5]
ipv4 = lambda:ipv4_full("{}.{}.{}.{}".format(*[int(random.randint(1234567, 891011121314))*x % 256 for x in range(1, 5)]))

def place():
    while True:
        location = Nominatim(user_agent='GetLoc').reverse((random.uniform(-90, 90), random.uniform(0, 180)))
        if location != None:
            return location.address

def egypt():
    elems = []
    for _ in range(random.randint(3, 15)):
        elems.append(random.choice(hieros.glyphs))
        elems.append(random.choice(hieros.seps))

    resFrag =  ''.join(elems[:-1])

    from splinter import Browser                
    with Browser() as browser: 
        browser.visit('https://nederhof.github.io/hierojax/resconversion.html')
        browser.fill('input-text', resFrag)
        browser.find_by_name('Process').click()
        glyphs = browser.find_by_class('hierojax')[0].innerHTML
        print(glyphs)

print("Welcome to RandomShell!")
print("A number of random generation services are provided\n")
while True:
    cmd = input(prompt)
    moveUp()
    clear(len(prompt) + len(cmd))

    try:
        if type(eval(cmd)) is type(moveUp):
            print(eval(f"{cmd}()"))
        else:
            raise NameError 
    except NameError:
        print("Command not found!")
    