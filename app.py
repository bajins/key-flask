from flask import Flask
# 模板模块
from flask import render_template
# json数据转换模块
from flask import jsonify
# request模块
from flask import request
import xshellkey as xshellkey  # 导入包下的模块并取别名
from xshellkey import generate_key  # 指定导入包下的函数

app = Flask(__name__)


# 自定义静态文件目录
# app = Flask(__name__ ,static_folder='/tmp')


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def hello_world():
    return render_template('index.html')


@app.route('/getKey', methods=['POST'])
def get_key():
    # 判断是否是post请求
    if request.method != 'POST':
        return jsonify({'code': 401, 'msg': "请求方式错误"})

    # 这种获取参数方式如果参数不存在不会抛异常
    product = request.form.get('app')
    if product.strip() == '':
        return jsonify({'code': 300, 'msg': "请选择产品"})
    # 这种获取参数方式如果参数不存在会抛异常
    version = request.form['version']
    if version.strip() == '':
        return jsonify({'code': 300, 'msg': "请选择版本"})

    # key = xshellkey.generateKey(app, version)
    key = generate_key(product, version)
    # 返回给用户  模版中使用到的users就是这里传递进去的
    return jsonify({'code': 200, 'msg': "请求成功", 'key': key})


if __name__ == '__main__':
    app.debug = True
    app.run()
