import requests
from time import time

filenames = ["{}-2.mp3".format(i + 1) for i in range(131)]
url = "http://anglaiscpge.fr/_Media/"

for target in filenames:
    beg = time()
    r = requests.get(url + target)

    with open(target, 'ab') as file:
        file.write(r.content)

    r.close()
    end = time()

    print("{} DOWNLOADED WITH SUCCES IN {} SEC".format(target, round(end - beg, 3)))
