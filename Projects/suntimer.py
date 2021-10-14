import time as t

t1 = 10
t2 = 5

current = t1

while True:
    for i in range(current):
        print(i+1)
        t.sleep(1)

    if current == t1:
        current = t2
        print("\nTime's up, get into the shadow!\n---\n")
    elif current == t2:
        current = t1
        print("\nTime's up, get back out in the sun!\n---\n")
