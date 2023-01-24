# base image  
FROM python:3.9-alpine
# setup environment variable  
ENV DockerHOME=/home/app/webapp  

# set work directory  
RUN mkdir -p $DockerHOME  

# where your code lives  
WORKDIR $DockerHOME  

# set environment variables  
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1  

# install dependencies  
RUN pip install --upgrade pip  

# copy whole project to your docker home directory. 
COPY . $DockerHOME  
# run this command to install all dependencies  
RUN pip install -r requirements.txt  
# port where the Django app runs  
EXPOSE 8002
# start server
CMD python manage.py makemigrations
RUN echo "make migration"
CMD python manage.py migrate --run-syncdb
RUN echo "make sync"
CMD python manage.py createsuperuser
RUN echo "make super user"
CMD python manage.py runserver 0.0.0.0:8002
RUN echo "done"