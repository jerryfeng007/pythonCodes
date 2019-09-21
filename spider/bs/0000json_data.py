import requests
import openpyxl


def json_data():
    wb = openpyxl.load_workbook('0000json_excel.xlsx')
    table = wb['Sheet1']

    url = 'https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%83%AD%E9%97%A8&sort=recommend&page_limit=275&page_start=0'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 Safari/537.36'}

    res = requests.get(url, headers=headers)

    if res.status_code == 200:
        res = res.json()  # 转换为了字典类型的数据
        # print(res)
        movies = res['subjects']
        # print(movies)
        for movie in movies:
            info = [movie['title'], movie['rate']]
            table.append(info)  # ---------------------注意这个用法
        wb.save('0000json_excel.xlsx')


json_data()
