import unittest
import HTMLTestRunner_CN_Chart_Screen
import time

# 能够遍历多个以test开头的测试类


def create_suite(case_path):
    uts = unittest.TestSuite()
    discover = unittest.defaultTestLoader.discover(case_path, pattern='test_*.py')

    for test_suite in discover:
        for test_case in test_suite:
            uts.addTest(test_case)  # 将测试用例加入unittest
    return uts


if __name__ == '__main__':
    case_path = r'D:\learnPY\appium\appiumproject\test_case'
    report_path = r'D:\learnPY\appium\appiumproject\report'

    suite = create_suite(case_path)

    # 获取当前时间 可确保测试报告文件不重名
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    report_name = report_path+'/'+now+'result.html'

    fp = open(report_name, 'wb')
    runner = HTMLTestRunner_CN_Chart_Screen.HTMLTestRunner(verbosity=2, stream=fp, title='自动化', description='测试')
    runner.run(suite)
    fp.close()
