# Display the multiplication table of variable num (1 to 10)

num = int(input("Display multiplication table of? "))

# Iterate 10 times from i = 1 to 10
for i in range(1, 11):
    print(f"{num} x {i} = {num*i}")
