def computepay(h, r):
    if h <= 40: 
        d = h*r
        return d
    elif h > 40:
        d = 40*r + (h-40)*(r*1.5)
        return d
hrs = input("Enter Hours:")
rph = input("Rate per hour: ")
h = float(hrs)
r = float(rph)
p = computepay(h, r)
print("Pay", p)