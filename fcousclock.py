import time

def start_focus_timer(duration):
    start_time = time.time()
    end_time = start_time + duration * 60

    while True:
        remaining_time = end_time - time.time()
        if remaining_time <= 0:
            print("时间到！")
            break

        minutes = int(remaining_time // 60)
        seconds = int(remaining_time % 60)

        print(f"剩余时间：{minutes:02d}:{seconds:02d}", end="\r")
        time.sleep(1)

# 设置专注时长为25分钟
focus_duration = 25
start_focus_timer(focus_duration)
