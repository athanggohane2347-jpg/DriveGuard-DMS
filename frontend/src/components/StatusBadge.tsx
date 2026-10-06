export function StatusBadge({ label, tone = 'green' }: { label: string; tone?: 'green' | 'yellow' | 'orange' | 'red' | 'blue' }) {
  return <span className={`badge ${tone}`}>{label}</span>;
}
