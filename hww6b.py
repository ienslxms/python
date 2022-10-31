sum=0
for n in range (1,31):
    print('введите температуру', n , 'дня')
    t=int(input())
    if t<0:
        sum=sum+1
print(sum, 'раз температура была ниже 0')
