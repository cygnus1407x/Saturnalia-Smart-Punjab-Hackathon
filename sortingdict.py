#the format of dictionary is                   
#{ number of road: corresponding number of vehicles } 
 
# we want to access the smallest value (which is placed first)
# then as we go forward, it gets: no increment of green light if there are upto 10 cars
# +5 second increment of GL if there are 10 to 30 cars
# +10 second increment of GL if there are 30 to 70 cars
# +12 scond increment of GL if there are 70 to 100 cars
# full +15 second increment of GL if there are more than 100 cars

from collections import OrderedDict
import json

num_of_roads=4
roads={}

for i in range(1,num_of_roads+1):
        num_of_vehicles=int(input("Enter number of vehicles on road: "))
        roads[i]= num_of_vehicles 
    
 #sorting using collections module
sorted_by_value = OrderedDict(sorted(roads.items(), key=lambda x: x[1])) 
print(sorted_by_value)

# converting to dict
json_str = json.dumps (sorted_by_value)
roadsdict2 = json.loads(json_str)

# final check
for j in roadsdict2:
    if roadsdict2[j]==0:
        print("Road",j,"--> Red Light")
    elif roadsdict2[j]>0 and roadsdict2[j]<=10:
        print("Road",j,"--> No increment in Green Light")
    elif roadsdict2[j]>10 and roadsdict2[j]<=30:
        print("Road",j,"--> +5s increment in Green Light")
    elif roadsdict2[j]>30 and roadsdict2[j]<=70:
        print("Road",j,"--> +10s increment in Green Light")
    elif roadsdict2[j]>70 and roadsdict2[j]<=100:
        print("Road",j,"--> +12 increment in Green Light")
    elif roadsdict2[j]>100:
        print("Road",j,"--> +15 increment in Green Light")


            
    



