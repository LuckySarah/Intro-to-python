def add (a,b, c):
    result = a + b + c
    return result
print(add(9,7,5))

def addition(*nums: object) -> int: # the * means any numbers or letters
    """  (to add documentation)
    Returns the sum of all the numbers passed as arguments
    Parameters:
        Integers or float or a mix of integers and floats
    Returns:
        Integers or floats
    """
    total = sum(nums)
    return total
addition(8,3,5)
print(addition(8, 3, 7, 100, 5))
print(addition(8, 3))

def build_profile(**kwargs): #uses a dictionary/key-word arguments
    for k, w in kwargs.items():
        print(k, w)
        print(f"{k}: {w}")
build_profile(experience='10, name="Jane", "age"="19", proffesion="programming", gender="female"')

def fancy_function(name, *nums, **kwargs):
    print(name)
    print(nums)
    print(kwargs)

# anonymous functions = lambda
def square(num):
    return num * num
result = square(5)
print(result)

square = lambda num : num * num
print(square(5))
result = square(2.5)
print(result)

surface_area_cylinder = lambda r, h : 22/7 * r**2 *2 + 22/7 *2 * r * h
print(surface_area_cylinder(14,20))

people= [
    {"name": "Alex", "age": 30},
    {"name": "Ray", "age": 45},
    {"name": "Tracy", "age": 25},
]
# lamba x: x['age']
sorted_by_age = sorted(people, key=lambda x: x["age"], reverse=True)
# reverse true from largest to smallest
print(sorted_by_age)




