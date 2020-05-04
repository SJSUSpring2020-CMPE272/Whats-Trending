# **What's Trending?**
## **Abstract**
What's trending is intended to help Youtubers from different countries to visualize what type of content is the most popular in their country. Our team will acquire data from the top trending Youtube videos from different countries to form visual statistics of the popular video categories, popular video tags and favorable hours to publish videos. Our team will also build a webpage where the user can provide a video id as input and can get to know the polarity of the video. A sentiment analysis is performed at the back end based on the video comments, so that the youtubers can create contents more responsibly without being offensive to anyone. <br><br>
Technology stack: Flask, AWS, Machine Learning algorithm(NLTK Vader SentimentIntensityAnalyzer), Python, Matplotlib, Seaborn, HTML/CSS, Bootstrap


## **Set up virtual environment**
This contains all the packages and dependencies used. 
```
source venv/bin/activate
venv\Scripts\activate
```

If you don't need view website on localhost anymore, deactivate the virtual environment. 
```
deactivate
```


## **View website**
Now that the virtual environment is activated, you can run view the website on localhost:5000. 
```
python3 main.py
python main.py
```

## Build & Run Docker Image 
This step is helpful if you want to save multiple versions of your project and share them with others. Make sure to [install
Docker](https://www.docker.com/products/docker-desktop) first! The key resource used here is the [uWSGI-Nginx-Flask](https://hub.docker.com/r/tiangolo/uwsgi-nginx-flask/)
container-- it combines all 3 applications into one container simpliying the process. We only needed to pull the tag and copy our files into the our
project's container.

We can start by building the image. Make sure to name and tag it so it's easy to reference back to (here the name is *myapp* with *tag* 1.0). When building the image, specify the path or directory that the *Dockerfile*
is located in. In this case, we are already in the same directory as the Dockerfile so we use ' . ' to indicate the current directory. 
```
docker build -t myapp:1.0 .
```

Once complete, you can view your image in your repository. 
```
docker images
```

Now run the image! Use ' -p ' to publish container's port to your host machine. The value on the left side of the colon
means host's port and the right value is the container's port. By default, the container's port is on 80. 
```
docker run -p 80:80 myapp
```

## To get the client_secrets.json
1. Go to [Google Cloud Console](https://console.cloud.google.com) and create a new project. 
2. Enable the YouTube Data API v3.
3. Create credentials (OAuth client ID, Application Type: Other) and download them to `client_secrets.json`.

## **References:**
1. [Modify & Redeploy Cloud Foundry App](https://cloud.ibm.com/docs/starters?topic=starters-download-modify-and-redeploy-your-cloud-foundry-app-with-the-command-line-interface)
2. [Johnafish/senticomment](https://github.com/johnafish/senticomment)
