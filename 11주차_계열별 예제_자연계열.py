finder = True
experiment = []
index = -1

while finder:
    what = input('어떤 작업을 진행하시겠습니까? 끝내길 원하신다면 \'종료\'를 입력하세요: ')

    if what == '종료':
        print('종료합니다')
        finder = False
    elif what == '기록':
        data1 = input('시약 영문: ')
        data2 = input('시약 국문: ')
        data3 = input('시약 용량: ')

        index += 1
        experiment.append([index + 1, data1, data2, data3])
        print(experiment)

    elif what == '추출':
        if index < 0:
            print('정보가 없습니다')
        else:
            print(f'{experiment[0][0]}번 순서에서 사용된 시약은 {experiment[0][1]}({experiment[0][2]}){experiment[0][3]}입니다.')
            experiment.remove(experiment[0])
            index -= 1
    else:
        print('잘못된 입력입니다')