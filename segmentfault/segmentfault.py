import unittest
import HTMLTestRunner


def create_suite():
    test_dir = './'
    discover = unittest.defaultTestLoader.discover(test_dir, pattern='test*.py')
    return discover


if __name__ == '__main__':
    suite = create_suite()
    with open('./res.html', 'wb') as f:
        runner = HTMLTestRunner.HTMLTestRunner(stream=f, verbosity=2, title='segmentfault测试报告')
        runner.run(suite)
