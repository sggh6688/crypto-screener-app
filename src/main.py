# 导入部分
import os
import sys
from flask import Flask, render_template, jsonify, request

# 数据目录设置
DATA_DIR = os.environ.get("DATA_DIR", os.path.join(os.path.dirname(os.path.dirname(__file__)), "crypto_data"))
REPORTS_DIR = os.environ.get("REPORTS_DIR", os.path.join(os.path.dirname(os.path.dirname(__file__)), "crypto_reports"))

# 确保目录存在
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)
if not os.path.exists(REPORTS_DIR):
    os.makedirs(REPORTS_DIR)

# 创建Flask应用实例 - 这一行是解决问题的关键！
app = Flask(__name__)

# 添加一个简单的首页路由
@app.route('/')
def index():
    return render_template('index.html')

# 这里可以添加您原有的其他路由和功能代码
# ...

# 主函数
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)), debug=False)
