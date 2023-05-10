import time
start_time = time.time()

for a in range(0, 501):
    for b in range(0, 501):
        c = 500 - a - b
        if a**2 + b**2 == c**2 and a + b + c == 500:
            print("a, b, c: %d, %d, %d" % (a, b, c))

print("time elapsed: {:.2f}s".format(time.time() - start_time))