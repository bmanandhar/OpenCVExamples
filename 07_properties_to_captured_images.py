#https://www.youtube.com/watch?v=FVnA3xpqEKY&list=PLS1QulWo1RIa7D1O6skqDQ-JZ1GGHKK-K&index=7&ab_channel=ProgrammingKnowledge

import cv2
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
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('frame', gray)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    else:
        break

cap.release()
cv2.destroyAllWindows()