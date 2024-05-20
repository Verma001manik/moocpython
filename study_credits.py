from functools import reduce
class CourseAttempt:
    def __init__(self,course,grade,credits):
        
        self.course = course 
        self.student_grade = grade 
        self.student_credits = credits 

        

    @property
    def course_name(self):
        return self.course
    @property
    def credits(self):
        return self.student_credits
    @property
    def grade(self):
        return self.student_grade
    def __str__(self):
        return f" {self.course}({self.student_credits}cr) {self.student_grade}"

def sum_of_all_credits(attempts: list):
    return reduce(lambda attempt, item: attempt.credits+ item , 0 )
s1 = CourseAttempt("Introduction to Programming", 5, 5)
s2 = CourseAttempt("Advanced Course in Programming", 4, 5)
s3 = CourseAttempt("Data Structures and Algorithms", 3, 10)
credit_sum = sum_of_all_credits([s1, s2, s3])
print(credit_sum)