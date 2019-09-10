# 把excel中的每一列数据取出来


def column_data(s, i):
    def inner(j):
        return s.cell(row=i, column=j).value
    return inner


def get_column_data(s, i):
    data = column_data(s, i)
    num = data(1)
    name = data(2)
    url = data(3)
    path = data(4)
    method = data(5)
    data_format = data(6)
    request_data = data(7)
    check_point = data(8)
    correlation = data(9)

    return (num,
            name,
            url,
            path,
            method,
            data_format,
            request_data,
            check_point,
            correlation)
