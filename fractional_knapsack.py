def fractional_knapsack():

    # Divide

    v = [
        64,
        111,
        58,
        168,
        98,
        192,
        142,
        129,
        214,
        205,
        240,
        243,
        127,
        190,
        150,
        216,
        221,
        242,
        242,
        123,
        215,
        237,
        113,
        93,
        202,
        187,
        71,
    ]

    w = [
        1,
        2,
        2,
        23,
        10,
        38,
        16,
        24,
        8,
        18,
        31,
        59,
        14,
        27,
        46,
        21,
        64,
        49,
        35,
        40,
        37,
        11,
        3,
        10,
        14,
        44,
        5,
    ]

    B = 31

    # (value/weight ratio, value, weight, index)
    items = sorted([(v[i] / w[i], v[i], w[i], i) for i in range(len(v))], reverse=True)

    remaining = B
    optimal_value = 0

    for ratio, value, weight, index in items:
        if remaining == 0:
            break

        fraction = min(1, remaining / weight)
        optimal_value += fraction * value
        remaining -= fraction * weight

    print(optimal_value)


fractional_knapsack()
