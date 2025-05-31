# gunicorn.conf.py
bind = "0.0.0.0:10000"  # Render会自动将此端口映射到外部
workers = 2
timeout = 120
