# 使用官方 Python 3.10 镜像
FROM python:3.10

# 设置工作目录
WORKDIR /app

COPY . .

# 安装 requirements-server.txt 中的依赖
RUN pip install --no-cache-dir -r requirements-server.txt -i https://mirror.sjtu.edu.cn/pypi/web/simple

# 给 core_server.py 脚本执行权限
RUN chmod +x core_server.py

# 暴露端口 6016
EXPOSE 6016

# 容器启动时运行 run.sh 脚本
CMD ["python", "./core_server.py"]