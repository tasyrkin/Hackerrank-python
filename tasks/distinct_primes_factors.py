# Enter your code here. Read input from STDIN. Print output to STDOUT
import fileinput

def check_fact(n, facts):
	count = 0
	while n > 1:
		count += 1
		if count > 1000000:
			print 'cant be factorized :/', n, facts
		for div in facts:
			if n % div == 0:
				n /= div

for line in fileinput.input():
	nums = map(lambda x: int(x), line.split())
	N = nums[0]
	K = nums[1]
	M = N+K+10
	fact = list([set() for _ in range(M)])
	fact[0].add(0)
	fact[1].add(1)
	for num in range(2, M):
		if len(fact[num]) == 0 and num * num <= M:
			for j in range(num*num, M, num):
				fact[j].add(num)
				#if num*num < j:
				#	break
	cnt = 0
	for num in range(2, N+K):
		if len(fact[num]) == 0:
			fact[num].add(num)
		new_set = set(fact[num])
		for div in fact[num]:
			if div == 0:
				continue
			idx = num / div
			if idx != 1:
				new_set.update(fact[idx])
			fact[num] = new_set
		if len(fact[num]) == K:
			cnt += 1
			if cnt == K:
				print num-K+1
				cnt -= 1
		else:
			cnt = 0
