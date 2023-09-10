from collections import Counter
from typing import Tuple


def offer_E(skus: str, total: int) -> Tuple[str, int]:
    # apply the offer (get one b free for 2 e) by removing b from the skus to charge
    count_e = skus.count("E")
    skus = list(skus)
    for i in range(count_e):
        try:
            skus.remove("B")
        except ValueError:
            break
    return ''.join(skus), total


def offer_A(skus: str, total: int) -> Tuple[str, int]:
    count_a = skus.count("A")
    skus = list(skus)



# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus: str):
    # iterate over skus table the cost return the cost. return -1 for invalid input.
    prices = {
        "A": 50,
        "B": 30,
        "C": 20,
        "D": 15,
    }
    total = 0
    counts = Counter(skus)
    for item, count in counts.items():
        if item == "A":
            total += (count // 3) * 130
            total += (count % 3) * prices[item]
        elif item == "B":
            total += (count // 2) * 45
            total += (count % 2) * prices[item]
        else:
            try:
                total += count * prices[item]
            except KeyError:
                return -1
    return total


