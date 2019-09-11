_sum =0
for i in range(1,101): 
    _sum += i   
    print(_sum)

for i in range(1,10):
    for j in range(1, i +1):
        print('%d * %d = %d'%(j,i,i*j),end="")
    print(end='\n')


print(1)
print(2)
for i in range(3, 11):
    for j in range(2, i):
        if i % j == 0:
            break
        else:
            print(i)


username =input ('请输入用户名')
password = input('请输入密码')
if username == "admin" and password =='123456':
    print('身份验证成功！')
else:  
    print('身份验证失败！')



x = float(input('请输入x的值'))
if x > 1:
   print(3 * x - 5)
elif -1 <= x <= 1:
   print(x + 2)
else:
   print(x * 5 + 3)


a = float(input('请输入a的值:'))
b = float(input('请输入b的值:'))
c = float(input('请输入c的值:'))
r1 = -1 * b + [(b * b - 4 * a *c) ** 0.5] / (2 * a)
r2 = -1 * b - [(b * b - 4 * a *c) ** 0.5] / (2 * a)
if b * b - 4 * a * c > 0 :
    print('%.2f 方程有两个实数根' %(r1,r2))
elif b * b - 4 * a * c == 0 :
    print('%.2f 方程有一个实数根' %r1)
else :
    print('方程有没有实根' )



import random
num1=random.randint(1,100)
num1=random.randint(1,100)
print(num1+num2)

def sum():
    sum=num1+num2
    a=int(input('请输入两个数的和：'))
    if sum==a:
        print('true')
    else:
        print('false')

sum()


def week():
    today = int(input('enter todays day:'))
    count =int(input('enter the number of days elapsed since today:'))
    fg=count%7
    b=today+fd
    c=b%7
    print('today is 星期%d and the future day is 星期%d'%(today,c))

week()


def contrast(money1,weight1,monet2,weight2):
    dan1 = money1 / weight1
    dan2 = money2 / weight2
    if dan1 > dan2:
        print('第二种大米价钱更好')
    elif dan1 < dan2:
        print('第一种大米价钱更好')
    else:
        print('两种大米价格相同')

def start():
    money1 = float(input('请输入第一种大米的价钱：'))
    weight1 = float(input('请输入第一种大米的重量：'))
    money2 = float(input('请输入第一种大米的价钱：'))
    weight1 = float(input('请输入第一种大米的重量：'))
    contrast(mony1,weight1,money,weight2)

start()
