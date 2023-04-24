h = input('Hours of work: ')
hrs = float(h)
sph = float(input('Rate for the hour: '))
if hrs <= 40:
    sf = sph*hrs
elif hrs > 40:
    sf = (sph*40) + (hrs-40)*1.5*sph
print(f'{sf}')