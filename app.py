from flask import Flask, render_template, request,jsonify
from flask_cors import CORS,cross_origin
import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
from urllib.request import urlopen as uReq
# import mysql.connector as conn
import pymongo as py




app = Flask(__name__)

@app.route('/',methods=['GET'])  # route to display the home page
@cross_origin()
def homePage():
    return render_template("index.html")

@app.route('/review',methods=['POST','GET']) # route to show the review comments in a web UI
@cross_origin()
def index():
    if request.method == 'POST':
        data=request.form.items()
        data=dict(data)
        search=data['content']
        No_of_pages=int(data['No_of_pages'])

        url = []
        reviews = []
        for i in range(1, No_of_pages + 1):
            search = search.replace(' ', '')
            url.append('https://www.flipkart.com/search?q=' + search + '&page=' + str(i))
            for j in url:
                uClient = uReq(j)
                flipkart_page = uClient.read()
                html = bs(flipkart_page, 'html.parser')
                box = html.find_all('div', {'class': "_1AtVbE col-12-12"})
                del box[0:3]
                for k in range(len(box) - 5):
                    link = box[k].div.div.div.a['href']
                    product_link = 'https://www.flipkart.com' + link
                    link = requests.get(product_link)
                    link = link.text
                    html1 = bs(link, 'html.parser')

                    try:
                        boxes = html1.find_all('div', {'class': "aMaAEs"})
                        Product_description = boxes[0].div.h1.text
                    except:
                        Product_description = 'No Product found'

                    try:
                        boxes = html1.find_all('div', {'class': "_25b18c"})
                        Product_price = boxes[0].div.text
                    except:
                        Product_price = 'No Price found'

                    try:
                        boxes = html1.find_all('div', {'class': "_3LWZlK"})
                        Average_rating = boxes[0].text
                    except:
                        Average_rating = 'No rating found'

                    boxes1 = html1.find_all('div', {'class': "col _2wzgFH"})

                    Customer_comment = []
                    Customer_rating = []
                    Customer_full_comment = []
                    Customer_location = []
                    Customer_name = []
                    for k in range(len(boxes1)):
                        try:
                            Customer_comment.append(boxes1[k].find('p', {"class": "_2-N8zT"}).text)
                        except:
                            Customer_comment = 'No comment found'
                        try:
                            Customer_rating.append(boxes1[k].div.div.text)
                        except:
                            Customer_rating = 'No rating found'
                        try:
                            Customer_full_comment.append(boxes1[k].find('div', {'class': "t-ZTKy"}).div.text)
                        except:
                            Customer_full_comment = 'No comment found'
                        try:
                            Customer_location.append(boxes1[k].find('p', {'class': '_2mcZGG'}).text.split()[2])
                        except:
                            Customer_location = 'No location found'

                        try:
                            Customer_name.append(boxes1[k].find('p', {'class': "_2sc7ZR _2V5EHH"}).text)
                        except:
                            Customer_name = 'No Name found'

                    mydict = {'Product_Description': Product_description, 'Product_Price': Product_price,
                              'Average_Rating': Average_rating
                        , 'Customer_Comment': Customer_comment, 'Customer_Rating': Customer_rating,
                              'Customer_Full_Comment': Customer_full_comment,
                              'Customer_Location': Customer_location, 'Customer_Name': Customer_name}
                    reviews.append(mydict)


        #             try:
        #                 mydb = conn.connect(host='localhost', user='root', passwd='snzk@#1329')
        #                 cursor = mydb.cursor()
        #                 cursor.execute('create database Flipkart_website')
        #                 cursor.execute('use Flipkart_website')
        #                 cursor.execute('create table Scrapped_details(Product_Description varchar(3000),Product_Price varchar(50),Average_Rating varchar(50),Customer_Comment varchar(2000),Customer_Rating varchar(50),Customer_Full_Comment varchar(7000),Customer_Location varchar(2000),Customer_Name varchar(2000))')
        #                 mydb.commit()
        #                 cursor.execute('insert into Scrapped_details values (%s,%s,%s,%s,%s,%s,%s,%s)', (Product_description, Product_price, Average_rating, str(Customer_comment), str(Customer_rating),
        #                 str(Customer_full_comment), str(Customer_location), str(Customer_name),))
        #                 mydb.commit()
        #                 cursor.fetchall()
        #
        #             except:
        #                 cursor.execute('use Flipkart_website')
        #                 cursor.execute('insert into Scrapped_details values (%s,%s,%s,%s,%s,%s,%s,%s)', (Product_description, Product_price, Average_rating, str(Customer_comment), str(Customer_rating),
        #                 str(Customer_full_comment), str(Customer_location), str(Customer_name),))
        #                 mydb.commit()
        #                 cursor.fetchall()
        # try:
        #     client = py.MongoClient("mongodb+srv://mongodb:mongodb@cluster0.gc1mb.mongodb.net/?retryWrites=true&w=majority")
        #     db = client['Flipkart_website']
        #     col = db['Scrapped_details']
        #     col.insert_many(reviews)
        # except Exception as e:
        #     print(e)

        df = pd.DataFrame(reviews)
        columns = list(df.columns)
        reviews1 = [[df.loc[i, col] for col in df.columns] for i in range(len(df))]
        return render_template('results.html', titles=columns, rows=reviews1)
    else:
        return render_template('index.html')

if __name__ == "__main__":
    app.run(port=8000)
