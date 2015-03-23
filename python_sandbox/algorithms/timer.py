"""
Homegrown timing tools for function calls
Does total time, best-of-time, and best-of-totals time
"""

import time, sys
timer = time.clock if sys.platform[:3] == 'win' else time.time

def total(reps, func, *args, **kwargs):
    """
    Total time to run func() reps times.
    Returns (total time, last result)
    """
    reps_list = list(range(reps))
    start = timer()
    for i in reps_list:
        ret = func(*args, **kwargs)
    elapsed = timer() - start
    return (elapsed, ret)