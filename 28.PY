# # Example 2: Multiple Inheritance in a multi-level hierarchy

# # Search order:
# #  search in the current class
# #  search the left parent all the way up the hierarchy
# #  search the right parent all the way up the hierarchy

# Case 1: method() exists in all classes
# class X:
#  def method(self):
#  print('In method X')
# class Y:
#  def method(self):
#  print('In method Y') 
# class A(X):
#  def method(self):
#  print('In method A') 
# class B(Y):
#  def method(self):
#  print('In method B')
# class C(A, B):
#  def method(self):
#  print('In method C')
# objectC=C()
# objectC.method()
# 13
# Department of Computer & Information Systems Engineering
# NED University of Engineering & Technology
# Output:
# In method C
# Class A
# method( )
# Class B
# method( )
# Class C
# method( )
# Class X
# method( )
# Class Y
# method( )
# Multiple Inheritance and Multi-level Hierarchy - Example 2
# CS 116 - Lecture 13 
# Multiple Inheritance
# Case 2: method() exists in classes A, B, X and Y
# class X:
#  def method(self):
#  print('In method X')
# class Y:
#  def method(self):
#  print('In method Y') 
# class A(X):
#  def method(self):
#  print('In method A') 
# class B(Y):
#  def method(self):
#  print('In method B')
# class C(A, B):
#  pass
# objectC=C()
# objectC.method() 14
# Department of Computer & Information Systems Engineering
# NED University of Engineering & Technology
# Class A
# method( )
# Class B
# method( )
# Class C
# Class X
# method( )
# Class Y
# method( )
# Output:
# In method A
# Multiple Inheritance and Multi-level Hierarchy - Example 2
# CS 116 - Lecture 13 
# Multiple Inheritance
# Case 3: method() exists in classes B, X and Y
# class X:
#  def method(self):
#  print('In method X')
# class Y:
#  def method(self):
#  print('In method Y') 
# class A(X):
#  pass 
# class B(Y):
#  def method(self):
#  print('In method B')
# class C(A, B):
#  pass
# objectC=C()
# objectC.method()
# 15
# Department of Computer & Information Systems Engineering
# NED University of Engineering & Technology
# Class A Class B
# method( )
# Class C
# Class X
# method( )
# Class Y
# method( )
# Output:
# In method X
# Multiple Inheritance and Multi-level Hierarchy - Example 2
# CS 116 - Lecture 13 
# Multiple Inheritance
# Case 4: method() exists in classes B and Y
# class X:
#  pass
# class Y:
#  def method(self):
#  print('In method Y') 
# class A(X):
#  pass 
# class B(Y):
#  def method(self):
#  print('In method B')
# class C(A, B):
#  pass
# objectC=C()
# objectC.method() 16
# Department of Computer & Information Systems Engineering
# NED University of Engineering & Technology
# Class A Class B
# method( )
# Class C
# Class X Class Y
# method( )
# Output:
# In method B
# Multiple Inheritance and Multi-level Hierarchy - Example 2
# CS 116 - Lecture 13 
# Multiple Inheritance
# Case 5: method() exists in class Y only
# class X:
#  pass
# class Y:
#  def method(self):
#  print('In method Y') 
# class A(X):
#  pass 
# class B(Y):
#  pass
# class C(A, B):
#  pass
# objectC=C()
# objectC.method()