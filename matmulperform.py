import numpy as np
import time
import sys
import csv
import matplotlib.pyplot as plt
from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

def matrix_multiplication(n):
    A = np.random.rand(n,n)
    B = np.random.rand(n,n)
    C = np.zeros((n,n))
    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]
    return C

def main():
    if rank == 0:
        n = 2
        while n <= 50:
            start_time = time.time()
            for i in range(100):
                matrix_multiplication(n)
            end_time = time.time()
            time_taken = end_time - start_time
            average_time = time_taken/100
            with open('Seq_exe.csv', 'a') as file:
                writer = csv.writer(file)
                writer.writerow([n, average_time])
            n += 1
    else:
        n = 2
        while n <= 50:
            start_time = time.time()
            for i in range(100):
                matrix_multiplication(n)
            end_time = time.time()
            time_taken = end_time - start_time
            average_time = time_taken/100
            with open('Paral_exe.csv', 'a') as file:
                writer = csv.writer(file)
                writer.writerow([n, average_time])
            n += 1

    #generate a graph of sequential vs parallel execution time where x-axis indicates n = 2 to 50 and the y-axis indicates the corresponding average processing time.
    if rank == 0:
        x = []
        y = []
        with open('Seq_exe.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                x.append(int(row[0]))
                y.append(float(row[1]))
        plt.plot(x, y, label = "Sequential")
        plt.xlabel('n')
        plt.ylabel('Average Processing Time')
        plt.title('Sequential Execution Time')
        plt.legend()
        plt.show()
    else:
        x = []
        y = []
        with open('Paral_exe.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                x.append(int(row[0]))
                y.append(float(row[1]))
        plt.plot(x, y, label = "Parallel")
        plt.xlabel('n')
        plt.ylabel('Average Processing Time')
        plt.title('Parallel Execution Time')
        plt.legend()
        plt.show()

        

if __name__ == '__main__':
    main()




