from collections import Counter
from typing import Dict, List
from .offer_functions import offer_A, offer_B, offer_F, offer_E

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
def checkout(skus: str) -> int:
    # apply offers first - then calculate prices
    offers = [
        offer_E,
        offer_A,
        offer_B,
        offer_F,
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
        "E": 40,
        "F": 10,
    }

    total = calculate_prices(skus=skus, prices=prices, total=total)
    return total


