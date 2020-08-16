from datetime import datetime
import time
now = datetime.now()
print(now)
# print('{:.2f}  {:.3f}  {:.4f}'.format(now.month,now.day,now.year))
print('{:02d}  {:03d}  {:04d}'.format(now.month,now.day,now.year))
print(time.localtime(time.time()))
print(time.strftime('%Y-%m-%d',time.localtime(time.time())))
print(time.strftime('%Y/%m/%d',time.localtime(time.time())))
print(time.strftime('%Y-%m-%d-%H-%M-%S-%W',time.localtime(time.time())))
print(time.strftime('%H:%M:%S',time.localtime(time.time())))