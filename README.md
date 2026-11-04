# DSA_in_Python
Practising Data Structures and Algorithms using Python
## Language
- Python

logic:
ds.append(nums[i])  # Include
backtrack(i+1)
ds.pop()            # Undo inclusion
backtrack(i+1)      # Exclude


Exact execution order
Step	Action	ds
1	Start	[]
2	Include 1	[1]
3	Include 2	[1,2]
4	Save subset	[1,2]
5	Pop 2	[1]
6	Exclude 2, save	[1]
7	Pop 1	[]
8	Include 2	[2]
9	Save subset	[2]
10	Pop 2	[]
11	Exclude 2, save	[]


You want to explore two possibilities for the next element, 2.
- First possibility: [1, 2]
- Second possibility: [1]
If you don't execute ds.pop(), the second possibility would incorrectly contain 2 too.

Therefore, pop() restores the previous state before exploring another branch.

This is called backtracking.

#Pattern for recurssion problems
# Include
ds.append(nums[i])
backtrack(i + 1)

# Backtrack
ds.pop()

# Exclude
backtrack(i + 1)
