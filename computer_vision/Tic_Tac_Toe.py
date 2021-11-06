Skip to content
Search or jump to…
Pull requests
Issues
Marketplace
Explore
 
@topguns837 
topguns837
/
Tic_Tac_Toe
Public
1
10
Code
Issues
Pull requests
Actions
Projects
Wiki
Security
Insights
Settings
Tic_Tac_Toe/main4.py /
@topguns837
topguns837 Add files via upload
Latest commit c917dc9 20 days ago
 History
 1 contributor
198 lines (128 sloc)  6.59 KB
   
import cv2
from cvzone.HandTrackingModule import HandDetector
from time import sleep
import numpy as np
import pandas as pd

board=np.array([["","",""],["","",""],["","",""]])

def winner(board):
    for i in range(0,3):
        if board[i][0]==board[i][1]==board[i][2]!="":
            return [1,board[i][0]] 
        elif board[0][i]==board[1][i]==board[2][i]!="":
            return [1,board[0][i]]

    if board[0][0]==board[1][1]==board[2][2]!="":
        return [1,board[0][0]]

    if board[0][2]==board[1][1]==board[2][0]!=""  :
        return  [1,board[1][1]]

    return [0,"0"]            



cap=cv2.VideoCapture(1)
cap.set(3,1920)
cap.set(4,1080)


detector=HandDetector(detectionCon=0.8)



finalText_11,finalText_12,finalText_13,finalText_21,finalText_22,finalText_23,finalText_31,finalText_32,finalText_33,="","","","","","","","",""



tic_tac=[]



count=0

while True:
    success,img=cap.read()
    img=detector.findHands(img)

    lmList,bboxinfo=detector.findPosition(img)
    

    if lmList:
        
        x_hand,y_hand=lmList[8][0],lmList[8][1]

        
        if "1"=="1":
               

            l,_,_=detector.findDistance(8,12,img)
               
            if l<60:

                    

                    
                sleep(0.5)
                    
                if 450<x_hand<600 and 50<y_hand<150:
                    if len(tic_tac)%2==0:
                        finalText_11,board[0][0]="X","X"
                        tic_tac.append("X")
                            
                    else:
                        finalText_11,board[0][0]="O","O"   
                        tic_tac.append("O") 
                elif 700<x_hand<850 and 50<y_hand<150:
                    if len(tic_tac)%2==0:
                        finalText_12,board[0][1]="X","X"
                        tic_tac.append("X")
                    else:
                        finalText_12,board[0][1]="O","O"   
                        tic_tac.append("O")
                elif 950<x_hand<1100 and 50<y_hand<150:
                    if len(tic_tac)%2==0:
                        finalText_13,board[0][2]="X","X"
                        tic_tac.append("X")
                    else:
                        finalText_13,board[0][2]="O","O"   
                        tic_tac.append("O")    
                    
                if 450<x_hand<600 and 250<y_hand<350:
                    if len(tic_tac)%2==0:
                        finalText_21,board[1][0]="X","X"
                        tic_tac.append("X")
                    else:
                        finalText_21,board[1][0]="O","O"   
                        tic_tac.append("O")
                elif 700<x_hand<850 and 250<y_hand<350:
                    if len(tic_tac)%2==0:
                        finalText_22,board[1][1]="X","X"
                        tic_tac.append("X")
                    else:
                        finalText_22,board[1][1]="O","O"   
                        tic_tac.append("O")
                elif 950<x_hand<1100 and 250<y_hand<350:
                    if len(tic_tac)%2==0:
                        finalText_23,board[1][2]="X","X"
                        tic_tac.append("X")
                    else:
                        finalText_23,board[1][2]="O","O"   
                        tic_tac.append("O")

                if 450<x_hand<600 and 450<y_hand<550:
                    if len(tic_tac)%2==0:
                        finalText_31,board[2][0]="X","X"
                        tic_tac.append("X")
                    else:
                        finalText_31,board[2][0]="O","O"   
                        tic_tac.append("O")
                elif 700<x_hand<850 and 450<y_hand<550:
                    if len(tic_tac)%2==0:
                        finalText_32,board[2][1]="X","X"
                        tic_tac.append("X")
                    else:
                        finalText_32,board[2][1]="O","O"   
                        tic_tac.append("O")
                elif 950<x_hand<1100 and 450<y_hand<550:
                    if len(tic_tac)%2==0:
                        finalText_33,board[2][2]="X","X"
                        tic_tac.append("X")
                    else:
                        finalText_33,board[2][2]="O","O"   
                        tic_tac.append("O")                                    
                    


    
    cv2.rectangle(img, (450,50), (600,150), (225, 0, 225), cv2.FILLED)
    cv2.rectangle(img, (700,50), (850,150), (225, 0, 225), cv2.FILLED)
    cv2.rectangle(img, (950,50), (1100,150), (225, 0, 225), cv2.FILLED)

    cv2.rectangle(img, (450,250), (600,350), (225, 0, 225), cv2.FILLED)
    cv2.rectangle(img, (700,250), (850,350), (225, 0, 225), cv2.FILLED)
    cv2.rectangle(img, (950,250), (1100,350), (225, 0, 225), cv2.FILLED)
  
    cv2.rectangle(img, (450,450), (600,550), (225, 0, 225), cv2.FILLED)
    cv2.rectangle(img, (700,450), (850,550), (225, 0, 225), cv2.FILLED)
    cv2.rectangle(img, (950,450), (1100,550), (225, 0, 225), cv2.FILLED)


    

    cv2.putText(img, finalText_11, (500, 130), cv2.FONT_HERSHEY_PLAIN, 5, (255, 255, 255), 5)
    cv2.putText(img, finalText_12, (750, 130), cv2.FONT_HERSHEY_PLAIN, 5, (255, 255, 255), 5)
    cv2.putText(img, finalText_13, (1000, 130), cv2.FONT_HERSHEY_PLAIN, 5, (255, 255, 255), 5)

    
    cv2.putText(img, finalText_21, (500, 330), cv2.FONT_HERSHEY_PLAIN, 5, (255, 255, 255), 5)
    cv2.putText(img, finalText_22, (750, 330), cv2.FONT_HERSHEY_PLAIN, 5, (255, 255, 255), 5)
    cv2.putText(img, finalText_23, (1000, 330), cv2.FONT_HERSHEY_PLAIN, 5, (255, 255, 255), 5)

    
    cv2.putText(img, finalText_31, (500, 530), cv2.FONT_HERSHEY_PLAIN, 5, (255, 255, 255), 5)
    cv2.putText(img, finalText_32, (750, 530), cv2.FONT_HERSHEY_PLAIN, 5, (255, 255, 255), 5)
    cv2.putText(img, finalText_33, (1000, 530), cv2.FONT_HERSHEY_PLAIN, 5, (255, 255, 255), 5)

    if len(tic_tac)%2==0:
        player_text="Player \'X\'" 

    else:
        player_text="Player \'O\' "      

    cv2.putText(img, player_text, (1250, 330), cv2.FONT_HERSHEY_PLAIN, 3, (255, 100, 100), 5)




    result=winner(board)
    

    if result[0]==1:
        text_result="\'" + str(result[1]) + "\'" +" Has Won "

        cv2.putText(img, text_result , (530, 730), cv2.FONT_HERSHEY_PLAIN, 5, (100, 255, 100), 5 )
        
        good_luck="Better Luck Next Time !"

        cv2.putText(img, good_luck , (230, 830), cv2.FONT_HERSHEY_PLAIN, 5, (100, 255, 100), 5 )

        

        

   

    cv2.imshow("Image",img)
    cv2.waitKey(1)
© 2021 GitHub, Inc.
Terms
Privacy
Security
Status
Docs
Contact GitHub
Pricing
API
Training
Blog
About
Loading complete
