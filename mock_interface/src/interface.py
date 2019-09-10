import re
import json
from commons import http_request
from commons import insert_results_to_excel


def interface_test(s,
                   num,
                   name,
                   url,
                   path,
                   method,
                   data_format,
                   check_point,
                   data,
                   log):

    time, response, status_code = None, None, None

    if method == 'GET' and data_format == 'Form':
        response, time, status_code = http_request.get_form(url, path, data)
    elif method == 'POST' and data_format == 'Form':
        response, time, status_code = http_request.post_form(url, path, data)
    elif method == 'POST' and data_format == 'Json':
        response, time, status_code = http_request.post_json(url, path, data)
    else:
        print('请求方法或请求格式不正确')

    # 查看响应的类型：dict、str、bytes，分别对应：r.json、r.text、r.content
    # print(type(response))

    response_json = response if type(response) is str else json.dumps(response)

    # 对响应数据做处理
    if status_code != 200:
        insert_results_to_excel.case_fail(s,
                                          num,
                                          response,
                                          time,
                                          name,
                                          status_code,
                                          log)
        return response

    if re.search(check_point, response_json):
        insert_results_to_excel.case_pass(s,
                                          num,
                                          response,
                                          time,
                                          name,
                                          status_code,
                                          log)
        return response

    else:
        insert_results_to_excel.case_fail(s,
                                          num,
                                          response,
                                          time,
                                          name,
                                          status_code,
                                          log)
        return response
