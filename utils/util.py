import inspect
import json
import socket
import sys


def is_empty(obj):
    """  判断数据是否为空 """
    if isinstance(obj, str):
        if obj is None or len(obj) <= 0 or obj.strip() == '':
            return True

    elif isinstance(obj, set) or isinstance(obj, dict) or isinstance(obj, list):
        if obj is None or len(obj) <= 0 or bool(obj) or not any(obj):
            return True
    else:
        if obj or obj is None:
            return True
    return False


def not_empty(obj):
    """  判断数据是否不为空 """
    return not is_empty(obj)


def get_kw_list(keywords):
    """ 获取类中所有方法 """
    func_list = []
    for m in keywords.__all__:
        _class = getattr(keywords, m)
        for name, value in inspect.getmembers(_class):
            if not name.startswith("_"):
                func_list.append(name)
    return func_list


def print_class(obj):
    """ 打印类中的属性和值 """
    print('\n'.join(['%s:%s' % item for item in obj.__dict__.items()]))
    print("===========================================================\r\n\r\n")


def check_version():
    v = sys.version_info
    if v.major == 3 and v.minor >= 5:
        return
    print('你当前安装的Python是%d.%d.%d，请使用Python3.6及以上版本' % (v.major, v.minor, v.micro))
    exit(1)


def decode(s):
    try:
        return s.decode('utf-8')
    # except AttributeError:
    #     return s.encode('utf-8')
    except UnicodeDecodeError:
        return s.decode('gbk')


def get_host_ip():
    """
    查询本机ip地址
    :return: ip
    """
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    finally:
        s.close()

    return ip


def get_remote_ip(host_name):
    """ 获取指定域名IP地址 """
    try:
        return socket.gethostbyname(host_name)
    except BaseException as e:
        print(" %s:%s" % (host_name, e))


# 将字典转成字符串
def dict2str(d):
    s = ''
    for i in d:
        val = ''
        if d[i] is not None:
            val = d[i]
        s = s + i + ': ' + val + '\r\n'
    return s


def check_json(input_str):
    try:
        json.loads(input_str)
        return True
    except BaseException as e:
        print(e)
        return False
