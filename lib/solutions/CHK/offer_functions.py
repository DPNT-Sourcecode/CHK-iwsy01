import copy
from typing import List, Tuple, Dict, Set


def remove_other_product_offer(
        skus: List[str],
        total: int,
        product: str,
        offer: Tuple[int, str],
) -> Tuple[List[str], int]:
    count = skus.count(product)
    multiple, other_product = offer
    to_remove = count // multiple
    # count ends up as the remainder after all offers applied
    for i in range(to_remove):
        try:
            skus.remove(other_product)
        except ValueError:
            break
    return skus, total


def multiproduct_offer(
        skus: List[str],
        total: int,
        product: str,
        offer: Dict[int, int],
) -> Tuple[List[str], int]:
    # generic of a multiproduct offer.
    count = skus.count(product)
    init_count = copy.deepcopy(count)
    for multiple, price in sorted(offer.items(), reverse=True):
        total += (count // multiple) * price
        count = count % multiple
    # count ends up as the remainder after all offers applied
    for i in range(init_count - count):
        try:
            skus.remove(product)
        except ValueError:
            break
    return skus, total


def group_offer(
        skus: List[str],
        total: int,
        product_group: Set[str],
        group_size: int,
        offer_price: int,
        prices: Dict[str, int],
) -> Tuple[List[str], int]:
    potential_chars = list()
    for char in skus:
        if char in product_group:
            potential_chars.append(char)
    # don't make any changes if there aren't enough products in group.
    if len(potential_chars) < group_size:
        return skus, total
    potential_chars = sorted(potential_chars, key=lambda char: prices[char],
                             reverse=True)
    potential_chars = potential_chars[:len(potential_chars)//group_size]
    # update the total
    total += (len(potential_chars) // group_size) * offer_price
    for char in potential_chars:
        skus.remove(char)
    return skus, total


