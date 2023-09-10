from collections import Counter
from typing import Tuple, Dict, List


def offer_E(skus: str, total: int) -> Tuple[List[str], int]:
    # apply the offer (get one b free for 2 e) by removing b from the skus to charge
    count_e = skus.count("E")
    skus = list(skus)
    for i in range(count_e // 2):
        try:
            skus.remove("B")
        except ValueError:
            break
    return skus, total


def offer_A(skus: str, total: int) -> Tuple[List[str], int]:
    count_a = skus.count("A")
    skus = list(skus)
    offer_5_num = count_a // 5
    offer_3_num = count_a % 5 // 3
    remaining = count_a % 5 % 3
    total += offer_5_num * 200
    total += offer_3_num * 130
    to_remove = count_a - remaining
    for i in range(to_remove):
        try:
            skus.remove("A")
        except ValueError:
            break
    return skus, total


def offer_B(skus: str, total: int) -> Tuple[List[str], int]:
    count_b = skus.count("B")
    skus = list(skus)
    total += (count_b // 2) * 200
    to_remove = count_b - (count_b % 2)
    for i in range(to_remove):
        try:
            skus.remove("B")
        except ValueError:
            break
    return skus, total


def calculate_prices(skus: List[str], prices: Dict[str, int], total: int) -> int:
    counts = Counter(skus)
    for item, count in counts.items():
        try:
            total += count * prices[item]
        except KeyError:
            return -1
    return total

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus: str):
    # apply offers first - then calculate prices
    offers = [
        offer_E,
        offer_A,
        offer_B,
    ]
    skus = list(skus)
    total = 0
    for offer in offers:
        skus, total = offer(skus, total)

    # iterate over skus table the cost return the cost. return -1 for invalid input.
    prices = {
        "A": 50,
        "B": 30,
        "C": 20,
        "D": 15,
    }

    total = calculate_prices(skus=skus, prices=prices, total=total)
    return total




