# This code run on integrated terminal
import chai
f = open('chai.py')

print(f.readline())
print(f.readline())
print(f.readline())
print(f.readline())
print(f.readline()) # ''

f = open('chai.py')
print(f.__next__())
print(f.__next__())
print(f.__next__())
print(f.__next__())
print(f.__next__()) # Exception StopIteration


for line in open('chai.py'):
    print(line)

for line in open('chai.py'):
    print(line, end="")

f = open('chai.py')
while True:
    line = f.readline()
    if not line: break # not line means nothing inside the line 
    # line will be break because line have empty string
    print(line, end='')
