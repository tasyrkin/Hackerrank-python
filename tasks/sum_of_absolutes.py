__author__ = 'tim'

import shlex

tokenizer = shlex.shlex(posix=True)
tokenizer.whitespace_split=True

n = int(tokenizer.get_token())
q = int(tokenizer.get_token())

nums = [0]*n
agg = [None]*n
for idx in range(n):
    num = int(tokenizer.get_token())
    nums[idx] = num
    agg_odd = agg[idx-1] if idx > 0 else 0
    agg[idx] = agg_odd + (1 if num%2==1 else 0)

for _ in range(q):
    left = int(tokenizer.get_token())-1
    right = int(tokenizer.get_token())-1
    odds_left = agg[left-1] if left > 0 else 0
    odds_right = agg[right]
    odds = odds_right - odds_left
    print 'Odd' if odds%2==1 else 'Even'