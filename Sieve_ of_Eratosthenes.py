import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

M = int(1e6) + 1

composite = [0 for i in xrange(int(M))]

def sieve():
	for i in xrange(2, M):
		cnt = 2
		while cnt*i < M:
			composite[cnt*i] = 1
			cnt += 1

if __name__ == '__main__':
	print composite[2]
	print composite[5]
	print composite[6]
	print composite[12]