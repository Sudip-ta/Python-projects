import time

my_time = int(input("Enter time in seconds: "))

for second in range(my_time,0,-1): #did not use reversed because then it would exclude the value of my_time itself and only consider just before it
    seconds = second%60
    minutes = int((second/60) % 60)
    hours = int((second/3600))
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1) #makes the program excution sleep for 1 second
print("TIMES UP!!")
