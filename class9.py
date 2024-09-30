for i in range(0,51):
    if i%3==0:
        print(i,end=' ')

count=0
for i in range(1,101):
    if i%3==0 or i%5==0:
        count=count+1
        print(i)
print('count is = ',count)

count=0
for i in range(1,101):
    if i%3==0:
        continue
    else:
        count = count + 1
        print(i,'')
print('count is =',count)

count=0
for i in range(1,101):
    if not(i%3==0 or i%5==0):
        continue
    else:
        print(i)
        count = count + 1
print('count is = ',count)

count=0
for i in range(1,500):
    if (i**2<500):
        count=count+1
        print(i*i)
print('square count is =',count)