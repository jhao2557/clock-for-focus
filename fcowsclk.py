import time

minutes = int(input("请输入专注时间（单位：分钟）： "))
seconds = minutes * 60

while seconds:
    mins, secs = divmod(seconds, 60)
    timer = '{:02d}:{:02d}'.format(mins, secs)
    print(timer, end="\r")
    time.sleep(1)
    seconds -= 1

print("恭喜你，专注完成！")
