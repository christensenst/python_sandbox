"producer and consumer threads communicating with a shared queue"

import thread, time
from Queue import Queue, Empty

numconsumers = 2  # how many consumers to start
numproducers = 4  # how many producers to start
nummessages = 4   # messages per producer to put

safeprint = thread.allocate_lock()   # else prints may overlap
data_queue = Queue()                 # shared global, infinite size

def producer(idnum):
    for msgnum in range(nummessages):
        time.sleep(idnum)
        data_queue.put('[producer id={}, count={}'.format(idnum, msgnum))
        
def consumer(idnum):
    while True:
        time.sleep(0.1)
        try:
            data = data_queue.get(block=False)
        except Empty:
            pass
        else:
            with safeprint:
                print 'consumer {} got => {}'.format(idnum, data)
                
if __name__ == '__main__':
    for i in range(numconsumers):
        thread.start_new_thread(consumer, (i,))
    for i in range(numproducers):
        thread.start_new_thread(producer, (i,))
    time.sleep(((numproducers - 1) * nummessages) + 1)
    print 'Main thread exit.'

