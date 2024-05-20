from flask import Flask, request, jsonify, send_from_directory
from flask_mysqldb import MySQL
import os

# from werkzeug.utils import secure_filename

app = Flask(__name__)

#
# CREATE DATABASE test_db;
# USE test_db;

# CREATE TABLE users (
#     id INT AUTO_INCREMENT PRIMARY KEY,
#     name VARCHAR(255) NOT NULL,
#     email VARCHAR(255)
# );
#

# 配置 MySQL 连接
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'test_db'
mysql = MySQL(app)

# 配置文件上传路径
app.config['UPLOAD_FOLDER'] = './help-scripts'


# 首页
@app.route('/')
def home():
    config_data = {
        key: str(value)
        for key, value in app.config.items()
        if not key.startswith('SECRET')
    }
    print(request.host)
    return jsonify(
        code="200",
        msg='Welcome to the Vul Test Environment!',
        # config_data=config_data,
    )


# sql injection
@app.route('/search')
def search():
    user_input = request.args.get('id')
    cursor = mysql.connection.cursor()
    query = f"SELECT * FROM users WHERE id = '{user_input}'"  # 故意构建的 SQL 注入漏洞
    cursor.execute(query)
    results = cursor.fetchall()
    cursor.close()
    return str(results)


# 对应相关网站的上传路径
custom_dir_name = '/files/upload/'


# 任意文件上传
@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify(code="400", msg="没有文件被上传")
    file = request.files['file']
    if file.filename == '':
        return jsonify(code="400", msg="没有选择文件")
    if file:
        # 安全做法
        # filename = secure_filename(file.filename)

        # 使用的原本上传文件名
        filename = file.filename
        save_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(save_path)
        url = f"http://{request.host}{custom_dir_name}{filename}"
        return jsonify(code="200", msg="上传成功", url=url)


# 对应相关网站的访问路径
@app.route(f'{custom_dir_name}<filename>')
def uploaded_file(filename):
    print(os.path.dirname(__file__))
    return send_from_directory(os.path.dirname(__file__), filename)


if __name__ == '__main__':
    app.run(debug=True)
