# Sort list by earliest end time
# Pick the first one.
# Iterate through list until next one with start time later than the first ones end time and select that


def select_intervals():

    intervals = [
            [4, 36],
            [17, 147],
            [5, 18],
            [62, 67],
            [16, 32],
            [96, 128],
            [21, 117],
            [19, 122],
            [64, 168],
            [45, 99],
            [12, 55],
            [20, 26],
            [79, 126],
            [3, 9],
            [89, 101],
            [55, 112],
            [26, 157],
            [1, 2],
            [16, 116],
            [49, 70],
            [26, 60],
            [52, 153],
            [16, 28],
            [20, 83],
            [158, 166],
            [3, 7],
            [7, 8],
            [61, 140],
            [1, 4],
            [12, 170],
            [19, 57],
            [35, 110],
            [54, 155],
            [93, 137],
            [47, 58],
            [49, 114],
            [115, 174],
            [60, 61],
            [64, 90],
            [3, 142],
            [4, 145],
            [89, 119],
            [24, 76],
            [22, 154],
            [63, 108],
            [8, 27],
            [26, 49],
            [18, 77],
            [106, 175],
            [2, 87],
            [7, 148],
            [65, 66],
            [36, 135],
            [17, 118],
            [96, 130],
            [38, 171],
            [4, 40],
            [24, 38],
            [22, 132],
            [129, 144],
        ]
        

    # 1. Sort intervals based on their end times (index 1)
    sorted_intervals = sorted(intervals, key=lambda x: x[1])

    # 2. Select the first interval
    selected = [sorted_intervals[0]]
    last_end_time = sorted_intervals[0][1]

    # 3. Iterate through the rest and pick compatible ones
    for current in sorted_intervals[1:]:
        current_start, current_end = current[0], current[1]
        
        # If the current interval starts after or when the last one ends
        if current_start > last_end_time:
            selected.append(current)
            last_end_time = current_end  # Update the tracking end time

    print(selected)

select_intervals()


