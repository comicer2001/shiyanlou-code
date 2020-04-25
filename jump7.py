a = 0
while a<100:
    a += 1
    if int(a) % 7 == 0 or int(a) % 10 == 7 or int(a) // 10 ==7:
        continue
    else:
        print(a)
