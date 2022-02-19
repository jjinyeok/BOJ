from sys import stdin
input = stdin.readline
N = int(input())
arr = list(map(int, input().split()))
arr.sort()
result = arr[0] * arr[len(arr) - 1]
print(result)
