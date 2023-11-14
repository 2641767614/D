import os
import pytz
from datetime import datetime

# 从环境变量中获取时区值，默认为 'Asia/Shanghai'
timezone = os.environ.get('TZ', 'Asia/Shanghai')

# 设置当前时区
os.environ['TZ'] = timezone
pytz.timezone(timezone).localize(datetime.now())

import shutil
from pathlib import Path

import yunzai_nonebot

root = Path(__file__).absolute().parent
config_path = root / "config.yaml"

if not config_path.exists():
    shutil.copy(root / "config_default.yaml", config_path)

yunzai_nonebot.init(Path(__file__).absolute().parent / "config.yaml")

for plugin in set(filter(lambda x: x, yunzai_nonebot.get_driver().config.plugins)):
    yunzai_nonebot.load_plugin(plugin.replace("-", "_"))

yunzai_nonebot.run()
