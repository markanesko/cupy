import numpy as np
import cupy as cp

def run():

    x_gpu = cp.array( [1, 2, 3] )

    print('x = ', x_gpu)

def main():

    run()

    return 0

main()