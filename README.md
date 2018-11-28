# EcoBinTesting

====================================================================================================
Both the raspberry pi setup and the gpu setup were done with the aid of the following tutorials

Raspberry pi
https://github.com/EdjeElectronics/TensorFlow-Object-Detection-on-the-Raspberry-Pi

GPU
https://github.com/EdjeElectronics/TensorFlow-Object-Detection-API-Tutorial-Train-Multiple-Objects-Windows-10

This is by no means the entirety of the code used in the creation of the ECO bin but if all code was to be 
included the size of the repository would be over 3 GB. This is the code we have deemed most applicable and unique
to our project, withstanding a lot of what was included in the tutotorial.

It is worth bearing in mind that none of this code will work when downloaded as it requires multiple dependencies
and for everything to be installed. For the GPU version of Tensorflow it also requires an NVidia GPU as well as 
CUDA toolkit and CUDNN.

If one wanted to test the object detection inference graph they would need to follow the instructions provided above
in the GPU GitHub tutorial and install all relevant dependencies. They could then import the graph as well as the 
labelmap file.

====================================================================================================
It is also worth noting that not all of the images used in training were included. This is due to the fact
that over 200 imaes were used per object. A sample of the images used along with their corresponding xml
documents which describe the object outline have been inclduded.

=============================================WARNING================================================
Tensor flow is extremely petty and setup is not smooth
=============================================WARNING================================================
