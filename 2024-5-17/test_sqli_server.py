from flask import Flask, request
from flask_mysqldb import MySQL

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


@app.route('/')
def home():
    return 'Welcome to the SQL Injection Test Environment!'


@app.route('/search')
def search():
    user_input = request.args.get('id')
    cursor = mysql.connection.cursor()
    query = f"SELECT * FROM users WHERE id = '{user_input}'"  # 故意构建的 SQL 注入漏洞
    cursor.execute(query)
    results = cursor.fetchall()
    cursor.close()
    return str(results)


if __name__ == '__main__':
    app.run(debug=True)
