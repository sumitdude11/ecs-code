"""Routines associated with the application data.
"""
import json
import csv
f = open("D:\ecs\course.json","r")
data = json.load(f)
fields = ["id","date_created","date_updated","description","discount_price","image_path","on_discount","price","title"]
filename = "ecs_data2.csv"
courses = {}
with open(filename, 'w',newline="") as csvfile:
    # creating a csv writer object
    csvwriter = csv.writer(csvfile)

    # writing the fields
    csvwriter.writerow(fields)

    # writing the data rows
    for i in data:
        if(i.values==""):
            csvwriter.writerow("")
        csvwriter.writerow(i.values())


def load_data():
    """Load the data from the json file.
    """
    f = open("D:\ecs\course.json","r")
    data = json.load(f)
    fields = ["id","date_created","date_updated","description","discount_price","image_path","on_discount","price","title"]
    filename = "ecs_data2.csv"
    courses = {}
    course = []
    with open(filename, 'w',newline="") as csvfile:
        # creating a csv writer object
        csvwriter = csv.writer(csvfile)

        # writing the fields
        csvwriter.writerow(fields)

        # writing the data rows
        for i in data:
            if(i.values==""):
                csvwriter.writerow("")
            csvwriter.writerow(i.values())
        file = "ecs_data2.csv"
    field=[]
    with open(file,'r') as csvfile:
        csvreader = csv.reader(csvfile)
        field = next(csvreader)
        for a in csvreader:
            if(a[8] not in courses):
                course.append(a[8])
                print(a[8])


    pass


