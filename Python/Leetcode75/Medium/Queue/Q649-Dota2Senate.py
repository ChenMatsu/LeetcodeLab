from collections import deque

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n = len(senate)
        r_queue = deque()
        d_queue = deque()

        for i, s in enumerate(senate):
            if s == 'R':
                r_queue.append(i)
            else:
                d_queue.append(i)

        while r_queue and d_queue:
            r_idx = r_queue.popleft()
            d_idx = d_queue.popleft()

            if r_idx < d_idx:
                r_queue.append(r_idx + n)
            else:
                d_queue.append(d_idx + n)
        
        return 'Radient' if r_queue else 'Dire'