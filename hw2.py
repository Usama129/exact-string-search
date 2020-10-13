import argparse
import exact
import time

parser = argparse.ArgumentParser(description='*** Exact String Matching ***')
requiredNamed = parser.add_argument_group('required named arguments')

requiredNamed.add_argument('-i', '--input', help='Input file name, containing text in FASTA format',
                           required=True)
requiredNamed.add_argument('-p', '--pattern', help='Pattern file name, containing pattern in FASTA format',
                           required=True)

args = parser.parse_args()

with open(args.input, 'r') as i:
    arr = i.read().splitlines()

arr.pop(0)
T = ''
T = T.join(arr)

with open(args.pattern, 'r') as p:
    brr = p.read().splitlines()

brr.pop(0)
P = ''
P = P.join(brr)

before = 0
after = 0
while (before == after):
    before = time.time()
    print(exact.brute_force(P, T))
    after = time.time()
print(before)
print(after)
print((after-before)*1000,"ms")