def nested_loop():
  for x in range(1,11):
    for y in range (1,6):
      if y % 3 == 0:
        continue
      elif y == 4:
        break
      elif x*y >= 10:
        return
      print(f"{x} x {y} = {x * y}")


def another_loop(Count):
  count = Count
  while count < 20:
    count += 1
    print(f"Count: {count}")
  print("End of counting.")

def askForNumbers():
  # Ask for numbers until we got one which can be divided by 5.

  number = int(input("Enter a number: "))
  while number % 5 != 0:
    print(f"{number} can not be divided by 5.")
    number = int(input("Enter a number: "))

  print(f"{number} finally can be divided by 5.")
  print(f"The number is: {number}")


# another_loop(5)

# nested_loop()

# truthy_checks()

# print(is_power_of(8,2)) # Should be True
# print(is_power_of(64,4)) # Should be True
# print(is_power_of(70,10)) # Should be False