# Enter your code here. Read input from STDIN. Print output to STDOUTimport sys
import sys
import time
curr_ms = lambda: int(round(time.time() * 1000))

data_raw = sys.stdin.readlines()
T = int(data_raw[0])

data = map(lambda x: map(lambda y: long(y), x.split()), data_raw[1:T+1])

#print data

def fast_pow(num, power):
	result = 1
	while power > 0:
		if power % 2 == 1:
			result = (result * num) % 100
		num = (num * num) % 100
		power >>= 1
	return result

start = curr_ms()
result_str = ''
for arr in data:
	K = arr[0]
	N = arr[1]
	repeat = K / 100
	repeat_res = 0
	if repeat > 0:
		repeat_res = 1
		for val in range(2, 100):
			repeat_res = (repeat_res + fast_pow(val, N))
		repeat_res = long(K / 100) * repeat_res
	rest = K % 100
	rest_res = 0
	if rest > 0:
		rest_res = 1
		for val in range(2, rest+1):
			rest_res = (rest_res + fast_pow(val, N))
	result = (repeat_res + rest_res) % 100
	#print ('0'+str(result)) if result < 10 else str(result)
	result_str += str((str('0')+str(result)) if result < 10 else str(result)) + str('\n')
print result_str
print curr_ms() - start
