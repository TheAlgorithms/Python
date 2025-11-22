"""
This code demonstrates the use of SOTA face embeddings model ARCFACE
through wrapper called insightface

It uses Retinaface Face detector to detect faces.

References : https://www.insightface.ai/
"""

import cv2
import numpy as np
from insightface.app import FaceAnalysis


def prepare_model(model_name: str = "buffalo_l", ctx_id: int = -1) -> FaceAnalysis:
    """
    Initialize and Prepare face analysis model

    Args:
        - model_name = default 'buffalo_l'
        - ctx_id = gpu number 1,2... , for CPU -1

    Return:
        Configured FaceAnalysis instance ready for inference

    """
    app = FaceAnalysis(model_name)
    app.prepare(ctx_id=ctx_id)

    return app


def get_facial_data(face_analysis_model: FaceAnalysis, frame: np.ndarray) -> list[dict]:
    """
    Extract facial data from a frame using the face analysis model

    Args:
        - face analysis model : prepared FaceanAlysis instance
        - frame : BGR image as numpy array (opencv format)
    Returns:
        - List of dict, each containing facial data for one detected face:
            - bounding_box: Face bounding box coordinates
            - keypoints: 5-point facial landmark
            - landmark_3d_68: 68-point 3d landmarks
            - landmakr_2d_106: 106-points 2d landmarks
            - pose: Head pose (pitch yaw roll)
            - gender: Predicted gender (0-female,1:male)
            - age: Predicted age
            - embeddings: 512-dimensional face vector

    Example:
            >>> # model = prepare_model(ctx_id = -1)
            >>> # frame = cv2.imread("test_face.jpg")
            >>> # faces = get_facial_data(model,frame)
            >>> # len(faces)>=0

    """

    results = face_analysis_model.get(frame)
    faces = []
    for result in results:
        face_data = {
            "bounding_box": result["bbox"],
            "keypoints": result["kps"],
            "landmark_3d_68": result["landmark_3d_68"],
            "pose": result["pose"],
            "landmark_2d_106": result["landmark_2d_106"],
            "gender": result["gender"],
            "age": result["age"],
            "embedding": result["embedding"],
        }
        faces.append(face_data)

    return faces


def run_webcam_demo(ctx_id: int = -1, source: str | int = 0) -> None:
    """
    Run live face analysis on wecam feed

    Args:
        - ctx_id: GPU context id -1 for cpu and >1 for gpu
        - source: camera int for webcam or path for video file
    """
    face_model = prepare_model(ctx_id=ctx_id)  # doctest: +SKIP
    capture = cv2.VideoCapture(source)

    while True:
        ret, frame = capture.read()
        if not ret:
            break

        faces = get_facial_data(face_model, frame)

        for face in faces:
            bbox = [int(coord) for coord in face["bounding_box"]]
            cv2.rectangle(
                frame,
                (bbox[0], bbox[1]),
                (bbox[2], bbox[3]),
                color=(0, 255, 0),
                thickness=2,
            )

        cv2.imshow("Face Analysis", frame)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    capture.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    run_webcam_demo(ctx_id=1)
