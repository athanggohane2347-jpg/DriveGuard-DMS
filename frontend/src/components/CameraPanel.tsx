import { Camera, ScanFace } from 'lucide-react';
import { MonitorPayload } from '../types';

export function CameraPanel({ payload }: { payload: MonitorPayload | null }) {
  const state = payload?.driver_state || 'WAITING';
  return (
    <section className="camera-panel">
      <div className="camera-top">
        <span><Camera size={16} /> Driver camera</span>
        <b>{payload?.mode || 'OFFLINE'}</b>
      </div>
      <div className="driver-frame">
        <div className="face-box">
          <ScanFace size={56} />
          <span>{state}</span>
        </div>
        <div className="landmark eye left" />
        <div className="landmark eye right" />
        <div className="landmark mouth" />
      </div>
      <p>{payload?.notice || 'Start monitoring to stream simulated or camera telemetry.'}</p>
    </section>
  );
}
