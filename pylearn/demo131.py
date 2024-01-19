# editor 百年
# date: 2024/1/19 15:11
import schedule
import time
# 定义函数
def job():
    print('哈哈---')

# 调用schedule模块每三秒执行一次函数job
schedule.every(3).seconds.do(job)
while True:
    schedule.run_pending()
    # 执行一次后休息1s
    time.sleep(1)