import os

import pytest
import requests
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

from testcase.yaml_util import YamlUtil


class TestResearch:
    # 测试用例存于test_api.yaml
    @pytest.mark.parametrize('args',YamlUtil(os.getcwd()+'\\test_api.yaml').read_yaml())
    def test_01_baili(self,args):
        #自动执行所有用例
        driver = webdriver.Chrome()
        url = args['request']['url']
        driver.get(url)
        param=args.get('param')
        # 在输入框中输入值:
        elem = driver.find_element(By.NAME, "wd")
        elem.send_keys(param)
        e = driver.find_element(By.NAME, "wd")
        #点击百度一下：
        driver.find_element(By.ID,"su").click()
        sleep(5)
        content = driver.page_source
        test=args.get('test')
        sleep(1)
        #断言
        assert test in content
        driver.quit()

    # # 测试当输入100个字符时，可以正常输入
    # @pytest.mark.parametrize('args', YamlUtil(os.getcwd() + '\\test_api.yaml').read_yaml())
    # def test_02_baili(self, args):
    #     driver = webdriver.Chrome()
    #     driver.get("https://www.baidu.com/s")
    #     # 在输入框中输入值
    #     elem = driver.find_element(By.NAME, "wd")
    #     elem.send_keys(
    #         "好好学习好好学习好好好好学习好好学习好好好好学习好好学习好好好好学习好好学习好好好好学习好好学习好好好好学习好好学习好好好好学习好好学习好好好好学习好好学习好好好好学习好好学习好好好好学习好好学习好好")
    #     sleep(1)
    #     e = driver.find_element(By.NAME, "wd")
    #     print(e.text)
    #     url = args['request']['url']
    #     params = args.get('request').get('param')
    #     res = requests.get(url, params=params)
    #     # print(res.text)
    #     # 断言
    #     assert e.text in res.text
    #
    #     sleep(1)
    #     driver.quit()
    #
    #
    # # 测试当输入超过100个字符时，超过那部分字段无法正常输入（即输入框处只能有100个字符 只能显示100个字符 超过的部分无法输入上去）
    # @pytest.mark.parametrize('args', YamlUtil(os.getcwd() + '\\test_api.yaml').read_yaml())
    # def test_03_baili(self, args):
    #     driver = webdriver.Chrome()
    #     driver.get("https://www.baidu.com/s")
    #     # 在输入框中输入值
    #     elem = driver.find_element(By.NAME, "wd")
    #     elem.send_keys(
    #         "好好学习好好学习好好好好学习好好学习好好好好学习好好学习好好好好学习好好学习好好好好学习好好学习好好好好学习好好学习好好好好学习好好学习好好好好学习好好学习好好好好学习好好学习好好好好学习好好学习好好学")
    #     sleep(1)
    #     e = driver.find_element(By.NAME, "wd")
    #     print(e.text)
    #     url = args['request']['url']
    #     params = args.get('request').get('param')
    #     res = requests.get(url, params=params)
    #     # print(res.text)
    #     # 断言
    #     assert e.text in res.text

        # sleep(1)
        # driver.quit()


if __name__ == '__main__':

    #TestResearch.test_01_baili()
    pytest.main()
