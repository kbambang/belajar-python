import datetime
import json

# x = datetime.datetime.now()
#print(x)

#x = datetime.datetime.now()
#print(x.year)
#print(x.strftime("%d/%m/%Y"))

#x = datetime.datetime(2020, 5, 17)
#print(x)

#arr_1 = [5, 78, 2, 0]
#assert(min(arr_1)) == 0
#assert(max(arr_1)) == 78

# function 5 pangkat 5

#assert(pow(5, 5)) == 3125

#try:
#    f = open("demofile.txt")
#    try:
#        f.writelines("Lorum ipsum")
#    except:
#        print("Something went wrong when writing to the file")
#    finally:
#        f.close()
#except:
#    print("Something went wrong when opening the file")

#try:
#    print(x)
#except:
#    print("Shomething went wrong")
#finally:
#    print("hehe")

## some JSON 
x =  '{"name":"John", "age": 30, "city": "New York}'

## parse x:
y = json.loads(x)

## the result is a python dictionary
print(y["age"])