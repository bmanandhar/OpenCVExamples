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

        font = cv2.FONT_HERSHEY_SIMPLEX
        text = 'Width: ' + str(cap.get(3)) + ' Height:' + str(cap.get(4))
        frame = cv2.putText(frame, text, (10,50), font, 1, (0,255,255), 2, cv2.LINE_AA )
        cv2.imshow('frame', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    else:
        break

cap.release()
cv2.destroyAllWindows()