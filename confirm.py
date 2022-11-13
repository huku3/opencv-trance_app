import face_recognition
import cv2

original_face_img = "images/man.png"

face_img = face_recognition.load_image_file(original_face_img)
face_landmarks_list = face_recognition.face_landmarks(face_img)

# print(face_landmarks_list)

face_image = cv2.imread(original_face_img)
# chin, left_eyebrow, right_eyebrow, nose_bridge,right_eye, left_eye, bottom_lip
print(face_landmarks_list[0]["top_lip"])
for chin_cordinate in face_landmarks_list[0]["top_lip"]:
    cv2.drawMarker(
        face_image,
        chin_cordinate,
        color=(255, 0, 0),
        markerType=cv2.MARKER_CROSS,
        thickness=1,
    )
cv2.imshow("image", face_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
