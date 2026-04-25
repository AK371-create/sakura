// Approximate league-average thresholds for mapping a stat value to a 0-100 percentile.
// These are eyeballed from MLB distributions and are intentionally simplified —
// enough to drive a Baseball-Savant-style percentile bar, not to be scientifically authoritative.

export type Direction = "higher_better" | "lower_better";

export interface PercentileSpec {
  p10: number; // 10th percentile value
  p50: number; // 50th percentile (league median)
  p90: number; // 90th percentile
  direction: Direction;
}

// Batting
export const BATTING_SPECS: Record<string, PercentileSpec> = {
  exit_velocity_avg: { p10: 85.5, p50: 88.5, p90: 92.5, direction: "higher_better" },
  launch_angle_avg: { p10: 5, p50: 12, p90: 20, direction: "higher_better" },
  barrel_batted_rate: { p10: 3, p50: 7.5, p90: 16, direction: "higher_better" },
  hard_hit_percent: { p10: 30, p50: 40, p90: 55, direction: "higher_better" },
  xba: { p10: 0.210, p50: 0.245, p90: 0.285, direction: "higher_better" },
  xslg: { p10: 0.340, p50: 0.410, p90: 0.530, direction: "higher_better" },
  xwoba: { p10: 0.280, p50: 0.320, p90: 0.395, direction: "higher_better" },
  k_percent: { p10: 32, p50: 22, p90: 14, direction: "lower_better" },
  bb_percent: { p10: 5, p50: 8.5, p90: 14, direction: "higher_better" },
};

// Pitching (for 4-seam, slider, etc. — used for BAA/whiff/hardhit on pitch arsenal)
export const PITCH_SPECS: Record<string, PercentileSpec> = {
  whiff: { p10: 14, p50: 25, p90: 40, direction: "higher_better" },
  hard_hit: { p10: 55, p50: 40, p90: 27, direction: "lower_better" },
  usage: { p10: 5, p50: 25, p90: 55, direction: "higher_better" },
};

// Parse ".245" or 0.245 into a number
function toNumber(v: number | string): number {
  if (typeof v === "number") return v;
  return parseFloat(v);
}

export function percentile(value: number | string, spec: PercentileSpec): number {
  const v = toNumber(value);
  if (isNaN(v)) return 50;

  const { p10, p50, p90, direction } = spec;
  let pct: number;

  if (direction === "higher_better") {
    if (v <= p10) pct = 10 * Math.max(0, (v / p10));
    else if (v <= p50) pct = 10 + ((v - p10) / (p50 - p10)) * 40;
    else if (v <= p90) pct = 50 + ((v - p50) / (p90 - p50)) * 40;
    else pct = Math.min(99, 90 + ((v - p90) / (p90 - p50)) * 9);
  } else {
    // lower is better: invert
    if (v >= p10) pct = 10 * Math.max(0, p10 / Math.max(v, 0.001));
    else if (v >= p50) pct = 10 + ((p10 - v) / (p10 - p50)) * 40;
    else if (v >= p90) pct = 50 + ((p50 - v) / (p50 - p90)) * 40;
    else pct = Math.min(99, 90 + ((p90 - v) / (p50 - p90)) * 9);
  }

  return Math.max(1, Math.min(99, Math.round(pct)));
}

// Color for a percentile — Baseball Savant palette (blue = poor, red = elite)
export function percentileColor(pct: number): string {
  if (pct >= 90) return "var(--sv-red)";
  if (pct >= 75) return "var(--sv-orange)";
  if (pct >= 60) return "var(--sv-yellow)";
  if (pct >= 40) return "var(--sv-neutral)";
  if (pct >= 25) return "var(--sv-cyan)";
  return "var(--sv-blue)";
}
