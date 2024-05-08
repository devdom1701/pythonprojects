class Student:
    def __init__(self,first_name,last_name,gpa,class1,class2,class3,class4,age,student_id,email,is_enrolled,dateofbirth):
        self.first_name = first_name
        self.last_name = last_name
        self.full_name = str(first_name) + str(last_name)
        self.gpa = gpa
        self.class1 = class1
        self.class2 = class2
        self.class3 = class3
        self.class4 = class4
        self.age = age
        self.student_id = student_id
        self.email = email
        self.is_enrolled = is_enrolled
        self.dateofbirth = dateofbirth

    def update_age(self,age):
        if age is int:
            self.age = age
        else:
            return f'Value of age isnt an integer'
    
    def print_classes(self):
        if self.class1 and self.class2 and self.class3 and self.class4 is str:
            print(self.class1,self.class2,self.class3,self.class4)
        else:
            return f'Value of classes isnt an string'

    def print_full_name(self):
        if self.first_name and self.last_name is str:
            print(self.first_name + self.last_name)
        else:
            return f'Value of names isnt a string'
    
    def add_class(self,string):
        if string and self.class1 is str:
            self.class1.write(string)
        else:
            return f'Value of class isnt an Integer'

    def update_gpa(self,gpa):
        if gpa is float:
            self.gpa = gpa
        else:
            return f'Value of gpa isnt float'

    def toggle_enrollment(self):
        if self.is_enrolled is bool:
            if self.is_enrolled == True:
                self.is_enrolled = False
            else:
                self.is_enrolled = True
        else:
            return f'Value of enrollement isnt Boolean'