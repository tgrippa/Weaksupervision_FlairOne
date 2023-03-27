## Docker

Build the Docker image
```
cd DL/FLAIR_Baseline
docker build -t flair_baseline .
```

Launch the Docker container (in detached mode) with mapping of port 88888, volumes and display capabilities
```
docker run -d --name tais -p 8888:8888 -v /media/tais/data/FNRS_processing/FLAIR_WeakSupervision/:/home/tais --runtime=nvidia flair_baseline
```

Check the log of the contained to find the tokenized URL to  access the jupyter lab 
```
docker logs tais
```

Monitor the GPU usage with nvidia-smi **in another terminal tab**.
```
docker exec -it tais watch -n 1 nvidia-smi
```



## Singularity

```
your_local_system$ docker save flair_baseline -o flair_baseline.tar 

singularity build --sandbox flair_baseline docker-archive://flair_baseline.tar
```



