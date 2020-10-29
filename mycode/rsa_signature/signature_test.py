import json
import time

import requests

from signature import prepare_sign_content, rsa_sign_private, rsa_sign_public


# 私钥
private_key = 'MIIBVQIBADANBgkqhkiG9w0BAQEFAASCAT8wggE7AgEAAkEAvInLeuUP0S1apUHNIhjFFG4VZFWfeO6G3ae6kMIFKxaLu4ppG7dbSCfnLpoJpwCu0KSt/QR6HBhGbQDiId/yuQIDAQABAkEAqm/y15UtOE7Ey/HxLCqyNqbRhdN1h5AxsT0IhgYvP+PhWGc3hRElMwNCdiNaJBh04R1iK6wmKoi3DSjkdU6IAQIhAPRL9khAdPMxjy5tpswNWeaDjNJrlUKEnItQUkoHqve5AiEAxZIDz235HcUgLg9ApYK4spOpzLDGCCgfO3FxmrUEUwECIEaLjQIOQvdbT1p75Ze1H0nWoRq+YGrF+qKsPicMkc1ZAiARlNTR+K9afthGQQU3tVJKUemiVXjJ8QgWehnp8oHYAQIhANsC2fEVjWv94Oy2c8I9qhuX+yfNtvZ2m+Kmf2o4JFrR'
# 公钥
public_key = 'MFwwDQYJKoZIhvcNAQEBBQADSwAwSAJBALyJy3rlD9EtWqVBzSIYxRRuFWRVn3juht2nupDCBSsWi7uKaRu3W0gn5y6aCacArtCkrf0EehwYRm0A4iHf8rkCAwEAAQ=='
# 授权客户Id
app_id = 'qweasdzxc'


def prefix_data(**kwargs):
    """
    数据前缀处理
    :param kwargs: 关键字参数（app_id, method, biz_content）
    :return: dict
    """
    return {
        "format": "json",
        "charset": "utf-8",
        "sign_type": "RSA2",
        "version": "1.0",
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
        "app_id": kwargs.get('app_id'),
        "method": kwargs.get('method'),
        "biz_content": json.dumps(kwargs.get('biz_content'), ensure_ascii=False)
    }


def fetch_data():
    # 接口平台访问地址
    url = "http://localhost:8081"
    # 接口平台请求参数类型
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    # 要查询用户信息
    biz_content = {
        "riskId": "T000001",
        "name": "张三",
        "phone": "158xxxx3744",
        "pid": "14042819870520xxxx"
    }
    data = prefix_data(app_id=app_id, method='KX.XFraud.search', biz_content=biz_content)
    c1 = prepare_sign_content(content=data)
    print(f'待签名内容: {c1}')

    sign = rsa_sign_private(c1, private_key)
    data['sign'] = sign
    print(f'签名: {sign}')

    c2 = rsa_sign_public(c1, public_key, sign)
    print(f'解签结果: {c2}')

    response = requests.request("POST", url, data=data, headers=headers)
    print(f'响应结果: {response.json()}')


if __name__ == '__main__':
    fetch_data()
