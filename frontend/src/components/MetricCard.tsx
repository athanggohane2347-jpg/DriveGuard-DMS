export function MetricCard({ label, value, hint }: { label: string; value: string | number; hint?: string }) {
  return (
    <section className="card metric" title={hint}>
      <span>{label}</span>
      <strong>{value}</strong>
    </section>
  );
}
