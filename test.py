from BloomFilter import BloomFilter

bf = BloomFilter(3)
bf.fit(['hello', 'world', 'duck'])

print(bf.contains('hello'))
print(bf.contains('hjdngid'))
print(bf.contains('world'))
print(bf.contains('worlвd'))

bf.save('test.filter')


print('---------')
zc = BloomFilter.load('test.filter')
print(zc.contains('hello'))
print(zc.contains('hjdngid'))
print(zc.contains('world'))
print(zc.contains('worlвd'))