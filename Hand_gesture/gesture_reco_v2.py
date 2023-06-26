import cv2
import mediapipe as mp
import numpy as np
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands

calib = 0
print_count=0
out_min =  np.zeros((5,1))
out_max =  np.ones((5,1))*180

# For webcam input:
cap = cv2.VideoCapture(0)
with mp_hands.Hands(model_complexity=0,
		    min_detection_confidence=0.5,
		    min_tracking_confidence=0.5) as hands:
	while cap.isOpened():
		success, image = cap.read()
		if not success:
			print("Ignoring empty camera frame.")
			# If loading a video, use 'break' instead of 'continue'.
			continue

		# To improve performance, optionally mark the image as not writeable to
		# pass by reference.
		image.flags.writeable = False
		image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
		results = hands.process(image)
		#print(type(results))
		# Draw the hand annotations on the image.
		image.flags.writeable = True
		image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)



		if results.multi_hand_landmarks:
			#print (results.multi_hand_landmarks)
			for hand_landmarks in results.multi_hand_landmarks:
				

###############################################################################   Calib Sequense   ###################################################################################################

				if (calib<2):
					if(calib==0 and print_count==0):
						print("****************************Start Caliberation sequence********************************")
						print("Keep Hand in open condition")
						print("Press 'q' to continue")
						print_count+=1
					elif(calib==1 and print_count==1):						
						print("Keep Hand in fully close condition")
						print("Press 'q' to continue")							
						print_count+=1

						print("calib: ", calib)
						print("print_count: ", print_count)
					
					if (cv2.waitKey(5) & 0xFF == ord('q')):
					
						print("calib: ", calib)
						print("print_count: ", print_count)					
						
						if(calib==0):
							calib+=1	 
							max_dist = curr_dist
							zc = wrist[2]
							   
							print("Max = ", max_dist)						
							#print("Open Condition:")
							#print(open_condition)		
						elif(calib==1):
							calib+=1		
							min_dist = curr_dist					
							print("Min = ", min_dist)
							#print()
							print("****************************Finishing Caliberation sequence********************************")
				elif(calib==2):
					z = wrist[2]
					if z > zc:					
						alpha =   zc/z
					elif z < zc:
						alpha =  -z/zc
					else:
						alpha = 1
					alpha = 1
					
					mapped = (alpha*((curr_dist - min_dist) * (out_max - out_min) / (max_dist - min_dist) + out_min));
					'''for i in range(len(mapped)):
						if mapped[i] > 180:
							mapped[i] = 180
						elif mapped[i] < 0:
							mapped[i] = 0
						else:
							mapped[i] = int(mapped[i])'''
					print(mapped)
					#print(fingertip)
#################################################################################  Calib sequense End #############################################################################################		   
				
				
#################################################################################   Finger Bend Calculation  ######################################################################################
				wrist = [hand_landmarks.landmark[mp_hands.HandLandmark.WRIST].x,hand_landmarks.landmark[mp_hands.HandLandmark.WRIST].y,hand_landmarks.landmark[mp_hands.HandLandmark.WRIST].z]
				fingertip = [[hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].x,hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].y], 
					     [hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].x,hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y],
					     [hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].x,hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].y],
					     [hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP].x,hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP].y],
					     [hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP].x,hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP].y]]
				
					
				motion = [[fingertip[0][0]-wrist[0],fingertip[0][1]-wrist[1]],
					  [fingertip[1][0]-wrist[0],fingertip[1][1]-wrist[1]],
					  [fingertip[2][0]-wrist[0],fingertip[2][1]-wrist[1]],
					  [fingertip[3][0]-wrist[0],fingertip[3][1]-wrist[1]],
					  [fingertip[4][0]-wrist[0],fingertip[4][1]-wrist[1]]]	
				curr_dist = np.zeros((5,1))
				
				
#################################################################################   Finger Bend Calculation End ###################################################################################
				for i in range(len(motion)):
					curr_dist[i] = np.sqrt(np.square(motion[i][0]) + np.square(motion[i][1])) 	   
							
#################################################################################   Mapping Calculation  ######################################################################################
				#for tip_data in motion: 
					#distance = 

#################################################################################   Mapping Calculation End ###################################################################################
				
				mp_drawing.draw_landmarks(
				    image,
				    hand_landmarks,
				    mp_hands.HAND_CONNECTIONS,
				    mp_drawing_styles.get_default_hand_landmarks_style(),
				    mp_drawing_styles.get_default_hand_connections_style())
		# Flip the image horizontally for a selfie-view display.
		cv2.imshow('MediaPipe Hands', cv2.flip(image, 1))
		if cv2.waitKey(5) & 0xFF == 27:
			break
cap.release()

