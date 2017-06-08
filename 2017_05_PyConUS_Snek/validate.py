def valid_username(un):
  usr = un.lower() \
	   .strip() \
           .encode("ascii","ignore") \
           .decode("utf-8")
  print(un)
  print(usr)

  if usr != un :
    return False

  return True

print(valid_username("asdf"))
print(valid_username("asfadsf asdadfs"))
print(valid_username("asdlfj🐍"))

