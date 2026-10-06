import { useState } from 'react';
import { ShieldCheck } from 'lucide-react';
import { api } from '../services/api';

export function Login({ onAuthed }: { onAuthed: () => void }) {
  const [mode, setMode] = useState<'login' | 'register'>('login');
  const [email, setEmail] = useState('demo@driveguard.local');
  const [password, setPassword] = useState('DriveGuard123!');
  const [name, setName] = useState('Demo Driver');
  const [error, setError] = useState('');

  async function submit() {
    try {
      const response = mode === 'login' ? await api.login({ email, password }) : await api.register({ email, password, name });
      localStorage.setItem('driveguard_token', response.access_token);
      onAuthed();
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Authentication failed');
    }
  }

  return (
    <div className="login-screen">
      <section className="login-panel">
        <div className="login-brand"><ShieldCheck size={34} /> <h1>DriveGuard DMS</h1></div>
        <p>AI-powered driver monitoring dashboard for drowsiness, fatigue, distraction, alerts, and trip history.</p>
        <div className="tabs">
          <button className={mode === 'login' ? 'active' : ''} onClick={() => setMode('login')}>Login</button>
          <button className={mode === 'register' ? 'active' : ''} onClick={() => setMode('register')}>Register</button>
        </div>
        {mode === 'register' && <input value={name} onChange={(e) => setName(e.target.value)} placeholder="Driver name" />}
        <input value={email} onChange={(e) => setEmail(e.target.value)} placeholder="Email" />
        <input value={password} onChange={(e) => setPassword(e.target.value)} placeholder="Password" type="password" />
        {error && <div className="error">{error}</div>}
        <button className="primary" onClick={submit}>{mode === 'login' ? 'Login' : 'Create account'}</button>
      </section>
    </div>
  );
}
