from os.path import split

# m = "ABCDEFG"
# musicinfos = ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]
# "HELLO" 가 출력되어야 합니다.

m = "ABC#$"
musicinfos = ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]
# "WORLD" 가 출력되어야 합니다.

def solution(m, musicinfos):
    answer = ''

    for i in musicinfos:
        info = i.split(',') # ['12:00', '12:14', 'HELLO', 'CDEFGAB']
        music_time = get_play_time(info[0], info[1])
        music = ''
        count = 0
        while count < music_time + 1:
            music_index = count % len(info[3])
            music += info[3][music_index]
            count += 1

        replaced_music = replace_step(music)
        replaced_m = replace_step(m)

        print(replaced_music)
        print(replaced_m)

        if replaced_m in replaced_music:
            answer = info[2]
            break
    else:
        return None
    return answer

def get_play_time(start, end):
    sh, sm = map(int, start.split(':'))
    eh, em = map(int, end.split(':'))
    return (eh * 60 + em) - (sh * 60 + sm)

def replace_step(m):
    return m.replace('C#', 'c').replace('D#', 'd').replace('F#', 'f').replace('G#', 'g').replace('A#', 'a')


print("정답 = 'WORLD' / 현재 풀이 값 = ", solution(m, musicinfos))
