# flask_demo

## 如何在生产环境中运行 flask

安装 gunicorn

```
pip install gunicorn
```

```bash
gunicorn -w 4 run:app
```

其中 `run` 代表 `run.py`，`app` 代表 Flask 实例，-w 4 表示 4 个工作进程。

### 端口怎么改变

要在使用 Gunicorn 运行你的 Flask 应用时更改端口，你可以使用 `-b` 或 `--bind` 参数来指定 IP 地址和端口号。默认情况下，Gunicorn 会在 8000 端口上监听。如果你想要更改为其他端口，比如 5000，你可以这样做：

```sh
gunicorn -w 4 -b 127.0.0.1:5000 run:app
```

这里的 `127.0.0.1:5000` 告诉 Gunicorn 在本地计算机上的 5000 端口上监听请求。

如果你想要让你的应用可以从任何 IP 地址访问，而不仅仅是 127.0.0.1（本地回环地址），你可以将 IP 部分改为 `0.0.0.0`：

```sh
gunicorn -w 4 -b 0.0.0.0:5000 run:app
```

使用 `0.0.0.0` 将允许你的应用接收发往所有服务器 IP 地址的请求，这通常用于生产部署。但是，请注意，在生产环境中，你可能还需要配置其他的安全和性能相关的设置。

## flask shell

```
export FLASK_APP=app:create_app('development')
```

## migrate 用法

1. 定义好数据模型
2. `flask db init`
3. `flask db migrate`
4. `flask db upgrade`
