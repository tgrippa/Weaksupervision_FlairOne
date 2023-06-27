Build the Docker image
```
cd DL/
docker build -t weaksuper_tf2_gpu .
```

Launch the Docker container with mapping of port 88888, volumes and display capabilities
```
docker run -p 8888:8888 -v "/media/tais/data/Dropbox/ULB/Boite_a_outils_geographe/DONNEES/Remote Sensing/ISPRS_Contest_Vaihingen/Vaihingen:/home/tais/data" -v "/media/tais/data/FNRS_processing/Vaihingen_WeakSupervision/git_repo:/home/tais/github" -v "/media/tais/data/FNRS_processing/Vaihingen_WeakSupervision/result:/home/tais/result" --runtime=nvidia --name tf2_gpu weaksuper_tf2_gpu
```

Monitor the GPU usage with nvidia-smi **in another terminal tab**.
```
docker exec -it tf2_gpu watch -n 1 nvidia-smi
```
