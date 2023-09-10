import copy
from typing import List, Tuple, Dict


def offer_E(skus: List[str], total: int) -> Tuple[List[str], int]:
    # apply the offer (get one b free for 2 e) by removing b from the skus to charge
    # note should be applied before any B offer.
    count_e = skus.count("E")
    for i in range(count_e // 2):
        try:
            skus.remove("B")
        except ValueError:
            break
    return skus, total


def multiproduct_offer(
        skus: List[str],
        total: int,
        offer: Dict[int: int],
        product: str
) -> Tuple[List[str], int]:
    # generic of a multiproduct offer.
    count = skus.count(product)
    init_count = copy.deepcopy(count)
    for multiple, price in sorted(offer, reverse=True):
        total += (count // multiple) * price
        count = count % multiple
    # count ends up as the remainder after all offers applied
    for i in range(init_count - count):
        try:
        skus.remove()


def offer_A(skus: List[str], total: int) -> Tuple[List[str], int]:
    count_a = skus.count("A")
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


def offer_B(skus: List[str], total: int) -> Tuple[List[str], int]:
    count_b = skus.count("B")
    total += (count_b // 2) * 45
    to_remove = count_b - (count_b % 2)
    for i in range(to_remove):
        try:
            skus.remove("B")
        except ValueError:
            break
    return skus, total


def offer_F(skus: List[str], total: int) -> Tuple[List[str], int]:
    count = skus.count("F")
    total += (count // 3) * 20  # 20 is 2xF cost
    to_remove = count - (count % 3)
    for i in range(to_remove):
        try:
            skus.remove("F")
        except ValueError:
            break
    return skus, total