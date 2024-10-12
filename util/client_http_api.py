from fastapi import FastAPI

import util.client_shortcut_handler
import time

from util.client_cosmic import Cosmic, console
from config import ClientConfig as Config

app=FastAPI()

@app.get('/api/start_record')
def start_record():
    util.client_shortcut_handler.launch_task()

    return "ok"

@app.get('/api/stop_record')
def stop_record():
    # 记录持续时间，并标识录音线程停止向队列放数据
    duration = time.time() - Cosmic.on

    # 取消或停止任务
    if duration < Config.threshold:
        util.client_shortcut_handler.cancel_task()
    else:
        util.client_shortcut_handler.finish_task()

    return "ok"

@app.get('/api/heartbeat')
def heartbeat():
    return "ok"

def run_service():
    print('api 已启动...')
    import uvicorn
    uvicorn.run(app,port=Config.api_port)

