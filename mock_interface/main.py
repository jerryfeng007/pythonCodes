from src import run_test
from commons import file_path
from commons import request_log
from commons import clear_last_results

if __name__ == '__main__':

    # 获取用例文件，运行之前先备份
    test_case, report, logfile = file_path.backup()

    # 清除上次的运行结果
    wb, s = clear_last_results.main(test_case)

    # 日志
    log = request_log.interface_log(logfile)

    # 运行(遍历excel中的用例)
    run_test.run_case(test_case, report, log, wb, s)
