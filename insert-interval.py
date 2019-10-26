# Based on: https://leetcode.com/problems/insert-interval/discuss/21809/Python-O(n)-and-O(nlgn)-solutions

def insert_intervals(intervals, new_interval):
	if not intervals:
            return [newInterval]

        if not newInterval:
            return intervals
	
	n = new_interval
	res = []

	for i in range(len(intervals)):
		curr = intervals[i]
		if curr[1] < n[0]:  # curr's end is less that n's start. So just append curr and continue
			res.append(curr)
		elif n[1] < curr[0]: # if n's end is less that curr's start. Append n and append rest of the intervals
                res.append(n)
                res.extend(intervals[i:])
                return res
            else:      # If there is overlap between curr and n, override n's min with the min of starts and max of ends.
		       # This helps to carry forward overlaps until no more overlaps are there or reach end of list.
                n[0] = min(n[0], curr[0])
                n[1] = max(n[1], curr[1])
        
        res.append(n)  # If we reach till here means whatever we have accumulated in n needs to added and that is the result.
        
        return res
