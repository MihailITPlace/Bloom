import os

from BloomFilter import BloomFilter


print("Введите слово")
query = input()

path = 'filters_en/'

filters = os.listdir(path)

с = 0

for i in filters:
    bf = BloomFilter.load(path + i)
    if bf.contains(query):
        с += 1
        print(i)

print('Поиск завершён')
print(с / len(filters))