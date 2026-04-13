import time

my_time = int(input("Enter time in seconds: "))

for second in reversed(range(0,my_time)):
    seconds = second%60
    minutes = int((second/60) % 60)
    hours = int((second/3600))
    print(f"{hours}:{minutes}:{seconds}")
    time.sleep(1)
print("TIMES UP!!")
