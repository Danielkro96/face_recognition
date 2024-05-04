import cv2 as cv


def capture_video():
    capture = cv.VideoCapture(0)

    if not capture.isOpened():
        print("ERROR: Unable to open camera")
        return

    while True:
        captured, frame = capture.read()

        if not captured:
            print("ERROR: Unable to capture video")
            break

        gray_frame = cv.cvtColor(frame, cv.COLOR_RGBA2GRAY)
        cv.imshow("frame", gray_frame)

        if cv.waitKey(1) == ord('q'):
            break

    capture.release()
    cv.destroyAllWindows()


if __name__ == "__main__":
    capture_video()
