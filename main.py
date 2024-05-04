import face_recognition
import cv2 as cv


def detect_face(image_path: str):
    image = face_recognition.load_image_file(image_path)
    face_locations = face_recognition.face_locations(image)

    image = cv.cvtColor(image, cv.COLOR_RGB2BGR)
    for top, right, bottom, left in face_locations:
        cv.rectangle(image, (left, top), (right, bottom), (0, 255, 0), 4)

    cv.namedWindow("Faces found", cv.WINDOW_NORMAL)
    cv.resizeWindow("Faces found", 600, 400)
    cv.imshow("Faces found", image)
    cv.waitKey(0)
    cv.destroyAllWindows()





if __name__ == "__main__":
    detect_face("known_faces/face1.jpg")
