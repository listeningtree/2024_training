import os

import pytest
import requests

from testcase.yaml_util import YamlUtil


class TestResearch:
    @pytest.mark.parametrize('args',YamlUtil(os.getcwd()+'\\test_api.yaml').read_yaml())
    def test_01_baili(self,args):

        url=args['request']['url']
        params=args.get('request').get('param')
        res=requests.get(url,params=params)
        #print(res.text)
        # 断言
        assert args.get('test') in res.text

if __name__ == '__main__':
    pytest.main()
