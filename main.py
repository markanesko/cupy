import numpy as np
import cupy as cp

def run():

    x_gpu = cp.array( [1, 2, 3] )
    euclidean_norm = cp.linalg.norm(x_gpu)

    print('euclidean_norm = ', euclidean_norm)

def main():

    run()

    return 0

main()