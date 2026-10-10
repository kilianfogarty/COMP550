def knapsack(weights: list[int], values: list[int], capacity: int) -> int:
        n = len(weights)
        # Create a 2D DP table with dimensions (n + 1) x (capacity + 1)
        dp = [[0] * (capacity + 1) for _ in range(n + 1)]
        
        for i in range(1, n + 1):
            w_i = weights[i - 1]
            v_i = values[i - 1]
            
            for w in range(capacity + 1):
                if w_i <= w:
                    # Choose the max between excluding or including the current item
                    dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - w_i] + v_i)
                else:
                    # Item is too heavy to include
                    dp[i][w] = dp[i - 1][w]
                    
        return dp[n][capacity]

def main():
    v = [3, 17, 15, 5, 10, 9, 13, 15, 2, 1, 16, 9, 15, 1, 9, 14, 5, 18, 18, 1, 1, 11, 18, 8, 5, 9, 1, 5, 9, 10, 5, 5, 5, 9, 6, 1, 16, 11, 13, 4, 19, 17, 3, 7, 14, 14, 18, 9, 16, 13]
    w = [6, 12, 17, 17, 10, 12, 1, 5, 16, 8, 4, 11, 14, 13, 8, 9, 10, 15, 10, 8, 10, 1, 1, 14, 19, 12, 8, 4, 10, 19, 15, 11, 17, 5, 10, 19, 11, 9, 6, 11, 19, 1, 15, 16, 17, 15, 16, 10, 11, 9]
    B = 40
    print(knapsack(w, v, B))

if __name__ == "__main__":
     main()