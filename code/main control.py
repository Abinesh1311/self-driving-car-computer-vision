import cv2
from lane_detection import detect_lane
from object_detection import detect_object

cap = cv2.VideoCapture(0)  # webcam / camera

while True:
    ret, frame = cap.read()
    if not ret:
        break

    lane_frame = detect_lane(frame)
    final_frame = detect_object(lane_frame)

    cv2.imshow("Self Driving Car - Demo", final_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
