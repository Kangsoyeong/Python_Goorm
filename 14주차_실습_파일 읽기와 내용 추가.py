f = open('data/meerkat.txt', 'r')

while True:
    data = f.readline()
    if not data:
        break
    elif '서식지' in data:
        print(data)

f.close()