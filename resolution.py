resx = int(input('Resolution X: '))
resy = int(input('Resolution Y: '))
div = int(input('division: '))
mul = int(input('multiplication: '))

step = resx / div

step0 = resy / div

step1 = step * mul

step2 = step0 * mul

print(step1)
print(step2)
