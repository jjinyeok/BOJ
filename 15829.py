N = int(input())
string_key = input()
arr = []
for i in range(N):
    arr.append(ord(string_key[i]) - 96)

result = 0
for i in range(N):
    result += arr[i] * 31 ** i

result %= 1234567891

print(result)