# Explanation for each problem

## Problem-A: Evaluating Fully Parenthesized Expression
Keyword: Data Structure, Recursion

Example: (1+(23\*345))

If () is replaced to [] and each element is separated by commna, this fomula
can be represented by Python's list.  
[1, '+', [23, '\*', 345 ] ]

As you can see, each list has up to 3 elements, we can assume that

1. If the list has 1 element, it's nemeric value
2. If the list has 2 elements, 1st one is sign('+' or '-'), 2nd is numeric
3. If the list has 3 elements, 1st and 3rd are numeric, and 2nd is operator ('+','-','\*','/')

 
In order to create and solve the nested list(list in list), **Recursion** is effective technique.
Following is the overall sequence to convert and evaluate data.

1. Convert String to flat list of Tokens
         ['(','1','+','(','23','*','345',')',')']
2. Convert the flat list to nested list, each list has up to 3 element
         [1.0,'+', [23.0,'*',345.0] ]
3. Evaluate the nested list


**In case of Python, *eval()* function can evaluate fomula, so just call it :-)**


## Problem-B: The Election
(ordinary algorithm is not yet impemented)

Keyword: Data Structure, Big number, 1000000007

If Python is allowed to solve this problem, it's not so difficult. Python can handle Unlimited integer.  

In other langueage, limitation of each data type is as foloows.

- 32bit signed integer: +- 2\*10^9
- 64bit signed integer: +- 4\*10^18
- 64bit float(double): precision 15-16 digit, 10^308

x(L+N)' can be up to  10^6 * (10^9 ^(10^5)), => 10^90006.
In this problem, it's necessary to answer not only modulo but also the result of comparison.  
One of the solution for this, is to have Double(Float) and Integer data for x(L+N)', Float data for rough size, Integer data for Modulo.  
Because Float data can be overflown at 10^308, it's necessary to divide it if it become more than specific number (for example 2^64), and save the divided count.  
**(NOTE)** 
Actually, above method is not enough, if the 2 comparison data are very near(total number of digits and first 16 digits are same), the answer may not be correct.
In order to reply acculate answer in any condition, handling unlimited integer may be necessary.
But it's very difficult to make such a test data. May be using float is an expected  answer for this question.

Code in *C* is something like this.  

```
struct _gain {
    int divided_count ; // number of time gain_real exceed 2**100
    double gain_real ;
    long gain_mod ;    // modulo of 10**9+7
} ;


struct _gain gain ;

// gain = tc.x_i[voter-1] * (m[3] ** (voter - m[1]))
// if gain > best_gain and gain > tc.x_i[voter-1]:

    gain.divided_count = 0
    gain.gain_mod = tc.x_i[voter-1]
    gain.gain_real = (double)tc.x_i[voter-1]

    for (i=0; i< voter-m[1]; i++) {
        gain.gain_mod = (gain_mod * m[3]) % BIG_PRIME_NUMBER ;
        gain.gain_real = gain_real * m[3] ;
        if gain_real > N2_64 {
            gain.divided_count ++ ;
            gain_real /= N2_64 ;
        }
    }

    if gain.divided_count > best... ||
       gain.divided_count == best.. && gain.gain_real > best....
```

## Problem-C: Finding the Determinant
Keyword: Recursion

It looks like that **A(n) = m\*A(n-1) - A(n-2)** (if n > 2)  
This is a varietion of Fibonacci sequence. Recursive program is a easy solution. One of the potential problem of resursive program is stack overflow. In this case, maximum number of n is 9, no problem.

```
A(1) = m (?)
A(2) = m 1  => m^2 - 1
       1 m
A(3) = m 1 0  => m*A(2) - 1* 1 1 + 0* 1 m ==> m*A(2) - m
       1 m 1                 0 m      0 1
       0 1 m
A(4) = m 1 0 0 => m*A(3) - 1* 1 1 0 +0-0 => m*A(3)-(1*A(2)-0) ==> m*A(3) - A(2)
       1 m 1 0                0 m 1
       0 1 m 1                0 1 m
       0 0 1 m
A(5) = m*A(4) - A(3)
```

## Problem-D: Bakery Delivery Scheduler
Keyword: Test case

This is the easiest problem in this ICPC contest. The basic logic is as follows.

1. Find the Max and Min location of delivery
2. Compare them with the starting location
3. Go nearer first, if the starting location is between Max and Min and Min is nearer, total distance is (starting_location - Min) * 2 + (Max - Starting location)

**It is necessary to care the situation that the Starting location is bigger then Max or smaller than Min.**


## Problem-E: Tree Pendant
Keyword: Data structure, Class, Recursion

Proper data structure is the key to simplify this kind of problem. Though, the probelm is not so difficult, but this problem requires relatively large code. It takes long time to code and debug.
It's practical to set low priority for this kind of problems in the contest.


## Problem-F: Chocolates
Keyword: Mathmatics, Fibonacci, Data structure

May be this is the most difficult problem.

- If number of chocolate type is 1 and number of people is more than 1, the answer is "NONE"
- If all of the weight are same, number of the **combination** can be calculated by mathmatical rule of **Combination with repetition** (nHr = (n+r-1)Cr)
- If number of chocolate type is 2, number of the **combination** can be calculated with LCM (Least Common Multiple) 
- If number of chocolate type is more than 2, counting **combination** seems to be very complex

- If we do not count **combination** but **permutation**, the variation of Fibonacci sequence can be applied. Simple example of this type of problem is as follows
    1. There are 5 step of stairs, and you are on the top of it
    2. You can do down 1 or 2 steps
    3. How many **permutations** exist ?

The answer to this question is 8
```
F(0)=1 :---
F(1)=1 :1
F(2)=2 :1-1, 2
F(3)=3 :1-1-1, 1-2, 2-1
F(4)=5 :1-1-1-1, 1-1-2, 1-2-1, 2-1-1, 2-2
F(5)=8 :1-1-1-1-1, 1-1-1-2, 1-1-2-1, 1-2-1-1, 2-1-1-1, 1-2-2, 2-1-2, 2-2-1
```

In order to go 3rd step, move 1 step from 2nd or move 2 step from 1st. So F(n) = F(n-1)+ F(n-2).


So how can we count **combination** instead of **permutation** by changing above algorithm?
If we can count *Sorted* sequence in the **permutation**, it's same as **combination**.
Let's assign the ID to each chocolate type (A,B,C,D,E), and prepare counters for last added chocolate type. So that we count xxx-C-C-D, but not xxx-C-D-C.


## Problem-G: Vampire Number
Keyword: Performance

It seems to be that there is not good algorithm to solve Vampire number effectively. Basically, we need to solve this problem with *brute force*, but there are some ideas to reduce the volume of calculation.

```
   for (n=U; n<=U; n++) {
       for (div=1; div<n; div++) {
           if (n % div == 0) {
              check_vampire(n,div)
              ...
   }
```

1. *C* code of most simple algorithm is like above. The O-notation of this algorithm is *O(n^2)*.
2. We can improbe that by changing the range of div, if n is 8 digit, we need to check from 1000 to 9999. O-notation is *O(nLog n)*
3. If n can be divided by A, n=A\*B, we just need to check A<=B condition, so the range of div is 1000 to sqrt(n) for 8 digit n. O-notation is also *O(nLog n)*, but better than method-2.
4. Another elegant algorithm is to use permutation. The number of calculation is 8P8=8!=40320 for 8 digit n. Unfortunately it's more than method-3. Also it's not easy to create permutaion pattern in *C*. Python has *itertools*, it's easy to do this.


## Problem-H: Like Father Like Son
Keyword: Data Structure

There are several ways to check the similarity of polygons. One of the easy way is to compare the list of the vector of coordinates after normalization.

For each Fathers,

1. Calculate the length of edges of the polygon
2. Move the min(x,y) of polygon to (0,0) and divide each coodinates by the length of the longest edge
3. Make rotation and reverse pattern

For each Sons,

1. Calculate the length of edges of the polygon
2. Move the min(x,y) of polygon to (0,0) and divide each coodinates by the length of the longest edge
3. If the list of vector matchs one of the Fathers, he is his Father


## Problem-I: Clustering
Keyword: Data Structure, Recursion

This is a typical problem of recursion.
Using *Class* will improve the readability of this kind of program.

I defined **CellData** class, whose instance represent each *Cell* (0 or 1 in test data). CellData class has a class variable *CellData.matrix*, which is a 2-dementional array of CellData instances.
Each CellData instance has following instance variables.

- self.r: (row number)
- self.c: (column number)
- self.val (0 or 1)
- self.cluster (if val==0 None, val==1 Cluster Number)
- self.neibour = (list of 8 adjacent CellData instance)

After the intialization, following loop will solve this problem. cell.set_cluster() will call set_cluster() of neibour cell.

```
    num_cluster = 0
    for r in range(tc.row):
        for c in range(tc.col):
            cell = CellData.matrix[r][c]
            if cell.val == 1 and cell.cluster == None:
                num_cluster += 1
                cell.set_cluster(num_cluster)
    print(num_cluster)
```


## Problem-J: Green Frog and Ordering
Keyword: Problem reading, Recursion

This problem statement is a little bit ambiguous. If it's not possible to move from 0 to 0, some problem can not be solved. For example (2, 1).  

Sample input and output shows big hint to solve this problem. Last movement shall be smallest number and 2nd smallest must be 2 or more bigger than smallest and already sorted except smallest element. If we remove smallest element, we can perform same logic to 2nd smallest.
So this problem can be solved by removing smallest element 1 by 1.

Though, this program is not resursive, the idea of recursion exists behind above algorithm. (Think from last movement to 1st movement)


## Problem-K: One Time Pad
Keyword: Test case

This is a easy problem. Take care of negative and big number of test case.


## Problem-L: Password for Sweethearts
Keyword: Data structure

The combination of Merging 2 strings can be calculated by Pemutaion with repetition. If the length of the 2 strings is *a* and *b*, it's 2^(*a+b*). It's same as binary number of length (*a+b*). If the number of '0' is *a*, it's valid.  
As for checking duplicate, making list is easy solution. One of the concern is data size. In this case, maximum name length is 5, so up to 2^10=1024 need to be cared. No problem.

If the number of people is 3. Use *Tenary* instead of *Binary*.
