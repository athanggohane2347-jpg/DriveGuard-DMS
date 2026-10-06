import { useEffect, useState } from 'react';
import { Bar, BarChart, CartesianGrid, Line, LineChart, ResponsiveContainer, Tooltip, XAxis, YAxis } from 'recharts';
import { api } from '../services/api';
import { MetricCard } from '../components/MetricCard';
import { MonitorPayload } from '../types';

export function DriverAnalysis({ payload }: { payload: MonitorPayload | null }) {
  return <section className="card"><h1>Driver Analysis</h1><div className="metric-grid"><MetricCard label="State" value={payload?.driver_state || 'ATTENTIVE'} /><MetricCard label="Safety" value={payload?.safety_score ?? 100} /><MetricCard label="Fatigue trend" value={String(payload?.metrics.fatigue_trend || 'STABLE')} /><MetricCard label="Possible impairment / abnormal behavior" value="Manual verification required" /></div><div className="contributors">{payload?.contributors.map((c) => <div key={c.name}><b>{c.name}</b><span>{c.points} points</span><p>{c.detail}</p></div>)}</div></section>;
}

export function Trips() {
  const [rows, setRows] = useState<any[]>([]);
  useEffect(() => { api.sessions().then(setRows).catch(() => setRows([])); }, []);
  return <TablePage title="Trip/session history" rows={rows} columns={['id', 'source', 'start_time', 'duration_seconds', 'average_safety_score', 'critical_events']} />;
}

export function Events() {
  const [rows, setRows] = useState<any[]>([]);
  useEffect(() => { api.events().then(setRows).catch(() => setRows([])); }, []);
  return <TablePage title="Events" rows={rows} columns={['timestamp', 'event_type', 'severity', 'confidence', 'safety_score', 'description']} />;
}

export function Analytics() {
  const [data, setData] = useState<any>(null);
  useEffect(() => { api.analytics().then(setData).catch(() => setData(null)); }, []);
  const typeRows = Object.entries(data?.events_by_type || {}).map(([name, value]) => ({ name, value }));
  return <><section className="metric-grid wide"><MetricCard label="Sessions" value={data?.totals.sessions ?? 0} /><MetricCard label="Average safety" value={data?.totals.average_safety_score ?? 100} /><MetricCard label="Warnings" value={data?.totals.warnings ?? 0} /><MetricCard label="Critical" value={data?.totals.critical_events ?? 0} /></section><section className="card chart"><h1>Safety score over time</h1><ResponsiveContainer width="100%" height={260}><LineChart data={data?.safety_score_over_time || []}><CartesianGrid stroke="#263545" /><XAxis dataKey="time" hide /><YAxis /><Tooltip /><Line type="monotone" dataKey="score" stroke="#21d07a" /></LineChart></ResponsiveContainer></section><section className="card chart"><h1>Events by type</h1><ResponsiveContainer width="100%" height={260}><BarChart data={typeRows}><CartesianGrid stroke="#263545" /><XAxis dataKey="name" /><YAxis /><Tooltip /><Bar dataKey="value" fill="#4ea1ff" /></BarChart></ResponsiveContainer></section></>;
}

export function DriverProfile() {
  const [driver, setDriver] = useState<any>(null);
  useEffect(() => { api.driver().then(setDriver).catch(() => setDriver(null)); }, []);
  return <section className="card"><h1>Driver Profile</h1><div className="metric-grid"><MetricCard label="Driver ID" value={driver?.id ?? '-'} /><MetricCard label="Name" value={driver?.name ?? '-'} /><MetricCard label="Calibration" value={driver?.calibration_status ?? 'NOT_CALIBRATED'} /><MetricCard label="Average safety" value={driver?.average_safety_score ?? 100} /><MetricCard label="Total sessions" value={driver?.total_sessions ?? 0} /><MetricCard label="Total events" value={driver?.total_events ?? 0} /></div><button className="primary">Start calibration</button><button>Reset baseline</button></section>;
}

export function SettingsPage() {
  const [settings, setSettings] = useState<any>(null);
  useEffect(() => { api.settings().then(setSettings).catch(() => setSettings(null)); }, []);
  if (!settings) return <section className="card"><h1>Settings</h1><p>Loading settings.</p></section>;
  const set = (key: string, value: any) => setSettings({ ...settings, [key]: value });
  return <section className="card"><h1>Settings</h1><div className="settings-grid">{Object.entries(settings).map(([key, value]) => <label key={key}><span>{key.replaceAll('_', ' ')}</span><input value={String(value)} onChange={(e) => set(key, typeof value === 'boolean' ? e.target.value === 'true' : typeof value === 'number' ? Number(e.target.value) : e.target.value)} /></label>)}</div><button className="primary" onClick={() => api.updateSettings(settings).then(setSettings)}>Save settings</button></section>;
}

export function SystemHealth() {
  const [system, setSystem] = useState<any>(null);
  useEffect(() => { api.system().then(setSystem).catch(() => setSystem(null)); }, []);
  return <section className="card"><h1>System Health</h1><div className="metric-grid"><MetricCard label="Status" value={system?.status ?? 'UNKNOWN'} /><MetricCard label="CPU" value={`${system?.cpu_percent ?? 0}%`} /><MetricCard label="Memory" value={`${system?.memory_percent ?? 0}%`} /><MetricCard label="Camera" value={system?.camera ?? 'SIMULATION'} /></div></section>;
}

export function About() {
  return <section className="card doc"><h1>About / Documentation</h1><p>DriveGuard DMS is a local-first AI driver monitoring prototype. It supports simulation, camera/video architecture, explainable risk scoring, alerts, event history, trip summaries, settings, and privacy-conscious defaults.</p><p>It is not a certified automotive safety system. It cannot diagnose medical states or prove alcohol intoxication. Any impairment-related observation requires manual verification.</p></section>;
}

function TablePage({ title, rows, columns }: { title: string; rows: any[]; columns: string[] }) {
  return <section className="card"><h1>{title}</h1><div className="table-wrap"><table><thead><tr>{columns.map((column) => <th key={column}>{column.replaceAll('_', ' ')}</th>)}</tr></thead><tbody>{rows.map((row, index) => <tr key={row.id || index}>{columns.map((column) => <td key={column}>{String(row[column] ?? '-')}</td>)}</tr>)}</tbody></table></div></section>;
}
