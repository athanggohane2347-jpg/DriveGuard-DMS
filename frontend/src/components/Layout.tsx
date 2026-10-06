import { Activity, BarChart3, Camera, FileClock, Gauge, HeartPulse, History, Info, LogOut, Settings, ShieldCheck, UserRound } from 'lucide-react';
import type { ReactNode } from 'react';

const items = [
  ['Dashboard', Gauge],
  ['Live Monitor', Camera],
  ['Driver Analysis', HeartPulse],
  ['Trips', History],
  ['Events', FileClock],
  ['Analytics', BarChart3],
  ['Driver Profile', UserRound],
  ['Settings', Settings],
  ['System Health', Activity],
  ['About', Info],
] as const;

export function Layout({ page, setPage, children, onLogout }: { page: string; setPage: (page: string) => void; children: ReactNode; onLogout: () => void }) {
  return (
    <div className="app-shell">
      <aside>
        <div className="brand"><ShieldCheck /> <span>DriveGuard DMS</span></div>
        <nav>
          {items.map(([label, Icon]) => (
            <button className={page === label ? 'active' : ''} key={label} onClick={() => setPage(label)} title={label}>
              <Icon size={18} /> <span>{label}</span>
            </button>
          ))}
        </nav>
        <button className="logout" onClick={onLogout}><LogOut size={18} /> Logout</button>
      </aside>
      <main>{children}</main>
    </div>
  );
}
