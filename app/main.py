import random
from datetime import datetime


def flip_coin() -> dict:
    results = {
        0 : 0,
        1 : 0,
        2 : 0,
        3 : 0,
        4 : 0,
        5 : 0,
        6 : 0,
        7 : 0.0,
        8 : 0.0,
        9 : 0.0,
        10 : 0.0
    }

    nb_tests = 20000
    for i in range(nb_tests + 1):
        d = datetime.now()
        random.seed(datetime.timestamp(d))

        head = 0
        for flip in range(0, 11):
            if random.randint(1, 2) == 1:
                head += 1

        results[head] += 1 / nb_tests

    for e in results:
        results[e] = round(100 * results[e], 2)

    return results
