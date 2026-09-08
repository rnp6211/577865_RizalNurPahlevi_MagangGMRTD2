import cv2
from ultralytics import YOLO

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Tidak dapat membuka kamera")
    exit()

model = YOLO("computer-vision/yolov8n.pt")
print(model.names)

while True:
    ret, frame = cap.read()

    if not ret:
        print("Tidak dapat mengambil frame")
        break

    output = frame.copy()

    results = model.predict(source=frame)

    if results is not None:
        result = results[0]
        for i in range(0, min(3, len(result.boxes))):
            xyxy = result.boxes.xyxy[i].round().int().tolist()
            cv2.rectangle(output, (xyxy[0], xyxy[1]), (xyxy[2], xyxy[3]), (0, 255, 0), 2)

            name = result.names[i]
            confidence = result.boxes.conf.tolist()
            text = "[" + str(round(confidence[i]*100)) + "%] " + name

            cv2.putText(output, text, (xyxy[0], xyxy[1]), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0))

    cv2.imshow("Objek terdeteksi", output)
    if cv2.waitKey(1) == ord('q'):
        break
    
