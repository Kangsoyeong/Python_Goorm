foreign = '외래어'
print('%s 표기법' %foreign)

print('제1장 표기의 기본 원칙')
#print('제%항 외래어는 국어의 현용 %d 자모 만으로 적는다.' %(1,24))

num=1
print('제%d항 외래어는 국어의 현용 %d 자모 만으로 적는다.' %(num, 24))

one = 1
#print('제%d항 %s의 1 음운은 원칙적으로 1 기호로 적는다.' %(num+1, foreign))
#print('제%d항 %s의 %d 음운은 원칙적으로 %d 기호로 적는다.' %(num+1, foreign, one, one))
#print('제{0}항 {1}의 {2} 음운은 원칙적으로 {2} 기호로 적는다.' .format(num+1, foreign, one))
print(f'제{num+1}항 {foreign}의 {one} 음운은 원칙적으로 {one} 기호로 적는다.')

print(f'제{num+2}항 받침에는 \'ㄱ, ㄴ, ㄹ, ㅁ, ㅂ, ㅅ, ㅇ\'만을 쓴다.')

print(f'제{num+3}항 파열음 표기에는 된소리를 쓰지 않는 것을 원칙으로 한다.')

print('제{five}항 이미 굳어진 {0}는 관용을 존중하되, 그 범위와 용례는 따로 정한다.'.format(foreign, five=5))

rules ="""외래어 표기법
제1장 표기의 기본 원칙
제1항 외래어는 국어의 현용 24 자모 만으로 적는다.
제2항 외래어의 1 음운은 원칙적으로 1 기호로 적는다.
제3항 받침에는 'ㄱ, ㄴ, ㄹ, ㅁ, ㅂ, ㅅ, ㅇ'만을 쓴다.
제4항 파열음 표기에는 된소리를 쓰지 않는 것을 원칙으로 한다.
제5항 이미 굳어진 외래어는 관용을 존중하되, 그 범위와 용례는 따로 정한다."""

print(rules.count('외래어'))
print(rules.find('외래어'))
print(rules.index('외래어'))
print(rules.find('한국어'))
#print(rules.index('한국어'))

print(rules.replace('외래어','한국어'))