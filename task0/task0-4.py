#P1001
a, b = map(int, input().split())
print(a + b)


#P1046
apples = list(map(int, input().split()))
hand_height = int(input())
reach_height = hand_height + 30
count = 0
for apple_height in apples:
    if apple_height <= reach_height:
        count += 1
print(count)


#P5737
x,y=map(int,input().split())
def is_leap_year(year):
    return (year%4==0 and year%100!=0) or(year%400==0)
leap_year=[]
for year in range(x,y+1):
    if  is_leap_year(year):
        leap_year.append(year)
print(len(leap_year))
print(' '.join(map(str, leap_year)))


#AT_arc017_1
N=int(input())
def is_prime(n):
    if n%2==0:
        return False
    for i in range(17,int(n**0.5)+1,2):
        if n%i==0:
            return False
    return True
if is_prime(N):
    print("Yes")
else:
    print("No")