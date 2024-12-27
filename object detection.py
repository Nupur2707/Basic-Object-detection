import cv2
import numpy as np

def detect_objects(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    edges = cv2.Canny(blurred, 50, 150)
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

 
    for contour in contours:
        
        area = cv2.contourArea(contour)
        if area > 500:  
            x, y, w, h = cv2.boundingRect(contour)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(frame, f"Object: {area:.0f}", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    return frame

def main():
    
    cap = cv2.VideoCapture(0)  

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        output_frame = detect_objects(frame)

        
        cv2.imshow("Object Detection", output_frame)

        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
