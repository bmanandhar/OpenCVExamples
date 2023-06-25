#https://www.youtube.com/watch?v=rRSyg9kYfcU&list=PLS1QulWo1RIa7D1O6skqDQ-JZ1GGHKK-K&index=8&ab_channel=ProgrammingKnowledge
import cv2
import datetime

cap = cv2.VideoCapture(0)
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH), ':width -b4')
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT), ':height -b4')
#whatever value we input, output will use the values that are vailable for it as default
cap.set(3, 3000) # 3 for width
cap.set(4, 3000) # 4 for height

print(cap.get(3), ':width -after')
print(cap.get(4),':height -after')

while (cap.isOpened()):
    ret, frame = cap.read()

    if ret:

        font = cv2.FONT_HERSHEY_SIMPLEX
        datet = str(datetime.datetime.now())
        frame = cv2.putText(frame, datet, (10,50), font, 1, (255,255,255), 2, cv2.LINE_AA )
        cv2.imshow('frame', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    else:
        break

cap.release()
cv2.destroyAllWindows()