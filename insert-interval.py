def insert_intervals(intervals, new_interval):
	if not intervals:
		return []
	
	if not new_interval:
		return intervals
	
	n = new_interval
	res = []

	for i in range(len(intervals)):
		curr = intervals[i]
		if n.end < curr.start:  # no overlap
			res.append(curr)
		elif n.start < curr.end:    
			if n.end < curr.start:  # Safe to add just just before curr since end is way before curr.
				res.append(n)     
				return res += intervals[i:]     # Just append everything after.
			n.start = min(n.start, curr.start)   # Overlap. So, just take min of start's of overlaps and max of end's of overlap.
			n.end = max(n.end, curr.end)         # but, don't append anyway. Just override the current `n` new_interval so that it gets merge in next iteration if need be.
	res.append(n)           # Append last remaining carried over all overrides.

	return res
  
