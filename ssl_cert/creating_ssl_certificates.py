# -*- coding=utf-8 -*-
# pyOpenSSL==20.0.1
# six==1.16.0
import OpenSSL
import time, os
from datetime import datetime, timedelta

__BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def zone_offset(z):
    """
    使用字典（dict）的get方法实现实现switch case语句
    根据时区计算时间
    :param z: 时区(zone)
    :return:
    """
    switcher = {
        "+0000": 0,
        "+0800": +8,
    }
    return switcher.get(z, 0)


def get_timestamp(t, z):
    """
    根据时间和时区计算时间戳
    :param t: 时间：20190304005100Z <class 'str'>
    :param z: 时区 +0800 <class 'str'>
    :return: 时间戳 1551660660000  <class 'int'>
    """
    t_time = datetime.strptime(t, "%Y%m%d%H%M%SZ") + timedelta(hours=zone_offset(z))
    return int(time.mktime(t_time.timetuple()))*1000


def certificate_information(f_path=os.path.join(__BASE_DIR, "ca.pem"), z="+0800"):
    """
    获取证书相关信息
    :param f_path: 证书的路径
    :param z: 时区，需要和运行环境的时区保持一致
    :return: 证书的相关信息 <class 'dict'>
    """
    cert = OpenSSL.crypto.load_certificate(OpenSSL.crypto.FILETYPE_PEM, open(f_path).read())
    cert_info = dict()
    cert_info["version"] = cert.get_version() + 1
    cert_info["serial_number"] = hex(cert.get_serial_number())
    cert_info["signature_algorithm"] = cert.get_signature_algorithm().decode("UTF-8")
    cert_info["common_name"] = cert.get_issuer().commonName
    cert_info["has_expired"] = cert.has_expired()
    cert_info["pub_extent"] = cert.get_pubkey().bits()
    cert_info["components"] = cert.get_issuer().get_components()
    cert_info["extension_count"] = cert.get_extension_count()
    cert_info["start_timestamp"] = get_timestamp(cert.get_notBefore().decode("UTF-8"), z)
    cert_info["expire_timestamp"] = get_timestamp(cert.get_notAfter().decode("UTF-8"), z)
    c_dict = dict()
    for item in  cert_info["components"]:
        c_dict[item[0].decode("utf-8")] = item[1].decode("utf-8")
    cert_info["components"] = c_dict
    return cert_info

def signed_certificate():
    cert_info = dict()
    cert_info["ca"] = dict()
    cert_info["ca"]["serial_number"] = "0x292825060443b581fe5e105be7c306a4cxxx0bf3"
    cert_info["credential_info"] = certificate_information()
    cert_info["cert"] = dict()
    cert_info["cert"]["certificate_data"] = open(os.path.join(__BASE_DIR, "cert_base64")).read()
    cert_info["cert"]["key_data"] = open(os.path.join(__BASE_DIR, "cert_base64")).read()
    return cert_info

# 配置时区，需要和运行环境的时区保持一致

if __name__ == '__main__':
    # 设置x509证书路径
    f = os.path.join(__BASE_DIR, "ca.pem")
    ca_info = certificate_information(f, "+0800")
    print(ca_info)
    aa = signed_certificate()
    print(aa)


