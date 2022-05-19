import time

bar = [
    " [=     ]",
    " [ =    ]",
    " [  =   ]",
    " [   =  ]",
    " [    = ]",
    " [     =]",
    " [    = ]",
    " [   =  ]",
    " [  =   ]",
    " [ =    ]",
]
num = 0

while True:
    u = num % len(bar)

    print(bar[u], end="\r")
    print(f" this is u: {u}", end="\r")

    time.sleep(.2)

    num += 1
