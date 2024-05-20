class CourseAttempt:
    def __init__(self,student,course,grade):
        self.student = student 
        self.course = course 
        self.student_grade = grade 
    @property
    def student_name(self):
        return self.student
    @property
    def course_name(self):
        return self.course
    @property
    def grade(self):
        return self.student_grade
    def __str__(self):
        return f"{self.student}, grade for {self.course} {self.student_grade}"


def names_of_students(attempts: list):
    r = map(lambda x: print(x.student) , attempts)
    return r 

def course_names(attempts: list) :
    r = map(lambda x : x.course , attempts)
    return sorted(r)

s1 = CourseAttempt("Peter Python", "Introduction to Programming", 3)
s2 = CourseAttempt("Olivia C. Objective", "Introduction to Programming", 5)
s3 = CourseAttempt("Peter Python", "Advanced Course in Programming", 2)

for name in course_names([s1, s2, s3]):
    print(name)