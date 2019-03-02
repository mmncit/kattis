x_mb = int(input())  # type: int # MB package
n = int(input())  # months
r_mb = 0  # remaining MB
for count in range(n):
    r_mb += (x_mb - int(input()))
r_mb += x_mb
print(r_mb) 
