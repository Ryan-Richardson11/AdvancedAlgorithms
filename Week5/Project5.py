import random

class Queue:

    def __init__(self):
        self.a_in = []
        self.a_out = []
        self.costly = 0
        self.cheap = 0

    def enqueue(self, d):
        self.a_in.append(d)
        self.cheap += 1

    def dequeue(self):
        if (self.a_out == []):
            for d in self.a_in:
                self.a_out.append(d)
            self.a_in = []
            self.costly += 1
        else:
            return self.a_out.pop(0)
    

Q = Queue()

while True:
    probRemove = int(input("Enter the probability of a dequeue (%): "))
    if probRemove <= 34 or probRemove >= 67:
        print("Value must at least 34 and no more than 67")
    else:
        for i in range(100000):
            if (random.randrange(100) < probRemove):
                Q.dequeue()
                
            else:
                Q.enqueue(random.randint(0, 10))

    print(f"Probability of dequeue {probRemove}%, probability of enqueue {100 - probRemove}%")
    print(f"Costly: {Q.costly:7} ({Q.costly/(Q.costly + Q.cheap):3.1}%)")
    print(f"Cheap: {Q.cheap:7} ({Q.cheap/(Q.costly + Q.cheap):3.1}%)")