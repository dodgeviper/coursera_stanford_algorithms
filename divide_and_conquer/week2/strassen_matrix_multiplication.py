"""
Strassen's algorithm: Subcubic Matrix multiplication algorithm

Simple matrix multiplication:
[a b   * [e f  = [ae + bg  af + bh
 c d]     g h]    ce + dg  cf + dh]
This algorithm is O(n^3)

Now Divide and conquer paradigm
1. Divide into smaller problems
2. Conquer problems recursively
3. Combine solutions from the subproblems.

Application of divide and conquer:
Idea:
Instead of dividing matrix into left half and right half. we divide the matrix
into quadrants so we will get 4 n/2*n/2 matrices.

Recursive Algorithm #1:
Step1: recursively compute the 8 necessary products.
Step2: do the necessary additions in O(n^2) time
Fact: runtime is O(n^3) same as the simple multiplication.

Can we reduce the recursive calls from 8 to some number...
this is where Strassen's algorithm.
Step1: recursively compute only 7.
Step2: do the necessary clever additions.
Fact: runtime is better than cubic time

The details:
X = (A B
     C D)
Y = (E F
     O H)

The 7 products:
P1 = A(F - H),
P2 = (A + B)H,
P3 = (C + D)E
P4 = D(C-E)
P5 = (A+D)(E+H)
P6 = (B-D)(C+H)
P7 = (A-C)(E+F)

CLAIM:
X * Y = (P5 + P4 -P2 +P6  P1 + P2
         P3+P4   P1+P5-P3-P7)
You can check
P5 + P4 -P2 +P6 = AE + BG
"""
