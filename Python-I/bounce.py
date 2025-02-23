
height= int(input("Enter the height from which the ball was dropped: "))
bounce= float(input("Enter the bounciness index of the ball: "))
times = int(input("Enter the number of time the ball is allowed to continue bouncing: "))
dist = 0

dist = height
for count in range(times-1):
    height = height * bounce
    dist = dist + 2 * height

dist = dist + height * bounce

print("The distance travelled is: ", dist, "units")


        