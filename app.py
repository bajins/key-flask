#!/usr/bin/env python
import sys

from flask import Flask, make_response, send_from_directory
# 模板模块
from flask import render_template
# json数据转换模块
from flask import jsonify
# request模块
from flask import request

from utils import util
from utils.content_type import judge_type
from utils.moba_xterm_Keygen import GenerateLicense, LicenseType
from utils.reg_workshop_keygen import GenLicenseCode
from utils.xshell_key import generate_key  # 指定导入包下的函数

app = Flask(__name__)


# 自定义静态文件目录
# app = Flask(__name__ ,static_folder='/tmp')


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/getKey', methods=['POST'])
def get_key():
    # 判断是否是post请求
    if request.method != 'POST':
        return jsonify({'code': 401, 'msg': "请求方式错误"})

    company = request.form.get('company')
    if util.is_empty(company):
        return jsonify({'code': 300, 'msg': "请选择公司"})
    # 这种获取参数方式如果参数不存在不会抛异常
    product = request.form.get('app')
    if product.strip() == '':
        return jsonify({'code': 300, 'msg': "请选择产品"})
    # 这种获取参数方式如果参数不存在会抛异常
    version = request.form['version']
    if version.strip() == '':
        return jsonify({'code': 300, 'msg': "请选择版本"})

    if company == "netsarang":
        key = generate_key(product, version)

    elif company == "mobatek":
        MajorVersion, MinorVersion = version.split('.')[0:2]
        GenerateLicense(LicenseType.Professional, 1, "woytu", int(MajorVersion), int(MinorVersion))

        # 使用make_response 来构造响应信息
        resp = make_response(send_from_directory("static/public", "Custom.mxtpro", as_attachment=True))  # 响应体数据
        resp.headers['Content-Type'] = judge_type("static/public/Custom.mxtpro")
        # 通过字典的形式添加响应头
        resp.headers["Content-Disposition"] = "attachment; filename={}".format(
            "Custom.mxtpro".encode().decode('latin-1'))

        return resp
    elif company == "torchsoft":
        key = GenLicenseCode("woytu", int(version))
    # 返回给用户  模版中使用到的users就是这里传递进去的
    return jsonify({'code': 200, 'msg': "请求成功", 'key': key})


def argvs():
    if len(sys.argv) < 2:
        return 5000
    # return string.atoi(sys.argv[1])
    return int(sys.argv[1])


if __name__ == '__main__':
    app.run(port=argvs())
    