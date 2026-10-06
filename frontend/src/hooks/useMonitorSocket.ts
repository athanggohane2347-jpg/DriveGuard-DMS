import { useEffect, useRef, useState } from 'react';
import { MonitorPayload } from '../types';
import { WS_URL } from '../services/api';

export function useMonitorSocket(active: boolean, sessionId: number | null) {
  const [payload, setPayload] = useState<MonitorPayload | null>(null);
  const [connected, setConnected] = useState(false);
  const socketRef = useRef<WebSocket | null>(null);

  useEffect(() => {
    if (!active) {
      socketRef.current?.close();
      setConnected(false);
      return;
    }
    const socket = new WebSocket(`${WS_URL}/ws/driver-monitor`);
    socketRef.current = socket;
    socket.onopen = () => {
      setConnected(true);
      if (sessionId) socket.send(JSON.stringify({ type: 'SET_SESSION', session_id: sessionId }));
    };
    socket.onmessage = (event) => setPayload(JSON.parse(event.data));
    socket.onclose = () => setConnected(false);
    return () => socket.close();
  }, [active, sessionId]);

  return { payload, connected };
}
