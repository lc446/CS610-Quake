# CS610-Midterm-Project
### Created by Lucca Cioffi

## This is a Docker Quake Server with custom map loading!

The Docker server pulls the [latest MVDSV](https://github.com/QW-Group/mvdsv/releases/latest/) and [latest ktx](https://github.com/QW-Group/ktx/releases/latest)

MVDSV is the actual server running, and KTX is what is used for the qwprogs.so file (game logic)

Since it is **illegal to distribute the pak1 file** as that is owned by iD Software, this upload contains a LibreQuake pak0 and pak1 instead. 

[Latest LibreQuake can be found here.](https://github.com/lavenderdotpet/LibreQuake/releases/latest)
It does NOT automatically pull new pak files if future LibreQuake releases come out.

If you want to use the official pak files, purchase Quake from a storefront such as Steam or GOG.

Steam: https://store.steampowered.com/app/2310/Quake/

GOG: https://www.gog.com/en/game/quake_the_offering

## Instructions:

# !!!IMPORTANT!!! 

#### Before you run this image and create a container, you need to supply your pak1.pak (if you purchased Quake) and any custom maps you would like to load. 
If you are loading a custom map, I highly recommend you modify the default server settings to load your map on launch.
```
basedir (contains DOCKER file)
|-/id1 (pak files, and server config)
   |-/maps (your custom maps)
```
#### Place your PAK files in \id1 like you would for a client installation of Quake

The server config is in \id1
Maps need to be in: \id1\maps

Once your files are placed where they need to be, navigate to the base directory where the DOCKERFILE is.

#### Build the image:
```
docker build -t cs610quake .
``` 

#### Run the container using that image:
```
docker run -d -p 27500:27500/udp cs610quake
```

To test your maps out, launch a QuakeWorld client (this was tested on ezQuake) and connect to localhost (the default port on a fresh install of ezQuake should already be 27500)

You can do so by hitting the tilde key (~) to open the console, then run the command in ezQuake
```
connect localhost
```

Enjoy!

![Lucca loaded into his server on a custom map](coolcubes-server.png)