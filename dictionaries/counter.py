from collections import Counter


ct = Counter('abracadabra')

print(ct)

ct.update('aaaaazzz')

print(ct.most_common(3))
