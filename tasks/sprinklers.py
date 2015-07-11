__author__ = 'tim'

#wrong solution :(

import shlex
import bisect

tokenizer = shlex.shlex(posix=True)
tokenizer.whitespace_split=True

T = int(tokenizer.get_token())

while T > 0:
    T -= 1

    N = int(tokenizer.get_token())
    M = int(tokenizer.get_token())
    S = int(tokenizer.get_token())
    Q = int(tokenizer.get_token())

    vacant = [0 for _ in range(M)]
    all_vacant = set()

    max_gap = 0

    for idx in range(M):
        vacant[idx] = int(tokenizer.get_token()) - 1
        all_vacant.add(vacant[idx])
        if idx > 0:
            if max_gap < vacant[idx] - vacant[idx-1] - 1:
                max_gap = vacant[idx] - vacant[idx-1] - 1

    left_items = vacant[0]
    right_items = N - vacant[-1] - 1

    min_price = 1<<64
    selected_I = -1
    selected_sprinkles = -1

    for I in range(N):
        roses_covered = 2*I + 1
        curr_sprlinkles = N/roses_covered + (1 if N%roses_covered>0 else 0)
        curr_price = I*Q + curr_sprlinkles*S
        if left_items <= I and right_items <= I and max_gap <= 2 * I and curr_sprlinkles <= M:
            ok = curr_sprlinkles != 1 or (I in all_vacant or (N-I-1) in all_vacant)
            if ok and min_price > curr_price:
                min_price = curr_price
                selected_I = I
                selected_sprinkles = curr_sprlinkles

    print selected_sprinkles, selected_I
    chosen_positions = []
    prev_position = -1
    for curr_sprinkle in range(selected_sprinkles):
        diff = selected_I if curr_sprinkle == 0 else 2 * selected_I
        curr_position = prev_position + diff + 1
        found_index = bisect.bisect_left(vacant, curr_position)
        if vacant[found_index] != curr_position:
            found_index = found_index - 1
        chosen_positions.append(vacant[found_index]+1)
        prev_position = vacant[found_index]
    print ' '.join([str(i) for i in chosen_positions])

