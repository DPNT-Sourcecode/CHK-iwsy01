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
