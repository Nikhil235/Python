my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#          0, 1, 2, 3, 4, 5, 6, 7, 8, 9
#        -10,-9,-8,-7,-6,-5,-4,-3,-2,-1

# list[start:end:stepover]

# stepover always 1 by default
# -1 is reverse in stepover

# print(my_list[-10])
# print(my_list[0:5])
# print(my_list[3:8])
# print(my_list[:])
# print(my_list[-7:-2])
# print(my_list[1:])
# print(my_list[:8])
# print(my_list[2::2])
# print(my_list[2:-1:2])
# print(my_list[-1:2:-1])
# print(my_list[::-1])

sample_url = 'http://coreyms.com'
print(sample_url)

# Reverse the url
reverse_url = sample_url[::-1]
# print sample_url
print(reverse_url)


# Get the top level domain
top_level_domain = sample_url[-4:]
# print sample_url
print(top_level_domain)


# Print the url without the http://
url = sample_url[7::1]
# print sample_url
print(url)

# Print the url without the http:// or the top level domain
url_2 = sample_url[7:-4]
# print sample_url
print(url_2)
