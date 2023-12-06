# Discrete_Logarithm
Useful algorithms to compute discrete logarithm

In mathematics, for given real numbers a and b, the logarithm log_b(a) is a number x such that b^x = a. Analogously, in any group G, powers b^k can be defined for all integers k, and the discrete logarithm log_b(a) is an integer k such that b^k = a. 

This logarithm is quite important in cryptography for if a "fast" (linear) algorithm were found, most encryption system would have to be rebuilt differently.

In this repository, one can find the implementation of various methods to compute the discrete logarithm of an element in Z/(pZ)*.
This includes brute-force, Baby-Giant steps and Pohlig-Hellman reduction.

The efficiency of those methods is compared using the measure function. 
