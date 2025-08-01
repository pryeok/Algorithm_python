

all_students = ["나연", "정연", "모모", "사나", "지효", "미나", "다현", "채영", "쯔위"]
present_students = ["정연", "모모", "채영", "쯔위", "사나", "나연", "미나", "다현"]


# all_students 들을 돌면서, hash table 의 키 값에 해당 학생들을 등록한다.
# present_students 를 돌면서 hash table 의 키값의 값을 제거한다.
# 그리고 나서 남아있는 hash table 의 키 값에 해당하는 학생이 결석한 학생이다.
def get_absent_student(all_array, present_array):

    dict = {}

    for key in all_array:

        dict[key] = True  # 아무 값이나 넣어도 상관 없습니다! 여기서는 키가 중요한거니까요
                          # key = 키 값, True = 밸류 값

    print(dict)
    # {'나연': True, '정연': True, '모모': True, '사나': True, '지효': True, '미나': True, '다현': True, '채영': True, '쯔위': True}

    for key in present_array:  # dict에서 key 를 하나씩 없앱니다
        del dict[key]

    for key in dict.keys():  # key 중에 하나를 바로 반환합니다! 한 명 밖에 없으니 이렇게 해도 괜찮습니다.
        return key

print(get_absent_student(all_students, present_students))

# print("정답 = 예지 / 현재 풀이 값 = ",get_absent_student(["류진","예지","채령","리아","유나"],["리아","류진","채령","유나"]))
# print("정답 = RM / 현재 풀이 값 = ",get_absent_student(["정국","진","뷔","슈가","지민","RM"],["뷔","정국","지민","진","슈가"]))