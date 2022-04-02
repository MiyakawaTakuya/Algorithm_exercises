# 日付や時刻の値への加算・減算と値の比較 https://www.javadrive.jp/python/date/index8.html#section1
# ループを逆順で回す方法  https://www.python.ambitious-engineer.com/archives/1757
from datetime import datetime

a, b, c = map(int, input().split())
b_c = b + c
timetable = []
limit_time = datetime.combine(
    datetime.date.today(), datetime.time(8, 59, 00))
board_time = limit_time - datetime.timedelta(minutes=b_c)
N = int(input())
for i in range(N):
    h, m = map(int, input().split())
    departure = datetime.combine(
        datetime.date.today(), datetime.time(h, m, 00))
    timetable.append(departure)
# 8:59分までに到着できる最も遅い乗車時刻を算出する 配列を後ろから回す
for i in reversed(timetable):
    if board_time >= i:
        answer = i - datetime.timedelta(minutes=a)
        print(answer.strftime('%H:%M'))  # 出力
        break
