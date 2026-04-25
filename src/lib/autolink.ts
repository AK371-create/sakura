// Auto-link helper: replaces first occurrence of known player names / key terms
// in article body paragraphs with links to the relevant page.
//
// IMPORTANT: applies to plain text only. Run before HTML escaping or use carefully
// in `set:html` context (we escape user-controlled segments here).

type LinkSpec = { pattern: RegExp; href: (lang: "ja" | "en") => string };

// Player name patterns (JP). Order matters — longer/specific names first.
const PLAYER_PATTERNS: Array<{ name: string; key: string; aliases?: string[] }> = [
  { name: "大谷翔平", key: "ohtani", aliases: ["大谷"] },
  { name: "山本由伸", key: "yamamoto" },
  { name: "今永昇太", key: "imanaga" },
  { name: "ダルビッシュ有", key: "darvish", aliases: ["ダルビッシュ"] },
  { name: "千賀滉大", key: "senga" },
  { name: "佐々木朗希", key: "sasaki" },
  { name: "菊池雄星", key: "kikuchi" },
  { name: "前田健太", key: "maeda" },
  { name: "松井裕樹", key: "matsui-yuki" },
  { name: "鈴木誠也", key: "suzuki" },
  { name: "吉田正尚", key: "yoshida" },
  { name: "イチロー", key: "ichiro" },
  { name: "松井秀喜", key: "matsui-hideki" },
  { name: "野茂英雄", key: "nomo", aliases: ["野茂"] },
  { name: "上原浩治", key: "uehara" },
  { name: "黒田博樹", key: "kuroda" },
  { name: "田中将大", key: "tanaka" },
  { name: "松坂大輔", key: "matsuzaka" },
  { name: "青木宣親", key: "aoki" },
  { name: "福留孝介", key: "fukudome" },
  { name: "岩村明憲", key: "iwamura" },
  { name: "平野佳寿", key: "hirano" },
  { name: "筒香嘉智", key: "tsutsugo" },
  { name: "秋山翔吾", key: "akiyama" },
  { name: "藤浪晋太郎", key: "fujinami" },
];

const PLAYER_PATTERNS_EN: Array<{ name: string; key: string }> = [
  { name: "Shohei Ohtani", key: "ohtani" },
  { name: "Yoshinobu Yamamoto", key: "yamamoto" },
  { name: "Shota Imanaga", key: "imanaga" },
  { name: "Yu Darvish", key: "darvish" },
  { name: "Kodai Senga", key: "senga" },
  { name: "Roki Sasaki", key: "sasaki" },
  { name: "Yusei Kikuchi", key: "kikuchi" },
  { name: "Kenta Maeda", key: "maeda" },
  { name: "Yuki Matsui", key: "matsui-yuki" },
  { name: "Seiya Suzuki", key: "suzuki" },
  { name: "Masataka Yoshida", key: "yoshida" },
  { name: "Ichiro Suzuki", key: "ichiro" },
  { name: "Hideki Matsui", key: "matsui-hideki" },
  { name: "Hideo Nomo", key: "nomo" },
  { name: "Koji Uehara", key: "uehara" },
  { name: "Hiroki Kuroda", key: "kuroda" },
  { name: "Masahiro Tanaka", key: "tanaka" },
  { name: "Daisuke Matsuzaka", key: "matsuzaka" },
  { name: "Norichika Aoki", key: "aoki" },
  { name: "Kosuke Fukudome", key: "fukudome" },
  { name: "Akinori Iwamura", key: "iwamura" },
  { name: "Yoshihisa Hirano", key: "hirano" },
  { name: "Yoshitomo Tsutsugo", key: "tsutsugo" },
  { name: "Shogo Akiyama", key: "akiyama" },
  { name: "Shintaro Fujinami", key: "fujinami" },
];

function escapeHtml(s: string): string {
  return s
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;")
    .replace(/'/g, "&#39;");
}

/**
 * Auto-link player names (and aliases) within plain text. Returns HTML.
 * For each player, only the FIRST occurrence in the text is linked, and only
 * once per article (caller-managed: pass a Set as `seenKeys`).
 */
export function autoLinkPlayers(
  text: string,
  lang: "ja" | "en",
  seenKeys: Set<string>,
  excludeKey?: string,
): string {
  const patterns = lang === "ja" ? PLAYER_PATTERNS : PLAYER_PATTERNS_EN;
  // Sort by name length DESC so longer matches win (e.g., "ダルビッシュ有" before "ダルビッシュ")
  const ordered = [...patterns].sort((a, b) => b.name.length - a.name.length);

  // Work on a structure where we accumulate replacement spans and rebuild.
  // Simpler: do greedy first-occurrence replacement per player.
  let escaped = escapeHtml(text);

  for (const p of ordered) {
    if (seenKeys.has(p.key)) continue;
    if (excludeKey && excludeKey === p.key) continue; // don't link to the same player's own page

    // Try main name + aliases (JP)
    const candidates: string[] = [p.name];
    if ("aliases" in p && Array.isArray((p as any).aliases)) {
      for (const a of (p as any).aliases) candidates.push(a);
    }

    for (const cand of candidates) {
      const escCand = escapeHtml(cand);
      const idx = escaped.indexOf(escCand);
      if (idx === -1) continue;
      // Avoid replacing inside an existing tag (ad-hoc check)
      const before = escaped.lastIndexOf("<", idx);
      const beforeClose = escaped.lastIndexOf(">", idx);
      if (before > beforeClose) continue;  // we're inside a tag

      const href = lang === "ja" ? `/players/${p.key}/` : `/en/players/${p.key}/`;
      const linkHtml = `<a class="autolink" href="${href}">${escCand}</a>`;
      escaped = escaped.substring(0, idx) + linkHtml + escaped.substring(idx + escCand.length);
      seenKeys.add(p.key);
      break;
    }
  }

  return escaped;
}
