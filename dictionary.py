trip = {
    "trip_id":"ub2",
    "pickup":["chennai","coimbatore","vellore"],
    "dropoff": "chennai"
}

#look up
print(trip["pickup"])

print(trip.get("pickup"))

print(trip.keys())

print(trip.values())

for key in trip.items():
    print(key)

#upsert
trip.update({"car_model":"suzuki"})
print(trip)

#pop
trip.pop("pickup")

for u,v in trip.items():
    print(u,v)

print(trip["pickup"][1])

#iteration
for location in trip["pickup"]:
    print(location)









