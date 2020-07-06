s = input()
counter = 1

for i in range(len(s) - 1):
    if s[i] == s[i + 1]:
        counter += 1
    else:
        if counter > 1:
            print(str(counter) + s[i], end='')
        else:
            print(s[i], end='')
        counter = 1
if counter > 1:
    print(str(counter) + s[-1], end='')
else:
    print(s[-1], end='')
