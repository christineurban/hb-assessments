"""
Part 1: Discussion

1. What are the three main design advantages that object orientation
   can provide? Explain each concept.

   ABSTRACTION -- Hiding details we don't need. We don't need to know how
   to get from A to B, we just need to know what to use (such as a method) to
   get from A to B. Makes code easier to read and intelligently separates
   code into sections.

   ENCAPSULATION -- Keeping everything together. Necessary data lives close
   to its functionality. Like a pill capsule, it contains the important parts.

   POLYMORPHISM -- Flexibility of types without conditionals (if/else
   statements. This means there isn't data inside a type (such as a class)
   that is specific to another type (such as a subclass), but is generic and
   can be used by other subclasses.

2. What is a class?

   Classes are like dictionaries but smarter. Like dictionaries, they can store
   data (attributes), and can be flexible. The advantage to dictionaries are
   that they are more structured, and has own smarts (methods).

3. What is an instance attribute?

   An attribute of an instance. Instance attributes are owned by the
   specific instance of a class. THey can come from a class or added after
   the instance is created.

4. What is a method?

   It is like a function, but is defined on a class. Functions can be called
   on their own, but methods must be called on a specific class.

5. What is an instance in object orientation?

   An instance is an individual occurence of a class. It is also known as an
   object.

6. How is a class attribute different than an instance attribute?
   Give an example of when you might use each.

   A class attribute is a hard-coded attribute that will transfer to all 
   instances when they are instantiated. This is ideal for global variables,
   such as a Dog class having a speak of "Woof".

   An instance attribute can either be inherited upon instantiation or added/
   changed after the instantiation. Adding instance attributes is ideal for
   local variables, such as a dog's name.


"""


# Parts 2 through 5:
# Create your classes and class methods
