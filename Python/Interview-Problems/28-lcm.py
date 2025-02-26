def find_gcd(a,b):
    if a==0:
        return b
    elif b==0:
        return a
    return find_gcd(b,a%b)

def find_lcm(a,b):
    return a*b//find_gcd(a,b)

a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
lcm = find_lcm(a,b)

print(lcm)