# 在文件顶部添加这些导入
import os
import sys
from flask import Flask, render_template, jsonify, request
# 修改数据目录路径，使用环境变量或默认值
DATA_DIR = os.environ.get("DATA_DIR", os.path.join(os.path.dirname(os.path.dirname(__file__)), "crypto_data"))
REPORTS_DIR = os.environ.get("REPORTS_DIR", os.path.join(os.path.dirname(os.path.dirname(__file__)), "crypto_reports"))

# 确保目录存在
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)
if not os.path.exists(REPORTS_DIR):
    os.makedirs(REPORTS_DIR)
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)), debug=False)
