class ClimbingRoute:
    def __init__(self,name,length,grade):
        self.name = name 
        self.length = length
        self.grade = grade 

    def __str__(self):
        return f"{self.name} Length {self.length} meters, grade {self.grade} "

class ClimbingArea:
    def __init__(self):
        

route1 = ClimbingRoute("Edge", 38, "6A+")
route2 = ClimbingRoute("Smooth operator", 9, "7A")
route3 = ClimbingRoute("Synchro", 14, "8C+")

def by_length(item: ClimbingRoute):
    return item.length
def by_grade(item: ClimbingRoute):
    return item.grade
def sort_by_length(items: ClimbingRoute):
    return reversed(sorted(items, key=by_length))
def sort_by_grade(items: ClimbingRoute):
    return reversed(sorted(items,key=by_grade))
r1 = ClimbingRoute("Edge", 38, "6A+")
r2 = ClimbingRoute("Smooth operator", 11, "7A")
r3 = ClimbingRoute("Synchro", 14, "8C+")
r4 = ClimbingRoute("Small steps", 12, "6A+")

routes = [r1, r2, r3, r4]
for route in sort_by_grade(routes):

    print(route)