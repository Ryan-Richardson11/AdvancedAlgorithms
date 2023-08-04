import random

class Queue:

    def __init__(self):
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

while True:
    probRemove = int(input("Enter the probability of a dequeue (%): "))
    if probRemove <= 34 or probRemove >= 67:
        print("Value must at least 34 and no more than 67")
    else:
        cheap, costly = 0, 0
        for i in range(100000):
            if (random.randrange(100) < probRemove):
                Q.dequeue()
                costly += 1
            else:
                Q.enqueue(random.randint(0, 10))
                cheap += 1
        break
    
print(f"Probability of dequeue {probRemove}%, probability of enqueue {100 - probRemove}%")
print(f"Costly: {costly:7} ({costly/(costly + cheap):3.1}%)")
print(f"Cheap: {cheap:7} ({cheap/(costly + cheap):3.1}%)")