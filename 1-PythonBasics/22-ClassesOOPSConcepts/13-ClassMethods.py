# class methods
# for defining class methods we use cls instead of self

# when we use class methods
# - When you want to access or modify class variables.
# - When you want to create alternative constructors.
# - When behavior should apply to the class as a whole, not individual objects.


# for class methods the first argument is cls
# these methods cannot access instance variables but access class variables
# they have class wide behaviour


class Student:
    count = 0
    def __init__(self,name):
        self.name = name
        Student.count +=1


    @classmethod
    def get_count(cls):
        return cls.count

    # cls refers to class here cls is Student
    # so instead of Student.count we can use cls.count
s1 = Student("Emma")
s2 = Student("Harry")
print(Student.get_count())
