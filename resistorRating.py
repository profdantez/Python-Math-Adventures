# Python implementation to find the
# resistance of the resistor with
# the given color codes

# Function to find the resistance
# using color codes
def findResistance(a, b, c, d, e):
	
	# Hash-map to store the values
	# of the color-digits
	color_digit = {'black': '0',
				'brown': '1',
				'red': '2',
				'orange': '3',
				'yellow': '4',
				'green' : '5',
				'blue' : '6',
				'violet' : '7',
				'grey' : '8',
				'white': '9'}
	
	multiplier = {'black': '1',
				'brown': '10',
				'red': '100',
				'orange': '1k',
				'yellow': '10k',
				'green' : '100k',
				'blue' : '1M',
				'violet' : '10M',
				'grey' : '100M',
				'white': '1G'}
	
	tolerance = {'brown': '+/- 1 %',
				'red' : '+/- 2 %',
				'green': "+/- 0.5 %",
				'blue': '+/- 0.25 %',
				'violet' : '+/- 0.1 %',
				'gold': '+/- 5 %',
				'silver' : '+/- 10 %',
				'none': '+/-20 %'}
	
	if a in color_digit and b in color_digit and c in color_digit and d in multiplier and e in tolerance:
			xx = color_digit.get(a)
			yy = color_digit.get(b)
			zz = color_digit.get(c)
			aa = multiplier.get(d)
			bb = tolerance.get(e)
			print("Resistance = "+xx + yy\
				+ zz+" x "+aa+" ohms "+bb)
	else:
		print("Invalid Colors")
		
# Driver Code
if __name__ == "__main__":
	a = "red"
	b = "orange"
	c = "yellow"
	d = "green"
	e = "gold"
	f = 'black'
	
	# Function Call
	findResistance(a, b, c, d, e)
