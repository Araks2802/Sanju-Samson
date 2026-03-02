"""
Sanju Samson – 97* vs West Indies | T20 World Cup 2026
REVAMP v3 — Cinematic Broadcast Aesthetic

pip install streamlit plotly pandas requests pillow
streamlit run samson_dashboard.py
"""

import streamlit as st
import plotly.graph_objects as go
import pandas as pd
import numpy as np
import requests
from io import BytesIO
from PIL import Image
import base64

st.set_page_config(
    page_title="Sanju Samson 97* | T20 WC 2026",
    page_icon="🏏",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ─── IMAGE ────────────────────────────────────────────────────────────────────
@st.cache_data
def load_img_file(path):
    try:
        img = Image.open(path).convert("RGBA")
        img.thumbnail((340, 340), Image.LANCZOS)
        buf = BytesIO(); img.save(buf, format="PNG")
        return f"data:image/png;base64,{base64.b64encode(buf.getvalue()).decode()}"
    except: return ""

@st.cache_data
def load_img_url(url):
    try:
        r = requests.get(url, timeout=5); r.raise_for_status()
        img = Image.open(BytesIO(r.content)).convert("RGBA")
        img.thumbnail((340, 340), Image.LANCZOS)
        buf = BytesIO(); img.save(buf, format="PNG")
        return f"data:image/png;base64,{base64.b64encode(buf.getvalue()).decode()}"
    except: return ""

LOCAL_IMAGE_PATH = "sanju_samson.png"
REMOTE_IMAGE_URL = ""
player_img = load_img_file(LOCAL_IMAGE_PATH) or load_img_url(REMOTE_IMAGE_URL) or ""

# ─── DATA ─────────────────────────────────────────────────────────────────────
bowlers = [
    {"name":"Shamar Joseph",    "cls":"fast",   "type":"Right-arm Fast",   "team_r":42,"team_w":2,"team_ov":"4.0","runs":12,"balls":8, "fours":2,"sixes":0,"dots":2},
    {"name":"Jason Holder",     "cls":"medium", "type":"Fast-medium",      "team_r":38,"team_w":2,"team_ov":"4.0","runs":17,"balls":8, "fours":3,"sixes":0,"dots":0},
    {"name":"Romario Shepherd", "cls":"fast",   "type":"Right-arm Fast",   "team_r":34,"team_w":0,"team_ov":"2.2","runs":24,"balls":9, "fours":2,"sixes":2,"dots":1},
    {"name":"Matthew Forde",    "cls":"medium", "type":"Right-arm Medium", "team_r":22,"team_w":0,"team_ov":"3.0","runs":7, "balls":9, "fours":1,"sixes":0,"dots":4},
    {"name":"Akeal Hosein",     "cls":"spin",   "type":"Left-arm Spin",    "team_r":22,"team_w":1,"team_ov":"2.0","runs":17,"balls":5, "fours":1,"sixes":2,"dots":1},
    {"name":"Gudakesh Motie",   "cls":"spin",   "type":"Left-arm Spin",    "team_r":18,"team_w":0,"team_ov":"2.0","runs":12,"balls":7, "fours":2,"sixes":0,"dots":1},
    {"name":"Roston Chase",     "cls":"spin",   "type":"Off-spin",         "team_r":18,"team_w":0,"team_ov":"2.0","runs":8, "balls":5, "fours":1,"sixes":0,"dots":0},
]

phases = [
    {"key":"pp",  "label":"Overs 1–6",     "name":"Powerplay","runs":24,"balls":13,"fours":2,"sixes":2,"sr":185},
    {"key":"mid", "label":"Overs 7–15",    "name":"Middle",   "runs":55,"balls":30,"fours":8,"sixes":1,"sr":183},
    {"key":"dt",  "label":"Overs 16–19.2", "name":"Death",    "runs":18,"balls":7, "fours":2,"sixes":1,"sr":257},
]

partnerships = [
    {"wkt":"1st","p2":"Abhishek", "runs":29, "balls":18, "samson":19, "overs":"1–2.x"},
    {"wkt":"2nd","p2":"Ishan",    "runs":12, "balls":9,  "samson":7,  "overs":"3–4.x"},
    {"wkt":"3rd","p2":"SKY",      "runs":58, "balls":35, "samson":36, "overs":"4.x–10.x"},
    {"wkt":"4th","p2":"Tilak",    "runs":42, "balls":26, "samson":22, "overs":"11–14.4"},
    {"wkt":"5th","p2":"Hardik",   "runs":38, "balls":22, "samson":24, "overs":"14.4–18.x"},
    {"wkt":"6th","p2":"Dube",     "runs":20, "balls":6,  "samson":14, "overs":"19–19.2"},
]

rr_df = pd.DataFrame({
    "Over":     list(range(1, 20)),
    # Confirmed over-by-over totals from live commentary:
    # end ov2=12, ov5=45, ov6=53, ov7=67, ov8=78, ov9=91, ov10=98,
    # ov11≈101, ov12≈104, ov13=121, ov14=136, ov15=146, ov16=160, ov17=171, ov18=179, ov19=189
    "Actual":   [6,  6, 16,  7,  8,  8, 14, 11, 13,  7,  3,  3, 17, 15, 10, 14, 11,  8, 10],
    "Required": [9.8, 9.8, 9.7, 9.6, 9.5, 9.5, 9.3, 9.5, 9.6, 9.8, 10.1, 10.4, 10.1, 9.8, 9.5, 9.1, 8.3, 6.9, 5.0],
})

# Team score progression (confirmed checkpoints)
prog_df = pd.DataFrame({
    "Ball":  [0,  12,  20,  26,  35,  42,  50,  60,  66,  78,  84,  96, 112, 116],
    "Score": [0,  12,  31,  41,  53,  67,  80,  98,  101, 121, 136, 160, 183, 199],
})

key_moments = [
    ("Over 3",   "🔥", "#f59e0b", "Hosein wiped",        "2 sixes + a four in the third over. Eden erupts. Samson has announced himself."),
    ("Ball 26",  "⭐", "#f5c842", "Half-century",         "Cover-driven off Motie. 50 off 26. Twelve innings of waiting, settled in one stroke."),
    ("Over 11",  "⚠️", "#e84040", "Danger — 107/4",       "SKY gone. India needed 89 more. Samson looked at the required rate and smiled."),
    ("Over 14",  "💎", "#a78bfa", "69 off 39",            "Tilak falls. 60 needed in 6 overs. Samson chose belief over caution."),
    ("Ball 49",  "🚀", "#00c9a7", "Six to level scores",  "Shepherd over square leg. India level with 1 ball to spare in the over."),
    ("Ball 50",  "🏆", "#f5c842", "97* — India win 🙏",   "Chips over mid-on. Kneels. Helmet off. Eyes skyward. The wait was worth it."),
]

# ─── FULL CSS ──────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Anton&family=Outfit:wght@300;400;500;600;700&family=Playfair+Display:ital,wght@1,500;1,700&display=swap');

:root {
  --gold: #f5c842;
  --gold-dim: rgba(245,200,66,0.15);
  --teal: #00c9a7;
  --blue: #60a5fa;
  --red: #e84040;
  --bg: #060912;
  --surface: rgba(255,255,255,0.028);
  --border: rgba(255,255,255,0.07);
  --text: #edeae0;
  --muted: rgba(255,255,255,0.22);
  --faint: rgba(255,255,255,0.07);
}

*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
html, body, [class*="css"] { font-family: 'Outfit', sans-serif; }
.stApp {
    background: var(--bg);
    background-image:
        radial-gradient(ellipse 100% 55% at 50% -5%,  rgba(245,200,66,0.11) 0%, transparent 55%),
        radial-gradient(ellipse 45% 45% at 2%  85%,   rgba(0,180,130,0.07)  0%, transparent 55%),
        radial-gradient(ellipse 35% 35% at 98% 15%,   rgba(96,165,250,0.05) 0%, transparent 50%);
}
#MainMenu, footer, header { visibility: hidden; }
.block-container { padding: 0 !important; max-width: 100% !important; }
div[data-testid="stMainBlockContainer"] { max-width: 100% !important; padding: 0 !important; }

/* ── TICKER ── */
.ticker-wrap {
    background: var(--gold);
    overflow: hidden; height: 34px;
    display: flex; align-items: center;
}
.ticker-label {
    background: #000;
    color: var(--gold);
    font-family: 'Anton', sans-serif;
    font-size: 11px; letter-spacing: 3px;
    padding: 0 18px; height: 100%;
    display: flex; align-items: center;
    flex-shrink: 0; white-space: nowrap;
}
.ticker-track {
    display: flex; gap: 0;
    animation: ticker 30s linear infinite;
    white-space: nowrap;
}
@keyframes ticker { 0%{transform:translateX(0)} 100%{transform:translateX(-50%)} }
.ticker-item {
    font-family: 'Anton', sans-serif;
    font-size: 11px; letter-spacing: 2px;
    color: #000; padding: 0 32px;
    border-right: 1px solid rgba(0,0,0,0.2);
    height: 34px; display: flex; align-items: center;
}

/* ── NAV ── */
.nav {
    display: flex; align-items: center; justify-content: space-between;
    padding: 12px 44px;
    border-bottom: 1px solid var(--border);
    background: rgba(6,9,18,0.92);
    backdrop-filter: blur(20px);
}
.nav-logo {
    font-family: 'Anton', sans-serif;
    font-size: 22px; letter-spacing: 3px;
    color: var(--text); display: flex; align-items: center; gap: 10px;
}
.nav-logo span { color: var(--gold); }
.nav-logo-sub { font-family: 'Outfit', sans-serif; font-size: 10px; font-weight: 400; letter-spacing: 3px; color: var(--muted); margin-left: 4px; align-self: flex-end; padding-bottom: 2px; }
.nav-tags { display: flex; gap: 6px; }
.nav-tag { font-size: 9px; font-weight: 600; letter-spacing: 2px; text-transform: uppercase; padding: 4px 12px; border-radius: 100px; color: var(--muted); border: 1px solid var(--faint); }
.nav-tag.hi { background: rgba(245,200,66,0.1); border-color: rgba(245,200,66,0.3); color: var(--gold); }
.nav-status { font-size: 11px; font-weight: 600; letter-spacing: 2px; color: var(--teal); display: flex; align-items: center; gap: 7px; }
.blink-dot { width: 7px; height: 7px; border-radius: 50%; background: var(--teal); animation: blink 1.8s ease-in-out infinite; }
@keyframes blink { 0%,100%{opacity:1} 50%{opacity:0.2} }

/* ── WRAP ── */
.wrap { padding: 36px 44px 80px; }

/* ── HERO ── */
.hero {
    position: relative; overflow: hidden;
    border-radius: 22px;
    border: 1px solid rgba(245,200,66,0.14);
    background: linear-gradient(125deg, #0d1525 0%, #080e1c 45%, #0b1c12 100%);
    margin-bottom: 28px;
    display: grid; grid-template-columns: 1fr 260px;
    min-height: 280px;
}
.hero-noise {
    position: absolute; inset: 0;
    background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 256 256' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noise'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noise)' opacity='0.035'/%3E%3C/svg%3E");
    pointer-events: none; opacity: 0.5;
}
.hero-top-line { position: absolute; top: 0; left: 0; right: 0; height: 3px; background: linear-gradient(90deg, transparent, var(--gold) 25%, var(--teal) 65%, transparent); }
.hero-97 {
    position: absolute; right: 255px; bottom: -30px;
    font-family: 'Anton', sans-serif; font-size: 340px;
    color: rgba(245,200,66,0.035); line-height: 1;
    pointer-events: none; user-select: none; letter-spacing: -12px;
}
.hero-body { display: flex; align-items: center; gap: 38px; padding: 42px 44px; position: relative; z-index: 1; }
.hero-img-outer { position: relative; flex-shrink: 0; }
.hero-glow { position: absolute; inset: -16px; border-radius: 50%; background: radial-gradient(circle, rgba(245,200,66,0.22) 0%, transparent 68%); animation: breathe 3.5s ease-in-out infinite; }
@keyframes breathe { 0%,100%{opacity:0.5;transform:scale(0.97)} 50%{opacity:1;transform:scale(1.03)} }
.hero-ring { position: absolute; inset: -5px; border-radius: 50%; background: conic-gradient(from 180deg, var(--gold) 0%, var(--teal) 35%, transparent 55%, var(--gold) 100%); animation: spin 7s linear infinite; }
@keyframes spin { to { transform: rotate(360deg); } }
.hero-img { position: relative; z-index: 1; width: 152px; height: 152px; border-radius: 50%; overflow: hidden; border: 3px solid var(--bg); background: var(--gold-dim); }
.hero-img img { width: 100%; height: 100%; object-fit: cover; object-position: top center; }
.hero-img-emoji { width: 100%; height: 100%; display: flex; align-items: center; justify-content: center; font-size: 60px; }
.hero-copy { flex: 1; }
.hero-badge {
    display: inline-flex; align-items: center; gap: 7px;
    border: 1px solid rgba(245,200,66,0.3);
    background: rgba(245,200,66,0.07);
    color: var(--gold); font-size: 9px; font-weight: 600;
    letter-spacing: 3px; text-transform: uppercase;
    padding: 4px 13px; border-radius: 2px; margin-bottom: 14px;
}
.hero-name {
    font-family: 'Anton', sans-serif; font-size: 78px;
    color: var(--text); text-transform: uppercase;
    line-height: 0.88; letter-spacing: 1px; margin-bottom: 18px;
}
.hero-name em { display: block; color: var(--gold); font-style: normal; font-size: 0.82em; letter-spacing: 8px; font-family: 'Outfit', sans-serif; font-weight: 300; }
.hero-meta { display: flex; gap: 8px; flex-wrap: wrap; }
.hero-meta-tag { font-size: 9px; font-weight: 500; letter-spacing: 2px; text-transform: uppercase; color: var(--muted); border: 1px solid var(--faint); padding: 3px 10px; border-radius: 100px; }

/* SCORE PANEL */
.score-panel {
    display: flex; flex-direction: column; justify-content: center; align-items: flex-end;
    padding: 36px 40px 36px 24px;
    border-left: 1px solid var(--border);
    position: relative; z-index: 1;
}
.score-num {
    font-family: 'Anton', sans-serif; font-size: 130px; line-height: 0.84;
    color: var(--gold); letter-spacing: -3px;
    text-shadow: 0 0 80px rgba(245,200,66,0.3);
}
.score-num sup { font-size: 0.32em; color: #d4920a; vertical-align: super; }
.score-sub { font-size: 12px; color: var(--muted); letter-spacing: 3px; text-align: right; margin-top: 4px; }
.score-sr { display: flex; gap: 10px; align-items: baseline; margin-top: 16px; justify-content: flex-end; }
.score-sr-lbl { font-size: 8px; font-weight: 600; letter-spacing: 3px; text-transform: uppercase; color: var(--faint); }
.score-sr-val { font-family: 'Anton', sans-serif; font-size: 28px; color: var(--teal); letter-spacing: 1px; }
.potm-chip { margin-top: 18px; background: linear-gradient(135deg, var(--gold), #c07800); color: #000; font-family: 'Anton', sans-serif; font-size: 9px; letter-spacing: 3px; padding: 7px 16px; border-radius: 2px; display: inline-block; }

/* ── RECORD STRIP ── */
.record-strip {
    display: flex; align-items: center; gap: 12px;
    background: rgba(232,64,64,0.05);
    border: 1px solid rgba(232,64,64,0.18);
    border-left: 3px solid var(--red);
    border-radius: 0 10px 10px 0;
    padding: 10px 18px; margin-bottom: 28px;
    font-size: 12px; color: rgba(255,255,255,0.3); line-height: 1.65;
}
.record-strip strong { color: var(--text); }

/* ── SECTION HEADER ── */
.sh {
    display: flex; align-items: center; gap: 16px;
    margin: 36px 0 16px;
}
.sh-label {
    font-family: 'Anton', sans-serif; font-size: 14px;
    letter-spacing: 5px; text-transform: uppercase;
    color: var(--gold); white-space: nowrap;
}
.sh-line { flex: 1; height: 1px; background: linear-gradient(90deg, rgba(245,200,66,0.25), transparent); }
.sh-pill { font-size: 9px; font-weight: 600; letter-spacing: 2px; text-transform: uppercase; color: var(--muted); border: 1px solid var(--faint); padding: 2px 10px; border-radius: 100px; white-space: nowrap; }

/* ── OVERVIEW STRIP ── */
.ov-strip { display: grid; grid-template-columns: repeat(5,1fr); gap: 10px; margin-bottom: 28px; }
.ov-card {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 14px; padding: 18px 20px;
    display: flex; justify-content: space-between; align-items: center;
    gap: 8px; position: relative; overflow: hidden;
    transition: transform 0.2s, border-color 0.2s;
}
.ov-card:hover { transform: translateY(-3px); border-color: rgba(245,200,66,0.22); }
.ov-card::before { content: ''; position: absolute; left: 0; top: 22%; bottom: 22%; width: 2px; background: var(--ac,var(--gold)); border-radius: 2px; opacity: 0.7; }
.ov-lhs { display: flex; flex-direction: column; gap: 5px; }
.ov-icon { font-size: 19px; }
.ov-lbl { font-size: 8px; font-weight: 600; letter-spacing: 3px; text-transform: uppercase; color: var(--muted); }
.ov-num { font-family: 'Anton', sans-serif; font-size: 52px; line-height: 1; color: var(--text); }
.ov-num.g { color: var(--gold); }
.ov-num.t { color: var(--teal); }
.ov-num.b { color: var(--blue); }

/* ── PHASE CARDS ── */
.phase-row { display: grid; grid-template-columns: repeat(3,1fr); gap: 10px; margin-bottom: 28px; }
.pc {
    background: var(--surface); border: 1px solid var(--border);
    border-radius: 14px; padding: 22px 24px;
    display: flex; align-items: center; gap: 22px;
    position: relative; overflow: hidden;
}
.pc::before { content: ''; position: absolute; top: 0; left: 0; bottom: 0; width: 3px; }
.pc.pp::before  { background: linear-gradient(180deg,var(--gold),#c07800); }
.pc.mid::before { background: linear-gradient(180deg,var(--blue),#2563eb); }
.pc.dt::before  { background: linear-gradient(180deg,#f97316,#c2410c); }
.pc-big { font-family: 'Anton', sans-serif; font-size: 76px; line-height: 1; flex-shrink: 0; }
.pc.pp  .pc-big { color: var(--gold); }
.pc.mid .pc-big { color: var(--blue); }
.pc.dt  .pc-big { color: #f97316; }
.pc-info { flex: 1; min-width: 0; }
.pc-over { font-size: 8px; font-weight: 600; letter-spacing: 3px; text-transform: uppercase; color: var(--muted); }
.pc-name { font-family: 'Anton', sans-serif; font-size: 21px; color: var(--text); letter-spacing: 1px; text-transform: uppercase; line-height: 1; margin: 4px 0 10px; }
.pc-sr-pill { display: inline-block; background: rgba(0,201,167,0.1); border: 1px solid rgba(0,201,167,0.22); color: var(--teal); font-size: 10px; font-weight: 600; letter-spacing: 1px; padding: 3px 10px; border-radius: 100px; margin-bottom: 9px; }
.pc-meta { display: flex; gap: 12px; flex-wrap: nowrap; }
.pc-tag { font-size: 10px; color: var(--muted); display: flex; align-items: center; gap: 4px; white-space: nowrap; }
.pc-dot { width: 5px; height: 5px; border-radius: 50%; flex-shrink: 0; }

/* ── TWO-COL ── */
.two-col { display: grid; grid-template-columns: 1fr 1fr; gap: 16px; margin-bottom: 28px; }
.chart-box { background: var(--surface); border: 1px solid var(--border); border-radius: 14px; padding: 4px; overflow: hidden; }

/* ── PARTNERSHIPS ── */
.pship-row { display: grid; grid-template-columns: repeat(6,1fr); gap: 8px; margin-bottom: 28px; }
.pship-card {
    background: var(--surface); border: 1px solid var(--border);
    border-radius: 12px; padding: 14px 15px;
    transition: transform 0.2s, border-color 0.2s;
}
.pship-card:hover { transform: translateY(-2px); border-color: rgba(245,200,66,0.2); }
.pship-wkt { font-size: 8px; font-weight: 600; letter-spacing: 3px; text-transform: uppercase; color: var(--muted); margin-bottom: 5px; }
.pship-names { font-size: 11px; font-weight: 600; color: var(--text); line-height: 1.3; margin-bottom: 9px; }
.pship-names em { color: var(--gold); font-style: normal; }
.pship-big { font-family: 'Anton', sans-serif; font-size: 42px; line-height: 1; color: var(--text); }
.pship-balls { font-size: 9px; color: var(--muted); letter-spacing: 1px; margin-bottom: 8px; }
.pship-bar-bg { height: 3px; background: var(--faint); border-radius: 2px; overflow: hidden; margin-bottom: 5px; }
.pship-bar-fg { height: 100%; border-radius: 2px; background: linear-gradient(90deg, var(--gold), rgba(245,200,66,0.4)); }
.pship-pct { display: flex; justify-content: space-between; font-size: 8px; color: var(--muted); }

/* ── BOWLER GRID ── */
.bowler-row-4 { display: grid; grid-template-columns: repeat(4,1fr); gap: 10px; margin-bottom: 10px; }
.bowler-row-3 { display: grid; grid-template-columns: repeat(3,1fr); gap: 10px; margin-bottom: 16px; }
.bc {
    background: var(--surface); border: 1px solid var(--border);
    border-radius: 14px; padding: 14px 16px;
    position: relative; overflow: hidden;
    transition: transform 0.2s, border-color 0.2s;
}
.bc:hover { transform: translateY(-2px); border-color: rgba(245,200,66,0.2); }
.bc .top-bar { position: absolute; top: 0; left: 0; right: 0; height: 2px; }
.bc.fast   .top-bar { background: linear-gradient(90deg,var(--gold),#f97316); }
.bc.medium .top-bar { background: linear-gradient(90deg,var(--teal),#0284c7); }
.bc.spin   .top-bar { background: linear-gradient(90deg,#a78bfa,#7c3aed); }
.bc-hd { display: flex; justify-content: space-between; align-items: flex-start; margin: 6px 0 4px; }
.bc-name { font-size: 13px; font-weight: 600; color: var(--text); }
.bc-pill { font-size: 7px; font-weight: 700; letter-spacing: 1px; text-transform: uppercase; padding: 2px 8px; border-radius: 100px; }
.bc.fast   .bc-pill { background: rgba(245,200,66,0.1);  color: var(--gold); }
.bc.medium .bc-pill { background: rgba(0,201,167,0.1);   color: var(--teal); }
.bc.spin   .bc-pill { background: rgba(167,139,250,0.1); color: #a78bfa; }
.bc-sub { font-size: 9px; color: var(--faint); margin-bottom: 10px; }
.bc-grid { display: grid; grid-template-columns: repeat(4,1fr); gap: 2px; background: rgba(0,0,0,0.22); border-radius: 8px; padding: 8px 4px; }
.bc-cell { text-align: center; }
.bc-val { font-family: 'Anton', sans-serif; font-size: 26px; line-height: 1; color: var(--text); }
.bc-val.g { color: var(--gold); font-size: 30px; }
.bc-val.b { color: var(--blue); }
.bc-val.t { color: var(--teal); }
.bc-val.x { color: rgba(255,255,255,0.12); }
.bc-lbl { font-size: 7px; color: rgba(255,255,255,0.18); letter-spacing: 1.5px; text-transform: uppercase; margin-top: 2px; }
.bc-ft { display: flex; justify-content: space-between; margin-top: 8px; padding-top: 7px; border-top: 1px solid var(--faint); font-size: 10px; color: var(--muted); }
.bc-ft b { color: rgba(255,255,255,0.5); }

/* ── SUMMARY BAR ── */
.sum-bar { display: flex; border: 1px solid var(--border); border-radius: 11px; overflow: hidden; margin-bottom: 28px; }
.sum-cell { flex: 1; text-align: center; padding: 11px 6px; border-right: 1px solid var(--faint); background: rgba(255,255,255,0.01); }
.sum-cell:last-child { border-right: none; }
.sum-val { font-family: 'Anton', sans-serif; font-size: 22px; color: var(--gold); line-height: 1; }
.sum-lbl { font-size: 7px; color: var(--muted); letter-spacing: 2px; text-transform: uppercase; margin-top: 3px; }

/* ── KEY MOMENTS ── */
.moments-grid { display: grid; grid-template-columns: repeat(3,1fr); gap: 10px; margin-bottom: 28px; }
.moment-card {
    background: var(--surface); border: 1px solid var(--border);
    border-radius: 14px; padding: 18px 20px;
    position: relative; overflow: hidden;
    transition: transform 0.2s, border-color 0.2s;
}
.moment-card:hover { transform: translateY(-2px); border-color: rgba(245,200,66,0.18); }
.moment-card::before { content: ''; position: absolute; top: 0; left: 0; right: 0; height: 2px; background: var(--mc, var(--gold)); }
.moment-top { display: flex; align-items: center; gap: 10px; margin-bottom: 10px; }
.moment-emoji { font-size: 22px; }
.moment-over { font-family: 'Anton', sans-serif; font-size: 13px; letter-spacing: 3px; color: var(--mc,var(--gold)); }
.moment-title { font-family: 'Anton', sans-serif; font-size: 20px; letter-spacing: 0.5px; color: var(--text); margin-bottom: 6px; line-height: 1.1; }
.moment-desc { font-size: 12px; color: var(--muted); line-height: 1.6; }

/* ── BOTTOM SPLIT ── */
.bottom-split { display: grid; grid-template-columns: 1fr 1fr; gap: 16px; margin-bottom: 28px; }

/* ── QUOTE ── */
.quote-card { background: var(--surface); border: 1px solid var(--border); border-top: 2px solid var(--gold); border-radius: 0 0 14px 14px; padding: 24px; }
.q-marks { font-family: 'Playfair Display', serif; font-size: 68px; line-height: 0.35; color: rgba(245,200,66,0.14); margin-bottom: 12px; }
.q-text { font-family: 'Playfair Display', serif; font-style: italic; font-size: 13.5px; color: rgba(255,255,255,0.38); line-height: 1.85; margin-bottom: 14px; }
.q-source { font-size: 9px; font-weight: 600; letter-spacing: 3px; text-transform: uppercase; color: var(--muted); }

/* ── RESULT ── */
.result-card { background: var(--surface); border: 1px solid var(--border); border-radius: 14px; overflow: hidden; }
.result-hdr { background: rgba(245,200,66,0.06); border-bottom: 1px solid rgba(245,200,66,0.12); padding: 10px 18px; font-size: 8px; font-weight: 700; letter-spacing: 4px; text-transform: uppercase; color: var(--gold); }
.result-body { padding: 18px; }
.result-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 1px; background: var(--faint); border-radius: 8px; overflow: hidden; margin-bottom: 14px; }
.result-cell { background: rgba(6,9,18,0.6); padding: 12px 14px; text-align: center; }
.r-lbl { font-size: 8px; color: var(--muted); letter-spacing: 2px; text-transform: uppercase; margin-bottom: 4px; }
.r-val { font-family: 'Anton', sans-serif; font-size: 34px; line-height: 1; color: var(--text); }
.result-footer { font-size: 11px; color: var(--muted); text-align: center; line-height: 1.75; }
.result-footer strong { color: var(--gold); }

/* ── FOOTER ── */
.foot { display: flex; justify-content: space-between; align-items: center; padding-top: 20px; border-top: 1px solid var(--faint); flex-wrap: wrap; gap: 10px; }
.foot-l { font-size: 10px; color: rgba(255,255,255,0.13); line-height: 1.9; }
.foot-r { font-family: 'Anton', sans-serif; font-size: 16px; letter-spacing: 4px; color: rgba(245,200,66,0.22); }
</style>
""", unsafe_allow_html=True)

# ─── HELPERS ──────────────────────────────────────────────────────────────────
def sh(label, pill=""):
    p = f'<span class="sh-pill">{pill}</span>' if pill else ""
    return f'<div class="sh"><span class="sh-label">{label}</span><div class="sh-line"></div>{p}</div>'

def bowler_card_html(b):
    sr  = round(b["runs"]/b["balls"]*100) if b["balls"] else 0
    rc  = "g" if b["runs"] > 0 else "x"
    fc  = "b" if b["fours"] > 0 else "x"
    xc  = "t" if b["sixes"] > 0 else "x"
    sc  = "var(--gold)" if b["runs"] > 0 else "rgba(255,255,255,0.18)"
    wkt = f" · <span style='color:var(--red);font-weight:700'>{b['team_w']}W</span>" if b["team_w"] else ""
    return f"""<div class="bc {b['cls']}">
      <div class="top-bar"></div>
      <div class="bc-hd"><span class="bc-name">{b['name']}</span><span class="bc-pill">{b['type']}</span></div>
      <div class="bc-sub">{b['team_ov']} ov · {b['team_r']} runs{wkt}</div>
      <div class="bc-grid">
        <div class="bc-cell"><div class="bc-val {rc}">{b['runs']}</div><div class="bc-lbl">Runs</div></div>
        <div class="bc-cell"><div class="bc-val">{b['balls']}</div><div class="bc-lbl">Balls</div></div>
        <div class="bc-cell"><div class="bc-val {fc}">{b['fours']}</div><div class="bc-lbl">4s</div></div>
        <div class="bc-cell"><div class="bc-val {xc}">{b['sixes']}</div><div class="bc-lbl">6s</div></div>
      </div>
      <div class="bc-ft"><span>SR <b style="color:{sc}">{sr}</b></span><span><b>{b['dots']}</b> dot{'s' if b['dots']!=1 else ''}</b></span></div>
    </div>"""

# ─── TICKER ───────────────────────────────────────────────────────────────────
ticker_items = [
    "🏏 SANJU SAMSON 97* OFF 50 BALLS",
    "⭐ PLAYER OF THE MATCH",
    "🇮🇳 INDIA 199/5 BEAT WEST INDIES 195/4",
    "🏆 INDIA TO T20 WC SEMI-FINALS",
    "📊 16 BOUNDARIES — MOST BY AN INDIAN IN T20 WC",
    "🚀 INDIA'S HIGHEST-EVER SUCCESSFUL T20 WC CHASE",
    "📅 SEMI-FINAL vs ENGLAND · WANKHEDE · MARCH 5",
    "💎 SR 194.00 · 12 FOURS · 4 SIXES",
]
double = ticker_items * 2
items_html = "".join(f'<div class="ticker-item">{t}</div>' for t in double)
st.markdown(f"""
<div class="ticker-wrap">
  <div class="ticker-label">LIVE UPDATE</div>
  <div style="overflow:hidden;flex:1">
    <div class="ticker-track">{items_html}</div>
  </div>
</div>
""", unsafe_allow_html=True)

# ─── NAV ──────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="nav">
  <div class="nav-logo">T20 WC <span>&nbsp;2026</span><span class="nav-logo-sub">SCORECARD</span></div>
  <div class="nav-tags">
    <span class="nav-tag hi">Super Eights</span>
    <span class="nav-tag">India</span>
    <span class="nav-tag">Eden Gardens</span>
    <span class="nav-tag">1 March 2026</span>
  </div>
  <div class="nav-status"><div class="blink-dot"></div>MATCH COMPLETE · IND WON</div>
</div>
<div class="wrap">
""", unsafe_allow_html=True)

# ─── HERO ─────────────────────────────────────────────────────────────────────
img_inner = (f'<img src="{player_img}" alt="Sanju Samson"/>'
             if player_img else '<div class="hero-img-emoji">🏏</div>')

st.markdown(f"""
<div class="hero">
  <div class="hero-noise"></div>
  <div class="hero-top-line"></div>
  <div class="hero-97">97</div>
  <div class="hero-body">
    <div class="hero-img-outer">
      <div class="hero-glow"></div>
      <div class="hero-ring"></div>
      <div class="hero-img">{img_inner}</div>
    </div>
    <div class="hero-copy">
      <div class="hero-badge"><div class="blink-dot" style="background:var(--gold)"></div>Player of the Match &nbsp;·&nbsp; T20 World Cup 2026</div>
      <div class="hero-name">Sanju<em>Samson</em></div>
      <div class="hero-meta">
        <span class="hero-meta-tag">Super Eights</span>
        <span class="hero-meta-tag">Eden Gardens, Kolkata</span>
        <span class="hero-meta-tag">India vs West Indies</span>
        <span class="hero-meta-tag">March 1, 2026</span>
      </div>
    </div>
  </div>
  <div class="score-panel">
    <div class="score-num">97<sup>*</sup></div>
    <div class="score-sub">off 50 balls</div>
    <div class="score-sr">
      <span class="score-sr-lbl">Strike Rate</span>
      <span class="score-sr-val">194</span>
    </div>
    <div class="potm-chip">🏆 POTM</div>
  </div>
</div>

<div class="record-strip">
  <span style="font-size:16px;flex-shrink:0">📋</span>
  <span>
    <strong>Records broken tonight:</strong>
    Highest score by an Indian in a T20 WC run-chase ·
    Most boundaries by an Indian in a T20 WC match (16) ·
    India's highest-ever successful T20 WC chase (199/5)
  </span>
</div>
""", unsafe_allow_html=True)

# ─── OVERVIEW ─────────────────────────────────────────────────────────────────
st.markdown(sh("Innings Overview"), unsafe_allow_html=True)
ov = [("🏏","97*","Runs","g","var(--gold)"),("⏱","50","Balls","","var(--text)"),
      ("4️⃣","12","Fours","b","var(--blue)"),("6️⃣","4","Sixes","t","var(--teal)"),("⚡","194","Strike Rate","g","var(--gold)")]
ov_html = "".join(f'<div class="ov-card" style="--ac:{ac}"><div class="ov-lhs"><div class="ov-icon">{i}</div><div class="ov-lbl">{l}</div></div><div class="ov-num {c}">{v}</div></div>' for i,v,l,c,ac in ov)
st.markdown(f'<div class="ov-strip">{ov_html}</div>', unsafe_allow_html=True)

# ─── PHASE ────────────────────────────────────────────────────────────────────
st.markdown(sh("Phase Breakdown"), unsafe_allow_html=True)
pc = {"pp":"var(--gold)","mid":"var(--blue)","dt":"#f97316"}
ph_html = ""
for p in phases:
    c = pc[p["key"]]
    ph_html += f"""<div class="pc {p['key']}">
      <div class="pc-big">{p['runs']}</div>
      <div class="pc-info">
        <div class="pc-over">{p['label']}</div>
        <div class="pc-name">{p['name']}</div>
        <div class="pc-sr-pill">SR {p['sr']}</div>
        <div class="pc-meta">
          <span class="pc-tag"><span class="pc-dot" style="background:{c}"></span>{p['balls']} balls</span>
          <span class="pc-tag"><span class="pc-dot" style="background:var(--blue)"></span>{p['fours']} fours</span>
          <span class="pc-tag"><span class="pc-dot" style="background:var(--teal)"></span>{p['sixes']} sixes</span>
        </div>
      </div>
    </div>"""
st.markdown(f'<div class="phase-row">{ph_html}</div>', unsafe_allow_html=True)

# ─── SCORE PROGRESSION ────────────────────────────────────────────────────────
st.markdown(sh("Score Progression"), unsafe_allow_html=True)

PLOT_BG = "rgba(255,255,255,0.015)"
GRID_C  = "rgba(255,255,255,0.045)"
AX_C    = "rgba(255,255,255,0.22)"

st.markdown('<div class="chart-box">', unsafe_allow_html=True)
fig2 = go.Figure()

# Required run rate — straight line: overs * 9.8, converted to balls
req_balls = list(range(0, 117))
req_runs  = [b * (9.8 / 6) for b in req_balls]

# Background shade — above required = good (green tint), below = danger
fig2.add_trace(go.Scatter(
    x=req_balls, y=req_runs,
    fill="tozeroy", fillcolor="rgba(232,64,64,0.06)",
    line=dict(color="rgba(0,0,0,0)"), showlegend=False, hoverinfo="skip",
))

# Required RR line
fig2.add_trace(go.Scatter(
    x=req_balls, y=req_runs,
    name="Required (9.8 rpo)", mode="lines",
    line=dict(color="rgba(232,64,64,0.6)", width=1.5, dash="dash"),
    hoverinfo="skip", showlegend=True,
))

# Gold fill under actual score
fig2.add_trace(go.Scatter(
    x=prog_df["Ball"], y=prog_df["Score"],
    fill="tozeroy", fillcolor="rgba(245,200,66,0.08)",
    line=dict(color="rgba(0,0,0,0)"), showlegend=False, hoverinfo="skip",
))

# Main score line — thicker, no markers for a cleaner read
fig2.add_trace(go.Scatter(
    x=prog_df["Ball"], y=prog_df["Score"],
    name="India", mode="lines",
    line=dict(color="#f5c842", width=3.5, shape="spline", smoothing=0.8),
    hovertemplate="Ball %{x} · %{y} runs<extra></extra>",
))

# Phase shading bands
fig2.add_vrect(x0=0,  x1=36,  fillcolor="rgba(245,200,66,0.03)", line_width=0)
fig2.add_vrect(x0=36, x1=96,  fillcolor="rgba(96,165,250,0.03)", line_width=0)
fig2.add_vrect(x0=96, x1=117, fillcolor="rgba(249,115,22,0.04)", line_width=0)

# Phase labels at top
for xv, lbl, col in [(18, "POWERPLAY", "rgba(245,200,66,0.2)"),
                      (63, "MIDDLE", "rgba(96,165,250,0.2)"),
                      (103, "DEATH", "rgba(249,115,22,0.2)")]:
    fig2.add_annotation(x=xv, y=205, text=lbl, showarrow=False,
                        font=dict(color=col, size=8, family="Outfit"), xanchor="center")

# Phase boundary lines
for xv in [36, 96]:
    fig2.add_vline(x=xv, line=dict(color="rgba(255,255,255,0.08)", width=1))

# Samson 50 milestone — ball 58
fig2.add_trace(go.Scatter(
    x=[58], y=[84], mode="markers",
    marker=dict(symbol="star", size=14, color="#00c9a7",
                line=dict(color="#00c9a7", width=1)),
    showlegend=False, hoverinfo="skip",
))
fig2.add_annotation(
    x=58, y=84, text="50★ off 26b", showarrow=True,
    arrowhead=0, arrowwidth=1, arrowcolor="rgba(0,201,167,0.5)",
    font=dict(color="#00c9a7", size=9, family="Outfit"),
    ax=30, ay=-30,
    bgcolor="rgba(0,201,167,0.08)",
    bordercolor="rgba(0,201,167,0.3)", borderwidth=1, borderpad=4,
)

# Win marker at ball 116
fig2.add_trace(go.Scatter(
    x=[116], y=[199], mode="markers",
    marker=dict(symbol="star", size=16, color="#f5c842",
                line=dict(color="#f5c842", width=1)),
    showlegend=False, hoverinfo="skip",
))
fig2.add_annotation(
    x=116, y=199, text="IND WIN 🏆", showarrow=True,
    arrowhead=0, arrowwidth=1, arrowcolor="rgba(245,200,66,0.5)",
    font=dict(color="#f5c842", size=9, family="Outfit"),
    ax=-40, ay=-28,
    bgcolor="rgba(245,200,66,0.08)",
    bordercolor="rgba(245,200,66,0.3)", borderwidth=1, borderpad=4,
)

fig2.update_layout(
    paper_bgcolor="rgba(255,255,255,0.02)",
    plot_bgcolor="rgba(0,0,0,0)",
    height=300,
    margin=dict(l=48, r=16, t=20, b=40),
    legend=dict(
        orientation="h", x=0.02, y=0.98,
        font=dict(color=AX_C, size=9, family="Outfit"),
        bgcolor="rgba(0,0,0,0)", borderwidth=0,
    ),
    xaxis=dict(
        showgrid=False, zeroline=False,
        color=AX_C, tickfont=dict(size=9, family="Outfit"),
        range=[0, 117],
        tickvals=[0, 18, 36, 54, 72, 90, 108, 116],
        ticktext=["0", "3", "6", "9", "12", "15", "18", "19.2"],
        title=dict(text="Over", font=dict(size=9, color=AX_C, family="Outfit")),
    ),
    yaxis=dict(
        showgrid=True, gridcolor="rgba(255,255,255,0.04)",
        zeroline=False, color=AX_C,
        tickfont=dict(size=9, family="Outfit"),
        range=[0, 215],
        title=dict(text="Runs", font=dict(size=9, color=AX_C, family="Outfit")),
    ),
)
st.plotly_chart(fig2, use_container_width=True, config={"displayModeBar": False})
st.markdown('</div>', unsafe_allow_html=True)


# ─── PARTNERSHIPS ─────────────────────────────────────────────────────────────
st.markdown(sh("Partnership Tracker", "6 stands · 199 runs"), unsafe_allow_html=True)
max_p = max(p["runs"] for p in partnerships)
psh = ""
for p in partnerships:
    w = round(p["runs"]/max_p*100)
    sp = round(p["samson"]/p["runs"]*100) if p["runs"] else 0
    psh += f"""<div class="pship-card">
      <div class="pship-wkt">{p['wkt']} Wicket · Ov {p['overs']}</div>
      <div class="pship-names"><em>Samson</em> + {p['p2']}</div>
      <div class="pship-big">{p['runs']}</div>
      <div class="pship-balls">{p['balls']} balls</div>
      <div class="pship-bar-bg"><div class="pship-bar-fg" style="width:{w}%"></div></div>
      <div class="pship-pct"><span>S {sp}%</span><span>{p['p2'][0]} {100-sp}%</span></div>
    </div>"""
st.markdown(f'<div class="pship-row">{psh}</div>', unsafe_allow_html=True)

# ─── BOWLERS ──────────────────────────────────────────────────────────────────
st.markdown(sh("Head-to-Head vs Each Bowler", "7 bowlers"), unsafe_allow_html=True)
all_cards = "".join(bowler_card_html(b) for b in bowlers)
st.markdown(f"""
<div class="bowler-row-4">{all_cards}</div>
<div class="sum-bar">
  <div class="sum-cell"><div class="sum-val">9</div><div class="sum-lbl">Dot Balls</div></div>
  <div class="sum-cell"><div class="sum-val">12</div><div class="sum-lbl">Fours</div></div>
  <div class="sum-cell"><div class="sum-val">4</div><div class="sum-lbl">Sixes</div></div>
  <div class="sum-cell"><div class="sum-val">72</div><div class="sum-lbl">Boundary Runs</div></div>
  <div class="sum-cell"><div class="sum-val">25</div><div class="sum-lbl">Running Runs</div></div>
  <div class="sum-cell"><div class="sum-val">7</div><div class="sum-lbl">Bowlers Faced</div></div>
  <div class="sum-cell"><div class="sum-val">16</div><div class="sum-lbl">Boundaries</div></div>
</div>
""", unsafe_allow_html=True)

# ─── BOWLER THREAT RADAR ──────────────────────────────────────────────────────
st.markdown(sh("Bowler Threat — Samson's SR vs Dot Ball %"), unsafe_allow_html=True)
st.markdown('<div class="chart-box">', unsafe_allow_html=True)
b_names = [b["name"].split()[-1] for b in bowlers]
b_sr    = [round(b["runs"]/b["balls"]*100) if b["balls"] else 0 for b in bowlers]
b_dot_r = [round(b["dots"]/b["balls"]*100) if b["balls"] else 0 for b in bowlers]
b_runs  = [b["runs"] for b in bowlers]
colors_radar = ["#f5c842" if s > 150 else "#e84040" if s > 100 else "#00c9a7" for s in b_sr]

fig4 = go.Figure()
fig4.add_trace(go.Scatter(
    x=b_dot_r, y=b_sr,
    mode="markers+text",
    text=b_names,
    textposition="top center",
    textfont=dict(color=AX_C, size=9),
    marker=dict(
        size=[max(14, r*0.9) for r in b_runs],
        color=colors_radar,
        opacity=0.85,
        line=dict(color="rgba(255,255,255,0.15)", width=1),
    ),
    hovertemplate="<b>%{text}</b><br>SR vs Samson: %{y}<br>Dot %: %{x}%<extra></extra>",
    showlegend=False,
))
fig4.add_hline(y=100, line=dict(color="rgba(255,255,255,0.1)", width=1, dash="dot"))
fig4.add_annotation(x=max(b_dot_r)+2, y=104, text="SR 100", showarrow=False,
                    font=dict(color="rgba(255,255,255,0.2)", size=8))
fig4.update_layout(
    title=dict(text="Bowler Threat — Samson's SR vs Dot Ball % (bubble = runs scored)",
               font=dict(color=AX_C, size=11, family="Outfit"), x=0.04, y=0.97),
    paper_bgcolor=PLOT_BG, plot_bgcolor="rgba(0,0,0,0)",
    height=260, margin=dict(l=44,r=12,t=42,b=44),
    xaxis=dict(showgrid=True, gridcolor=GRID_C, zeroline=False, color=AX_C, tickfont=dict(size=9),
               title=dict(text="Dot Ball % conceded", font=dict(size=9, color=AX_C))),
    yaxis=dict(showgrid=True, gridcolor=GRID_C, zeroline=False, color=AX_C, tickfont=dict(size=9),
               title=dict(text="Samson's SR vs bowler", font=dict(size=9, color=AX_C))),
)
st.plotly_chart(fig4, use_container_width=True, config={"displayModeBar":False})
st.markdown('</div>', unsafe_allow_html=True)

# ─── KEY MOMENTS GRID ─────────────────────────────────────────────────────────
st.markdown(sh("Key Moments"), unsafe_allow_html=True)
km_html = ""
for over, emoji, color, title, desc in key_moments:
    km_html += f"""<div class="moment-card" style="--mc:{color}">
      <div class="moment-top"><span class="moment-emoji">{emoji}</span><span class="moment-over">{over}</span></div>
      <div class="moment-title">{title}</div>
      <div class="moment-desc">{desc}</div>
    </div>"""
st.markdown(f'<div class="moments-grid">{km_html}</div>', unsafe_allow_html=True)

# ─── BOTTOM SPLIT ─────────────────────────────────────────────────────────────
st.markdown(sh("Match Summary"), unsafe_allow_html=True)
left, right = st.columns(2, gap="medium")

with left:
    st.markdown("""
    <div class="quote-card">
      <div class="q-marks">"</div>
      <div class="q-text">
        From the day I started playing and dreaming of representing my country,
        this is the day I was waiting for. My journey has been very special,
        with lots of ups and downs. There were times I doubted myself. But I kept believing.
        Thanks to the Lord Almighty. This is one of the greatest days of my life.
      </div>
      <div class="q-source">— Sanju Samson, Player of the Match Speech</div>
    </div>
    """, unsafe_allow_html=True)

with right:
    st.markdown("""
    <div class="result-card">
      <div class="result-hdr">Final Result — India won by 5 wickets</div>
      <div class="result-body">
        <div class="result-grid">
          <div class="result-cell"><div class="r-lbl">Target</div><div class="r-val">196</div></div>
          <div class="result-cell"><div class="r-lbl">India Scored</div><div class="r-val" style="color:var(--teal)">199/5</div></div>
          <div class="result-cell"><div class="r-lbl">Balls to Spare</div><div class="r-val" style="color:var(--gold)">4</div></div>
          <div class="result-cell"><div class="r-lbl">Margin</div><div class="r-val">5 Wkts</div></div>
        </div>
        <div class="result-footer">
          India advance to <strong>T20 WC 2026 Semi-Finals</strong><br>
          vs England · Wankhede, Mumbai · March 5, 2026
        </div>
      </div>
    </div>
    """, unsafe_allow_html=True)

# ─── FOOTER ───────────────────────────────────────────────────────────────────
st.markdown("""
<div class="foot">
  <div class="foot-l">
    Data: ESPNcricinfo / ICC Official Scorecard · T20 World Cup 2026 Super Eights<br>
    Eden Gardens, Kolkata · March 1, 2026 · India 199/5 beat West Indies 195/4 by 5 wickets
  </div>
  <div class="foot-r">#TEAMINDIA · #T20WC2026</div>
</div>
</div>
""", unsafe_allow_html=True)
