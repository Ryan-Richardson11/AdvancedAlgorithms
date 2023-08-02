import random

class Queue:

    def __inti__(self):
        self.a_in = []
        self.a_out = []

    def enqueue(self, d):
        self.a_in.append(d)

    def dequeue(self):
        if (self.a_out == []):
            for d in self.a_in:
                self.a_out.append(d)
            self.a_in = []
        return self.a_out.pop(0)
    
    def generate_array(self, n):
        arr = []
        for i in range(n):
            arr.append(random.randint(0, 100))
        return arr


Q = Queue()
while True:
    probRemove = int(input("Enter the probability of a dequeue (%): "))
    if probRemove <= 34 or probRemove >= 67:
        print("Value must at least 34 and no more than 67")
        cheap, costly = 0, 0
        for i in range(100000):
            if (random.randrange(100) < probRemove):
