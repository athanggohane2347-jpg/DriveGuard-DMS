import { useEffect, useState } from 'react';
import { AlertTriangle, Camera, CheckCircle2 } from 'lucide-react';
import { api } from '../services/api';
import { CameraPanel } from '../components/CameraPanel';
import { MetricCard } from '../components/MetricCard';
import { ScoreRing } from '../components/ScoreRing';
import { StatusBadge } from '../components/StatusBadge';
import { MonitorPayload } from '../types';

export function Dashboard({ payload }: { payload: MonitorPayload | null }) {
  const [summary, setSummary] = useState<any>(null);
  useEffect(() => { api.dashboard().then(setSummary).catch(() => setSummary(null)); }, []);
  const score = payload?.safety_score ?? summary?.safety_score ?? 100;
  return (
    <>
      <header className="topbar">
        <div><h1>DriveGuard DMS</h1><span>Driver Camera {'->'} AI analysis {'->'} Risk Score {'->'} Alert {'->'} History</span></div>
        <div className="top-status"><StatusBadge label={summary?.system_status || 'ONLINE'} /><StatusBadge label={payload?.camera.status || 'SIMULATION'} tone="blue" /></div>
      </header>
      <div className="dashboard-grid">
        <CameraPanel payload={payload} />
        <section className="card state-card">
          <div className="section-title"><CheckCircle2 size={18} /> Driver status</div>
          <h2>{payload?.driver_state || summary?.driver_state || 'ATTENTIVE'}</h2>
          <ScoreRing score={score} />
          <div className="metric-grid">
            <MetricCard label="Drowsiness" value={`${payload?.scores.drowsiness ?? 12}%`} />
            <MetricCard label="Fatigue" value={`${payload?.scores.fatigue ?? 21}%`} />
            <MetricCard label="Distraction" value={`${payload?.scores.distraction ?? 8}%`} />
            <MetricCard label="Attention" value={`${payload?.scores.attention ?? 91}%`} />
          </div>
        </section>
      </div>
      <div className="two-col">
        <section className="card">
          <div className="section-title"><Camera size={18} /> Current detections</div>
          <div className="detections">
            {Object.entries(payload?.detections || { eyes: 'OPEN', blinking: 'NORMAL', yawning: 'NO', head_pose: 'NORMAL', gaze: 'FORWARD', phone: 'NOT_DETECTED' }).map(([key, value]) => (
              <div key={key}><span>{key.replace('_', ' ')}</span><b>{String(value)}</b></div>
            ))}
          </div>
        </section>
        <section className="card">
          <div className="section-title"><AlertTriangle size={18} /> Event timeline</div>
          <div className="timeline">
            {(payload?.alerts?.length ? payload.alerts : summary?.recent_events || []).map((event: any, index: number) => (
              <div key={event.id || index}><b>{event.type || event.event_type}</b><span>{event.message || event.description}</span></div>
            ))}
            {!payload?.alerts?.length && !summary?.recent_events?.length && <p>No recent events.</p>}
          </div>
        </section>
      </div>
    </>
  );
}
