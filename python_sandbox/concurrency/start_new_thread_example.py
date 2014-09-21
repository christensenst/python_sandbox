import thread

def child(tid):
    print 'Hello frome thread ' + str(tid)
    
def parent():
    i = 0
    while True:
        i += 1
        # when the called function returns, the thread silently exits
        thread.start_new_thread(child, (i,))
        if raw_input() == 'q': break

if __name__ == "__main__":
    parent()