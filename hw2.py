import argparse
from bruteforce import brute_force
from kmp import knuth_morris_pratt
from rabinkarp import rabin_karp
from timeit import default_timer as timer

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


print("Running brute-force...")
start = timer()
pos, comp = brute_force(P, T)
bruteforce = timer() - start
if pos == -1:
    print("Could not find pattern in text")
else:
    print("Found pattern at position", pos+1) # adding 1 to pos because function returns 0-based index
print("Runtime was",round(bruteforce*1000000),"microseconds. Performed",comp,"character comparisons")

print("\nRunning Knuth-Morris-Pratt...")
start = timer()
pos,comp = knuth_morris_pratt(T, P)
kmp = timer() - start
if pos == -1:
    print("Could not find pattern in text")
else:
    print("Found pattern at position", pos+1)
print("Runtime was",round(kmp*1000000),"microseconds. Performed",comp,"character comparisons")

print("\nRunning Rabin-Karp...")
start = timer()
pos, comp = rabin_karp(T, P)
rk = timer() - start
if pos == -1:
    print("Could not find pattern in text")
else:
    print("Found pattern at position", pos+1)
print("Runtime was",round(rk*1000000),"microseconds. Performed",comp,"character comparisons")


if kmp < bruteforce and kmp < rk:
    print("\nKnuth-Morris-Pratt performed best")
elif bruteforce < kmp and bruteforce < rk:
    print("\nBrute-force performed best")
else:
    print("\nRabin-Karp performed best")