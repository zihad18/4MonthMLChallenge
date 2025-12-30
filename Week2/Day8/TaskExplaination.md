## The Linear Scan
if we wants to find -5 from a list of 10 million numbers without knowing the representation of that list. We must have to apply Linear Search . So the Time Complexity will be O(N)

## The Hash Lookup 
When we convert that list into a set. it becomes the hash table. So When We try to find a value in that hash table. It calculate hashing value for it then give us the memory slot.


## The Insertion Trap
Usually the ```python append()``` function insert the value in the next empty memory slot which takes O(1) time complexity. But ```python insert(0,a)```for inserting an element in 0th index needs shifting of the previous all element one space then it saves in 0th index.
