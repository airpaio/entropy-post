import os

# run a /dev/random blocking command
count = 0
while True:
    read_random = os.system('head -c 32 /dev/random | base64 >> rchars.txt')
    count += 1
    with open('count.txt', 'w') as f:
        f.write(str(count))
