from threading import Thread,Semaphore
import time
import random
# a queue from which the producer will produce and the consumer
# will consume the data
queue = []
# maximum limit of the queues
MAX_NUM = 10
# initializing semaphores
sem = Semaphore()

class ProducerThread(Thread):
    def run(self):
        nums = range(5)
        global queue

        while True:
            sem.acquire() # wait operation to stop
            # consuming
            if len(queue) == MAX_NUM:
                print('List is full, producer will wait')
                #signal operation only when the queue is full and
                #allow the consumer to consume data
                sem.release()
                print('space in queue, Consumer notified the producer')
            
            num = random.choice(nums)
            # added any random number from 0 to 4 to the list
            queue.append(num)
            print('Produced',num)
            # signal operation to allow the consumer to consume data
            sem.release()
            # to allow the program to run bit slower
            time.sleep(random.random())

class ConsumerThread(Thread):
    def run(self):
        global queue

        while True:
            # wait for the operation to stop producing
            sem.acquire()
            if not queue:
                print('The list is empty,consumer waiting')
                # signal operation only when the queue is empty and
                # allow the producer to produce data
                sem.release()
                print('The producer added something to the queue and notified the consumer')
            num = queue.pop(0)
            print('Consumed',num)
            # signal operation to allow the producer to produce
            sem.release()
            time.sleep(random.random())
