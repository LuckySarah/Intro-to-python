# greet()  #call --use  no arguements/params == data
from functions import file


def greet():
    print("hello")
# greet()

def greeting(name):
    print(f"Hello {name}")

# greeting('sila')
# greeting('Allan')
# greeting('Ahmed')

def volume_cylinder(radius, height):
    v = radius * height
    v = 22/7 * radius**2 * height
    print(round(v, 2))

# volume_cylinder(10, 20)
# volume_cylinder(7,  14)

def volume_cylinder_better(radius, height):
    v = 22/7 * radius**2 * height
    return v
# result = volume_cylinder_better(6.5,9.8)
# print(round(result,3))

# with open("volumes.txt", "w") as f:
#   file.write(str(result))

def volume_surface(radius, height):
    v = 22/7 * radius**2 * height
    a = 22/7 * radius**2 * 2 + 22/7 * radius* 2 * height
    return v, a
# if you dont want to recieve some values you want only the specific do volume, _
# volume, area = volume_surface(10, 20)
# print(f"volume is {volume} and area is {area}")

#if you care about params use named paramas
# v, a = volume_surface(height=20, radius=10)
 #print(f"volume is {v} and area is {a}")

def divide(a, b, should_round = False): # by default
    result = a / b
    if should_round== True:
        return round(result, 2)
    else:
        return result

print(divide(10, 2))

print(divide(b=20))


