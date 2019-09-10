from configparser import ConfigParser

cp = ConfigParser()
cp.read('info.cfg', encoding='utf8')


def get_item(num):
    if len(cp.sections()) == 0:
        raise Exception('没有找到info.cfg文件，或者文件的内容为空!')
    if not isinstance(num, int):
        raise Exception('num必须为int类型!')
    if num > len(cp.sections())-1 or num < 0:
        raise Exception('num超出了范围!')
    section = cp.sections()[num]

    def inner(arg):
        if arg not in [x[0] for x in cp.items(section)]:
            raise Exception('section中没有找到这个arg!')
        return eval(cp.get(section, arg))  # 使用eval函数主要解决"'client_id'"嵌套引号的问题
    return inner


# 获取用例文件
def get_file_cfg():
    file_cfg = get_item(0)
    test_case = file_cfg('test_case')
    report = file_cfg('report')
    logfile = file_cfg('logfile')
    test_case_backup = file_cfg('test_case_backup')
    return test_case, report, logfile, test_case_backup


# 获取用例文件_nt
def get_nt_file_cfg():
    nt_file_cfg = get_item(1)
    test_case = nt_file_cfg('test_case')
    report = nt_file_cfg('report')
    logfile = nt_file_cfg('logfile')
    test_case_backup = nt_file_cfg('test_case_backup')
    return test_case, report, logfile, test_case_backup
