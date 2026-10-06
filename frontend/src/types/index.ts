export type Severity = 0 | 1 | 2 | 3 | 4;

export type MonitorPayload = {
  timestamp: string;
  session_id: number | null;
  mode: string;
  driver_state: string;
  safety_score: number;
  risk_score: number;
  contributors: { name: string; points: number; detail: string }[];
  scores: {
    drowsiness: number;
    fatigue: number;
    distraction: number;
    attention: number;
    phone_risk: number;
  };
  detections: Record<string, string | boolean>;
  metrics: Record<string, number | string | null>;
  head_pose: { yaw: number; pitch: number; roll: number };
  camera: { status: string; lighting: string };
  alerts: { type: string; severity: Severity; message: string; safety_score: number }[];
  notice: string;
};
