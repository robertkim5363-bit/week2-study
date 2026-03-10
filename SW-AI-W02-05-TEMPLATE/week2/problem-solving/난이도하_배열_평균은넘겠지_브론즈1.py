# 배열 - 평균은 넘겠지 (백준 브론즈1)
# 문제 링크: https://www.acmicpc.net/problem/4344

C = int(input())

for i in range(C):
    # Read the line and split it into integers (your arrow placement was perfect!)
    data = list(map(int, input().split()))
    
    # 1. Use 'data' instead of 'i' to slice the list
    count = data[0]
    result = data[1:]
    
    # Calculate the average
    average = sum(result) / count
    
    # 2. Initialize the counter to 0 before the loop
    above_count = 0
    
    for a in result:
        if a > average:
            above_count += 1
            
    # 3. Multiply by 100 to make it a percentage
    percentage = (above_count / count) * 100
    
    # 4. Perfect the f-string formatting with the colon
    print(f"{percentage:.3f}%")
