# print("hello world")
# print("hello world2")
# print(1)
# print(2.2)
# print(True)
# print(False)
# print("dduhhqid1")
# print("------------")
# print(None)
# print(True+1)
# print(False-1)


# # Python 赋值 不需要 写数据类型（int /string/float 这些）
# num=123
# print(num)
# num=num+2
# print(num)
# num+=2
# print(num)
# num="ok"
# print(num)
# num=True
# print(num)


# num=20.7
# for i in range(2):
#     num+=50
# print(num)


# # a=10,b=20 这是一种错误书写方式，java有数据类型的话，书写是对的，但是python不行
# a,b=10,20
# print(a,b)
# num=a
# a=b
# b=num
# print(a,b)

# a,b,c=100,200,300
# print(a,b,c)
# d=a
# a=b 
# b=c
# c=d
# print(a,b,c)


# # type()函数可以查看数据类型
# b="abc"
# c=True
# print(type(a))
# print(type(b))
# print(type(c))  

# # isinstance()函数可以判断一个变量是否是某个数据类型
# print(isinstance(a,int))
# print(isinstance(b,float))
# print(isinstance(c,bool))
# # 数据类型转换有int()函数、float()函数、str()函数、bool()函数等
# print(int(3.14))  # 3   
# print(float(3))  # 3.0
# print(str(123))  # "123"        
# print(bool(0))   # False
# print(bool(1))   # True



# # 字符串三种定义方式：双引号、单引号、三引号  
# # 双引号和单引号不支持换行，三引号支持换行（显示格式与书写时相当）  
# d="def"
# e='ghi'
# f="""
# jkl
# 法王噶我国爱国
# """
# print(d)
# print(e)    
# print(f)

# # 转义字符：\n换行 \t制表符 \\反斜杠 \'单引号 \"双引号
# # 在字符串中使用这些特殊字符时需要使用转义字符
# g="abc\ndef"
# print(g)
# # 双引号字符串中直接书写单引号不影响
# # 单引号字符串中直接书写双引号不影响
# h="abc'def"
# i='abc"def'
# print(h)
# print(i)

# # 字符串拼接可以使用+号
# # 也可以使用逗号，逗号会在字符串之间添加一个空格
# j="abc"
# k="def"
# print(j+k)
# print(j,k)

# # 字符串拼接时，只能拼接字符串类型的数据，不能拼接其他类型的数据
# # print(j+1)  # 这会报错，因为1是整数类型，不能与字符串类型的j拼接
# # 可以使用str()函数将其他类型的数据转换为字符串类型，然后再进行拼接
# print(j+str(1))

# # 字符串格式化
# # format()函数可以在字符串中使用{}占位符来表示需要替换的内容，然后在format()函数中传入需要替换的内容，按照顺序进行替换
# name="Alice"
# age=25
# print("My name is {} and I am {} years old.".format(name, age))
# # f-string格式化字符串，在字符串前面加上f，然后在字符串中使用{}占位符来表示需要替换的内容，直接在{}中书写需要替换的内容即可
# print(f"My name is {name} and I am {age} years old.")
# # 更推荐使用f-string格式化字符串

# # input函数可以获取用户输入的数据，input()函数返回的是字符串类型的数据
# user_input=input("请输入一些内容：")
# print("你输入的内容是：", user_input)

# # 算术运算符
# print(5 + 3)  # 8，加法运算符
# print(5 - 3)  # 2，减法运算符
# print(5 * 3)  # 15，乘法运算符
# print(5 / 3)  # 1.6666666666666667，除法运算符
# print(5 // 3) # 1，整除运算符
# print(5 % 3)  # 2，取模运算符
# print(5 ** 3) # 125，幂运算符

# # 赋值运算符
# x = 10
# x += 5  # 等同于 x = x + 5  
# print(x)  # 15
# x -= 3  # 等同于 x = x - 3  
# print(x)  # 12
# x *= 2  # 等同于 x = x * 2
# print(x)  # 24
# x /= 4  # 等同于 x = x / 4
# print(x)  # 6.0
# x //= 2 # 等同于 x = x // 2
# print(x)  # 3.0
# x %= 2  # 等同于 x = x % 2
# print(x)  # 1.0
# x **= 3 # 等同于 x = x ** 3
# print(x)  # 1.0

# # 比较运算符
# print(5 > 3)   # True，大于运算符
# print(5 < 3)   # False，小于运算符
# print(5 >= 3)  # True，大于等于运算符
# print(5 <= 3)  # False，小于等于运算符
# print(5 == 3)  # False，等于运算符  
# print(5 != 3)  # True，不等于运算符

# # 逻辑运算符
# print(True and False)  # and只有当两个操作数都为True时，结果才为True，否则为False   
# print(True or False)   # or只要有一个操作数为True，结果就为True，只有当两个操作数都为False时，结果才为False
# print(not True)        # not是取反运算符，not True的结果为False，not False的结果为True

# print(5 > 3 and 2 < 4)  # True and True -> True
# print(5 > 3 or 2 > 4)   # True or False -> True
# print(not (5 > 3))       # not True -> False

# a=int(input("请输入一个整数："))
# print(f"你输入的整数{a}，在不在15到20之间：{a > 15 and a < 20}")

# b=78
# if b > 80:
#     print("成绩优秀")
# elif b > 60:
#     print("成绩及格")
# else:    print("成绩不及格")    

# a=89
# b=92
# if a > 70 and b > 70:
#     print("成绩优秀")   
# elif 70 >a> 60 and 70>b > 60:
#     print("成绩及格")
# else:    print("成绩不及格")    

# a=29
# b=90 
# if a > 70 and b > 70:
#     print("成绩优秀")
# elif 70 >a> 60 and 70>b > 60:
#     print("成绩及格")
# else:    print("成绩不及格")

# if b>60:
#     print("b的成绩及格")
#     if b>80:
#         print("成绩优秀")
#         if b>90:
#             print("成绩非常优秀")   
#         else:
#             print("成绩不非常优秀")
#     else:    print("成绩不优秀")



# # 需求1：输入一个整数，判断这个整数是奇数还是偶数
# def check_odd_even(number):
#     if number % 2 == 0:
#         return "偶数"
#     else:
#         return "奇数"

# number = int(input("请输入一个数字: "))
# print(f"{number}是{check_odd_even(number)}")

# 需求2：输入一个整数，判断是否成年
# def check_adult(age):
#     if age >= 18:
#         return "成年"
#     else:
#         return "未成年"
# age = int(input("请输入你的年龄: "))
# print(f"你已经{check_adult(age)}")

# 需求3：输入一个整数，判断是正数、负数还是零
# def check_number(num):
#     if num > 0:
#         return "正数"
#     elif num < 0:
#         return "负数"
#     else:
#         return "零"
# number = int(input("请输入一个数字: "))
# print(f"{number}是{check_number(number)}")

# 需求4：输入一个整数，判断是否及格，大于等于60分为及格
# def check_pass(score):
#     if score >= 60:
#         return "及格"
#     else:
#         return "不及格"
# score = int(input("请输入你的成绩: "))
# print(f"你的成绩{check_pass(score)}")

# 结构模式匹配match...case跟switch...case类似，可以用来替代多重if...elif...else语句，使代码更简洁易读
# def check_grade(score):
#     match score:
#         case x if x >= 80:
#             return "优秀"
#         case x if x >= 60:
#             return "及格"
#         case _:
#             return "不及格"
# score = int(input("请输入你的成绩: "))
# print(f"你的成绩{check_grade(score)}")  

# while循环可以重复执行一段代码，直到满足某个条件才停止
count = 0
while count < 5:
    print(f"当前计数: {count}")
    count += 1

# 计算1到100之间的偶数累加之和
total = 0
num = 1
while num <= 100:
    if num % 2 == 0:
        total += num
    num += 1
print(f"1到100之间的偶数累加之和是: {total}")

# for循环可以遍历一个序列（如列表、字符串等）中的每个元素
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)