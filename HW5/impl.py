class Queue(object):
    def __init__(self):   # default no-arg constructor
        self.queue_list = []

    def enqueue(self, v):  # adds v to the back of the queue; no return value
        if v == float('inf') or v == float('-inf') or v != v or v is None:
            raise ValueError
        else:
            self.queue_list.append(v)

    def dequeue(self):    # removes and returns the element at the front of the queue
        if len(self.queue_list) == 0:
            return None
        else:
            return self.queue_list.pop(0)

    def len(self):     # returns the number of elements in the queue
        return len(self.queue_list)


"""q = Queue()
# x = [-57901, -209804601999361120768121972779977630, 8.430359835112085e-304]
x = ['']
if len(x) > 0:
    y = x[0]
    for n in x:
        q.enqueue(n)
    z = q.dequeue()
    print(y)
    print(y == z)

q.enqueue(None)"""