score = float(input("Enter Score: "))
if 0.0 < score < 1.0:
    if 1.0 < score <= 0.9:
        print('A')
    elif 0.9 > score >= 0.8:
        print('B')
    elif 0.8 > score >= 0.7:
        print('C')
    elif 0.7 > score >= 0.6:
        print('D')
    elif 0.6 > score:
        print('F')
else:
    score = float((input('error, ')))
