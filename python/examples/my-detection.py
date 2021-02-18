#!/usr/bin/python3
#
# Copyright (c) 2019, NVIDIA CORPORATION. All rights reserved.
#
# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the "Software"),
# to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.  IN NO EVENT SHALL
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
# DEALINGS IN THE SOFTWARE.
#

import jetson.inference
import jetson.utils

gst_str = str("nvarguscamerasrc ! video/x-raw(memory:NVMM), width=(int)%d, height=(int)%d, format=(string)NV12, framerate=(fraction)%d/1 ! " +
            "nvvidconv ! video/x-raw, format=(string)BGRx ! " +
			"videoconvert ! video/x-raw, format=(string)BGR ! " +
			"appsink")

gst_str = gst_str % (2592, 1458, 30)

gst_str = "nvarguscamerasrc ! video/x-raw(memory:NVMM), width=(int)1280, height=(int)720, framerate=(fraction)120/1, format=(string)NV12 ! nvvidconv flip-method=2 ! video/x-raw ! appsink name=mysink"

# net = jetson.inference.detectNet("ssd-mobilenet-v2", threshold=0.5)
camera = jetson.utils.videoSource(gst_str)      # '/dev/video0' for V4L2
display = jetson.utils.videoOutput("display://0") # 'my_video.mp4' for file

while display.IsStreaming():
	img = camera.Capture()
	print(img)
	# detections = net.Detect(img)
	# display.Render(img)
	# display.SetStatus("Object Detection | Network {:.0f} FPS".format(net.GetNetworkFPS()))
