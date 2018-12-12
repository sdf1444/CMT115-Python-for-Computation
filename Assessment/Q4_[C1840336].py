import sqlite3 as db
import csv
from datetime import date, timedelta
from datetime import datetime
from collections import Counter
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure, show
import pylab

#Run query and the result is stored as 'data'.
#Code adapted from python documentation.
#Accessed 02/12/18.
#https://docs.python.org/3.7/library/sqlite3.html
with db.connect("Q3_sqlite_[C1840336].db") as conn:
    cur = conn.cursor()
    sql = "SELECT ID, Tweet, Created_at, Location, Geo_coordinates, Followers_for_the_user, Friends, Sentiment_analysis FROM Trump"
    cur.execute(sql)
    data = cur.fetchall()
#End of reference.

#Create the csv file.
#Code adapted from python documentation.
#Accessed 02/12/18.
#https://docs.python.org/2/library/csv.html
with open("Q3_csv_[C1840336].csv","a", encoding="utf-8") as f:
    writer = csv.writer(f)
    #Add the header/column names.
    header = ["ID", "Tweet", "Created_at", "Location", "Geo_coordinates", "Followers_for_the_user", "Friends", "Sentiment_analysis"]
    writer.writerow(header)
    #Iterate over 'data' and write to the csv file.
    for row in data:
        writer.writerow(row)
#End of reference.

#Strip out empty rows from "Trump.csv" and write output to "Trump2.csv".
#Code adapted from stackoverflow.
#Accessed 02/12/18.
#https://stackoverflow.com/questions/4521426/delete-blank-rows-from-csv
with open("Q3_csv_[C1840336].csv", "r", encoding="utf-8") as input, open("Q3_csv_[C1840336]2.csv", 'w', encoding='utf-8', newline='') as output:
    writer = csv.writer(output)
    for row in csv.reader(input):
        if any(field.strip() for field in row):
            writer.writerow(row)
#End of reference.

sentiment_analysis = []

pos_neg_neutral = []

#Open "Trump2.csv" and extract the "Sentiment_analysis" row into a list.
with open("Q3_csv_[C1840336]2.csv", encoding="utf-8") as csvFile:
    reader = csv.DictReader(csvFile)
    for row in reader:
        sentiment_analysis.append(row["Sentiment_analysis"])

#Create a list of positive, negative and neutral depending on sentiment analysis value. 
pos_neg_neutral.append("Reaction")

for i in sentiment_analysis:
    if float(i) > 0:
        pos_neg_neutral.append("Positive")
    elif float(i) == 0:
        pos_neg_neutral.append("Neutral")
    else:
        pos_neg_neutral.append("Negative")

#Open "Trump2.csv" and output to "Trump3.csv" everything from "Trump2.csv" and then add a column for pos_neg_neutral list.
with open("Q3_csv_[C1840336]2.csv", 'r', encoding="utf-8") as in_csv, open("Q3_csv_[C1840336]3.csv", 'w', encoding="utf-8") as out_csv:
    reader = csv.reader(in_csv)
    writer = csv.writer(out_csv)
    for row, new_col in zip(reader, pos_neg_neutral):
        row.append(new_col)
        writer.writerow(row)

#Strip out empty rows from "Trump3.csv" and write output to "Trump4.csv".
#Code adapted from stackoverflow.
#Accessed 02/12/18.
#https://stackoverflow.com/questions/4521426/delete-blank-rows-from-csv
with open("Q3_csv_[C1840336]3.csv", "r", encoding="utf-8") as input, open("Q3_csv_[C1840336]4.csv", 'w', encoding='utf-8', newline='') as output:
    writer = csv.writer(output)
    for row in csv.reader(input):
        if any(field.strip() for field in row):
            writer.writerow(row)

#Extract dates, hours and minutes from the "Created_at" column from "Trump4.csv" and create a bar chart of the frequency of the tweets over time.
dates = []

with open("Q3_csv_[C1840336]4.csv", encoding = "utf-8") as csvFile:
    reader = csv.DictReader(csvFile)
    for row in reader:
        #Group by dates, hours and minutes.
        #Code writen using datetime module.
        #Accessed 06/12/18.
        #https://docs.python.org/3/library/datetime.html
        dt = datetime.strptime(row["Created_at"], '%Y-%m-%d %H:%M:%S')
        d = datetime(year=dt.year, month=dt.month, day=dt.day, hour=dt.hour, minute=dt.minute, second=dt.second)
        dates.append(d.strftime("%Y-%m-%d %H:%M"))
        #End of reference.

        #Count the frequncy of the extracted dates, hours and minutes.
        #Code written using a Counter class.
        #Accessed 06/12/18.
        #https://docs.python.org/3/library/collections.html#collections.Counter
        counts = Counter(dates)
        counts2 = dict(sorted(counts.items()))
        #End of reference.

#Bar graph for frequency of tweets over time.
def graph1(Datetime,Frequency):
    plt.bar(range(len(counts2)), list(counts2.values()), align='center')
    plt.xticks(range(len(counts2)), list(counts2.keys()))
    plt.title("Frequency of tweets over time")
    plt.xlabel("Datetime")
    plt.ylabel("Frequency")
    plt.xticks(rotation=13)
    plt.tick_params(axis = 'x', which = 'major', labelsize = 6)
    plt.savefig("Frequency of tweets over time.png")
    plt.close()
graph1("Datetime", "Frequency")

#Extract dates, hours and minutes from the "Created_at" column and the "Reaction" column from "Trump4.csv" and to create a plot of the positive and negative tweets overtime with neutral tweets included.
lst1 = []
lst2 = []

with open("Q3_csv_[C1840336]4.csv", encoding="utf-8") as csvFile:
    reader = csv.DictReader(csvFile)
    for row in reader:
        #Group by dates, hours and minutes.
        #Code writed using datetime module.
        #Accessed 06/12/18.
        #https://docs.python.org/3/library/datetime.html
        dt = datetime.strptime(row["Created_at"], '%Y-%m-%d %H:%M:%S')
        d = datetime(year=dt.year, month=dt.month, day=dt.day, hour=dt.hour, minute=dt.minute, second=dt.second)
        lst1.append(d.strftime("%Y-%m-%d %H:%M"))
        # End of reference.
        lst2.append(row["Reaction"])

#Create a tuple list from lst1 and lst2, create a set and then sort the set.
lst3 = list(zip(lst1, lst2))
s = set(lst3)
s2 = sorted(s)

#Create a dictionary for the sorted set and then count the unique key, value pairs.
#Code adapted from stackoverflow.
#Accessed 06/12/18.
#https://stackoverflow.com/questions/2600191/how-to-count-the-occurrences-of-a-list-item
f = {}
for i in list(s2):
    f[i] = lst3.count(i)
# End of reference.

#Create a 1x1 plot.
#Subplot code adapted from matplotlib.org
#Accessed 06/12/18.
#https://matplotlib.org/api/_as_gen/matplotlib.pyplot.subplot.html
fig = figure()
sub = fig.add_subplot(111)
#End of reference.

#Set the x and y axis.
k = f.keys()
Xs = [i[0] for i in k]
Ys = [i[1] for i in k]

#A plot of the positive and negative tweets overtime with neutral tweets also included. 
def graph2(Datetime,Reaction):
    sub.plot(Xs, Ys, 'bo')
    plt.title("Positive and negative tweets overtime")
    plt.xlabel("Datetime")
    plt.ylabel("Reaction")
    plt.xticks(rotation=13)
    plt.tick_params(axis = 'x', which = 'major', labelsize = 6)
    plt.tick_params(axis = 'y', which = 'major', labelsize = 8.2)

    #Annotate each plot point with the count.
    #Code adapted from stackoverflow.
    #Accessed 06/12/18.
    #https://stackoverflow.com/questions/13268587/how-do-i-annotate-with-a-subscripted-text-in-matplotlib 
    for i in k:
        sub.annotate(f[i], xy=i)
    #End of reference.

    plt.savefig("Positive and negative tweets overtime.png")
    plt.close()
graph2("Datetime", "Reaction")