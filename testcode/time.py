import time

ticks = int(time.time())
print('当前时间戳： ', ticks)

new_ticks = str(ticks).replace('.', '')
print(new_ticks)
