class CourseRecord:
    def __init__(self):
        self.__courses = {}
    def add_course(self, course,grade,credits):

        if course not in self.__courses:
            self.__courses[course] = []
        self.__courses[course].append((grade,credits))

    def get_course_data(self,course):
        if course not in self.__courses:
            return None
        else :
            return self.__courses[course]
        
    def get_all(self):
        return self.__courses
class CourseRecordApplication:
    def __init__(self):
        self.__course_record = CourseRecord()

    def help(self):
        print("0 exit")
        print("1 add course data")
        print("2 get course data ")
        print("3 statistics")

    def add_entry(self):
        course_name = input("course:")
        grades = input("grades")
        credits = input("credits")
        self.__course_record.add_course(course_name,grades,credits)
    
    def search(self):
        course = input("course:")
        data  = self.__course_record.get_course_data(course)
        if data == None:
            print("no entry for this course ")
        else:
            for grade, credits in data:
                print(f"{course} ({credits} cr) grade {grade}")

    def statistics(self):
        completed_course = 0 
        for course in self.__course_record.get_all():
            if(course):
                completed_course += 1 
        print(f"{completed_course}courses")
    def execute(self):
        self.help()
        while(True):
            print("")
            command = input("command:")
            if command == "0":
                break
            elif command =="1":
                self.add_entry()
            
            elif command == "2":
                self.search()
            elif command == "3":
                self.statistics()
            else:
                self.help()

course = CourseRecordApplication()
course.execute()
