export function ScoreRing({ score }: { score: number }) {
  const color = score > 75 ? '#21d07a' : score > 55 ? '#f5c84b' : score > 35 ? '#f28a35' : '#ff4d5e';
  return (
    <div className="score-ring" style={{ background: `conic-gradient(${color} ${score * 3.6}deg, #1f2a36 0)` }}>
      <div>
        <strong>{score}</strong>
        <span>/100</span>
      </div>
    </div>
  );
}
