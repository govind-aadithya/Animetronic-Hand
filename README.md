# Animetronic-Hand

## Objective
Gesture controlled animetronic hand intended to perform teleoperation. 

The project was developed as a proof of concept for teleoperation using gesture tracking.

## Purpose
This was a concept developed for a Hardware Hackathon "Byte into Hardware" held at NJIT on April'23. The theme of the hackathon was to empower accessibility for differently abled. 

## Hardware
1. 3D Printed Animetronic Hand
2. Tower Pro Servos (SG90)
3. Logitech Web Cam
4. Arduino
5. IMU - MPU6050.

## Approach
The project uses Computer Vision to perform gesture tracking and interpret the geture made by the user. This is then sent to the Arduino as actuation commands to make the animetronic hand replicate the gesture.
To complete the loop, we used a logitech webcam to provide a video feed to the user by couping it with servos for yaw control. The command to the yaw control is given via an IMU that tracks the yaw of the user's head.

### Architecture
![Architecture](/images/Archi.png)

## Animetronic Hand
The .stp file was developed and printed on a Ultimaker 3D Printer. Since on slicing the file, the print duration was over 48hrs, the print was spit in several parts and prited on multiple printers.
The files can be found in the [CAD folder](./CAD) of the project.

![3D Printed Parts](/images/3d_printed_parts.png)

![Final Assembly](/images/Assembled_hand.png)

## Gesture Tracking and Control
In order to track the gesture, the project leverages the [Mediapipe](https://developers.google.com/mediapipe/solutions/vision/hand_landmarker/python) package to locate the keypoints. Once the keypoints are obtained we perform a caliberation to eliminate scaling and map the movements of the keypoints from the fingers to obtain the degree of actuation. This is then sent to Arduino as servo actuation commands to actuate the animetronic hand. 

![Gesture Tracking](/images/gesture.gif)

The [video](https://www.youtube.com/watch?v=KrDJfOwzTok) shows the tracking along with the caliberatio process and servo command generation.
