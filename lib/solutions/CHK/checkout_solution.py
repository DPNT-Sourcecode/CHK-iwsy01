from collections import Counter


# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
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



