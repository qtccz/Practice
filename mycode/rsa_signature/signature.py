import base64

from Crypto.PublicKey import RSA
from Crypto.Hash import SHA256
from Crypto.Signature import PKCS1_v1_5
from base64 import b64decode


def prepare_sign_content(**kwargs):
    """
    待签名文本处理
    :param kwargs: 关键字参数
    :return: str
    """
    params = []
    for k1, prepare_params in kwargs.items():
        if not isinstance(prepare_params, dict):
            print(f'{k1} type is {type(prepare_params)}, need a dict')
        elif not prepare_params:
            print(f'{k1} value is None, value is {prepare_params}')
        else:
            prepare_params_keys = list(prepare_params.keys())
            prepare_params_keys.sort()
            for key in prepare_params_keys:
                if prepare_params_keys.index(key) == 0:
                    params.append("")
                else:
                    params.append("&")
                params.append(f'{key}={prepare_params[key]}')
        return "".join(params)


def rsa_sign_private(data, private_key):
    """
    RSA私钥签名
    :param data: 明文数据
    :param private_key: RSA签名需要的私钥
    :return: 签名后的字符串sign
    """
    key_bytes = bytes(private_key, encoding="utf-8")
    key_bytes = b64decode(key_bytes)
    rsa_key = RSA.importKey(key_bytes)
    signer = PKCS1_v1_5.new(rsa_key)
    digest = SHA256.new()
    digest.update(data.encode("utf8"))
    sign = signer.sign(digest)
    signature = base64.b64encode(sign)
    return str(signature, encoding="utf-8")


def rsa_sign_public(data, public_key, signature):
    """
    RSA公钥验签
    :param data: 明文数据
    :param public_key: RSA验签需要的公钥
    :param signature: 接收到的sign签名
    :return: 验签结果,布尔值
    """
    key_bytes = bytes(public_key, encoding="utf-8")
    key_bytes = b64decode(key_bytes)
    rsa_key = RSA.importKey(key_bytes)
    verifier = PKCS1_v1_5.new(rsa_key)
    digest = SHA256.new()
    digest.update(data.encode("utf-8"))
    # 因为签名时对签名值进行过base64编码，所以验签时需要解码
    return verifier.verify(digest, base64.b64decode(signature))
