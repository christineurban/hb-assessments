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
   on their own, but methods must be called on a specific class and always take
   at least one parameter.

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


class Student(object):
    """A student at Hackbright."""

    def __init__(self, first_name, last_name, address):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address


class AbstractQuestion(object):
    """A single question evaluator"""

    questions = []

    def __init__(self, name):
        self.name = name

    def add_question(self, question, correct_answer):
        # adds question and answer as values in dictionary
        self.questions.append({"question": question,
                               "correct_answer": correct_answer})

    def ask_and_evaluate(self):
        answer = raw_input(self.question["question"] + " > ")
        # prints question on screen and awaits user input

        if answer == self.question["correct_answer"]:
            return True
        else:
            return False

    def administer(self):
        score = 0
        total_q = 0

        for self.question in self.questions:
            ask_question = self.ask_and_evaluate()

            if ask_question is True:
                score += 1
                total_q += 1
            else:
                total_q += 1

        return float(score) / float(total_q)


class Exam(AbstractQuestion):
    """An exam with multiple questions. Returns % score.

    Everything occurs in parent class.
    """


class Quiz(AbstractQuestion):
    """A quiz with multiple questions. Pass/Fail at 50%."""

    def administer(self):
        percent = super(Quiz, self).administer()

        if percent > 0.5:
            return True
        else:
            return False


def take_test(test, student):
    """A Student instance takes test and is assigned its score"""

    student.score = test.administer()
    print student.score

     
def example(test):
    """An test and student example"""

    # I pulled the instantiation of the test classes out of the
    # function for step 5, to test each out individually.

    test.questions.extend(({"question": "roses are",
                           "correct_answer": "red"},

                          {"question": "sky color",
                           "correct_answer": "blue"},

                          {"question": "they call me mellow",
                           "correct_answer":  "yellow"},
                          
                          {"question": "plums are",
                           "correct_answer": "purple"},
                          
                          {"question": "grass is",
                           "correct_answer": "green"},
                          ))

    student = Student("Christine", "Urban", "Oakland")

    take_test(test, student)

exam = Exam("Colors")
quiz = Quiz("Colors")


# Uncomment the lines below, one at a time, to see how exam and 
# quiz work. Reload Python file after trying each example.

# example(exam)
# example(quiz)