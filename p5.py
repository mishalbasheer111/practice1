numbers = [4, 8, 15, 16, 23, 42]

def stats(nums):
    return min(nums), max(nums), sum(nums) / len(nums)

def grade(marks, passing=50):
    return "Pass" if marks >= passing else "Fail"

lo, hi, avg = stats(numbers)
print(lo, hi, avg)
print(grade(55), grade(55, passing=60))
