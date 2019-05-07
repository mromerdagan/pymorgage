import numpy

def amortization_lines(initial_amount, rate, nper):
	regular_payment = numpy.pmt(rate, nper, -initial_amount)
	period_beginning = initial_amount
	for i in range(nper):
		interest = period_beginning * rate
		principal = regular_payment - interest
		next_ = period_beginning - principal
		yield (period_beginning, interest, principal, next_)
		period_beginning = next_


