import face_recognition
import cv2
from PIL import Image

video_capture = cv2.VideoCapture(0)

while True:
    ret, frame = video_capture.read()

    rgb_frame = frame[:, :, ::-1]

    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

    l_n = []
    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        a = right - left
        b = bottom - top
        l_temp = [top, right, bottom, left, a, b]
        l_n.append(l_temp)

        #rectangle
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

    for face in l_n:
        temp_a = face[4]
        target_a_low = temp_a * 0.65
        target_a_high = temp_a / 0.65
        temp_b = face[5]
        target_b_low = temp_b * 0.65
        target_b_high = temp_b / 0.65

        for each in l_n:
            if each[4] != temp_a:
                if (each[4] > target_a_low) and (each[4] < target_a_high):
                    distance_a = abs(each[4] - temp_a)
                    base_a = 0
                    if (temp_a > each[4]):
                        base_a = temp_a
                    else:
                        base_a = each[4]
                    print("Temp_a ", temp_a)
                    print("Base_a ", base_a)
                    horizontal_dist = abs(each[1] - face[1] - base_a)
                    print(horizontal_dist)
                    horizontal_safe_dist = base_a * 11
                    print(horizontal_safe_dist)

                    if (horizontal_safe_dist > horizontal_dist):
                        print("PLS KEEP SAFETY DISTANCE")
                        font = cv2.FONT_HERSHEY_DUPLEX

                        cv2.putText(frame,
                                    'PLS KEEP SAFETY DISTANCE',
                                    (50, 50),
                                    font, 1,
                                    (0, 255, 255),
                                    2,
                                    cv2.LINE_4)

    cv2.imshow('Video', frame)

video_capture.release()
cv2.destroyAllWindows()