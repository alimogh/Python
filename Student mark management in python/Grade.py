class Student:
    def __init__(self,first_name,last_name,homework,test,lesson):
        self.first_name = first_name
        self.last_name = last_name
        self.homework = homework
        self.test = test
        self.lesson = lesson
        self.averageMark = 0
        self.ch = ""
        self.studentID = 0
    def calculate(self):
        self.averageMark = (float(self.homework) + float(self.test) +float(self.lesson)) /3 * 20
           
    def grade(self):
        if self.averageMark<=10:
            self.ch = "A"  
        elif self.averageMark<=20:
            self.ch = "A+" 
        elif self.averageMark<=30:
            self.ch = "B"  
        elif self.averageMark<=40:
            self.ch = "B+"        
        elif self.averageMark<=50:
            self.ch = "C"  
        elif self.averageMark<=60:
            self.ch = "C+"
        elif self.averageMark<=70:
            self.ch = "D"  
        elif self.averageMark<=80:
            self.ch = "D+"
        elif self.averageMark<=90:
            self.ch = "E"  
        elif self.averageMark<=100:
            self.ch = "E+"    
    def setID(self,id):
        self.studentID = id   
    def setFirstName(self,first_name):
        self.first_name = first_name
    def setLastName(self,last_name):
        self.last_name = last_name
    def setHomework(self,homework):
        self.homework = homework
    def setTest(self,test):
        self.test = test
    def setLesson(self,lesson):
        self.lesson = lesson
    def getID(self):
        return self.studentID  
    def getFirstName(self):
        return self.first_name
    def getLastName(self):
        return self.last_name
    def getHomework(self):
        return self.homework
    def getTest(self):
        return self.test
    def getLesson(self):
        return self.lesson
    def getAverage(self):
        return self.averageMark
    def getGrade(self):
        return self.ch                             
  
#main       
while 1:
    #the list of the students        
    studentManager = []  
    #identify the students by id
    ID = 0
    #open the file and save student objects into studentManger
    f = open("student.txt","r")
    tmp = f.read()
    students = tmp.split("\n")
    if (len(students)-1)!=0:
        for i in range(0,len(students)-1):
            content = students[i].split()
            content.insert(0,str(i+1))
            stu = Student(content[1],content[2],content[3],content[4],content[5])
            stu.calculate()
            stu.grade()
            stu.setID(int(content[0]))
            studentManager.append(stu)
    ID = len(students)
    
    print("...........................................................................")
    print("ID  first_name   last_name  Homework  Test  Lesson Average  Grade")
    for i in range(1,ID):
        mid = ""
        mid =str(studentManager[i-1].getID())+"   " +studentManager[i-1].getFirstName()+"        "+studentManager[i-1].getLastName()+"       "+str(studentManager[i-1].getHomework())+"      "+str(studentManager[i-1].getTest())+"     "+str(studentManager[i-1].getLesson())+"      "+str(studentManager[i-1].getAverage())+"      "+studentManager[i-1].getGrade()           
        print(mid)
        
    print("Press 'A' to append student mark")
    print("Press 'E' to edit student mark")
    print("Press 'D' to delete student mark")
    print("Press 'Q' to quit")
    
    
    f.close()
    
    function_key = input()
    if function_key=="q":
        break
    while function_key=="a":
        #open the student.txt - only writing
        f = open("student.txt", "a")
        #Enter the student name and marks
        print("Enter the first_name of the student")
        first_name = input()
        
        print("Enter the last_name of the student")
        last_name = input()
        
        print("Enter the homework mark (0~5) of the student")
        homework = input()
        try:
            if float(homework)<0 or float(homework)>5:
                print("Enter the homework correctly")
                f.close()
                break
        except ValueError:
            print("Please input integer only...") 
            f.close()
            break
        
        print("Enter the test mark (0~5) of the student")
        test = input()
        try:
            if float(test)<0 or float(test)>5:
                print("Enter the test correctly")
                f.close()
                break
        except ValueError:
            print("Please input integer only...") 
            f.close()
            break
        
        print("Enter the lesson mark (0~5) of the student")
        lesson = input()
        try:
            if float(lesson)<0 or float(lesson)>5:
                print("Enter the lesson correctly")
                f.close()
                break
        except ValueError:
            print("Please input integer only...") 
            f.close()
            break
        #create student object
        stu = Student(first_name,last_name,homework,test,lesson)
        #calculate the student's average mark and determine the grade
        stu.calculate()
        stu.grade()
        stu.setID(ID)
        ID = ID + 1
        studentManager.append(stu)
        #append the student to the file
        info = [stu.first_name ,stu.last_name,stu.homework,stu.test,stu.lesson,str(stu.averageMark),stu.ch]
        for i in range(0,len(info)):
            f.writelines(info[i])
            f.write(" ")
        f.write("\n")    
        #close the file
        f.close()
        break  
             
    while function_key == "e":
        f = open("student.txt","w")   
        print("What id do you edit?")  
        num = input()
        num = int(num)
        if num<0 or num >ID:
            print("Enter the correct number")
            f.close() 
            break   
        print ("What do u edit?")
        print("Enter F to edit first_name")
        print("Enter L to edit last_name")
        print("Enter H to edit Homework mark")
        print("Enter T to edit Test mark")
        print("Enter C to edit Lesson mark")
        key = input()
        print("Enter the value you want to edit")
        value = input()
        if key=="f":
            studentManager[num-1].setFirstName(value)
        elif key=="l":
            studentManager[num-1].setLastName(value)
        elif key=="h":
            try:
                if float(value)<0 or float(value)>5:
                    print("Enter the value of homework correctly")
                    f.close()
                    break
            except ValueError:
                print("Please input integer only...") 
                f.close()
                break
            studentManager[num-1].setHomework(value)
            studentManager[num-1].calculate()
            studentManager[num-1].grade()
        elif key=="t":
            try:
                if float(value)<0 or float(value)>5:
                    print("Enter the value of test correctly")
                    f.close()
                    break
            except ValueError:
                print("Please input integer only...")
                f.close() 
                break
            studentManager[num-1].setTest(value)
            studentManager[num-1].calculate()
            studentManager[num-1].grade()
        elif key=="c":
            try:
                if float(value)<0 or float(value)>5:
                    print("Enter the value of lesson correctly")
                    f.close()
                    break
            except ValueError:
                print("Please input integer only...")
                f.close() 
                break
            studentManager[num-1].setLesson(value)
            studentManager[num-1].calculate()
            studentManager[num-1].grade()
        else:
            print("Enter the correct what u want to edit")
            f.close()
            break
        
        for i in range(0,len(studentManager)):
            info = [studentManager[i].first_name ,studentManager[i].last_name,studentManager[i].homework,studentManager[i].test,studentManager[i].lesson,str(studentManager[i].averageMark),studentManager[i].ch]
            for i in range(0,len(info)):
                f.writelines(info[i])
                f.write(" ")
            f.write("\n")  
        f.close()                          
        break    
    while function_key =="d":
        f=open("student.txt","r")
        print("What id do you remove?")
        num = input()
        try:
            if int(num)<1 or int(num)>len(studentManager):
                print("Enter the id correctly")
                f.close()
                break
        except ValueError:
                print("Please input integer only...") 
                f.close()
                break
        studentManager.pop(int(num)-1)  
        lines = f. readlines()
        f. close()
        del lines[int(num)-1]
        new_file = open("student.txt", "w+")
        for line in lines:
            new_file. write(line)
        new_file. close()    
        break
        
                  