# Codejam2020
 python implementation of codejam 2020

For interactive problems, execute program locally with : 
```
python (num)_interactive_runner.py python (num)_testing_tool.py (test_case) -- python (num).py
```
or use the google interface

## Qualification Round
Problems can be found at : https://codingcompetitions.withgoogle.com/codejam/round/000000000019fd27

### 1. Vestigium

Straightforward implementation.

### 2. Nesting Depth

Straightforward implementation.

### 3. Parenting Partnering Returns 

Sort the activity array by starting time, then assign the activities to the two people greedily.

### 4. ESAb ATAd (interactive)

For the first ten queries, find the first 5 and the last 5 digits.
Categorize into the 1 of the 2 scenarios below according to the digit result.

1. The staring digits are the reverse of the ending digits, or the staring digits is the reverse of the ending digits complemented
```
ex1 : Staring digits : 10000 Last five digits : 00001
ex2 : Ending digits : 10000 Last five digits : 11110
```
In ex1, there will only be 2 results for 4 different operations : complement == complement and reverse != reverse == no change
In ex2, there will only be 2 results for 4 different operations : complement == reverse != complement and reverse == no change
Denote any position as the anchor position.

2. Otherwise
```
ex1 : Staring digits : 10001 Ending digits : 11000
```
In any of the cases categorized in 2, we can always find at least one series of 4 bits, 2 from the starting digits and 2 from the ending digits in symmetric position, such that the concatenation result of the 4 bits has odd numbers of 0s and 1s. In ex1, we can select the last two from the starting digits and get 01, whose symmetric position will be the first two digits in the ending digits : 11. The concatenated string is 0111, which has odd number of 0s and 1s. Denote the sequence as the anchor sequence, and denote 2 positions from the first (or last) digits that generate this sequence as the anchor position.

After quantum flucuation occured, we only need to check the anchored position(s) to know which type of change occured. In the first case, if any bit changed value, then we assume that the string has gone through the "complement" operation because the others are either equivalent to this operation, or doesn't fit the check result. If any bit remains the same, then the string has not changed. In the second case, we can find the exact operation after checking the new values of the anchor bits. each assignment of a two digit binary value corresponds to a unique change.

We need only at most two checks for every 10 queries, 150 queries can find us a bit string of length 10 + 14 * 8, which is greater than 100. Also note that the starting and ending strings need to be updated and recategorized after every 10 queries if the strings are still in the first category. If the string was recategorized from 1 to 2, apply the second category rules to the string, and find its anchor positions.

### 5. Indicium

Before solving this problem, we need to know some fundemental properties of the trace of Latin squares. Assume we have a latin square of size n. 

1. A Latin square with trace consisting of [k,k,k...k](n entries) can be satisfied
2. A Latin square with trace consisting of [k,k,k...k](n-2 entries) + [x,x] (2 entries) can be satisfied
3. A Latin square with trace consisting of [k,k,k...k](n-2 entries) + [x] (1 entries) + [y] (1 entries) can be satisfied
4. A Latin square with trace consisting of [k,k,k...k](n-1 entries) + [x] (1 entries) can NEVER be satisfied

The simple matrix generation code for case 1, 2, and 3 are as follow :

```python
# Case 1
m = []
base = [i+1 for i in range(n)]
for i in range(n):
    m.append(base)
    base = [base[-1]] + base[:-1]
return m
```

```python
# Case 2
m = [[0]*n for i in range(n)]
for i in range(n-3):
    m[i] = base
    base = [base[-1]] + base[:-1]
m[n-3][0] = 2
m[n-2][-2] = 2
m[n-1][-1] = 2
m[n-3][-3] = 1
m[n-2][-1] = 1
m[n-1][-2] = 1
m[n-3][-1] = 3
m[n-3][-2] = n
m[n-2][0] = 3
m[n-1][0] = 4
base2 = [i+3 for i in range(1,n-3)]
for c in range(1,n-3):
    m[n-3][c] = base2[c-1]
base3 = [3,min(5,n)]
mod2 = 1
for c in range(1,n-2):
    for j in range(2):
        m[n-2+(mod2+j)%2][c] = base3[j]
    mod2 += 1 % 2
    base3 = [min(b+1,n) for b in base3]
mod3 = 2
return m
```

```python
# Case 3
m = []
for i in range(n):
    m.append(base)
    base = [base[-1]] + base[:-1]
m.append(m.pop(-2))
return m
```
We then categorize every possible n,trace pairs into one of the three categories. The relation between the trace sum and n can help us determine the type of the matrix.

1. trace sum = n -> only trace option = [1,1,1...1] (type 1, satisfiable)
2. trace sum = n + 1 -> only trace option = [1,1,1...1],[2] (type 4, unsatisfiable)
3. trace sum = n * n -> only trace option = [n,n,n...n] (type 1, satisfiable)
4. trace sum = n * n - 1 -> only trace option = [n,n,n...n],[n-1] (type 4, unsatisfiable)
5. n + 2 <= trace <= n * n - 2 -> there exist trace option of type 2 or type 3, we can find it by simple math formulas
6. For special case n = 3, type 2 is the complement of type 4. Manually set the satisfiable trace sum of n = 3, which is trace sum = 3 or 6 or 9

After decomposing the trace sum into desired trace, the only step left is to change the numbers on the basic matrix. Simply map the elements of the basic trace into the elements of the new trace. For each element in map.values() that is not in map.keys(), there will be an element in map.keys() that is not in map.values(). Randomly map those the extra elements in values to the extra elements in keys to ensure that each element occurs exactly n times in the latin matrix.
