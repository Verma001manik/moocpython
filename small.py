def smallest_average(person1: dict, person2: dict, person3: dict):
    average1 = person1["result1"] + person1["result2"] + person1["result3"]
    average2 = person2["result1"] + person2["result2"] + person2["result3"]
    average3 = person3["result1"] + person3["result2"] + person3["result3"]

    result = min(average1, average2, average3)
    if(average1<average2 and average1< average3):
        print(person1)
    elif(average2<average1 and average2<average3):
        print(person2)
    else: 
        print(person3)

person1 = {"name": "Mary", "result1": 2, "result2": 3, "result3": 3}
person2 = {"name": "Gary", "result1": 5, "result2": 1, "result3": 8}
person3 = {"name": "Larry", "result1": 3, "result2": 1, "result3": 1}

smallest_average(person1, person2, person3)
