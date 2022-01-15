num = int(input())

if num%2==1 and num>0:
	print(f'입력한 수 {num}는 홀수입니다.')
elif num<=0:
	print('자연수가 아닙니다.')
else:
	print(f'입력한 수 {num}는 짝수입니다.')