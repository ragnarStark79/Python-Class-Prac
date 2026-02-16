class Student:
  def __init__(self, name):
    self.name = name
    self.__present = 0
    self.__total_classes = 0

  def mark_present(self):
    self.__present += 1
    self.__total_classes += 1

  def mark_absent(self):
    self.__total_classes += 1

  def get_attendance(self):
    if self.__total_classes == 0:
      return 0.0
    return (self.__present / self.__total_classes) * 100

  def is_eligible(self):
    return self.get_attendance() >= 75
  
  def total_students(self):
    return self.__total_classes


student1 = Student("Alice")
student2 = Student("Bob")
student1.mark_present()
student2.mark_present()
print(student1.get_attendance())
print(student2.get_attendance())