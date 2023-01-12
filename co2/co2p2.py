n = int(input("Enter a limit:"))
f = [0,1]
for i in range(n-2):
    s = f[i]+f[i+1]
    f.append(s)
print("Fibonacci series is:")
print(f)