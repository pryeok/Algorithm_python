

genres = ["classic", "pop", "classic", "classic", "pop"] # 노래의 장르
plays = [500, 600, 150, 800, 2500]


def get_melon_best_album(genre_array, play_array): # 노래별 재생 횟수

    result = []

    genre_dict = {}

    for i in range(len(genre_array)):
        genre = genre_array[i]
        play = play_array[i]

        if genre not in genre_dict:
            genre_dict[genre] = []  # 리스트로 초기화

        genre_dict[genre].append((i, play))  # (인덱스, 재생 수) 형태로 저장
        # {'classic': [(0, 500), (2, 150), (3, 800)], 'pop': [(1, 600), (4, 2500)]}


    return genre_dict


print("정답 = [4, 1, 3, 0] / 현재 풀이 값 = ", get_melon_best_album(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))
# print("정답 = [0, 6, 5, 2, 4, 1] / 현재 풀이 값 = ", get_melon_best_album(["hiphop", "classic", "pop", "classic", "classic", "pop", "hiphop"], [2000, 500, 600, 150, 800, 2500, 2000]))