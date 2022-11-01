string1 = "Pierwsza linijka tekstu"
string2 = "Zajecia python"

common_list = []
for item in string1:
    if item in string2 and item not in common_list:
        common_list.append(item)

print(common_list)
final_list = list(set(string1 + string2))
print(final_list)
