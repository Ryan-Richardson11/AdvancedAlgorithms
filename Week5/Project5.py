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
    

Q = Queue()
cheap, costly = 0, 0
logical = len(Q.a_in)
memory = logical
while True:
    probRemove = int(input("Enter the probability of a dequeue (%): "))
    if probRemove <= 34 or probRemove >= 67:
        print("Value must at least 34 and no more than 67")
    else:
        for i in range(100000):
            if (random.randrange(100) < probRemove):
                if logical > 0:
                    Q.dequeue()
                    costly += 1
            else:
                if logical > memory: 
                    Q.enqueue(random.randint(0, 10))
                    logical += 1
                    cheap += 1
                else:
                    Q.enqueue(random.randint(0, 10))
                    memory *= 2
                    logical += 1
                    costly +=1
        break
print(f"Probability of dequeue {probRemove}%, probability of enqueue {100 - probRemove}%")