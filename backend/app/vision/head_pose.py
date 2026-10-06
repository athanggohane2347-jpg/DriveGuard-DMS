from dataclasses import dataclass


@dataclass
class HeadPose:
    yaw: float
    pitch: float
    roll: float


def classify_head_pose(pose: HeadPose, yaw_limit: float = 25, pitch_down_limit: float = 18) -> str:
    if pose.pitch > pitch_down_limit:
        return "LOOKING_DOWN"
    if pose.yaw > yaw_limit:
        return "TURNED_RIGHT"
    if pose.yaw < -yaw_limit:
        return "TURNED_LEFT"
    if abs(pose.roll) > 22:
        return "TILTED"
    return "NORMAL"
