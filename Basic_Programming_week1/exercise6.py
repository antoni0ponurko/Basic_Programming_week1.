total_seconds = int(input("Enter the number of seconds: "))

days = total_seconds // (24 * 3600)
remaining_seconds = total_seconds % (24 * 3600)

hours = remaining_seconds // 3600
remaining_seconds %= 3600

minutes = remaining_seconds // 60
seconds = remaining_seconds % 60


print(f"d:h:m:s -> {days}:{hours}:{minutes}:{seconds}")
