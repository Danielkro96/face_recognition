## Real-time Face Recognition Experimentation

This project is a real-time face recognition experiment developed in Python \
using the face_recognition and OpenCV libraries. It allows for the detection \
and recognition of faces in live video streams captured from a webcam. 

### Features:

* Real-time Face Detection: Utilizes the face_recognition library to detect faces in live video streams.
* Face Recognition: Compares the detected faces with a set of known faces to recognize individuals.
* Experimental Playground: Ideal for experimenting with face recognition algorithms and exploring real-time applications.

### Usage:

1. Clone the Repository:
  ```sh
  git clone https://github.com/your-username/real-time-face-recognition.git
  ```

2. Install Dependencies:
   * Navigate to the project directory:
     ```sh
     cd face_recognition
     ```
   * Install the required Python packages using pip:
     ```sh
     pip install -r requirements.txt
     ```
     
3. Add Known Faces:
   * Add images of known faces to the known_faces directory. \
   Ensure that each image contains only one face and is in JPG format.

4. Run the Real-time Face Recognition Script:
   * Execute the main.py script to start real-time face recognition:
     ```sh
     python main.py
     ```