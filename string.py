a="dharshini"
b="123@d"
print(a.upper())
print(a.lower())
print(a.capitalize())

mobile="9999999999"
masked=mobile[:2]+"******"+mobile[-2:]
print(masked)

song="shape OF You"
artist="DHARSHINI ab"
formatted=f"{song.title()} - {artist.title()}"
print(formatted)

location="chennai central"
fixed_location= location.replace("chennai central","thambaram")
print(fixed_location)

message="your booking_id is: AB12345"
booking_id=message.split(":")[1].split(".")[0].strip()
print(booking_id)