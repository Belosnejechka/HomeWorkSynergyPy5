str = input()
x = 0
while x < len(str):
    if (str[x] == ' ') and (str[x+1] == ' '):
        str = str[0:x] + str[x+1:len(str)]
        x += 1
        print(str)
    else:
        x += 1
