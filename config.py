# * coding:utf-8 *
# Author:sisul
#创建时间：2020/4/6 21:03


import os

ROOT_PATH = os.path.dirname(os.path.abspath(__file__))

LOG_IMG = os.path.join(ROOT_PATH, 'log_img')

if os.path.exists(LOG_IMG):
    pass
else:
    os.mkdir(LOG_IMG)
