str1 = "hello radhika"

reverse_str = ""
for i in range(len(str1) - 1, -1, -1):
    reverse_str += str1[i]

print("string:", str1)
print("reversed string:", reverse_str)