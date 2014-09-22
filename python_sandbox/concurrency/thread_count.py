import thread, time

def counter(myId, count):                          # function run in threads
    for i in range(count):
        time.sleep(1)                              # simulate real work
        print "[{0}] => {1}".format(myId, i)

def thread_count():
    for i in range(5):                             # spawn 5 threads
        thread.start_new_thread(counter, (i, 5))   # each thread loops 5 times
    time.sleep(6)
    print "Main thread exiting."                   # don't exit too early

if __name__ == "__main__":
    thread_count()
