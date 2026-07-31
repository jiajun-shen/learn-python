print('hello, world')
print('The quick brown fox' , 'jumps over', 'the lazy dog')
print(300 + 100)
print('200 + 100 =', 100 + 200, '加法运算')  #逗号是空格 引号外的没有缩进的

name = input()
name = input('please enter your name: ')    #这一步变量name被重新赋值了
print('hello,', name)

name = 1024*768
print('1024 * 768 =', name)

a = int(input('please enter a number: '))
if a >= 0:                   #当语句以冒号:结尾时 ,按enter键换行,缩进4个空格（TAB）,表示if语句的内容
    print('a是一个正数')
else:
    print('a是一个负数')

x = 10
x = x + 2        # 这个时候下一行开始x的值是12

a = 'ABC'
b = a
a = 'XYZ'
print(b)         # b是ABC

                 # /除法计算结果是浮点数，//称为地板除只取结果的整数部分

a = 123
# int a = 123      # 错误！  C语言里变量类型必须提前声明是这样写的 但是py不行 就是说a是个整数且a是变量 过约束了在py里不行 不允许变量声明int和变量名a分开写
input('a')       #这里的a是一个字符串，不是变量，单写这个后续是不知道a是什么的
a = input('a')   # 后续都知道a的值了 a从此是变量
a = int(input("请输入一个整数："))  #你输入这个东西是a变量的值了 且a变量一定是整数 不是数就报错  有小数点自动删去




text1 = r'Hello\nBob' #text1是变量 他的值是个字符串 输出是Hello\nBob
text2 = r'''Hello
Bob\nPython'''       #text2是变量 他的值是个字符串 输出是Hello换行Bob\nPython

print(r'''line1
line2
line3''')         #   两个意思一样的r代表后面所有的引号里的内容/都会保留没有别的意思 ' ' '里面表示换行都按' ' '。。。' ' '里面的行数空行来
print('''line1       
line2
line3''')

#格式化  写代码输出的那一步的时候简单，因为和英语语序一样 只要加一个f在引号前面
name = "Sylvain"
age = 23
print(f"My name is {name}, I'm {age} years old.")   # f-string 有f在引号前后面的大括号里的变量才会被代入表达出来，不然就是原文不会有变量值的代入
    #My name is Sylvain, I'm 23 years old.














# >>> t = ('a', 'b', ['A', 'B'])
# >>> t[2][0] = 'X'
# >>> t[2][1] = 'Y'
# >>> t
# ('a', 'b', ['X', 'Y'])            tuple中的list元素是可以变的，通过对小list一个一个变换