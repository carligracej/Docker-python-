def hi(name):
    print('Hi ' + name + '!')

girls = ['Rachel', 'Monica', 'Phoebe', 'Ola', 'You']
for name in girls:
    hi(name)
    print('Next girl')
sortednames = []
print girls
girls.sort()
print girls
s = sorted (girls,
        key = lambda a: len (a))
print s