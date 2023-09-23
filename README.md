# Animatronic-Hand

## Objective
Gesture-controlled animatronic hand intended to perform teleoperation. 

The project was developed as a proof of concept for teleoperation using gesture tracking.

## Purpose
This was a concept developed for a Hardware Hackathon "Byte into Hardware" held at NJIT in April'23. The theme of the hackathon was to empower accessibility for differently abled. 

## Hardware
1. 3D Printed Animatronic Hand
2. Tower Pro Servos (SG90)
3. Logitech Web Cam
4. Arduino
5. IMU - MPU6050.

## Approach
The project uses Computer Vision to perform gesture tracking and interpret the gestures made by the user. This is then sent to the Arduino as actuation commands to make the Animatronic hand replicate the gesture.
To complete the loop, we used a Logitech webcam to provide a video feed to the user by coupling it with servos for yaw control. The command to the yaw control is given via an IMU that tracks the yaw of the user's head.

### Architecture
![Architecture](/images/Archi.png)

## Animatronic Hand
The .stp file was developed and printed on an Ultimaker 3D Printer. Since on slicing the file, the print duration was over 48hrs, the print was spit in several parts and printed on multiple printers.
The files can be found in the [CAD folder](./CAD) of the project.

![3D Printed Parts](/images/3d_printed_parts.png)

![Final Assembly](/images/Assembled_hand.png)

## Gesture Tracking and Control
In order to track the gesture, the project leverages the [Mediapipe](https://developers.google.com/mediapipe/solutions/vision/hand_landmarker/python) package to locate the keypoints. Once the keypoints are obtained, we perform a calibration to eliminate scaling and map the movements of the keypoints from the fingers to obtain the degree of actuation. This is then sent to Arduino as servo actuation commands to actuate the Animatronic hand.

![Gesture Tracking](/images/gesture.gif)

The [video](https://www.youtube.com/watch?v=KrDJfOwzTok) shows the tracking along with the calibration process and servo command generation.

The complete video showing the process from start to finish can be found [here](https://youtu.be/Sb4F23Tmr3c?si=_DHQ8RgZvzNWH9Fh).
