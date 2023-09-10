from collections import Counter
from typing import Dict, List
from .offer_functions import multiproduct_offer, remove_other_product_offer, group_offer


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
    # define prices and offers
    prices = {
        "A": 50,
        "B": 30,
        "C": 20,
        "D": 15,
        "E": 40,
        "F": 10,
        "G": 20,
        "H": 10,
        "I": 35,
        "J": 60,
        "K": 70,
        "L": 90,
        "M": 15,
        "N": 40,
        "O": 10,
        "P": 50,
        "Q": 30,
        "R": 50,
        "S": 20,
        "T": 20,
        "U": 40,
        "V": 50,
        "W": 20,
        "X": 17,
        "Y": 20,
        "Z": 21,
    }

    remove_other_product_offers = [
        ("E", (2, "B")),
        ("N", (3, "M")),
        ("R", (3, "Q")),
    ]

    multiproduct_offers = [
        ("A", {5: 200, 3: 130}),
        ("B", {2: 45}),
        ("F", {3: 20}),
        ("H", {10: 80, 5: 45}),
        ("K", {2: 120}),
        ("P", {5: 200}),
        ("Q", {3: 80}),
        ("U", {4: 120}),
        ("V", {3: 130, 2: 90}),
    ]

    group_offers = [
        ({"S", "T", "X", "Y", "Z"}, 3, 45)
    ]
    skus = list(skus)
    total = 0
    # apply the offers first
    for prod, offer in remove_other_product_offers:
        skus, total = remove_other_product_offer(
            skus=skus,
            total=total,
            product=prod,
            offer=offer
        )

    for product, price_map in multiproduct_offers:
        skus, total = multiproduct_offer(
            skus=skus,
            total=total,
            product=product,
            offer=price_map
        )

    for group, size, price in group_offers:
        skus, total = group_offer(
            skus=skus,
            total=total,
            product_group=group,
            group_size=size,
            offer_price=price,
            prices=prices
        )

    # iterate over remaining skus, tally and return the cost. return -1 for
    # invalid input.
    total = calculate_prices(skus=skus, prices=prices, total=total)
    return total



