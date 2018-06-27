# _*_ coding:UTF-8 _*_

if __name__ == '__main__':
    import time
    start = time.clock()
    starttime = time.time()
    print("start"+str(start))
    print("starttime" + str(starttime))
    for i in range(1000):
        print(i)
    end = time.clock()
    print("end" + str(end))
    print("different is %6.3f" %(end - start))