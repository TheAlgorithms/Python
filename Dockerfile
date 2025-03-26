# 使用轻量级基础镜像
FROM alpine:latest

# 安装必要工具（如 shell 和 ls 命令）
RUN apk add --no-cache bash coreutils

# 将仓库内容复制到 /app 目录
COPY . /app

# 设置工作目录
WORKDIR /app

# 默认启动命令：打印欢迎信息和 /app 目录内容
CMD ["bash", "-c", "echo 'Hello from Docker image' && ls -la /app"]
