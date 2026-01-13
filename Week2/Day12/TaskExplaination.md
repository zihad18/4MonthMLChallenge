### Task 12.1 problem Explaination

In python we call **init**(self,\*args) inside here the function is a constructor . when a new object is initialized it will be called. As is_actice is True by defination of constructor.

### Task 12.2 problem Explaination

In python in every method inside a class should have first parameter as self object. As it is called using self when we call any object like `User.method(new_obj)` so its mandatory to write self otherwise it will throw TypeError.

### Task 12.3 problem Explaination

Print(user) will show usually memory address so to get the info from the object. In class we use **str**() and **repr**() . Where **str**() is end user friendly and **repr**() is developer friendly.

### Task 12.4 problem Explaination

Name mangling helps us to hide the name it some sorts of bit.Like it also make unique as we can see it via class name (\_ClassName**property). In User.password is become self.**password as name mangling for security.

### Task 12.5 problem Explaination

Using @property decorator we get getter like encapsulation in calling properties from class with safety.

### Task 12.6 problem Explaination

Class atributes are globally defined So if we change it all the instances will be affected by it but if we change the instances attribute value only the instances will be accountable for that.

### Task 12.7 problem Explaination

According to MRO principle the method is first searched on the calling class then sequentialy in c3 linear order into parent classes.

### Task 12.8 problem Explaination

Using super().**init**() in the inherited class we get all the implementation of parent classes . then we can override if we need.

### Task 12.9 problem Explaination

In operator overloading we have to define inside the class how our operator will work in our cases. for example in wallet class we calculate the balance of the two objects then return the answer and thats how we implemented two wallet addition.

### Task 12.10 problem Explaination

In this case the operator overloading is used we check the all attributes of the two instances are same or not by this we give verdict using **eq**() operator
