#!/usr/local/bin/python3

# Have a look at the sequence, do an estimate of the A+T content visually: maybe somewhere around 50% (0.5) or so?
# We need to store the information we need - the A and T count, and the length of the DNA sequence
my_dna = "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"
length = len(my_dna)
a_count = my_dna.count('A')
t_count = my_dna.count('T')

# We can print these out to check that they look OK
print("length: " + str(length))
print("A count: " + str(a_count))
print("T count: " + str(t_count))

# Now let's try the calculation
at_content = (a_count + t_count) / length
print("A+T content is " + str(at_content))

# converted to percentage, as requested
print("A+T content is",str(int(100*at_content)),"percent")

