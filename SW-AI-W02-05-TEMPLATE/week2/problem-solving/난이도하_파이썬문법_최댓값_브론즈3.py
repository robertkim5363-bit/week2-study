# 파이썬 문법 - 최댓값 (백준 브론즈3)
# 문제 링크: https://www.acmicpc.net/problem/2562

nums = []

# Loop 9 times (range(1, 10) gives you 1, 2, 3, 4, 5, 6, 7, 8, 9)
for i in range(1, 10):
    num = int(input())
    nums.append(num)  # The list appends the number!

max_val = max(nums)   # Use a safe variable name
max_position = nums.index(max_val) + 1

print(max_val)
print(max_position)
