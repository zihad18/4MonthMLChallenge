### Task 9.1 problem Explaination

In the first task we have created a function `gen()` where we defined **yield** keyword 3 times from 1,2,3 . So when I call the function it will give me value as serial respectively. We implement a for loop until the function's all value are printed. It will print

```
1
2
3
```

### Task 9.2 problem Explaination

Here we are comparing list_comprehension with generator expresion using python `sys.getsizeof()` function. We observed that testing with 1 Milion number size the list comprehension takes around 8 MB size in the RAM. On the other hand the generator expresion takes only 192 Bytes size in RAM memory. The reason is simple list stores the whole memory for all the time while the generator store the metadata(instruction pointer and Scope) and some of the data in entire dataset as it works lazily.

### Task 9.3 problem Explaination

In this problem we just define a function which can calculate fibonnaci numbers but we use **yield** instead of return or printing then in function thats why we can generate infinte times of this amazing series as much as we want.

### Task 9.4 problem Explaination

As the generator instances usually become frozer after call and stores its states and when it completes its all value we cannot recall that instance anymore its not like traditional function which does not remember its previous call. So we need to reinitialize object for calling again .

### Task 9.5 problem Explaination

### Task 9.6 problem Explaination

### Task 9.7 problem Explaination

### Task 9.8 problem Explaination

### Task 9.9 problem Explaination

### Task 9.10 problem Explaination
