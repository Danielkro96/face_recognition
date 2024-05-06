import face_recognition
import os
import cv2 as cv


def encode_faces(dir_path: str):
    list_people_encoded = []

    for face in os.listdir(dir_path):
        image = face_recognition.load_image_file(f'{dir_path}/{face}')
        encoding = face_recognition.face_encodings(image)[0]
        list_people_encoded.append((encoding, face.strip(".jpg")))

    return list_people_encoded


def detect_faces(frame, known_encodings, known_names):
    frame_rgb = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
    frame_small = cv.resize(frame_rgb, (0, 0), fx=0.5, fy=0.5)
    face_locations = face_recognition.face_locations(frame_small)
    face_locations = [(top * 2, right * 2, bottom * 2, left * 2) for (top, right, bottom, left) in face_locations]

    for top, right, bottom, left in face_locations:
        face_encoding = face_recognition.face_encodings(frame_rgb, [(top, right, bottom, left)])[0]

        # Compare face encoding with known encodings
        matches = face_recognition.compare_faces(known_encodings, face_encoding)
        name = "Unknown"

        if True in matches:
            first_match_index = matches.index(True)
            name = known_names[first_match_index]

        cv.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 4)
        cv.putText(
            frame, name,
            (left + 10, bottom + 30),
            cv.FONT_HERSHEY_SIMPLEX, 1.2, (200, 200, 200), 3)
    cv.imshow("Faces found", frame)


def detect_face_by_live_video():
    known_encodings = []
    known_names = []

    # Encoding known faces
    for face_file in os.listdir('known_faces'):
        image = face_recognition.load_image_file(f'known_faces/{face_file}')
        encoding = face_recognition.face_encodings(image)[0]
        known_encodings.append(encoding)
        known_names.append(face_file.strip(".jpg"))

    capture = cv.VideoCapture(0)

    if not capture.isOpened():
        raise RuntimeError("Unable to open camera")

    skip_frames = 0
    while True:
        ret, frame = capture.read()

        if not ret:
            raise RuntimeError("Unable to capture frame")

        if skip_frames > 0:
            # cv.imshow("Faces found", frame)
            skip_frames -= 1
            continue

        detect_faces(frame, known_encodings, known_names)

        key = cv.waitKey(1)
        if key == ord('q'):
            break

        skip_frames = 1

    capture.release()
    cv.destroyAllWindows()


if __name__ == "__main__":
    detect_face_by_live_video()
