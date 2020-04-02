password = input('insert password frt ')
pw_array = []
pw_ascii = []
for j in range(len(password)):
    pw_array.append(password[j])
for i in range(len(password)):
    pw_ascii.append(ord(pw_array[i]))
def base5(pw):
    converted = ''
    while pw != 0:
        mod5 = pw % 5
        pw = pw // 5
        converted += str(mod5)
    return converted[::-1]
for k in range(len(password)):
    print(base5(int(pw_ascii[k])))
