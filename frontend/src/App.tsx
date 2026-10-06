import { useState } from 'react';
import type { ReactNode } from 'react';
import { Layout } from './components/Layout';
import { token, api } from './services/api';
import { useMonitorSocket } from './hooks/useMonitorSocket';
import { Login } from './pages/Login';
import { Dashboard } from './pages/Dashboard';
import { LiveMonitor } from './pages/LiveMonitor';
import { About, Analytics, DriverAnalysis, DriverProfile, Events, SettingsPage, SystemHealth, Trips } from './pages/SimplePages';

export default function App() {
  const [authed, setAuthed] = useState(Boolean(token()));
  const [page, setPage] = useState('Dashboard');
  const [active, setActive] = useState(true);
  const [sessionId, setSessionId] = useState<number | null>(null);
  const { payload } = useMonitorSocket(active, sessionId);

  if (!authed) return <Login onAuthed={() => setAuthed(true)} />;

  async function startSession() {
    const session = await api.startSession();
    setSessionId(session.id);
    setActive(true);
  }

  async function stopSession() {
    if (sessionId) await api.stopSession(sessionId);
    setActive(false);
  }

  function logout() {
    localStorage.removeItem('driveguard_token');
    setAuthed(false);
  }

  const pages: Record<string, ReactNode> = {
    Dashboard: <Dashboard payload={payload} />,
    'Live Monitor': <LiveMonitor payload={payload} active={active} setActive={setActive} startSession={startSession} stopSession={stopSession} reset={() => setSessionId(null)} />,
    'Driver Analysis': <DriverAnalysis payload={payload} />,
    Trips: <Trips />,
    Events: <Events />,
    Analytics: <Analytics />,
    'Driver Profile': <DriverProfile />,
    Settings: <SettingsPage />,
    'System Health': <SystemHealth />,
    About: <About />,
  };
  const content = pages[page] || pages.Dashboard;

  return <Layout page={page} setPage={setPage} onLogout={logout}>{content}</Layout>;
}
