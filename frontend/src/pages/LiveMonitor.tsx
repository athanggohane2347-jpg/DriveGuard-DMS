import { Pause, Play, RotateCcw, Square } from 'lucide-react';
import { CameraPanel } from '../components/CameraPanel';
import { MetricCard } from '../components/MetricCard';
import { ScoreRing } from '../components/ScoreRing';
import { MonitorPayload } from '../types';

export function LiveMonitor({ payload, active, setActive, startSession, stopSession, reset }: {
  payload: MonitorPayload | null;
  active: boolean;
  setActive: (value: boolean) => void;
  startSession: () => void;
  stopSession: () => void;
  reset: () => void;
}) {
  return (
    <>
      <header className="topbar"><div><h1>Live Driver Monitor</h1><span>Real-time driver state, landmarks, pose, gaze, alerts, FPS, and latency.</span></div></header>
      <div className="toolbar">
        <button className="primary" onClick={startSession}><Play size={16} /> Start monitoring</button>
        <button onClick={() => setActive(false)}><Pause size={16} /> Pause</button>
        <button onClick={stopSession}><Square size={16} /> Stop</button>
        <button onClick={reset}><RotateCcw size={16} /> Reset session</button>
      </div>
      <div className="dashboard-grid">
        <CameraPanel payload={payload} />
        <section className="card state-card">
          <h2>{payload?.driver_state || (active ? 'CONNECTING' : 'STOPPED')}</h2>
          <ScoreRing score={payload?.safety_score ?? 100} />
          <div className="metric-grid">
            <MetricCard label="FPS" value={String(payload?.metrics.fps ?? 0)} />
            <MetricCard label="Latency" value={`${payload?.metrics.latency_ms ?? 0} ms`} />
            <MetricCard label="Yaw" value={`${payload?.head_pose.yaw ?? 0} deg`} />
            <MetricCard label="Pitch" value={`${payload?.head_pose.pitch ?? 0} deg`} />
          </div>
        </section>
      </div>
      <section className="card">
        <div className="section-title">Alert messages</div>
        <div className="timeline">
          {payload?.alerts.map((alert, index) => <div key={index}><b>Level {alert.severity}</b><span>{alert.message}</span></div>) || <p>No alerts.</p>}
        </div>
      </section>
    </>
  );
}
