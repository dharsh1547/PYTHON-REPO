trip_summary=("ubergo","chennai","airport",45,"completed")
print(trip_summary)
print(trip_summary[1])

#length
print(len(trip_summary))

#count and index
print(trip_summary.count("completed"))
print(trip_summary.index("airport"))

"""
this set of code is not possible as it cannot update anything
trip_summary[1]="karur"
print(trip_summary)"""

#unordered
#removes duplicates

a=set[1,2,3]
b=set(a)

#representation of not allowing duplicates
cities=["chennai","banglore","chennai","delhi","banglore"]
uniquecities=set(cities)

#union
city1={"chennai","banglore","vellore"}
city2={"hydrabed","maldives","mumbai"}
print(city1.union(city2))

#intersection
city1={"chennai","banglore","vellore"}
city2={"hydrabed","maldives","mumbai"}
print(city1.intersection(city2))

#difference
city1={"chennai","banglore","vellore"}
city2={"hydrabed","maldives","mumbai"}
print(city1.difference(city2))

#adds value randomly
city1.add("karur")
print(city1)

#remove a value
city1.remove("chennai")
print(city1)

my_set={1,2,3}
print(my_set)

my_set.remove(2)
my_set.add(99)
print(my_set)

#safe remove
my_set.discard(8)
#removes the value if it exists or else it does'nt show error

