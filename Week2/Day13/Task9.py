import time
class Timer:
    def __enter__(self):
        self.start = time.perf_counter()
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end = time.perf_counter()
        self.elapsed = self.end - self.start
        print(f"Time takes {self.elapsed:.6f} seconds")
    
with Timer():
    sum((i**2 for i in range(1,1000000)))