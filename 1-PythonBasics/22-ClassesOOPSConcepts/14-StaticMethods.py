# Static Methods -> this is used when
# 1. when method does not need self or cls
# 2. when the method logically belongs to class but does not touch its data


# in static methods you cannot access instance and class attributes
# thses are used as utility or helper functions

class UtilMethods:
    @staticmethod
    def add(a,b):
        return a+b

print(UtilMethods.add(2,3))