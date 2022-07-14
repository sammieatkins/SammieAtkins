import operator
import csv

# markdict = {"Tom":67, "Tina": 54, "Akbar": 87, "Kane": 43, "Divya":73}
# marklist= sorted(markdict.items(), key=operator.itemgetter(1)) 
# sortdict=dict(marklist)
# print(sortdict)

# markdict = {"Tom":67, "Tina": 54, "Akbar": 87, "Kane": 43, "Divya":73}
# marklist = sorted(markdict.items(), key=lambda x:x[1])
# sortdict = dict(marklist)
# print(sortdict)

# orders = {
# 	'cappuccino': 54,
# 	'latte': 56,
# 	'espresso': 72,
# 	'americano': 48,
# 	'cortado': 41
# }

# sort_orders = sorted(orders.items(), key=lambda x: x[1], reverse=True)

# for i in sort_orders:
# 	print(i[0], i[1])

books_dict = {}
with open("books.csv") as file:
    reader = csv.reader(file)
    next(reader)
    for row_list in reader:
        if len(row_list) != 0:
            key = row_list[0]
            books_dict[key] = row_list[1:len(row_list) - 1]

# sort_author = sorted(books_dict.items(), key=lambda x: x[1], reverse=True)
# for i in sort_author:
#     print(i[0], i[1])

def main():
    print_dict(books_dict)

def print_dict(dictionary):
    for line in dictionary:
        print(line)

# books_list = sorted(books_dict.items(), key=lambda x:x[0])
# sortdict = dict(books_list)
# print(sortdict)

main()