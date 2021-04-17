# Timelapse Pi Camera #

A python module to turn a Raspberry Pi into a Timelapse camera node.

## Functions ##

This module will work with [Future Project]() to provide snapshots that will become timelapse videos or gifs. The timelapse server is still under development.

## Development Goals ##

1. Run as a service/docker to take shots from the pi camera based on a config file.
    - [ ] Read config file for timelapse parameters
    - [ ] Utilize picamera to take a snapshot based on imported parameters
    - [ ] Update parameters based off an API or some other form of network input.
    - [ ] Persistent running based out of a service or docker.
    - [ ] Save images into an SMB Share
    - [ ] Save images over the network to the timelapse server
    
