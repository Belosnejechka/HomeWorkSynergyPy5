str = input()
a = 0
b = len(str)-1
while (True):
    if str[a] == str[b]:
        a += 1
        b -= 1
    else:
        print("No")
        break
    if a == b or a > b:
        print("Yes")
        break