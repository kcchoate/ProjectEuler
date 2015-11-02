def collatz(n):#simply returns the next item in the chain
    if n % 2 == 0:
        return int (n/2)
    else:
        return 3*n + 1

max_chain_length = 1
chain_length = 1
n = 1
answer = 1

for i in range(1,1000000):#iterate through each possible number, saving the longest chain and it's source.
    n = i
    while (n != 1):#assumes that the Collatz problem will always reduce to 1
        n = collatz(n)
        chain_length += 1
    if max_chain_length < chain_length:
        max_chain_length = chain_length
        answer = i
    chain_length = 1

print (answer)