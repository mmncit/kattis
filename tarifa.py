x_mb = int(input()) # package
n = int(input()) # months
r_mb = 0 # remaining mb
for count in range(n):
    r_mb += (x_mb - int(input()))
r_mb += x_mb
print(r_mb) 
