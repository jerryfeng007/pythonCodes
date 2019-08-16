import re

print('--------------------------使用正则表达式去除所有标点符号和换行------------------------------------------')

con = '''
I have "a" dream; that, my! four little children: will
one day live. in a nation where? they will 'not'

I have a dream that one day down in Alabama, with its vicious racists, . . . one day.

'''

con = re.sub(r'[^\w]', ' ', con)
# con = re.sub(r'\W', ' ', con)
print(con)

print('--------------------------知识补充---re.sub()--------------------------------------')

# 替换，把某个内容中的某部分，替换为其他的内容
# 比如：
c = 'i love u'
c = re.sub('love', 'hate', c)
print(c)

print('--------------------------知识补充---正则表达式--------------------------------------')

#  \w     匹配数字字母下划线
#  \W     匹配非数字字母下划线
#  [^abc] 匹配除了a,b,c之外的字符

print('--------------------------知识补充---r--------------------------------------')

# r，表示原生字符串，不转义 -----推荐
# 比如：
path = r'D:\myPython\pythonCodes\variable.py'
print(path)

# 如果不使用r，也可以使用\\ -----就是不太好区分
# 比如：
path = 'D:\\myPython\pythonCodes\\variable.py'
print(path)
