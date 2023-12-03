from typing import List

def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)

        lowest = 10E9 + 1

        while left <= right:
            middle = ((left + right) // 2) + (not ((left + right) % 2 == 0))
            attempt = 0
            for p in piles:
                attempt += (p // middle) + (not (p % middle == 0))
            if attempt <= h:
                if middle < lowest:
                    lowest = middle
            if attempt <= h:
                right = middle - 1
            if attempt > h:
                left = middle + 1
        return lowest

if __name__ == '__main__':
    # piles = [3, 6, 7, 11]
    piles = [312884470]
    h = 968709470
    print(f"Output: {minEatingSpeed(piles, h)}")