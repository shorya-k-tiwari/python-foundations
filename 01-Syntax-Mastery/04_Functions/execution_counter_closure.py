"""
Execution Counter using Closures

Tracks how many times a function is executed
"""

def make_counter():
    count = 0
    def counter():
        nonlocal count
        count += 1
        print(f"Action executed {count} time(s)")
    return counter

tracker = make_counter()
tracker()
tracker()
tracker()