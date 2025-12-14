seconds = int(input("Input time in seconds: "))
hours, seconds = seconds // 3600, seconds % 3600
minutes, seconds = seconds // 60, seconds % 60
print(f"Hour: {hours} Minutes: {minutes} Seconds: {seconds}")