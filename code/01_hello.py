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
print(b)         #b是ABC

                 # /除法计算结果是浮点数，//称为地板除只取结果的整数部分
