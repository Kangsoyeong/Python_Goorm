year = int(input())
month = int(input())
date = int(input())
day = input()


print(f"오늘은 {year}년 {month}월 {date}일 {day}입니다.")
print("오늘은 %d년 %d월 %d일 %s입니다." %(year, month, date, day))
print("오늘은 {0}년 {1}월 {2}일 {3}입니다.".format(year, month, date, day))