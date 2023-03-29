Build the Docker image
```
# To build the image with your user name UID and GID 
docker build --build-arg UNAME=$USER --build-arg UID=$(id -u) --build-arg GID=$(id -g) -t grass_r_jupyter .
```

Launch the Docker container with mapping of port 88888, volumes and display capabilities
```
docker run -p 8888:8888 -v "/media/tais/data/FNRS_processing/FLAIR_WeakSupervision/FLAIR_One_Dataset/subset_dataset:/home/tais/data" -v "/media/tais/data/FNRS_processing/FLAIR_WeakSupervision/git_repo:/home/tais/github" -v "/media/tais/data/FNRS_processing/FLAIR_WeakSupervision/GRASSDATA:/home/tais/GRASSDATA" -v "/media/tais/data/FNRS_processing/FLAIR_WeakSupervision/results_grassgis:/home/tais/result" -v /tmp/.X11-unix:/tmp/.X11-unix -e DISPLAY=unix$DISPLAY --name grass grass_r_jupyter
```

Launch GRASS GIS graphical user interface **in another terminal**.
```
sudo docker exec -it grass bash
grass@CONTENER_ID:~$ grass
```
