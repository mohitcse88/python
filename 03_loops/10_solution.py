# 10. Exponential Backoff
# Problem: Implement an exponential backoff strategy that doubles the wait time between retries, starting from 1 second, but stops after 5 retries.

import time 

wait_time = 1 # time in second 
max_retries = 5 
attempt = 0 

while attempt < max_retries:
    print("Attempt", attempt+1, " -wait time ",wait_time)
    time.sleep(wait_time)
    wait_time *= 2 #doubles the wait time
    attempt += 1