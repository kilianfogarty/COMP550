from bisect import bisect_left


def lengthOfLIS(nums: list[int]) -> int:
    ends = []

    for a in nums:
        i = bisect_left(ends, a)

        if i == len(ends):
            ends.append(a)
        else:
            ends[i] = a

    return ends

def lengthOfLIS2(nums: list[int]) -> int:
        if not nums:
            return 0
            
        n = len(nums)
        # d[i] stores the length of the LIS ending at index i
        d = [1] * n
        
        for i in range(1, n):
            for j in range(i):
                if nums[j] < nums[i]:
                    d[i] = max(d[i], d[j] + 1)
                    
        return d

def lengthOfLIS3(nums: list[int]) -> list[int]:
        if not nums:
            return []
            
        n = len(nums)
        d = [1] * n
        parent = [-1] * n  # Tracks the previous index in the LIS
        
        max_len = 1
        best_end = 0  # Stores the index where the longest overall LIS ends
        
        for i in range(1, n):
            for j in range(i):
                if nums[j] < nums[i] and d[j] + 1 > d[i]:
                    d[i] = d[j] + 1
                    parent[i] = j  # nums[j] precedes nums[i] in this increasing subsequence
                    
            if d[i] > max_len:
                max_len = d[i]
                best_end = i
                
        # Reconstruct the sequence by backtracking from best_end
        lis = []
        curr = best_end
        while curr != -1:
            lis.append(nums[curr])
            curr = parent[curr]
            
        # Since we backtracked from end to start, reverse it to get the correct order
        return lis[::-1]


def main():

    A = [
        14,
        84,
        76,
        26,
        50,
        45,
        65,
        79,
        10,
        3,
        83,
        43,
        76,
        1,
        45,
        72,
        23,
        94,
        90,
        4,
        3,
        54,
        93,
        38,
        22,
        42,
        3,
        22,
        44,
        50,
        24,
        23,
        22,
        46,
        29,
        3,
        83,
        56,
        64,
        19,
        99,
        86,
        12,
        33,
        72,
        71,
        93,
        42,
        83,
        67,
        31,
        59,
        88,
        84,
        51,
        59,
        4,
        25,
        79,
        42,
        18,
        55,
        70,
        67,
        38,
        44,
        51,
        78,
        52,
        39,
        49,
        3,
        5,
        70,
        98,
        59,
        39,
        17,
        50,
        98,
        77,
        54,
        86,
        23,
        51,
        95,
        58,
        46,
        27,
        55,
        95,
        1,
        78,
        82,
        88,
        74,
        81,
        52,
        56,
        43,
    ]

    print(lengthOfLIS3(A))


if __name__ == "__main__":
    main()
