import re, os

path = 'C:\\Users\\Antonina\\Desktop\\card\\books\\'

first_list = [x for x in os.listdir(path)]

with open('files_list.txt', 'a', encoding="utf-8") as f:
	for x in os.listdir(path):
		f.write(x)

filtered_list = [f for f in first_list if re.search(r'(\w)(20\d\d)?([.]pdf|epub|docx|doc)', f)]

print(filtered_list)	
	
for n in filtered_list:
	a = n.split(".")
	for b in range(1, 3):
		duplicate = "%s(%d)%s" % (a[:-1], b, a[-1])
		duplicate.join(",")
		print(duplicate)
		if duplicate in first_list:
			print(duplicate)



