def dist(v, mu):                    	# suppose reaction time is 1
    v = v * 1000 / 60 / 60
    return ((v*v) / (2*mu*9.81)) + v

def speed(d, mu):           			# suppose reaction time is 1
    v = (mu*mu*9.81*9.81 + 2*mu*9.81*d)**0.5 - mu*9.81
    return v / 1000 * 60 * 60

print(speed(159, 0.8))