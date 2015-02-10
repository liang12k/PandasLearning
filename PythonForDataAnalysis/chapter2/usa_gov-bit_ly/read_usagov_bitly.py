import json

path = "usagov_bitly_data2012-03-16-1331923249.txt"
# print open(path).readline()

# # list comprehension; json loads collection of strings
records = [json.loads(line) for line in open(path)]
print records[0]
