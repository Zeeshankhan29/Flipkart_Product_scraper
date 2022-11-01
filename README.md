# **Project** - Flipkart Scrapping & Storing in Mysql ,Mongodb for Analysis

This project is designed to search any Product in Flipkart website and ultimately store the data in the Databases like Mysql and Mongodb for Analysis ....... Please refer the video for better understanding

Github_link - https://lnkd.in/gXe2T8K5


Scraper_details would look something like this
![image](https://user-images.githubusercontent.com/95518247/199228695-84007d1b-96c6-4677-bb64-17c76ee3d7c5.png)



#python #pythonprogramming #pythonlearning #dataanalysis #dataextraction #dataanalytics #datamodeling #businessanalysis #businessanalytics #mysql #mongodb


To check docker version
```
dockers --version
```
To build docker we use
```
docker build .
```
To give the name to the docker image we use
```
docker build . -t <tag_name>
```
We must follow this heirarcy
```
FROM python:3.9
RUN mkdir /app
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
CMD python app.py
```
We check the docker images we use
```
docker images
```
#To push your image to docker hub

we must login to docker hub
```
docker login
```
After login we follow

```
docker tag <repository_name>:<tag> <username>/<repository_name> 
docker push <username>/<repository_name>
wait for the upload
```
To pull docker image we follow

```
docker pull <user_name>/<repository_name>
```

To Run docker image 

```
docker run -p 5000:5000  <docker image id> or <repository name>
```
To check running docker containers
```
docker ps
```
To stop docker container

```
docker stop <container_id>

```


# **You can run this project using Dockers image**

You can pull the docker image and run it in the docker container using the following command 
in your terminal
```
docker pull zeeshankhan29/scraper

```




# **Conclusion:**

1.This project can be used in real time  and can be used to  Analyse, making Bussineess Decision.

2.Using this project we can store the data either in Mongodb or in Mysql.



