import os
import urllib

import pytest
import urllib.parse
import requests

from testcase.yaml_util import YamlUtil

class TestResearch:
    #测试用例存于：test_api.yaml
    @pytest.mark.parametrize('args',YamlUtil(os.getcwd()+'\\test_api.yaml').read_yaml())
    def test_01_baili(self,args):
        #自动执行所有用例
        url = args['request']['url']
        headers=args['request']['headers']
        req = urllib.request.Request(url,headers=headers)
        html = urllib.request.urlopen(req).read().decode('UTF-8', 'ignore')
        assert args.get('test') in html
        #若test中存的字段在返回的html中能够找到 则判为用例通过

if __name__ == '__main__':
    pytest.main()
