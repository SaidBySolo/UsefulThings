import random


def random_hex():
    result = ""
    for _ in "RGB":
        i = random.randrange(0, 2**8)
        result += i.to_bytes(1, "big").hex()
    return result


def random_rgb():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
