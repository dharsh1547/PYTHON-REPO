#creating lists for different apps
playlist=["shape of you", "vaanam mella","naa ready"]
favorite_foods=["pizza","burger","pasta"]
recent_locations=["home","airport","court"]

print("playlist:",playlist)
print("favorite_foods:",favorite_foods)
print("recent_locations:",recent_locations)

#list methods

#append
playlist.append("oorum blood")
print("after append:",playlist)

#insert
playlist.insert(1,"power paandi")
print("after insert:",playlist)

#removing
playlist.remove("oorum blood")
print("after remove:",playlist)

#pop
playlist.pop()
print("after remove:",playlist)

#reverse
playlist.reverse()
print("after remove:",playlist)

#count (prints the index position)
print("count", playlist.count("vaanam mella"))

#list slicing
print("top 2 songs",playlist[0:2])

#last 2 info
print("last 2:", playlist[-2:])

#customised
print(playlist[1:3])

#list iteration
for food in favorite_foods:
    print("all foods:", food)

for song in playlist:
    print(song + " by dharshini", song)

#check if
if "dosa" in favorite_foods:
    print("yes")
else:
    print("no")

#update(mutable)
favorite_foods[1]="shawarma"
print(favorite_foods)

mixed = ["dharshini", 19, 1.50]
for a in mixed:
    print(a)

#taking index position
for i,location in enumerate(recent_locations):
    print( i,location)