from app.vision.eye_analyzer import classify_eye_state, eye_aspect_ratio
from app.vision.head_pose import HeadPose, classify_head_pose
from app.vision.mouth_analyzer import is_yawning, mouth_aspect_ratio


def test_eye_aspect_ratio_open_eye():
    points = [(0, 0), (1, 1), (3, 1), (4, 0), (3, -1), (1, -1)]
    assert round(eye_aspect_ratio(points), 2) == 0.5
    assert classify_eye_state(0.3) == "OPEN"


def test_eye_state_closed():
    assert classify_eye_state(0.12, threshold=0.21) == "CLOSED"


def test_mouth_aspect_ratio_yawn():
    points = [(0, 0), (1, 3), (2, 3), (3, 3), (4, 0), (3, -3), (2, -3), (1, -3)]
    assert mouth_aspect_ratio(points) > 1.0
    assert is_yawning(mouth_aspect_ratio(points))


def test_head_pose_logic():
    assert classify_head_pose(HeadPose(yaw=31, pitch=0, roll=0)) == "TURNED_RIGHT"
    assert classify_head_pose(HeadPose(yaw=0, pitch=24, roll=0)) == "LOOKING_DOWN"
    assert classify_head_pose(HeadPose(yaw=1, pitch=1, roll=1)) == "NORMAL"
