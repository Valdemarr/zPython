currentLastPoint = 0
fig, ax = plt.subplots()
while currentLastPoint < len(x):
    currentLastPoint += 1
    plt.plot(x[0], y[0])
    plt.plot([], [])
    for i in range(0, currentLastPoint):
        plt.plot(x[i], y[i], 'o')
    time.sleep(1)
    plt.show()
