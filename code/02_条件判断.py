
birth = input('birth: ')
if birth < 2000:
    print('00前')
else:
    print('00后')    #是错的 因为这个birth的值是字符串


s = input('birth: ') #自己手输入一个数字
birth = int(s)       #int数字字符串就是把数字字符串转变成数字然后再取整  如果输入的不是数字字符串那么就会报错
if birth < 2000:
    print('00前')
else:
    print('00后')

height = 1.75
weight = 80.5
bmi = weight / (height * height)
if bmi < 18.5:
    print('过轻')
elif bmi < 25:
    print('正常')
elif bmi < 28:
    print('过重')
else:
    print('肥胖')



args = ['gcc', 'hello.c', 'world.c']   #先码一下，以后回头看
match args:
    # 只有 gcc，没有文件
    case ['gcc']:
        print('gcc: missing source file(s).')
    # gcc + 至少一个文件
    case ['gcc', file1, *files]:
        print('gcc compile: ' + file1 + ', ' + ', '.join(files))
    # 只有 clean
    case ['clean']:
        print('clean')
    # 其他所有情况
    case _:
        print('invalid command.')