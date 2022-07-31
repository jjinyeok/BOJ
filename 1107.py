from sys import stdin
n = int(stdin.readline())
m = int(stdin.readline())
buttons = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
if m != 0:
    broken_buttons = list(stdin.readline().split())
    for broken_button in broken_buttons:
        buttons.remove(broken_button)

if buttons == []:
    print(abs(n - 100))

else:
    n_plus = n * 1
    answer_plus = 987654321
    while n_plus <= 10000000:
        str_n = str(n_plus)
        check = True
        for alphabet in str_n:
            if alphabet not in buttons:
                check = False
        if check:
            answer_plus = n_plus
            break
        n_plus += 1

    n_minus = n * 1
    answer_minus = 987654321
    while n_minus >= 0:
        str_n = str(n_minus)
        check = True
        for alphabet in str_n:
            if alphabet not in buttons:
                check = False
        if check:
            answer_minus = n_minus
            break
        n_minus -= 1
    
    print(min(abs(answer_plus - n) + len(str(answer_plus)), abs(answer_minus - n) + len(str(answer_minus)), abs(100 - n)))
