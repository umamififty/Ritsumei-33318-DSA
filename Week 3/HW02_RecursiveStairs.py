# Done by Khoo Zhenyu 2600220458-3
# Done on April 27 2023
# This program counts the number of ways to climb a staircase of n steps.

def count_ways(n):
    if n == 0 or n == 1:
        return 1
    else:
        return count_ways(n-1) + count_ways(n-2)
    
input = int(input("Enter a number: "))
print(count_ways(input))