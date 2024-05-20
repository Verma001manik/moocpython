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
def accepted(attempts: list):
    return filter(lambda attempt : attempt.grade >=1,attempts)

def attempts_with_grade(attempts: list, grade: int) :
    return filter(lambda attempt: attempt.grade ==grade,attempts)

def passed_students(attempts: list, course: str):
    unsorted_result = filter(lambda attempt: attempt.grade>0,attempts)
    return unsorted_result
    
s1 = CourseAttempt("Peter Python", "Introduction to Programming", 3)
s2 = CourseAttempt("Olivia C. Objective", "Introduction to AI", 5)
s3 = CourseAttempt("Peter Python", "Introduction to AI", 0)
s4 = CourseAttempt("Jack Java", "Introduction to AI", 3)

for attempt in passed_students([s1, s2, s3, s4], "Introduction to AI"):
    
    print(attempt)