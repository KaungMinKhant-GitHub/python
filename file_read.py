file = open('./test.txt')

# for line in file:
#     print(line)

# list_read = file.readlines()
# print(list_read)

s = file.seek(4)
read_file = file.read(100)
print(read_file)