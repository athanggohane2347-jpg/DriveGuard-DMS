const API_URL = import.meta.env.VITE_API_URL || 'http://127.0.0.1:8000';
export const WS_URL = import.meta.env.VITE_WS_URL || 'ws://127.0.0.1:8000';

export function token() {
  return localStorage.getItem('driveguard_token');
}

async function request<T>(path: string, options: RequestInit = {}): Promise<T> {
  const headers = new Headers(options.headers);
  headers.set('Content-Type', 'application/json');
  const authToken = token();
  if (authToken) headers.set('Authorization', `Bearer ${authToken}`);
  const response = await fetch(`${API_URL}${path}`, { ...options, headers });
  if (!response.ok) throw new Error(await response.text());
  return response.json() as Promise<T>;
}

export const api = {
  register: (body: { email: string; password: string; name: string }) =>
    request<{ access_token: string; user: unknown }>('/api/auth/register', { method: 'POST', body: JSON.stringify(body) }),
  login: (body: { email: string; password: string }) =>
    request<{ access_token: string; user: unknown }>('/api/auth/login', { method: 'POST', body: JSON.stringify(body) }),
  dashboard: () => request<any>('/api/dashboard'),
  driver: () => request<any>('/api/driver'),
  sessions: () => request<any[]>('/api/sessions'),
  events: () => request<any[]>('/api/events'),
  analytics: () => request<any>('/api/analytics'),
  settings: () => request<any>('/api/settings'),
  updateSettings: (body: any) => request<any>('/api/settings', { method: 'PUT', body: JSON.stringify(body) }),
  system: () => request<any>('/api/system/status'),
  startSession: () => request<any>('/api/session/start?source=SIMULATION', { method: 'POST' }),
  stopSession: (sessionId: number) => request<any>(`/api/session/stop?session_id=${sessionId}`, { method: 'POST' }),
};
