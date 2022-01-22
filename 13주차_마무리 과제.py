# 순수익 : Last-a(초기비용)
# a=투자한 액수(초기비용), b=투자한 날짜 수
a = int(input('투자 액수를 입력하세요: '))
b = int(input('투자한 날짜 수를 입력하세요: '))

total = 10000
total = a

if 100<=a and a<=10000 and 1<=b and b<=10:
	for i in range(1, b+1):
		change = int(input('%d일차 변동 데이터를 입력하세요: '%i))
		for j in range(i, i+1):
			total += total*(change/100)

gain = total - a
print('%d'%gain)

if gain > 0:
	print('이득입니다.')
elif gain == 0:
	print('본전입니다.')
else:
	print('손해입니다.')