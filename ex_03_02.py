sh = input("Enter Hours: ")
sr = input("Enter Rate: ")
fh = float(sh)
fr = float(sr)
# print(fh, fr)
if fh > 40:
    # print("Overtime")
    reg = fr * fh
    otp = (fh - 40.0) * (fr * 1.5)
    # print('Base', reg, 'Overtime', otp)
    print('Pay', reg + otp)
else:
    # print('Regular')
    xp = fh * fr
    print("Pay:", xp)