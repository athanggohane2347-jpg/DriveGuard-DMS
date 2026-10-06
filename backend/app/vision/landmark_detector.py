class LandmarkDetector:
    def detect(self, frame: object | None) -> dict:
        if frame is None:
            return {"face_landmarks": [], "eye_landmarks": [], "mouth_landmarks": []}
        return {"face_landmarks": [], "eye_landmarks": [], "mouth_landmarks": []}
