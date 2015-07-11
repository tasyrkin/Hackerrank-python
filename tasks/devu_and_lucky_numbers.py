__author__ = 'tim'
import shlex

tokenizer = shlex.shlex(posix=True)
tokenizer.whitespace_split=True

x = int(tokenizer.get_token())
y = int(tokenizer.get_token())
z = int(tokenizer.get_token())
MOD = 1000000007

sum = [[[0 for _ in range(z+1)] for _ in range(y+1)] for _ in range(x+1)]
cnt = [[[0 for _ in range(z+1)] for _ in range(y+1)] for _ in range(x+1)]

tenth = [1 for _ in range(x+y+z+1)]
tenth[0] = 1
for idx in range(1, x+y+z+1):
    tenth[idx] = (10*tenth[idx-1])%MOD

if x > 0:
    cnt[1][0][0] = 1
    sum[1][0][0] = 0
if y > 0:
    cnt[0][1][0] = 1
    sum[0][1][0] = 0
if z > 0:
    cnt[0][0][1] = 1
    sum[0][0][1] = 0

for xi in range(x+1):
    for yi in range(y+1):
        for zi in range(z+1):
            if xi>0:
                cnt[xi][yi][zi] = (cnt[xi][yi][zi] + cnt[xi-1][yi][zi]) % MOD
                prev = (4*tenth[xi+yi+zi-1]) % MOD
                prev = (prev * (1 if cnt[xi-1][yi][zi] == 0 else cnt[xi-1][yi][zi])) % MOD
                prev = (prev + sum[xi-1][yi][zi]) % MOD
                sum[xi][yi][zi] = (sum[xi][yi][zi]+prev) % MOD
            if yi>0:
                cnt[xi][yi][zi] = (cnt[xi][yi][zi] + cnt[xi][yi-1][zi]) % MOD
                prev = (5*tenth[xi+yi+zi-1]) % MOD
                prev = (prev * (1 if cnt[xi][yi-1][zi] == 0 else cnt[xi][yi-1][zi])) % MOD
                prev = (prev + sum[xi][yi-1][zi]) % MOD
                sum[xi][yi][zi] = (sum[xi][yi][zi]+prev) % MOD
            if zi>0:
                cnt[xi][yi][zi] = (cnt[xi][yi][zi] + cnt[xi][yi][zi-1]) % MOD
                prev = (6*tenth[xi+yi+zi-1]) % MOD
                prev = (prev * (1 if cnt[xi][yi][zi-1] == 0 else cnt[xi][yi][zi-1])) % MOD
                prev = (prev + sum[xi][yi][zi-1]) % MOD
                sum[xi][yi][zi] = (sum[xi][yi][zi]+prev) % MOD

res = 0
for xi in range(x+1):
    for yi in range(y+1):
        for zi in range(z+1):
            res = (res + sum[xi][yi][zi]) % MOD

print res