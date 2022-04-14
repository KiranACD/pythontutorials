from operator import le
import random

class RandomIntegers:

    def __init__(self, length, *, seed = 0, lower = 0, upper = 10):
        self.length = length
        self.seed = seed
        self.lower = lower
        self.upper = upper

    def __len__(self):
        return self.length
    
    def __iter__(self):
        return self.RandomIntegersIterator(self.length, seed = self.seed,
                                                        lower = self.lower,
                                                        upper = self.upper)

    class RandomIntegersIterator:

        def __init__(self, length, *, seed, lower, upper):
            self.length = length
            self.lower = lower
            self.upper = upper
            random.seed(seed)
            self.num_requested = 0

        def __iter__(self):
            return self
        
        def __next__(self):

            if self.num_requested >= self.length:
                raise StopIteration
            else:
                result = random.randint(self.lower, self.upper)
                self.num_requested += 1
                return result

if __name__ == '__main__':

    randoms = RandomIntegers(10)
    for num in randoms:
        print(num, end = ', ')
    
    # We will get the same numbers as before because we are default setting seed to 0.
    print()
    for num in randoms:
        print(num, end = ', ')

    print()

    print(sorted(randoms))
    