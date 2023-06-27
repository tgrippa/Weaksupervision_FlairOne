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
### Build from Docker image

```
your_local_system$ docker save flair_baseline -o flair_baseline.tar 

singularity build --sandbox flair_baseline docker-archive://flair_baseline.tar
```

### Build from Singularity.def recipe
```
# On your local computer, build a Singularity imagefile (.sif) from the .def file
sudo singularity build flair_baseline.sif Singularity.def

# Transfer it to the cluster using scp command

# On the cluster, creat the image from the imagefile
singularity build flair_baseline flair_baseline.sif
```

### Direct run with NVIDIA GPU
```
# Run the singularity container using cluster GPU (--nv)
singularity run --nv flair_baseline 
```

### Run as service with NVIDIA GPU
```
singularity instance start --nv flair_baseline flair
singularity instance list --logs
cat /home/tgrippa/.singularity/instances/logs/dges-gpu01/tgrippa/flair.err
singularity shell instance://flair
```