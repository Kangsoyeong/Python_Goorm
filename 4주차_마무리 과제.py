num=1
law = ("""대한민국 헌법
제{one}장 총강
제{one}조
\t{one}. 대한민국은 민주공화국이다.
\t{two}. 대한민국의 주권은 \'국민\'에게 있고, 모든 권력은 \'국민\'으로부터 나온다.
제{two}조
\t{one}. 대한민국의 \'국민\'이 되는 요건은 법률로 정한다.
\t{two}. 국가는 법률이 정하는 바에 의하여 재외\'국민\'을 보호할 의무를 진다.
제{three}조
\t{one}. 대한민국의 영토는 한반도와 그 부속도서로 한다.""".format(one=1, two=2, three=3))

print(law)
print(law.count('법률'))
print(law.find('주권'))
print(law.replace('대한민국', '한국'))