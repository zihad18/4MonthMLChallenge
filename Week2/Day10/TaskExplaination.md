### Task 10.1 problem Explaination

We just make a wrapper function without using any syntatic sugar like @ . We just use default behaviour of python function . Its simple decorator function.

### Task 10.2 problem Explaination

Now we do the same operation using @ a syntax sugar of python.

### Task 10.3 problem Explaination

As Expected the code crashes because we should use the `*args` in wrapper function's argument for passing any kinds of function with their varieties of arguments.

### Task 10.4 problem Explaination

If we does not return func(\*args) in wrapper function. It will not return value so we will get None from it. As our code gets.

### Task 10.5 problem Explaination

As the task asks we implemented the timer decorator which calculate the time and we are doing these types of activity in wrapper of decorator.

### Task 10.6 problem Explaination

We store USER as a global variable and we check it before function calling inside the wrapper where we check is the global USER is admin or not if not then we throw PermissionError as it enhances the security.

### Task 10.7 problem Explaination

We build a decorator which has the functionality of cache that's means if anyone check a prime or not once then when the function check it again for the same input it does not calculate the value again instead of that it just using hashing function aka dictionary in python takes only O(1) to get the answer.

### Task 10.8 problem Explaination

Usually when we called the function it returns the wrapper that's why when we see the function name it show wrapper not the original decorator name. If need to see the decorator function name we have to use `functools.wraps(func)` .

### Task 10.9 problem Explaination

the ordering matters in decorator when we call both decorator and its act like pipeline

### Task 10.10 problem Explaination

`repeat(time=3)` needs 3 nested function to execute
