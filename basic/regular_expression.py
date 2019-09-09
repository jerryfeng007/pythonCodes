import re

print('----------------------常用方法--------------------------------------------------------')

# re.match只匹配字符串的开始，如果字符串开始不符合正则表达式，则匹配失败，函数返回None
print(re.match('www', 'wwwcom').group())  # 在起始位置匹配
print(re.match('www', 'comwww'))          # 不在起始位置匹配

# re.search,扫描整个字符串并返回第一个成功的匹配
print(re.search('xqtesting', 'http://www.xqtesting.com').group())
print(re.search('m', 'http://www.xqtesting.com/blog.html').group())

# re.findall,从左到右扫描字符串，按顺序返回匹配，如果无匹配结果返回空列表
print(re.findall(r'\d', 'one1two2three3four4'))
print(re.findall('four', 'one1two2three3four4four'))

# sub用于替换字符串中的匹配项
print(re.sub('g..t', 'xiaoqiang', 'gaat gbbt gcct'))

# split返回切割后的列表
print(re.split(r'\+', '123+456*789'))

print('--------------------------案例：使用正则表达式去除所有标点符号和换行----------------------')

con = '''
I have "a" dream; that, my! four little children: will
one day live. in a nation where? they will 'not'

I have a dream that one day down in Alabama, with its vicious racists, . . . one day.

'''

con = re.sub(r'[^\w]', ' ', con)
# con = re.sub(r'\W', ' ', con)
print(con)

print('--------------------------知识补充---正则表达式--------------------------------------')

#  \w     匹配数字字母下划线
#  \W     匹配非数字字母下划线
#  [^abc] 匹配除了a,b,c之外的字符

print('--------------------------知识补充: r  ----------------------------------------------')

# r，表示原生字符串，不转义 -----推荐
# 比如：
path = r'D:\myPython\pythonCodes\variable.py'
print(path)

# 如果不使用r，也可以使用\\ -----就是不太好区分
# 比如：
path = 'D:\\myPython\\pythonCodes\\variable.py'
print(path)
