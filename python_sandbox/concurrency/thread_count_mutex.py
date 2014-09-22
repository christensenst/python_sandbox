# The print statements are synchronized with thread locks so that no 2 threads will ever execute a print call
# at the same point in time - each print statement is on its own line as expected.

import thread, time

def counter(myId, count):                          # function run in threads
    for i in range(count):
        time.sleep(1)                              # simulate real work
        mutex.acquire()
        print "[{0}] => {1}".format(myId, i)
        mutex.release()

def thread_count_mutex():
    for i in range(5):                             # spawn 5 threads
        thread.start_new_thread(counter, (i, 5))   # each thread loops 5 times
    time.sleep(6)
    print "Main thread exiting."                   # don't exit too early
    
mutex = thread.allocate_lock()                 # make a global lock object

if __name__ == "__main__":
    thread_count_mutex()