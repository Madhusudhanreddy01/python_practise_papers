# 19. Define a generator to print the numbers between o to n (including) which are divisible by 
# 5 and should be even 
# N = 20 
# Output : 10 20

def divisible(n):
    for i in range(1,n+1):
        if i % 10==0 and i % 2==0:
            yield i
for num in divisible(20):
    print(num)
