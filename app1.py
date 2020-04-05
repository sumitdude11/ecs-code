import mysql.connector
from flask import Flask, render_template, request
import numpy as np
from sklearn import linear_model
import pandas as pd
import sys

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("index.html")

@app.route('/check',methods=['POST'])
def check1():
    print("hello ")
    d1 = str(request.form["n1"])
    d2 = str(request.form["n3"])
    d6 = str(request.form.get("n2"))
    print(d6)

#for database

#for csv
    import csv
    filename = "INvideos.csv"
    fields = []
    rows = []


    with open(filename,'r',encoding="utf8") as csvfile:
        csvreader = csv.reader(csvfile)
        fields.append(next(csvreader))
        for row2 in csvreader:
            if(int(row2[8])>70000 and row2[1]==d1):
                print(22)
                if (("Teaser" in row2[15]) or ("Trailer" in row2[15])):
                    if((d2=="teaser" or d2=="all")):
                        print(2)
                        row2.append("teaser")
                        rows.append(row2)
                        conn = mysql.connector.connect(host="localhost", user="root", password="", db="projectdb")
                        cursor = conn.cursor()
                        print(6)
                        cursor.execute(
                            "insert into datadb(video_id,trending_date,views,title,likes,dislike,comment,category) values('" +
                            row2[0] + "','" + row2[1] + "','" + row2[7] + "','" + row2[2] + "','" + row2[8] + "','" + row2[
                                9] + "','" + row2[10] + "','teaser'"")")

                        conn.commit()
                elif (("comedy" in row2[15]) or ("Funny" in row2[15])):
                    if ((d2 == "comedy" or d2=="all")):
                        print(2)
                        row2.append("comedy")
                        rows.append(row2)
                        conn = mysql.connector.connect(host="localhost", user="root", password="", db="projectdb")
                        cursor = conn.cursor()
                        print(6)
                        cursor.execute(
                            "insert into datadb(video_id,trending_date,views,title,likes,dislike,comment,category) values('" +
                            row2[0] + "','" + row2[1] + "','" + row2[7] + "','" + row2[2] + "','" + row2[8] + "','" + row2[
                                9] + "','" + row2[10] + "','funny'"")")

                        conn.commit()


                elif(("song" in row2[15]) or ("Song" in row2[15]) ):
                    if ((d2 == "song" or d2=="all")):
                        print(2)
                        row2.append("song")
                        rows.append(row2)
                        conn = mysql.connector.connect(host="localhost", user="root", password="", db="projectdb")
                        cursor = conn.cursor()
                        print(6)
                        cursor.execute("insert into datadb(video_id,trending_date,views,title,likes,dislike,comment,category) values('" + row2[0]+"','"+row2[1]+"','"+row2[7]+"','"+row2[2]+"','"+row2[8]+"','"+row2[9]+"','"+row2[10]+"','song'"")")

                        conn.commit()

                elif(("movie" in row2[15]) or ("Film" in row2[15]) or ("film" in row2[15]) or ("Movie" in row2[15])):
                    if ((d2 == "movie" or d2=="all")):
                        print(2)
                        row2.append("movie")
                        rows.append(row2)
                        conn = mysql.connector.connect(host="localhost", user="root", password="", db="projectdb")
                        cursor = conn.cursor()
                        print(6)
                        cursor.execute(
                            "insert into datadb(video_id,trending_date,views,title,likes,dislike,comment,category) values('" +
                            row2[0] + "','" + row2[1] + "','" + row2[7] + "','" + row2[2] + "','" + row2[8] + "','" + row2[
                                9] + "','" + row2[10] + "','movie'"")")

                        conn.commit()

                elif(("news" in row2[15]) or ("News" in row2[15])):
                    if ((d2 == "news" or d2=="all")):
                        print(2)
                        row2.append("news")
                        rows.append(row2)
                        conn = mysql.connector.connect(host="localhost", user="root", password="", db="projectdb")
                        cursor = conn.cursor()
                        print(6)
                        cursor.execute(
                            "insert into datadb(video_id,trending_date,views,title,likes,dislike,comment,category) values('" +
                            row2[0] + "','" + row2[1] + "','" + row2[7] + "','" + row2[2] + "','" + row2[8] + "','" +
                            row2[9] + "','" + row2[10] + "','news'"")")
                        conn.commit()

                elif(d2=="other" or d2=="all"):
                    print(2)
                    row2.append("others")
                    rows.append(row2)
                    conn = mysql.connector.connect(host="localhost", user="root", password="", db="projectdb")
                    cursor = conn.cursor()
                    print(6)
                    cursor.execute(
                        "insert into datadb(video_id,trending_date,views,title,likes,dislike,comment,category) values('" +
                        row2[0] + "','" + row2[1] + "','" + row2[7] + "','" + row2[2] + "','" + row2[8] + "','" + row2[
                            9] + "','" + row2[10] + "','others'"")")

                    conn.commit()


    return render_template("page2.html",data=rows)


if __name__ == '__main__':
    app.run()
