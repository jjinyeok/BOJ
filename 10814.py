N = int(input())
book = []
person = []
for i in range(N):
    age, name = (input().split())
    person.append(int(age))
    person.append(i)
    person.append(name)
    book.append(person)
    person = []
book.sort()

for i in range(N):
    print(book[i][0], book[i][2])