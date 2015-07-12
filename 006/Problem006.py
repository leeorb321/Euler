import time
start_time = time.time()

def sum_square_diff(n):
    return (n * (n+1)/2)**2 - (n * (2*n + 1) * (n+1)/6)

print sum_square_diff(100)

print("--- %s seconds ---" % (time.time() - start_time))