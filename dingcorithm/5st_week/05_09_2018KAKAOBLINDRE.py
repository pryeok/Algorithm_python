from datetime import datetime, timedelta


lines = [
    "2016-09-15 20:59:57.421 0.351s",
    "2016-09-15 20:59:58.233 1.181s",
    "2016-09-15 20:59:58.299 0.8s",
    "2016-09-15 20:59:58.688 1.041s",
    "2016-09-15 20:59:59.591 1.412s",
    "2016-09-15 21:00:00.464 1.466s",
    "2016-09-15 21:00:00.741 1.581s",
    "2016-09-15 21:00:00.748 2.31s",
    "2016-09-15 21:00:00.966 0.381s",
    "2016-09-15 21:00:02.066 2.62s"
]
# 7 이 출력되어야 합니다.

# 01:00:02.003 ~ 01:00:04.002에서 2초 동안 처리
# 연월일, (시작)시, 분, 초, (끝)시, 분, 초
#

def solution(lines):
    answer = 0

    traffic_dict = {}
    start_time = 0
    end_time = 0

    for line in lines:
        traffic_times = line.split(" ")


        print(traffic_times)
        print(traffic_times[1])
        print(traffic_times[2])


        end_time = float(traffic_times[1].split(":")[2])

        different_time = traffic_times[2].replace("s", "")
        start_time = end_time - float(different_time)

        print("start_time :: ", int(start_time))
        print("end_time :: ", int(end_time))

        count = int(start_time) - int(end_time)

        dt = datetime.strptime(traffic_times[0] + " " + traffic_times[1], "%Y-%m-%d %H:%M:%S")
        dt_plus_1sec = dt + timedelta(seconds=1)
        print(dt_plus_1sec)
        print(dt)

        # traffic_dict[]


        # print(traffic_times[0] + " " + traffic_times[1])


    return answer


print("정답 = '7' / 현재 풀이 값 = ", solution(lines))