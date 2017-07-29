def make_averager():
	series = []

	def averager(new_value):
		series.append(new_value)
		total = sum(series)
		return total/len(series)

	return averager

avg = make_averager()
avg(10)