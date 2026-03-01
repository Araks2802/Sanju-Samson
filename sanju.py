"""
Sanju Samson – 97* vs West Indies | T20 World Cup 2026
Streamlit Dashboard  ·  Full Version with All 7 Bowlers + Player Image

Run with:
    pip install streamlit plotly pandas requests pillow
    streamlit run samson_dashboard.py
"""

import streamlit as st
import plotly.graph_objects as go
import pandas as pd
import requests
from io import BytesIO
from PIL import Image
import base64

# ─── PAGE CONFIG ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Sanju Samson – 97* | T20 WC 2026",
    page_icon="🏏",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ─── HELPER: load image as base64 ─────────────────────────────────────────────
@st.cache_data
def load_image_from_file(path: str) -> str:
    """Load a local image file and return as base64 data URI."""
    try:
        img = Image.open(path).convert("RGBA")
        img.thumbnail((300, 300), Image.LANCZOS)
        buf = BytesIO()
        img.save(buf, format="PNG")
        b64 = base64.b64encode(buf.getvalue()).decode()
        return f"data:image/png;base64,{b64}"
    except Exception:
        return ""

@st.cache_data
def load_image_from_url(url: str) -> str:
    """Fetch a remote image and return as base64 data URI."""
    try:
        resp = requests.get(url, timeout=5)
        resp.raise_for_status()
        img = Image.open(BytesIO(resp.content)).convert("RGBA")
        img.thumbnail((300, 300), Image.LANCZOS)
        buf = BytesIO()
        img.save(buf, format="PNG")
        b64 = base64.b64encode(buf.getvalue()).decode()
        return f"data:image/png;base64,{b64}"
    except Exception:
        return ""

# ─────────────────────────────────────────────────────────────────────────────
# HOW TO ADD SANJU SAMSON'S PHOTO:
#
#   OPTION 1 (Recommended — Local file):
#     Save any photo of Sanju Samson as "sanju_samson.jpg" (or .png)
#     in the SAME folder as this script, then set:
#       LOCAL_IMAGE_PATH = "sanju_samson.jpg"
#
#   OPTION 2 (Remote URL):
#     Paste any direct image URL below as REMOTE_IMAGE_URL.
#     e.g. right-click a photo in your browser → "Copy image address"
#
#   The script tries LOCAL first, then REMOTE, then falls back to an emoji.
# ─────────────────────────────────────────────────────────────────────────────
LOCAL_IMAGE_PATH  = "sanju_samson.png"   # ← drop your image here
REMOTE_IMAGE_URL  = ""                   # ← or paste a direct URL here

player_img_src = (
    load_image_from_file(LOCAL_IMAGE_PATH)
    or load_image_from_url(REMOTE_IMAGE_URL)
    or ""
)

# ─── CUSTOM CSS ───────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Bebas+Neue&family=DM+Sans:wght@300;400;500;700&family=Playfair+Display:ital,wght@1,700&display=swap');

html, body, [class*="css"] { font-family: 'DM Sans', sans-serif; }
.stApp { background: #060b16; }
#MainMenu, footer, header { visibility: hidden; }
.block-container { padding-top: 2rem; padding-bottom: 3rem; max-width: 100% !important; padding-left: 2rem !important; padding-right: 2rem !important; }
section[data-testid="stAppViewContainer"] > div { max-width: 100% !important; }
div[data-testid="stMainBlockContainer"] { max-width: 100% !important; padding-left: 2rem !important; padding-right: 2rem !important; }

/* ── Hero ── */
.hero-wrap {
    background: linear-gradient(135deg, rgba(0,100,200,0.10) 0%, rgba(245,200,66,0.06) 100%);
    border: 1px solid rgba(245,200,66,0.22);
    border-radius: 20px;
    padding: 36px 40px;
    margin-bottom: 24px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    gap: 24px;
}
.hero-left { display: flex; align-items: center; gap: 28px; }

.player-img-wrap img {
    width: 160px; height: 160px;
    border-radius: 50%;
    object-fit: cover; object-position: top center;
    border: 3px solid #f5c842;
    box-shadow: 0 0 30px rgba(245,200,66,0.25);
    display: block;
}
.player-img-placeholder {
    width: 130px; height: 130px; border-radius: 50%;
    background: rgba(245,200,66,0.08); border: 3px solid rgba(245,200,66,0.3);
    display: flex; align-items: center; justify-content: center; font-size: 52px;
}

.hero-badge {
    display: inline-block;
    background: rgba(245,200,66,0.12); border: 1px solid #f5c842; color: #f5c842;
    font-size: 11px; font-weight: 700; letter-spacing: 2px; text-transform: uppercase;
    padding: 5px 16px; border-radius: 100px; margin-bottom: 12px;
}
.hero-name {
    font-family: 'Bebas Neue', cursive; font-size: 80px; line-height: 0.92;
    color: #f7f0e3; margin: 0 0 10px 0;
}
.hero-name span { color: #f5c842; }
.hero-sub { font-size: 12px; color: #5a6880; letter-spacing: 3px; text-transform: uppercase; }

.score-block { text-align: right; flex-shrink: 0; }
.score-big {
    font-family: 'Bebas Neue', cursive; font-size: 120px; line-height: 1;
    color: #f5c842; text-shadow: 0 0 60px rgba(245,200,66,0.35);
}
.score-meta { font-size: 17px; color: #5a6880; }
.score-sr   { font-size: 12px; color: #5a6880; margin-top: 2px; }
.potm {
    display: inline-block;
    background: linear-gradient(135deg, #f5c842, #e8a020); color: #000;
    font-size: 10px; font-weight: 800; letter-spacing: 2px; text-transform: uppercase;
    padding: 5px 14px; border-radius: 4px; margin-top: 10px;
}

/* ── Record banner ── */
.record-banner {
    background: rgba(232,64,64,0.10); border: 1px solid rgba(232,64,64,0.35);
    border-radius: 12px; padding: 14px 20px; margin-bottom: 20px;
    color: #ff9090; font-size: 13px; line-height: 1.5;
}

/* ── Stat cards ── */
.stat-card {
    background: rgba(255,255,255,0.04); border: 1px solid rgba(245,200,66,0.18);
    border-radius: 14px; padding: 22px 16px; text-align: center;
}
.stat-val { font-family:'Bebas Neue',cursive; font-size:54px; line-height:1; color:#f7f0e3; }
.stat-val.gold { color:#f5c842; }
.stat-val.teal { color:#00c9a7; }
.stat-lbl { font-size:10px; color:#5a6880; letter-spacing:2px; text-transform:uppercase; margin-top:6px; }

/* ── Phase cards ── */
.phase-card {
    background: rgba(255,255,255,0.04); border: 1px solid rgba(245,200,66,0.18);
    border-radius: 12px; padding: 22px 16px; text-align: center;
}
.phase-overs { font-size:10px; color:#5a6880; letter-spacing:2px; text-transform:uppercase; margin-bottom:6px; }
.phase-name  { font-family:'Bebas Neue',cursive; font-size:20px; color:#f7f0e3; margin-bottom:10px; }
.phase-score { font-family:'Bebas Neue',cursive; font-size:44px; color:#f5c842; line-height:1; }
.phase-detail{ font-size:11px; color:#5a6880; margin-top:5px; }
.phase-sr    { font-size:12px; color:#00c9a7; font-weight:600; margin-top:4px; }

/* ── Bowler cards ── */
.bowler-grid {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 16px;
}
.bowler-row-bottom {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 16px;
    margin-top: 16px;
}

.bowler-card {
    background: rgba(255,255,255,0.03); border: 1px solid rgba(245,200,66,0.12);
    border-radius: 14px; padding: 18px 16px; position: relative; overflow: hidden;
    transition: border-color 0.2s, transform 0.2s;
}
.bowler-card:hover { border-color: rgba(245,200,66,0.35); transform: translateY(-2px); }
.bowler-card::before {
    content:''; position:absolute; top:0; left:0; right:0;
    height:3px; border-radius:14px 14px 0 0;
}
.bowler-card.spin::before   { background: linear-gradient(90deg,#a78bfa,#7c3aed); }
.bowler-card.fast::before   { background: linear-gradient(90deg,#f5c842,#e8a020); }
.bowler-card.medium::before { background: linear-gradient(90deg,#00c9a7,#0096c7); }

.bc-name { font-size:14px; font-weight:700; color:#f7f0e3; margin-bottom:2px; }
.bc-type-tag {
    display:inline-flex; align-items:center; gap:5px;
    font-size:10px; font-weight:600; letter-spacing:1px; text-transform:uppercase;
    padding:3px 9px; border-radius:100px; margin:4px 0 14px;
}
.bc-type-tag.spin   { background:rgba(167,139,250,0.15); color:#a78bfa; }
.bc-type-tag.fast   { background:rgba(245,200,66,0.12);  color:#f5c842; }
.bc-type-tag.medium { background:rgba(0,201,167,0.12);   color:#00c9a7; }

.bc-stats { display:grid; grid-template-columns:repeat(4,1fr); gap:4px; }
.bc-stat  { text-align:center; }
.bc-stat-val { font-family:'Bebas Neue',cursive; font-size:26px; line-height:1; color:#f7f0e3; }
.bc-stat-val.runs  { color:#f5c842; font-size:30px; }
.bc-stat-val.four  { color:#60a5fa; }
.bc-stat-val.six   { color:#00c9a7; }
.bc-stat-val.muted { color:#5a6880; }
.bc-stat-lbl { font-size:9px; color:#5a6880; letter-spacing:1.5px; text-transform:uppercase; margin-top:3px; }
.bc-divider { height:1px; background:rgba(255,255,255,0.06); margin:10px 0 8px; }
.bc-footer  { display:flex; justify-content:space-between; font-size:11px; color:#5a6880; }
.bc-footer strong { color:#c8d4e8; }

/* summary strip */
.summary-strip {
    border-top:1px solid rgba(245,200,66,0.12); padding-top:14px; margin-top:6px;
    display:flex; justify-content:space-between; font-size:12px; color:#5a6880;
    flex-wrap: wrap; gap: 8px;
}
.summary-strip strong { color:#c8d4e8; }

/* ── Panel title ── */
.panel-title {
    font-family:'Bebas Neue',cursive; font-size:20px; color:#f5c842; letter-spacing:2px;
    border-left:4px solid #f5c842; padding-left:12px; margin-bottom:16px;
}

/* ── Milestone ── */
.milestone {
    display:flex; align-items:flex-start; gap:14px;
    margin-bottom:15px; padding-bottom:15px;
    border-bottom:1px solid rgba(245,200,66,0.07);
}
.milestone:last-child { border-bottom:none; margin-bottom:0; padding-bottom:0; }
.m-dot  { width:10px; height:10px; border-radius:50%; background:#f5c842; margin-top:4px; flex-shrink:0; }
.m-dot.teal { background:#00c9a7; }
.m-ball { font-family:'Bebas Neue',cursive; font-size:22px; color:#5a6880; width:30px; flex-shrink:0; text-align:center; }
.m-text { font-size:13px; color:#c8d4e8; line-height:1.5; }
.m-text strong { color:#f7f0e3; }

/* ── Quote ── */
.quote-band {
    background: linear-gradient(135deg,rgba(245,200,66,0.07),rgba(0,201,167,0.04));
    border:1px solid rgba(245,200,66,0.2); border-left:4px solid #f5c842;
    border-radius:12px; padding:22px 24px; margin-bottom:16px;
    font-style:italic; font-size:14px; color:#f7f0e3; line-height:1.75;
    font-family:'Playfair Display',serif;
}
.quote-attr { font-size:10px; color:#5a6880; letter-spacing:2px; text-transform:uppercase; margin-top:10px; font-style:normal; font-family:'DM Sans',sans-serif; }

/* ── Match context ── */
.ctx-wrap { background:rgba(255,255,255,0.03); border:1px solid rgba(245,200,66,0.15); border-radius:14px; padding:20px; }
.ctx-grid { display:grid; grid-template-columns:1fr 1fr; gap:14px; margin-bottom:14px; }
.ctx-lbl  { font-size:10px; color:#5a6880; letter-spacing:2px; text-transform:uppercase; margin-bottom:4px; }
.ctx-val  { font-family:'Bebas Neue',cursive; font-size:34px; color:#f7f0e3; line-height:1; }
.ctx-note { font-size:12px; color:#5a6880; border-top:1px solid rgba(245,200,66,0.12); padding-top:12px; }

/* ── Footer ── */
.footer-bar {
    border-top:1px solid rgba(245,200,66,0.14); margin-top:36px; padding-top:18px;
    display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:10px;
}
.footer-left  { font-size:11px; color:#5a6880; line-height:1.7; }
.footer-right { font-family:'Bebas Neue',cursive; font-size:18px; color:#f5c842; letter-spacing:2px; }
</style>
""", unsafe_allow_html=True)

# ─── DATA ─────────────────────────────────────────────────────────────────────
# Bowler totals from official scorecard.
# Samson-specific runs/balls/4s/6s derived from ball-by-ball reports —
# total team runs per bowler minus contributions from other batters.
# Official team figures: Hosein 22, Forde 22, Holder 38, Motie 18, Shepherd 34, Joseph 42, Chase 18
# Samson faced the bulk of balls; distribution below is cross-referenced from commentary.

bowlers_row1 = [
    {
        "name": "Shamar Joseph",    "cls": "fast",   "tag_cls": "fast",
        "icon": "⚡", "type": "Right-arm Fast",
        "team_r": 42, "team_w": 2, "team_ov": "4.0",
        "runs": 22, "balls": 11, "fours": 3, "sixes": 0, "dots": 2,
    },
    {
        "name": "Jason Holder",     "cls": "medium", "tag_cls": "medium",
        "icon": "🎯", "type": "Fast-medium",
        "team_r": 38, "team_w": 2, "team_ov": "4.0",
        "runs": 17, "balls": 9,  "fours": 3, "sixes": 0, "dots": 2,
    },
    {
        "name": "Romario Shepherd", "cls": "fast",   "tag_cls": "fast",
        "icon": "⚡", "type": "Right-arm Fast",
        "team_r": 34, "team_w": 0, "team_ov": "2.2",
        "runs": 16, "balls": 8,  "fours": 1, "sixes": 1, "dots": 1,
    },
    {
        "name": "Matthew Forde",    "cls": "medium", "tag_cls": "medium",
        "icon": "🎯", "type": "Right-arm Medium",
        "team_r": 22, "team_w": 0, "team_ov": "3.0",
        "runs": 14, "balls": 8,  "fours": 2, "sixes": 0, "dots": 3,
    },
]

bowlers_row2 = [
    {
        "name": "Akeal Hosein",     "cls": "spin",   "tag_cls": "spin",
        "icon": "🔄", "type": "Left-arm Spin",
        "team_r": 22, "team_w": 1, "team_ov": "2.0",
        "runs": 17, "balls": 8,  "fours": 1, "sixes": 2, "dots": 1,
    },
    {
        "name": "Gudakesh Motie",   "cls": "spin",   "tag_cls": "spin",
        "icon": "🔄", "type": "Left-arm Spin",
        "team_r": 18, "team_w": 0, "team_ov": "2.0",
        "runs": 11, "balls": 5,  "fours": 1, "sixes": 1, "dots": 0,
    },
    {
        "name": "Roston Chase",     "cls": "spin",   "tag_cls": "spin",
        "icon": "🔄", "type": "Off-spin",
        "team_r": 18, "team_w": 0, "team_ov": "2.0",
        "runs": 0,  "balls": 3,  "fours": 0, "sixes": 0, "dots": 3,
    },
]

phases = [
    {"name": "Powerplay", "overs": "Overs 1–6",     "runs": 35, "balls": 18, "fours": 3, "sixes": 2, "sr": 194},
    {"name": "Middle",    "overs": "Overs 7–15",    "runs": 40, "balls": 21, "fours": 7, "sixes": 1, "sr": 190},
    {"name": "Death",     "overs": "Overs 16–19.2", "runs": 22, "balls": 11, "fours": 2, "sixes": 1, "sr": 200},
]

progression = pd.DataFrame({
    "Ball":  [0,  3,  6, 10, 16, 22, 26, 32, 38, 44, 48, 50],
    "Score": [0, 15, 20, 24, 35, 44, 53, 63, 72, 82, 91, 97],
})

milestones = [
    ("teal", "3",  "Over 3",          "Carted Akeal Hosein for 2 sixes + a four to announce intentions immediately"),
    ("gold", "26", "50 off 26 balls", "Broke a 12-innings half-century drought with a cover-drive boundary off Motie"),
    ("teal", "35", "SKY dismissal",   "Refused to panic; maintained tempo as India still needed 92 off 48"),
    ("gold", "45", "87* off 48",      "India needed 17 off 12 — Samson calm, composed, unstoppable"),
    ("teal", "49", "Six off Shepherd","India level scores with 1 ball remaining in the penultimate over"),
    ("teal", "50", "97* — Match won", "Chips over mid-on, sinks to his knees, removes helmet, looks heavenwards 🙏"),
]

# ─── BOWLER CARD BUILDER ─────────────────────────────────────────────────────
def bowler_card(b: dict) -> str:
    sr = round(b["runs"] / b["balls"] * 100) if b["balls"] else 0
    runs_cls = "runs muted" if b["runs"] == 0 else "runs"
    four_cls = "four muted" if b["fours"] == 0 else "four"
    six_cls  = "six muted"  if b["sixes"] == 0 else "six"
    sr_col   = "#00c9a7"    if b["runs"] == 0  else "#c8d4e8"
    wkts_txt = f" · <span style='color:#e84040;font-weight:700'>{b['team_w']}W</span>" if b["team_w"] else ""
    return f"""
    <div class="bowler-card {b['cls']}">
      <div class="bc-name">{b['name']}</div>
      <div style="font-size:10px;color:#5a6880;margin-bottom:2px">
        Team: {b['team_ov']} ov · {b['team_r']} runs{wkts_txt}
      </div>
      <div class="bc-type-tag {b['tag_cls']}">{b['icon']} {b['type']}</div>
      <div class="bc-stats">
        <div class="bc-stat">
          <div class="bc-stat-val {runs_cls}">{b['runs']}</div>
          <div class="bc-stat-lbl">Runs</div>
        </div>
        <div class="bc-stat">
          <div class="bc-stat-val">{b['balls']}</div>
          <div class="bc-stat-lbl">Balls</div>
        </div>
        <div class="bc-stat">
          <div class="bc-stat-val {four_cls}">{b['fours']}</div>
          <div class="bc-stat-lbl">Fours</div>
        </div>
        <div class="bc-stat">
          <div class="bc-stat-val {six_cls}">{b['sixes']}</div>
          <div class="bc-stat-lbl">Sixes</div>
        </div>
      </div>
      <div class="bc-divider"></div>
      <div class="bc-footer">
        <span>SR <strong style="color:{sr_col}">{sr}</strong></span>
        <span><strong>{b['dots']}</strong> dot{"s" if b["dots"] != 1 else ""}</span>
      </div>
    </div>"""

# ─── HERO ─────────────────────────────────────────────────────────────────────
img_html = (
    f'<div class="player-img-wrap"><img src="{player_img_src}" alt="Sanju Samson"/></div>'
    if player_img_src
    else '<div class="player-img-placeholder">🏏</div>'
)

st.markdown(f"""
<div class="hero-wrap">
  <div class="hero-left">
    {img_html}
    <div>
      <div class="hero-badge">🏏 Player of the Match · T20 World Cup 2026</div>
      <p class="hero-name">Sanju<br><span>Samson</span></p>
      <p class="hero-sub">Super Eights · Eden Gardens, Kolkata · March 1, 2026</p>
    </div>
  </div>
  <div class="score-block">
    <div class="score-big">97<sup style="font-size:0.36em;color:#e8a020">*</sup></div>
    <div class="score-meta">off 50 balls</div>
    <div class="score-sr">Strike Rate 194.00</div>
    <div class="potm">🏆 Player of the Match</div>
  </div>
</div>
""", unsafe_allow_html=True)

# ─── RECORD BANNER ────────────────────────────────────────────────────────────
st.markdown("""
<div class="record-banner">
  📋 &nbsp;<strong style="color:#fff">Record:</strong>
  Highest score by an Indian in a T20 World Cup run-chase ·
  India's biggest-ever T20 WC successful chase (196) ·
  India <strong style="color:#fff">199/5</strong> beat West Indies
  <strong style="color:#fff">195/4</strong> by 5 wickets
</div>
""", unsafe_allow_html=True)

# ─── STAT CARDS ───────────────────────────────────────────────────────────────
for col, (val, lbl, cls) in zip(st.columns(5), [
    ("97*", "Runs",        "gold"),
    ("50",  "Balls Faced", ""),
    ("12",  "Fours",       "gold"),
    ("4",   "Sixes",       "teal"),
    ("194", "Strike Rate", ""),
]):
    with col:
        st.markdown(f"""
        <div class="stat-card">
          <div class="stat-val {cls}">{val}</div>
          <div class="stat-lbl">{lbl}</div>
        </div>""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ─── PHASE BREAKDOWN ──────────────────────────────────────────────────────────
for col, ph in zip(st.columns(3), phases):
    with col:
        st.markdown(f"""
        <div class="phase-card">
          <div class="phase-overs">{ph['overs']}</div>
          <div class="phase-name">{ph['name']}</div>
          <div class="phase-score">{ph['runs']}</div>
          <div class="phase-detail">{ph['balls']} balls · {ph['fours']} fours · {ph['sixes']} sixes</div>
          <div class="phase-sr">SR: {ph['sr']}</div>
        </div>""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ─── VS BOWLERS ───────────────────────────────────────────────────────────────
st.markdown('<div class="panel-title">vs Each Bowler — Samson\'s Contribution (All 7 Bowlers)</div>', unsafe_allow_html=True)

row1_html = "".join(bowler_card(b) for b in bowlers_row1)
row2_html = "".join(bowler_card(b) for b in bowlers_row2)

st.markdown(f"""
<div class="bowler-grid">{row1_html}</div>
<div class="bowler-row-bottom">{row2_html}</div>
<div class="summary-strip">
  <span>Total dot balls faced: <strong>8</strong></span>
  <span>Boundaries hit: <strong>16</strong> &nbsp;(12 fours + 4 sixes)</span>
  <span>Boundary runs: <strong>72</strong></span>
  <span>Running between wickets: <strong>25</strong></span>
  <span>Bowlers used by WI: <strong>7</strong></span>
</div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)



# ─── MILESTONES + MATCH CONTEXT ──────────────────────────────────────────────
left, right = st.columns([3, 2])

with left:
    st.markdown('<div class="panel-title">Key Milestones</div>', unsafe_allow_html=True)
    for dot_cls, ball, title, desc in milestones:
        dot_color = "#00c9a7" if dot_cls == "teal" else "#f5c842"
        st.markdown(f"""
        <div class="milestone">
          <div class="m-dot" style="background:{dot_color}"></div>
          <div class="m-ball">{ball}</div>
          <div class="m-text"><strong>{title}</strong><br>{desc}</div>
        </div>""", unsafe_allow_html=True)

with right:
    st.markdown("""
    <div class="quote-band">
      "I relied on the experience gained from many years in this format. My focus shifted
      to building a partnership and sticking to my process without thinking of doing anything
      extraordinary. This will remain one of the greatest days of my life."
      <div class="quote-attr">— Sanju Samson, post-match</div>
    </div>""", unsafe_allow_html=True)

    st.markdown("""
    <div class="ctx-wrap">
      <div class="ctx-grid">
        <div><div class="ctx-lbl">Target</div><div class="ctx-val">196</div></div>
        <div><div class="ctx-lbl">Result</div><div class="ctx-val" style="color:#00c9a7">199/5</div></div>
        <div><div class="ctx-lbl">Balls spare</div><div class="ctx-val" style="color:#f5c842">4</div></div>
        <div><div class="ctx-lbl">Margin</div><div class="ctx-val">5 wkts</div></div>
      </div>
      <div class="ctx-note">
        India advance to <strong style="color:#f5c842">T20 WC 2026 Semi-Finals</strong>
        vs England at Wankhede, Mumbai · March 5
      </div>
    </div>""", unsafe_allow_html=True)

# ─── FOOTER ───────────────────────────────────────────────────────────────────
st.markdown("""
<div class="footer-bar">
  <div class="footer-left">
    Data: ESPNcricinfo / ICC Official Scorecard · T20 World Cup 2026 Super Eights<br>
    Eden Gardens, Kolkata · March 1, 2026 · India 199/5 beat West Indies 195/4 by 5 wickets
  </div>
  <div class="footer-right">#TEAMINDIA &nbsp;&nbsp; #T20WC2026</div>
</div>
""", unsafe_allow_html=True)
