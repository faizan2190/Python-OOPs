# THE DIAMOND PATTERN

# Search order:
#  search in the current class
#  search the left parent
#  search the right parent


# # A child class inherits attributes and methods from all the parents


# class A:
#     def method(self):
#         print("In method A")
# class B:
#     def method(self):
#         print("In method B")
# class C(A, B):
#     def method(self):
#         print("In method C")

# objC = C()
# objC.method()


# class A:
#     def method(self):
#         print("In method A")
# class B:
#     def method(self):
#         print("In method B")
# class C(A, B):
#     pass

# objC = C()
# objC.method()


class A:
    pass
class B:
    def method(self):
        print("In method B")
class C(A, B):
    pass

objC = C()
objC.method()

