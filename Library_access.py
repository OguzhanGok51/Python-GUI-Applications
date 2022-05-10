class Library():
    def __init__(self,book="books",cd="cd's",file="files"):
        self._book = book
        self._cd = cd
        self.__file = file
class Student(Library):
    def studentacces (self):
        print("Student can acces {} and {}.".format(self._book,self._cd))
class Teacher(Library):
    def teacheracces (self):
        print("Teacher can acces {} and {}.".format(self._book,self._cd))
students = Student()
teachers = Teacher()
while True:
  print("If you are a teacher please press '1'")
  print("If you are student please press '2'")
  print("ıf you want exit please press '3'")
  enter=int(input())
  if enter == 1:
    teachers.teacheracces()
    print("Welcome teacher, you can also acces to {}, have a good day.".format(teachers._Library__file))
  elif enter == 2:
    students.studentacces()
    print("Welcome student!")
  else:
    print("Thanks for coming, goodbye!")
  break
