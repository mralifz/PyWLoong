def facto(x):
    print('x')
    if x==1:
        return 1
    else:
        return (x*facto(x-1))
num = int(input('a:'))
res = facto(num)
print(res)
                
