# Enter your code here. Read input from STDIN. Print output to STDOUT
import fileinput
import time
curr_ms = lambda: int(round(time.time() * 1000))

M = 10000000000

def fast_pow(num, power):
	result = long(1)
	while power > 0:
		if power%2 == 1:
			#result = (result * num) % M
			result = result * num
		num = (num * num) % M
		power >>= 1
	return result%M

for line in fileinput.input():
	start = curr_ms()
	N = int(line)
	result = long(1)
	pows = list([-1 for _ in range(N+1)])
	print 'init list:' + str(curr_ms() - start)
	pows[1] = 1
	for num in range(2, N+1):
		if pows[num] == -1:
			pows[num] = fast_pow(num, num)
			#new_num = num*num
			#new_pow = num
			#new_step = 2
			#while new_num <= N:
				#pows[new_num] = fast_pow(pows[num], new_step*new_pow)
				#new_num *= num
				#new_pow *= num
				#new_step += 1
			result = result + pows[num]
			#print 'num ' + str(num) + ':' + str(curr_ms() - start)
		#print 'num:' + str(num) + ' pows:' + str(pows)
	print 'final' + ':' + str(curr_ms() - start)
	print result%M
