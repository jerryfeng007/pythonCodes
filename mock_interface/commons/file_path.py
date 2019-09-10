import os
import shutil
from commons import get_cfg


def backup():

    # 获取文件
    test_case, report, logfile, test_case_backup = \
        get_cfg.get_nt_file_cfg() if os.name == 'nt' else get_cfg.get_file_cfg()

    # 备份test_case文件
    shutil.copyfile(test_case, test_case_backup)

    print('获取用例文件并备份成功！')
    return test_case, report, logfile
