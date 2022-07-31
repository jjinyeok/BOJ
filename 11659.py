from sys import stdin

n, m = map(int, stdin.readline().split())
ns = list(map(int, stdin.readline().split()))
answers = [ns[0]]
for n in range(1, len(ns)):
    answers.append(answers[n - 1] + ns[n])
for _ in range(m):
    start, end = map(int, stdin.readline().split())
    answer = answers[end - 1] - answers[start - 1] + ns[start - 1]
    print(answer)
