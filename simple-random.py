# Stripped down version of intstream.py that has no library dependancies, i.e. vanilla Python. It is also deterministic.

BASESTREAM = 8539734222673566 # change this value in your local copy but use a similar length
seed = eval(input("Enter your seed: "))
BIGNUM = 3**3**8 * seed

chunk = BASESTREAM + seed
for i in range(seed):
    print(chunk)
    chunk = BIGNUM % (BASESTREAM * chunk)
     