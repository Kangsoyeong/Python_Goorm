year = int(input())

if year%4 == 0 and year%100 != 0:
	print(f'연도를 입력하세요: {year}년은 윤년입니다.')
elif year%400 == 0:
	print(f'연도를 입력하세요: {year}년은 윤년입니다.')
else:
	print(f'연도를 입력하세요: {year}년은 윤년이 아닙니다.')