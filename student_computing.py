class Student:
    def info(self,Student_ID):
        self.__Name="Oğuzhan"
        self.__Surname="Gök"
        self.__Student_ID=Student_ID
        self.__Phone_No="002351"
        self.__Birth_Date="22.03.2001"
    def get_info(self):
        return self.__Name + \
               " " + \
               self.__Surname + \
               " " + \
               self.__Student_ID + \
               " " + \
               self.__Phone_No + \
               " " + \
               self.__Birth_Date
class Semester1(Student):
        courses={
            "a101":"AA",
            "b232":"CD",
             "c541":"AA"
        }
class Semester2(Student):
        courses={
            "a78":"AA",
            "c45":"BB",
            "FGG":"CC"
        }
def get_Transcript(ID,Semester):
    Oğuzhan=Student()
    Oğuzhan.info(ID)
    print(Oğuzhan.get_info())
    if Semester=="1":
        print(Semester1.courses)
    elif Semester=="2":
        print(Semester2.courses)
get_Transcript("190444065","1")
get_Transcript("190444065","2")




