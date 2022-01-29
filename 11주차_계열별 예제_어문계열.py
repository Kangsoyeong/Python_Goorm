finder = True
history = []
index = -1

while finder:
    what = input('어떤 작업을 진행하시겠습니까? 끝내길 원하신다면 \'종료\'를 입력하세요: ')

    if what == '종료':
        print('종료합니다')
        finder = False
    elif what == '기록':
        time = input('시기: ')
        data1 = input('문학적 경향: ')
        data2 = input('대표 작가: ')
        data3 = input('소설명: ')

        history.append([time, data1, data2, data3])
        index += 1
        print(history)

    elif what == '추출':
        if index < 0:
            print('정보가 없습니다')
        else:
            print(
                f'{history[0][0]}의 문학적 경향은 {history[0][1]}입니다. 이 시기 대표 작가 {history[0][2]}은(는) {history[0][3]} 소설을 집필했습니다.')
            history.remove(history[0])
            index -= 1

    else:
        print('잘못된 입력입니다')