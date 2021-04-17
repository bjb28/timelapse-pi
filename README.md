# Timelapse Pi Camera #

![GitHub](https://img.shields.io/github/license/bjb28/timelapse-pi)
[![Coverage Status](https://coveralls.io/repos/github/bjb28/timelapse-pi/badge.svg?branch=main)](https://coveralls.io/github/bjb28/timelapse-pi?branch=main)
[![Total alerts](https://img.shields.io/lgtm/alerts/g/bjb28/timelapse-pi.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/bjb28/timelapse-pi/alerts/)
[![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/bjb28/timelapse-pi.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/bjb28/timelapse-pi/context:python)

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
   

## License ##

This is [CC0 1.0 Universal](https://github.com/bjb28/timelapse-pi/blob/main/LICENSE)
