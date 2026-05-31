import threading 
import time

def fun(seconds):
    print(f"Sleeping for {seconds} seconds")
    time.sleep(seconds)

# fun(4)
# fun(2)
# fun(1)

t1 = threading.Thread(target=fun, args=[4])
t2 = threading.Thread(target=fun, args=[2])
t3 = threading.Thread(target=fun, args=[1])

t1.start()
t2.start()
t3.start()