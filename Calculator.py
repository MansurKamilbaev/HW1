a=int(input('a= '))
b=int(input('b= '))
deystvie=input('add/sub/mul/div: ')
if deystvie =='add':
    c=a+b
elif deystvie=='sub':
    c=a-b
elif deystvie=='mul':
    c=a*b
elif deystvie=='div':
    c=a/b
else:
    c='Error'
print('Result=',c)