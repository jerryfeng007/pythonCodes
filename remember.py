# 1.列表练习题--哈哈
'''
有5名学生【张三、李四、王五、赵六、马七】，每个学生有5门科目【语文、数学、英语、物理、化学】
为这5位同学随机生成5门考试的成绩【成绩介于50-100之间】
需求：按照均分的倒序打印出成绩的明细

名次   姓名   语文   数学   外语   物理   化学   总分   均分
================================================================
1       赵六  89      69      100     61  82      401     80.2
2       张三  86      75      70      76  70      377     75.5
3       王五  86      75      70      76  70      377     75.4
4       李四  86      75      70      76  70      377     75.1
5       马七  86      75      70      76  70      377     75.0
=================================================================
'''
import random
if __name__ == '__main__':
    score = []
    sum_score = []
    student = ['张三', '李四', '王五', '赵六', '马七']
    kecheng = ['语文', '数学', '英语', '物理', '化学']

    # 给每个学生随机生成5门成绩，放入score列表
    for i in student:
        score_temp = []  # 注意，一定是在这里定义空列表，在for循环外面是不行的
        for j in kecheng:
            s = random.randint(50, 99)
            score_temp.append(s)
        score.append(score_temp)
    print(score)

    # 计算总分，放入sum_score列表
    for k in score:
        sum_score.append(sum(k))
    print(f'{student}的总分分别为{sum_score}')

    # 打印
    print('名次 姓名   语文   数学    外语    物理     化学    总分     均分')
    print('================================================================')

    # 使用for循环依次打印名次
    for i in range(len(student)):
        max_total_score = max(sum_score)              # 求总分的最大值
        max_index = sum_score.index(max_total_score)  # 获取总分最大值的索引
        name = student[max_index]                     # 根据索引获取该同学的名字
        print(i+1, end='\t')
        print(name, end='\t\t')
        for j in range(len(kecheng)):                 # 打印该同学5门课的成绩
            print(score[max_index][j], end='\t\t')
        print(max_total_score, end='\t\t')
        print('%.2f' % (max_total_score/5))
        del sum_score[max_index]  # 把总分列表中这次总分最大者删掉
        del score[max_index]      # 把分数列表中这个学生的成绩删掉
        del student[max_index]    # 把学生列表中这次最大分数者删掉

'''
需要注意的第1点：
for i in student:
    score_temp = []  # 注意，一定是在这里定义空列表，在for循环外面是不行的
    for j in kecheng:
        s = random.randint(50, 99)
        score_temp.append(s)
    score.append(score_temp)
    print(score)
    
需要注意的第2点：
for i in range(len(student)):
    max_total_score = max(sum_score)              # 求总分的最大值
    max_index = sum_score.index(max_total_score)  # 获取总分最大值的索引
    name = student[max_index]                     # 根据索引获取该同学的名字
这里获取最大值的索引，然后再利用这个索引去获取其他列表对应索引的值

需要注意的第3点：
del sum_score[max_index]  # 把总分列表中这次总分最大者删掉
del score[max_index]      # 把分数列表中这个学生的成绩删掉
del student[max_index]    # 把学生列表中这次最大分数者删掉
只有删除这次的值，下一次循环数据才不会重复。
'''

# 2.有10个学生，姓名自行添加，有三门考试，语文、数学、英语
'''
随机为他们生成分数【50，100】,打印一张成绩排名表,数据存储格式如下：
95001:{'姓名': '张三', '名次': 4, '总分': 234, '明细': [67, 78, 89]},
95001:{'姓名': '张三', '名次': 4, '总分': 234, '明细': [67, 78, 89]},
95001:{'姓名': '张三', '名次': 4, '总分': 234, '明细': [67, 78, 89]},
95001:{'姓名': '张三', '名次': 4, '总分': 234, '明细': [67, 78, 89]}
'''
# 思路，通过存储格式可以看出，需要存储在一个大字典里

num = [95001, 95002, 95003, 95004, 95005, 95006, 95007, 95008, 95009, 95010]
student = ['冯一', '曹二', '张三', '李四', '王五', '赵六', '田七', '马八', '包九', '崔十']
kemu = ['语文', '数学', '英语']
info = ['姓名', '名次', '总分', '明细']

# 定义一个大字典，类似：
# {95001:{'姓名': '张三', '名次': 4, '总分': 234, '明细': [67, 78, 89]},
#  95002:{'姓名': '李四', '名次': 5, '总分': 233, '明细': [66, 78, 89]},...}
dict_all = {}.fromkeys(num)

# 把10个同学的三门成绩放入列表，格式为：[[], [], []]
score = []
for i in student:
    score_temp = []
    for j in kemu:
       s = random.randint(50, 100)
       score_temp.append(s)
    score.append(score_temp)

# 求总分
sum_score = []
for i in score:
    sum_score.append(sum(i))

# 排名
print('学号    姓名   名次   语文   数学   外语   总分')
print('=========================================================')
for i in range(len(student)):
    # 求总分的最大值
    max_score = max(sum_score)
    # 获取最大值的索引
    max_index = sum_score.index(max_score)

    # 根据该索引，获取不同列表中该学生的信息
    xuehao = num[max_index]
    name = student[max_index]
    zongfen = max_score
    mingxi = score[max_index]

    # 把所有信息放入大字典
    dict_all[xuehao] = {info[0]: name, info[1]: i+1, info[2]: zongfen, info[3]: mingxi}

    # 打印
    print(xuehao, end='\t')
    print(name, end=' \t')
    print(i+1, end=' \t  ')
    print(mingxi[0], end='\t ')
    print(mingxi[1], end='\t    ')
    print(mingxi[2], end='\t   ')
    print(zongfen)

    # 删除本次的值，下一次循环从剩下的里面再次计算最大值
    num.pop(max_index)
    student.pop(max_index)
    sum_score.pop(max_index)
    score.pop(max_index)

# 打印大字典
# print(dict_all)

# 3.总结
'''----------------------------------------------------------------------------------------------------------------------
数据类型主要有：数字、字符串、列表、元组、字典、集合
不可变类型：数字、字符串、元组
可变类型：列表、字典、集合

字符串是有序的，不可修改的
列表是有序的，可修改的
元组是有序的，不可修改的
字典是无序的，可修改的
集合是无序的，可修改的，不允许重复的

总结：
字符串、列表、元组是有序的
集合、字典是无序的

列表、集合、字典可修改
字符串、元组是不可修改的

集合不允许重复

字典的特点：
因为字典是无序的，所以字典没有索引值
因为字典没有索引值，所以字典以键取值
因为字典以键取值，所以字典的键唯一且不可修改
因为字典的键不可修改，所以列表和字典不可以给字典做键

其他：
因为元组的方法比较少，而且元组不可以被修改，所以他的安全性和稳定性比较好，经常被作为配置文件的一部分
如果只有一个元素，一定不要忘记加逗号， path = （pathname,）
------------------------------------------------------------------------------------------------------------------------'''
# 4.9x9乘法表
'''
1x1=1 
1x2=2 2x2=4 
1x3=3 2x3=6 3x3=9 
1x4=4 2x4=8 3x4=12 4x4=16 
1x5=5 2x5=10 3x5=15 4x5=20 5x5=25 
1x6=6 2x6=12 3x6=18 4x6=24 5x6=30 6x6=36 
1x7=7 2x7=14 3x7=21 4x7=28 5x7=35 6x7=42 7x7=49 
1x8=8 2x8=16 3x8=24 4x8=32 5x8=40 6x8=48 7x8=56 8x8=64 
1x9=9 2x9=18 3x9=27 4x9=36 5x9=45 6x9=54 7x9=63 8x9=72 9x9=81  
'''
'''
第一步：
1x9=9 2x9=18 3x9=27 4x9=36 5x9=45 6x9=54 7x9=63 8x9=72 9x9=81  先实现这一行
'''
# i = 9  # 先写死
# for j in range(1, 10):
#     print(f'{j}x{i}={j * i}', end=' ')

'''
第二步
在上面的基础上，把i变活，i取值1-9，需要注意i与j的关系
'''
for i in range(1, 10):
    for j in range(1, i+1):
        print(f'{j}x{i}={j * i}', end=' ')
    print()  # 需要加一个空行

# 5.反转
# 字符串反转
# 方法1
s = 'HelloWorld'
print(s[::-1])
# 方法2
s = 'HelloWorld'
s1 = ''
for i in s:
    s1 = i + s1
print(s1)

# 列表反转
# 方法1
list1 = [1, 2, 3, 2, 5, 4]
print(list1[::-1])
# 方法2：
list1 = [1, 2, 3, 2, 5, 4]
list1.reverse()
print(list1)

# 元组反转
tuple1 = (1, 2, 1, 4, 3)
print(tuple1[::-1])

# 6.删除列表中所有的1
# 方法1：这个方法的坏处，是把所有的元素都去重了，所以结果可能不正确
L = [1, 2, 3, 1, 3, 1, 5, 1]
s = set(L)    # 去重（备注：set()是集合，不允许重复的值）
L = list(s)   # 把集合转变为列表
L.remove(1)
print(L)

# 方法2：靠谱
L1 = [1, 2, 3, 1, 3, 1, 5, 1]
while True:
    L1.remove(1)
    if 1 not in L1:
        print(L1)
        break

# 7.交换两个变量的值
a = 10
b = 20
a, b = b, a   # 序列解包赋值
print(a, b)

# 8.eval()函数：把指定的字符串，转化为数字、列表、元组、集合、字典
# 转化为数字
a = '123'
a = eval(a)
print(a, type(a))

# 转化为列表
a = '[1, 2, 3]'
a = eval(a)
print(a, type(a))

# 转化为元组
a = '(1, 2, 3)'
a = eval(a)
print(a, type(a))

# 转化为集合
a = '{1, 2, 3}'
a = eval(a)
print(a, type(a))

# 转化为字典
a = '{"name": "Jerry", "age": 18}'
a = eval(a)
print(a, type(a))

# 9. ''.join()函数：把字符串、列表、元组中的元素，以指定的字符(分隔符)连接生成一个新的字符串
b = 'abcde'
# 用指定的分隔符生成新的字符串
b = '-'.join(b)
print(b, type(b))

# 字符串转化为列表
b = list('abcde')
print(b)
# 列表转化为字符串
b = ','.join(b)
print(b, type(b))

# 字符串转化为元组
b = tuple('abcde')
print(b)
# 元组转化为字符串
b = ''.join(b)
print(b, type(b))

# 字符串转化为字典的key
b = {}.fromkeys('abcde')
print(b)
# 元组转化为字符串
b = '-'.join(b)
print(b, type(b))

num = [95001, 95002, 95003, 95004, 95005, 95006, 95007, 95008, 95009, 95010]
dict_all = {}.fromkeys(num)
print(dict_all)

# {95001: None, 95002: None, 95003: None, 95004: None, 95005: None, 95006: None, 95007: None, 95008: None, 95009: None, 95010: None}
for i in range(1, 11):
    dict_all[num[i-1]] = i
print(dict_all)

# 10.响应的类型
'''
r.text----str类型，注意是双引号
{"errCode":0,"msg":"success","data":["600000","600004","600006","600007","600008","600009","000001","000002","000004","000005","000006","600570"]}

r.json---dict类型，注意是单引号
{'errCode': 0, 'msg': 'success', 'data': ['600000', '600004', '600006', '600007', '600008', '600009', '000001', '000002', '000004', '000005', '000006', '600570']}

r.content--字节(二进制)类型
b'{"errCode":0,"msg":"success","data":["600000","600004","600006","600007","600008","600009","000001","000002","000004","000005","000006","600570"]}'
'''

# 11.json.dumps 和 json.loads
# 如果post请求数据为json格式（其实类型是str），那么需要先把请求数据data（一般为dict）转换为json格式
# data = json.dumps(data)  转化后，data为str 

# 把json格式转化为python中的格式，其实是由str变为别的类型
# data = json.loads(data)  转化后，data由str变为了其他的类型






