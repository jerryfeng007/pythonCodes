import shutil
from src import interface
from commons import get_excel_column_data


def run_case(test_case, report, log, wb, s):
    # 空字典，后续保存数据
    correlation_dict = {}

    # 遍历时，取出每一列的数据
    for i in range(2, s.max_row+1):
        if s.cell(row=i, column=10).value != 'Yes':
            continue
        (num,
         name,
         url,
         path,
         method,
         data_format,
         request_data,
         check_point,
         correlation) = get_excel_column_data.get_column_data(s, i)

        # 在request_data、path中查找是否存在需要关联的数据
        if correlation_dict:
            for keyword in correlation_dict:
                if request_data.find(keyword) > 0:
                    request_data = request_data.replace(keyword, (correlation_dict[keyword]))
                if path.find(keyword) > 0:
                    path = path.replace(keyword, (correlation_dict[keyword]))
            print('最终请求数据=', request_data)
            print('最终请求path=', path)

        # 运行
        response = interface.interface_test(s,
                                            num,
                                            name,
                                            url,
                                            path,
                                            method,
                                            data_format,
                                            check_point,
                                            eval(request_data),
                                            log)

        if correlation:
            correlation = correlation.split(';')  # 如果有多个关联参数则用分号隔开
            print('关联公式为：', correlation)

            try:
                for j in correlation:
                    param = j.split('=')
                    print('param[0]为：', param[0])
                    print('param[1]为：', param[1])

                    response1 = response  # 有多个关联参数的情况

                    if len(param) != 2:
                        raise Exception("关联参数拆分出现错误!")

                    for key in param[1][1:-1].split(']['):  # split处理${date}=[result][data]这样的数据
                        print("key为：", key)
                        print('response1为：', response1)
                        response1 = response1[key]
                        print('response1为：', response1)

                        correlation_dict[param[0]] = response1  # 关联到的响应放到字典里，方便后续去遍历替换参数
                        print('correlation_dict为：', correlation_dict)

                print('最终关联的值为：', correlation_dict)

            except Exception as e:
                print('上一个请求响应中的数据缺失，导致关联失败', str(e))

    wb.save(test_case)
    shutil.copy(test_case, report)
    print('所有用例执行完毕！')
