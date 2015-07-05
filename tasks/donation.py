# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

def binary_search(arr, lo, hi, to_find):
	while lo <= hi:
		mid = lo + (hi-lo)/2
		if arr[mid] < to_find:
			lo = mid+1
		elif arr[mid] > to_find:
			hi = mid-1
		else:
			return mid
	return -lo-1

data_raw = sys.stdin.readlines()

dp = list([0])
cnt = 0
while dp[cnt] <= 10000000000000000:
	cnt += 1
	dp.append(dp[cnt-1] + (cnt*cnt))

T = int(data_raw[0])

data = map(lambda x: int(x), data_raw[1:T+1])

for candies in data:
	idx = binary_search(dp, 0, len(dp)-1, candies)
	if idx > 0:
		print idx
	else:
		print abs(idx)-1-1
