from collections import Counter
import matplotlib.pyplot as plt


frutas = Counter(manzana=20, pera=15, sandia=19, platano=15).most_common()

x, y = zip(*frutas)

plt.bar(x, y)

plt.show()
