import json
import csv

data = []
with open("test-data.json", "r") as fp:
    temp = fp.read()
    data = json.loads(temp)

#     temp[service["table_name"]] = [i for n, i in enumerate(
                    #         temp[service["table_name"]]) if i not in
                    #         temp[service["table_name"]][:n]]

duplicates = [i for n, i in enumerate(data) if i in data[:n]]
unique = [i for n, i in enumerate(data) if i not in data[:n]]
# print(temp)
with open("actual-data-2.csv","w+") as my_csv:
    csvWriter = csv.writer(my_csv,delimiter=',')
    csvWriter.writerows(data)

with open("duplicate-2.csv","w+") as my_csv:
    csvWriter = csv.writer(my_csv,delimiter=',')
    csvWriter.writerows(duplicates)

with open("unique-2.csv","w+") as my_csv:
    csvWriter = csv.writer(my_csv,delimiter=',')
    csvWriter.writerows(unique)