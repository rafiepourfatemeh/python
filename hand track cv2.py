import cv2
import mediapipe as mp
import time
cap=cv2.VideoCapture(0)        
mp_hands=mp.solutions.hands
hands=mp_hands.Hands()
mp_draw=mp.solutions.drawing_utils
while True:
    done,frame=cap.read()
    color=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    results=hands.process(color)
    if (results.multi_hand_landmarks):
        for hand_landmarks in results.multi_hand_landmarks:
            for lm in hand_landmarks.landmark:
                height,width,channel=frame.shape
                x,y=int(lm.x*width),int(lm.y*height)
                cv2.circle(frame,(x,y),10,(255,0,255),cv2.FILLED)
            mp_draw.draw_landmarks(frame,hand_landmarks,mp_hands.HAND_CONNECTIONS)
        cv2.imshow("captured frame",frame)                         
    if cv2.waitKey(1)==ord("q"):
        break
        cv2.destroyAllWindows()
        cap.release()