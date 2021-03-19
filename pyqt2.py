import json
import csv

f = open('C:\Users\hp\PycharmProjects\ecs_code\static\challenge\json\course.json',"r")
data = json.load(f)
fields = ["id","date_created","date_updated","description","discount_price","image_path","on_discount","price","title"]
filename = "ecs_data.csv"
with open(filename, 'w',newline="") as csvfile:
    # creating a csv writer object
    csvwriter = csv.writer(csvfile)

    # writing the fields
    csvwriter.writerow(fields)

    # writing the data rows
    for i in data:
        csvwriter.writerow(i.values())
