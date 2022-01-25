movies = ["Dark Knight", "Harry Porter", "Parasite", "Matrix", "La La Land"]

print()
print("===========영화 목록===========")
for i in movies:
    print(i)
print("==============================")

choice = input('예매하실 영화를 선택해주세요: ')

while choice not in movies:
    print("예매할 수 없는 영화입니다")
    choice = input('예매하실 영화를 선택해주세요: ')

print('%s를 선택하셨습니다' % (choice))

check = False

while (not (check)):

    people = int(input('관람 인원 수를 입력해주세요: '))
    if people <= 0:
        print("관람 인원 수는 양수만 가능합니다")
    else:
        check = True
print("관람할 인원 수는 %d명입니다" % people)

coupon_dic = {'WELCOME': 2000, 'VALENTINE': 3000, 'CHRISTMAS': 4000, 'INDEPENDENCE': 5000}
process = True

usage = input('할인권을 사용하시려면 y, 금액 확인으로 넘어가시려면 n을 입력해주세요: ')

while process:
    if usage == 'y':
        coupon = input('쿠폰 번호를 입력해주세요: ')
        if coupon in coupon_dic:
            sale = coupon_dic.get(coupon)
            print("%d원 할인됩니다" % sale)
            del (coupon_dic[coupon])
            process = False
        else:
            print('존재하지 않는 할인권입니다')
            usage = input('할인권을 다시 입력하려면 y, 아니면 n을 입력해주세요: ')
    elif usage == 'n':
        sale = 0
        print('할인권을 사용하지 않았습니다')
        process = False
    else:
        usage = input('잘못된 입력입니다. 다시 입력해주세요: ')
        process = False

origin_price = people * 12000
sale_price = sale * people
total_price = origin_price - sale_price

print("")
print("<예매 상세 내역>")
print("==============================")
print('영화 제목: %s' % choice)
print('관람 인원: %d명' % people)
print('합산 금액: %d원' % origin_price)
print('할인 금액: %d원' % sale_price)
print("------------------------------")
print('실 결제액: %d원' % total_price)
print("==============================")