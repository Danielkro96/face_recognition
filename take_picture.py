import cv2 as cv


def take_picture():
    capture = cv.VideoCapture(0)

    if not capture.isOpened():
        print("ERROR: Unable to open camera")
        return

    captured, frame = capture.read()

    if not captured:
        print("ERROR: Unable to capture the frame")
        capture.release()
        return

    cv.imwrite("./captured_images/captured_image.jpg", frame)
    capture.release()

    print("INFO: Image captured successfully")


if __name__ == "__main__":
    take_picture()
