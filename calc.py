x=int(input('enter first number :'))
y=int(input('enter second number : '))
opr=input('enter operator ex: x/+-  :')
if opr=="x":
    result=x*y
elif opr=='-':
    result=x-y
elif opr=='/':
    result=x/y
elif opr=='+':
    result=x+y
elif opr=='^':
    result=x^y
elif opr=='%':
    result=x^y
print(result)