"""
Sanju Samson – 97* vs West Indies | T20 World Cup 2026
Streamlit Dashboard — Redesigned UI/UX

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

# ─── IMAGE LOADER ─────────────────────────────────────────────────────────────
@st.cache_data
def load_image_from_file(path: str) -> str:
    try:
        img = Image.open(path).convert("RGBA")
        img.thumbnail((320, 320), Image.LANCZOS)
        buf = BytesIO()
        img.save(buf, format="PNG")
        return f"data:image/png;base64,{base64.b64encode(buf.getvalue()).decode()}"
    except Exception:
        return ""

@st.cache_data
def load_image_from_url(url: str) -> str:
    try:
        resp = requests.get(url, timeout=5)
        resp.raise_for_status()
        img = Image.open(BytesIO(resp.content)).convert("RGBA")
        img.thumbnail((320, 320), Image.LANCZOS)
        buf = BytesIO()
        img.save(buf, format="PNG")
        return f"data:image/png;base64,{base64.b64encode(buf.getvalue()).decode()}"
    except Exception:
        return ""

# ── DROP YOUR IMAGE HERE ──────────────────────────────────────────────────────
# Save Sanju Samson's photo as "sanju_samson.jpg" in the same folder, OR
# paste a direct image URL into REMOTE_IMAGE_URL below.
LOCAL_IMAGE_PATH = "sanju_samson.png"
REMOTE_IMAGE_URL = ""

player_img_src = (
    load_image_from_file(LOCAL_IMAGE_PATH)
    or load_image_from_url(REMOTE_IMAGE_URL)
    or ""
)

# ─── CSS ──────────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Barlow+Condensed:ital,wght@0,300;0,600;0,800;1,300&family=Barlow:wght@300;400;500;600&family=Playfair+Display:ital,wght@1,600&display=swap');

/* ── Reset & Base ── */
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
html, body, [class*="css"] { font-family: 'Barlow', sans-serif; }
.stApp {
    background: #07090f;
    background-image:
        radial-gradient(ellipse 70% 50% at 10% 0%, rgba(255,200,40,0.07) 0%, transparent 55%),
        radial-gradient(ellipse 50% 40% at 90% 100%, rgba(0,180,130,0.06) 0%, transparent 50%);
}
#MainMenu, footer, header { visibility: hidden; }
.block-container {
    padding: 1.5rem 2.5rem 4rem !important;
    max-width: 100% !important;
}
section[data-testid="stAppViewContainer"] > div { max-width: 100% !important; }
div[data-testid="stMainBlockContainer"] {
    max-width: 100% !important;
    padding-left: 2.5rem !important;
    padding-right: 2.5rem !important;
}

/* ── Divider ── */
.section-gap { margin-top: 2rem; margin-bottom: 0.5rem; }

/* ── Section label ── */
.section-label {
    display: flex;
    align-items: center;
    gap: 12px;
    margin-bottom: 16px;
}
.section-label-line {
    flex: 1;
    height: 1px;
    background: linear-gradient(90deg, rgba(255,200,40,0.4), transparent);
}
.section-label-text {
    font-family: 'Barlow Condensed', sans-serif;
    font-size: 11px;
    font-weight: 600;
    letter-spacing: 4px;
    text-transform: uppercase;
    color: #f5c842;
    white-space: nowrap;
}

/* ── HERO ── */
.hero {
    position: relative;
    overflow: hidden;
    border-radius: 20px;
    border: 1px solid rgba(255,200,40,0.15);
    background: linear-gradient(135deg, #0d1220 0%, #0a0f1a 60%, #0d1a12 100%);
    padding: 0;
    margin-bottom: 1.5rem;
    display: flex;
    min-height: 240px;
}

.hero-accent-bar {
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 4px;
    background: linear-gradient(90deg, #f5c842 0%, #00c9a7 50%, #f5c842 100%);
}

.hero-bg-number {
    position: absolute;
    right: -20px;
    top: 50%;
    transform: translateY(-50%);
    font-family: 'Barlow Condensed', sans-serif;
    font-size: 280px;
    font-weight: 800;
    color: rgba(245,200,66,0.04);
    line-height: 1;
    pointer-events: none;
    user-select: none;
}

.hero-left {
    display: flex;
    align-items: center;
    gap: 32px;
    padding: 36px 40px;
    flex: 1;
    position: relative;
    z-index: 1;
}

.hero-img-container {
    position: relative;
    flex-shrink: 0;
}

.hero-img-ring {
    position: absolute;
    inset: -6px;
    border-radius: 50%;
    background: conic-gradient(from 0deg, #f5c842, #00c9a7, #f5c842);
    animation: spin 8s linear infinite;
    opacity: 0.7;
}

@keyframes spin { to { transform: rotate(360deg); } }

.hero-img-inner {
    position: relative;
    width: 150px;
    height: 150px;
    border-radius: 50%;
    overflow: hidden;
    background: rgba(245,200,66,0.08);
    border: 3px solid #07090f;
    z-index: 1;
}

.hero-img-inner img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    object-position: top center;
    display: block;
}

.hero-img-emoji {
    width: 100%;
    height: 100%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 60px;
}

.hero-info { flex: 1; }

.hero-tag {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    background: rgba(245,200,66,0.1);
    border: 1px solid rgba(245,200,66,0.3);
    color: #f5c842;
    font-size: 10px;
    font-weight: 600;
    letter-spacing: 3px;
    text-transform: uppercase;
    padding: 4px 14px;
    border-radius: 2px;
    margin-bottom: 14px;
}

.hero-tag-dot {
    width: 6px; height: 6px;
    border-radius: 50%;
    background: #f5c842;
    animation: blink 1.5s ease-in-out infinite;
}
@keyframes blink { 0%,100%{opacity:1} 50%{opacity:0.2} }

.hero-name {
    font-family: 'Barlow Condensed', sans-serif;
    font-size: 76px;
    font-weight: 800;
    line-height: 0.88;
    color: #f0ece0;
    text-transform: uppercase;
    letter-spacing: 2px;
    margin-bottom: 14px;
}
.hero-name em {
    font-style: italic;
    font-weight: 300;
    color: #f5c842;
    font-size: 0.85em;
    letter-spacing: 6px;
    display: block;
}

.hero-meta {
    display: flex;
    align-items: center;
    gap: 16px;
    flex-wrap: wrap;
}
.hero-meta-item {
    font-size: 11px;
    color: #4a5a70;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    font-weight: 600;
}
.hero-meta-sep { color: #1e2a38; font-size: 14px; }

.hero-right {
    display: flex;
    flex-direction: column;
    align-items: flex-end;
    justify-content: center;
    padding: 36px 44px 36px 20px;
    position: relative;
    z-index: 1;
    border-left: 1px solid rgba(255,255,255,0.04);
    min-width: 280px;
}

.hero-score {
    font-family: 'Barlow Condensed', sans-serif;
    font-size: 130px;
    font-weight: 800;
    line-height: 0.85;
    color: #f5c842;
    letter-spacing: -2px;
    text-shadow: 0 0 80px rgba(245,200,66,0.3);
}

.hero-score sup {
    font-size: 0.35em;
    color: #e8a020;
    vertical-align: super;
}

.hero-score-sub {
    font-size: 13px;
    color: #4a5a70;
    letter-spacing: 3px;
    text-transform: uppercase;
    text-align: right;
    margin-top: 4px;
    font-weight: 600;
}

.hero-sr {
    margin-top: 14px;
    display: flex;
    align-items: center;
    gap: 10px;
    justify-content: flex-end;
}

.hero-sr-label {
    font-size: 10px;
    color: #4a5a70;
    letter-spacing: 2px;
    text-transform: uppercase;
}

.hero-sr-value {
    font-family: 'Barlow Condensed', sans-serif;
    font-size: 28px;
    font-weight: 700;
    color: #00c9a7;
}

.potm-badge {
    margin-top: 16px;
    display: inline-flex;
    align-items: center;
    gap: 8px;
    background: linear-gradient(135deg, #f5c842, #e8a020);
    color: #000;
    font-size: 9px;
    font-weight: 800;
    letter-spacing: 2.5px;
    text-transform: uppercase;
    padding: 6px 16px;
    border-radius: 2px;
}

/* ── RECORD BANNER ── */
.record-banner {
    display: flex;
    align-items: center;
    gap: 16px;
    background: linear-gradient(90deg, rgba(232,64,64,0.08), transparent);
    border: 1px solid rgba(232,64,64,0.25);
    border-left: 3px solid #e84040;
    border-radius: 0 10px 10px 0;
    padding: 12px 20px;
    margin-bottom: 1.5rem;
}
.record-icon { font-size: 18px; flex-shrink: 0; }
.record-text { font-size: 12px; color: #c07070; line-height: 1.6; }
.record-text strong { color: #f0ece0; }

.stat-grid {
    display: grid;
    grid-template-columns: repeat(5, 1fr);
    gap: 12px;
    margin-bottom: 1.5rem;
}

.stat-card {
    background: rgba(255,255,255,0.03);
    border: 1px solid rgba(255,255,255,0.06);
    border-radius: 12px;
    padding: 18px 20px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 12px;
    position: relative;
    overflow: hidden;
    transition: border-color 0.25s, transform 0.25s;
    white-space: nowrap;
}
.stat-card:hover {
    border-color: rgba(245,200,66,0.3);
    transform: translateY(-3px);
}
.stat-card::before {
    content: '';
    position: absolute;
    left: 0; top: 20%; bottom: 20%;
    width: 2px;
    background: var(--accent, #f5c842);
    border-radius: 2px;
    opacity: 0.6;
}

.stat-left {
    display: flex;
    flex-direction: column;
    gap: 4px;
}

.stat-icon {
    font-size: 20px;
    line-height: 1;
}

.stat-lbl {
    font-size: 9px;
    color: #3a4a5e;
    letter-spacing: 2.5px;
    text-transform: uppercase;
    font-weight: 600;
    white-space: nowrap;
}

.stat-val {
    font-family: 'Barlow Condensed', sans-serif;
    font-size: 52px;
    font-weight: 800;
    line-height: 1;
    color: #f0ece0;
    flex-shrink: 0;
}
.stat-val.gold { color: #f5c842; }
.stat-val.teal { color: #00c9a7; }
.stat-val.blue { color: #60a5fa; }

/* ── PHASE CARDS ── */
.phase-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 12px;
    margin-bottom: 1.5rem;
}

.phase-card {
    background: rgba(255,255,255,0.025);
    border: 1px solid rgba(255,255,255,0.05);
    border-radius: 12px;
    padding: 20px 24px;
    position: relative;
    overflow: hidden;
    display: flex;
    align-items: center;
    gap: 24px;
}

.phase-card::before {
    content: '';
    position: absolute;
    top: 0; left: 0; bottom: 0;
    width: 3px;
}
.phase-card.pp::before  { background: linear-gradient(180deg, #f5c842, #e8a020); }
.phase-card.mid::before { background: linear-gradient(180deg, #60a5fa, #3b82f6); }
.phase-card.dt::before  { background: linear-gradient(180deg, #f97316, #ea580c); }

.phase-score {
    font-family: 'Barlow Condensed', sans-serif;
    font-size: 72px;
    font-weight: 800;
    line-height: 1;
    flex-shrink: 0;
}
.phase-card.pp  .phase-score { color: #f5c842; }
.phase-card.mid .phase-score { color: #60a5fa; }
.phase-card.dt  .phase-score { color: #f97316; }

.phase-right {
    flex: 1;
    min-width: 0;
    overflow: hidden;
}

.phase-top {
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
    margin-bottom: 8px;
}

.phase-overs {
    font-size: 9px;
    color: #3a4a5e;
    letter-spacing: 2px;
    text-transform: uppercase;
    font-weight: 600;
}

.phase-name {
    font-family: 'Barlow Condensed', sans-serif;
    font-size: 22px;
    font-weight: 700;
    color: #f0ece0;
    text-transform: uppercase;
    letter-spacing: 1px;
    margin-bottom: 2px;
    line-height: 1;
}

.phase-sr-pill {
    background: rgba(0,201,167,0.12);
    border: 1px solid rgba(0,201,167,0.2);
    color: #00c9a7;
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 1px;
    padding: 4px 10px;
    border-radius: 100px;
    white-space: nowrap;
}

.phase-detail {
    font-size: 11px;
    color: #3a4a5e;
    display: flex;
    gap: 14px;
    flex-wrap: nowrap;
    align-items: center;
    white-space: nowrap;
}

.phase-detail-item {
    display: flex;
    align-items: center;
    gap: 5px;
    flex-shrink: 0;
}
.phase-detail-dot {
    width: 6px; height: 6px;
    border-radius: 50%;
    flex-shrink: 0;
}

/* ── BOWLER CARDS ── */
.bowler-grid-top {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 12px;
    margin-bottom: 12px;
}
.bowler-grid-bot {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 12px;
}

.bowler-card {
    background: rgba(255,255,255,0.025);
    border: 1px solid rgba(255,255,255,0.05);
    border-radius: 12px;
    padding: 16px;
    position: relative;
    overflow: hidden;
    transition: border-color 0.2s, transform 0.2s;
}
.bowler-card:hover {
    border-color: rgba(245,200,66,0.25);
    transform: translateY(-2px);
}

.bowler-card .top-stripe {
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 2px;
}
.bowler-card.spin   .top-stripe { background: linear-gradient(90deg,#a78bfa,#7c3aed); }
.bowler-card.fast   .top-stripe { background: linear-gradient(90deg,#f5c842,#f97316); }
.bowler-card.medium .top-stripe { background: linear-gradient(90deg,#00c9a7,#0096c7); }

.bc-header {
    display: flex;
    align-items: flex-start;
    justify-content: space-between;
    margin-bottom: 10px;
    margin-top: 6px;
}

.bc-name {
    font-size: 14px;
    font-weight: 700;
    color: #f0ece0;
    line-height: 1.2;
}

.bc-type-pill {
    font-size: 9px;
    font-weight: 700;
    letter-spacing: 1px;
    text-transform: uppercase;
    padding: 3px 8px;
    border-radius: 100px;
    white-space: nowrap;
    flex-shrink: 0;
}
.bowler-card.spin   .bc-type-pill { background: rgba(167,139,250,0.15); color: #a78bfa; }
.bowler-card.fast   .bc-type-pill { background: rgba(245,200,66,0.1);   color: #f5c842; }
.bowler-card.medium .bc-type-pill { background: rgba(0,201,167,0.1);    color: #00c9a7; }

.bc-team-line {
    font-size: 10px;
    color: #2e3d50;
    margin-bottom: 12px;
    font-weight: 500;
}

.bc-stats {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 4px;
    background: rgba(0,0,0,0.2);
    border-radius: 8px;
    padding: 10px 6px;
}

.bc-stat { text-align: center; }

.bc-stat-val {
    font-family: 'Barlow Condensed', sans-serif;
    font-size: 28px;
    font-weight: 700;
    line-height: 1;
    color: #f0ece0;
}
.bc-stat-val.runs { color: #f5c842; font-size: 32px; }
.bc-stat-val.four { color: #60a5fa; }
.bc-stat-val.six  { color: #00c9a7; }
.bc-stat-val.zero { color: #2e3d50; }

.bc-stat-lbl {
    font-size: 8px;
    color: #2e3d50;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    margin-top: 3px;
    font-weight: 600;
}

.bc-footer {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-top: 10px;
    padding-top: 8px;
    border-top: 1px solid rgba(255,255,255,0.04);
}

.bc-sr {
    font-size: 11px;
    color: #2e3d50;
    font-weight: 500;
}
.bc-sr strong { font-weight: 700; }

.bc-dots {
    font-size: 10px;
    color: #2e3d50;
}

/* ── SUMMARY STRIP ── */
.summary-strip {
    display: flex;
    gap: 0;
    border: 1px solid rgba(255,255,255,0.05);
    border-radius: 10px;
    overflow: hidden;
    margin-top: 14px;
}
.summary-item {
    flex: 1;
    text-align: center;
    padding: 12px 8px;
    border-right: 1px solid rgba(255,255,255,0.04);
    background: rgba(255,255,255,0.02);
}
.summary-item:last-child { border-right: none; }
.summary-val {
    font-family: 'Barlow Condensed', sans-serif;
    font-size: 22px;
    font-weight: 700;
    color: #f5c842;
    line-height: 1;
}
.summary-lbl {
    font-size: 9px;
    color: #2e3d50;
    letter-spacing: 2px;
    text-transform: uppercase;
    margin-top: 4px;
    font-weight: 600;
}

/* ── SCORE PROGRESSION ── */
.chart-container {
    background: rgba(255,255,255,0.02);
    border: 1px solid rgba(255,255,255,0.05);
    border-radius: 12px;
    padding: 20px 16px 8px;
    margin-bottom: 1.5rem;
}

/* ── MILESTONES ── */
.milestone-list { position: relative; }
.milestone-list::before {
    content: '';
    position: absolute;
    left: 4px;
    top: 8px; bottom: 8px;
    width: 1px;
    background: linear-gradient(180deg, #f5c842, rgba(245,200,66,0.1));
}

.milestone {
    display: flex;
    gap: 16px;
    align-items: flex-start;
    padding: 0 0 20px 0;
    position: relative;
}
.milestone:last-child { padding-bottom: 0; }

.m-dot-wrap {
    position: relative;
    flex-shrink: 0;
    width: 10px;
    margin-top: 5px;
}
.m-dot {
    width: 10px; height: 10px;
    border-radius: 50%;
    background: #f5c842;
    box-shadow: 0 0 8px rgba(245,200,66,0.5);
    position: relative;
    z-index: 1;
}
.m-dot.teal {
    background: #00c9a7;
    box-shadow: 0 0 8px rgba(0,201,167,0.5);
}

.m-content { flex: 1; }

.m-ball {
    font-family: 'Barlow Condensed', sans-serif;
    font-size: 11px;
    font-weight: 600;
    letter-spacing: 2px;
    color: #3a4a5e;
    text-transform: uppercase;
    margin-bottom: 2px;
}

.m-title {
    font-size: 14px;
    font-weight: 700;
    color: #f0ece0;
    margin-bottom: 2px;
}

.m-desc {
    font-size: 12px;
    color: #3a4a5e;
    line-height: 1.5;
    font-weight: 400;
}

/* ── QUOTE ── */
.quote-card {
    background: rgba(255,255,255,0.02);
    border: 1px solid rgba(255,255,255,0.05);
    border-top: 2px solid #f5c842;
    border-radius: 0 0 12px 12px;
    padding: 24px;
    margin-bottom: 14px;
}
.quote-marks {
    font-family: 'Playfair Display', serif;
    font-size: 60px;
    line-height: 0.5;
    color: rgba(245,200,66,0.2);
    margin-bottom: 8px;
}
.quote-text {
    font-family: 'Playfair Display', serif;
    font-style: italic;
    font-size: 14px;
    color: #8a9ab8;
    line-height: 1.8;
    margin-bottom: 14px;
}
.quote-attr {
    font-size: 10px;
    color: #3a4a5e;
    letter-spacing: 3px;
    text-transform: uppercase;
    font-weight: 600;
}

/* ── MATCH CONTEXT ── */
.match-ctx {
    background: rgba(255,255,255,0.02);
    border: 1px solid rgba(255,255,255,0.05);
    border-radius: 12px;
    overflow: hidden;
}
.match-ctx-header {
    background: rgba(245,200,66,0.06);
    border-bottom: 1px solid rgba(245,200,66,0.1);
    padding: 12px 20px;
    font-size: 9px;
    font-weight: 700;
    letter-spacing: 3px;
    text-transform: uppercase;
    color: #f5c842;
}
.match-ctx-body { padding: 20px; }

.ctx-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 1px;
    background: rgba(255,255,255,0.04);
    border-radius: 8px;
    overflow: hidden;
    margin-bottom: 16px;
}
.ctx-cell {
    background: rgba(255,255,255,0.02);
    padding: 14px 16px;
    text-align: center;
}
.ctx-lbl {
    font-size: 9px;
    color: #2e3d50;
    letter-spacing: 2px;
    text-transform: uppercase;
    font-weight: 600;
    margin-bottom: 4px;
}
.ctx-val {
    font-family: 'Barlow Condensed', sans-serif;
    font-size: 36px;
    font-weight: 800;
    line-height: 1;
    color: #f0ece0;
}

.ctx-semi {
    font-size: 11px;
    color: #2e3d50;
    line-height: 1.6;
    text-align: center;
}
.ctx-semi strong { color: #f5c842; }

/* ── FOOTER ── */
.dash-footer {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-top: 2.5rem;
    padding-top: 1rem;
    border-top: 1px solid rgba(255,255,255,0.04);
    flex-wrap: wrap;
    gap: 12px;
}
.footer-left  { font-size: 11px; color: #2e3d50; line-height: 1.8; }
.footer-right {
    font-family: 'Barlow Condensed', sans-serif;
    font-size: 16px;
    font-weight: 700;
    letter-spacing: 3px;
    color: rgba(245,200,66,0.4);
}
</style>
""", unsafe_allow_html=True)

# ─── DATA ─────────────────────────────────────────────────────────────────────
bowlers_row1 = [
    {"name": "Shamar Joseph",    "cls": "fast",   "type": "Right-arm Fast",
     "team_r": 42, "team_w": 2, "team_ov": "4.0",
     "runs": 12, "balls": 8, "fours": 2, "sixes": 0, "dots": 2},
    {"name": "Jason Holder",     "cls": "medium", "type": "Fast-medium",
     "team_r": 38, "team_w": 2, "team_ov": "4.0",
     "runs": 17, "balls": 8,  "fours": 3, "sixes": 0, "dots": 0},
    {"name": "Romario Shepherd", "cls": "fast",   "type": "Right-arm Fast",
     "team_r": 34, "team_w": 0, "team_ov": "2.2",
     "runs": 24, "balls": 9,  "fours": 2, "sixes": 2, "dots": 1},
    {"name": "Matthew Forde",    "cls": "medium", "type": "Right-arm Medium",
     "team_r": 22, "team_w": 0, "team_ov": "3.0",
     "runs": 7, "balls": 9,  "fours": 1, "sixes": 0, "dots": 4},
]
bowlers_row2 = [
    {"name": "Akeal Hosein",     "cls": "spin",   "type": "Left-arm Spin",
     "team_r": 22, "team_w": 1, "team_ov": "2.0",
     "runs": 17, "balls": 5,  "fours": 1, "sixes": 2, "dots": 1},
    {"name": "Gudakesh Motie",   "cls": "spin",   "type": "Left-arm Spin",
     "team_r": 18, "team_w": 0, "team_ov": "2.0",
     "runs": 12, "balls": 7,  "fours": 2, "sixes": 0, "dots": 1},
    {"name": "Roston Chase",     "cls": "spin",   "type": "Off-spin",
     "team_r": 18, "team_w": 0, "team_ov": "2.0",
     "runs": 8,  "balls": 5,  "fours": 1, "sixes": 0, "dots": 0},
]

phases = [
    {"key": "pp",  "name": "Powerplay", "overs": "Overs 1–6",     "runs": 24, "balls": 13, "fours": 3, "sixes": 2, "sr": 185},
    {"key": "mid", "name": "Middle",    "overs": "Overs 7–15",    "runs": 53, "balls": 27, "fours": 7, "sixes": 1, "sr": 196},
    {"key": "dt",  "name": "Death",     "overs": "Overs 16–19.2", "runs": 20, "balls": 10, "fours": 2, "sixes": 1, "sr": 200},
]

progression = pd.DataFrame({
    "Ball":  [0,  3,  6, 10, 16, 22, 26, 32, 38, 44, 48, 50],
    "Score": [0, 15, 20, 24, 35, 44, 53, 63, 72, 82, 91, 97],
})

milestones = [
    ("teal", "Ball 3",  "Hosein Assault",      "2 sixes + a four in the third over — Samson signals he means business from ball one"),
    ("gold", "Ball 26", "50 off 26 Balls",     "Breaks a 12-innings half-century drought. A cover drive off Motie, pure and effortless"),
    ("teal", "Ball 35", "Kept His Head",        "SKY falls cheaply. India 107/4, needing 89 more. Samson never flinches"),
    ("gold", "Ball 45", "87* — In the Zone",   "India require 17 off 12. Samson is ice. Every ball goes exactly where he wants it"),
    ("teal", "Ball 49", "Six off Shepherd",    "Clears the square leg fence. India level with 1 ball of the over left — crowd erupts"),
    ("teal", "Ball 50", "97* — India Win",     "Chips Shepherd over mid-on. Kneels on the pitch. Helmet off. Eyes skyward. 🙏"),
]

# ─── BOWLER CARD HTML ─────────────────────────────────────────────────────────
def bowler_card_html(b: dict) -> str:
    sr = round(b["runs"] / b["balls"] * 100) if b["balls"] else 0
    runs_cls = "runs" if b["runs"] > 0 else "runs zero"
    four_cls = "four" if b["fours"] > 0 else "zero"
    six_cls  = "six"  if b["sixes"] > 0 else "zero"
    sr_color = "#f5c842" if b["runs"] > 0 else "#2e3d50"
    wkts     = f"<span style='color:#e84040;font-weight:800'> {b['team_w']}W</span>" if b["team_w"] else ""
    return f"""
    <div class="bowler-card {b['cls']}">
      <div class="top-stripe"></div>
      <div class="bc-header">
        <div class="bc-name">{b['name']}</div>
        <div class="bc-type-pill">{b['type']}</div>
      </div>
      <div class="bc-team-line">{b['team_ov']} ov &nbsp;·&nbsp; {b['team_r']} runs{wkts}</div>
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
      <div class="bc-footer">
        <div class="bc-sr">SR <strong style="color:{sr_color}">{sr}</strong></div>
        <div class="bc-dots">{b['dots']} dot{'s' if b['dots']!=1 else ''}</div>
      </div>
    </div>"""

# ─── HERO ─────────────────────────────────────────────────────────────────────
img_inner = (
    f'<img src="{player_img_src}" alt="Sanju Samson"/>'
    if player_img_src
    else '<div class="hero-img-emoji">🏏</div>'
)

st.markdown(f"""
<div class="hero">
  <div class="hero-accent-bar"></div>
  <div class="hero-bg-number">97</div>
  <div class="hero-left">
    <div class="hero-img-container">
      <div class="hero-img-ring"></div>
      <div class="hero-img-inner">{img_inner}</div>
    </div>
    <div class="hero-info">
      <div class="hero-tag">
        <div class="hero-tag-dot"></div>
        Player of the Match &nbsp;·&nbsp; T20 World Cup 2026
      </div>
      <div class="hero-name">
        Sanju
        <em>Samson</em>
      </div>
      <div class="hero-meta">
        <span class="hero-meta-item">Super Eights</span>
        <span class="hero-meta-sep">·</span>
        <span class="hero-meta-item">Eden Gardens, Kolkata</span>
        <span class="hero-meta-sep">·</span>
        <span class="hero-meta-item">March 1, 2026</span>
        <span class="hero-meta-sep">·</span>
        <span class="hero-meta-item">India vs West Indies</span>
      </div>
    </div>
  </div>
  <div class="hero-right">
    <div class="hero-score">97<sup>*</sup></div>
    <div class="hero-score-sub">off 50 balls</div>
    <div class="hero-sr">
      <span class="hero-sr-label">Strike Rate</span>
      <span class="hero-sr-value">194.00</span>
    </div>
    <div class="potm-badge">🏆 Player of the Match</div>
  </div>
</div>
""", unsafe_allow_html=True)

# ─── RECORD BANNER ────────────────────────────────────────────────────────────
st.markdown("""
<div class="record-banner">
  <div class="record-icon">📋</div>
  <div class="record-text">
    <strong>Record:</strong> Highest score by an Indian in a T20 World Cup run-chase ·
    India's biggest-ever T20 WC successful chase ·
    India <strong>199/5</strong> beat West Indies <strong>195/4</strong> by 5 wickets
  </div>
</div>
""", unsafe_allow_html=True)

# ─── STAT CARDS ───────────────────────────────────────────────────────────────
stats = [
    ("🏏", "97*",  "Runs",        "gold", "#f5c842"),
    ("⏱",  "50",   "Balls Faced", "",     "#f0ece0"),
    ("4️⃣",  "12",   "Fours",       "blue", "#60a5fa"),
    ("6️⃣",  "4",    "Sixes",       "teal", "#00c9a7"),
    ("⚡",  "194",  "Strike Rate", "gold", "#f5c842"),
]

cards_html = ""
for icon, val, lbl, cls, accent in stats:
    cards_html += f"""
    <div class="stat-card" style="--accent:{accent}">
      <div class="stat-left">
        <div class="stat-icon">{icon}</div>
        <div class="stat-lbl">{lbl}</div>
      </div>
      <div class="stat-val {cls}">{val}</div>
    </div>"""

st.markdown(f'<div class="stat-grid">{cards_html}</div>', unsafe_allow_html=True)

# ─── SECTION LABEL ────────────────────────────────────────────────────────────
st.markdown("""
<div class="section-label">
  <span class="section-label-text">Innings Breakdown by Phase</span>
  <div class="section-label-line"></div>
</div>""", unsafe_allow_html=True)

# ─── PHASE CARDS ──────────────────────────────────────────────────────────────
# ─── PHASE CARDS ──────────────────────────────────────────────────────────────
phase_dot_colors = {
    "pp":  {"fours": "#f5c842", "sixes": "#f5c842"},
    "mid": {"fours": "#60a5fa", "sixes": "#60a5fa"},
    "dt":  {"fours": "#f97316", "sixes": "#f97316"},
}

phase_html = ""
for ph in phases:
    dc = phase_dot_colors[ph["key"]]
    phase_html += f"""
    <div class="phase-card {ph['key']}">
      <div class="phase-score">{ph['runs']}</div>
      <div class="phase-right">
        <div class="phase-top">
          <div>
            <div class="phase-overs">{ph['overs']}</div>
            <div class="phase-name">{ph['name']}</div>
          </div>
          <div class="phase-sr-pill">SR {ph['sr']}</div>
        </div>
        <div class="phase-detail">
          <div class="phase-detail-item">
            <div class="phase-detail-dot" style="background:{dc['fours']}"></div>
            {ph['balls']} balls
          </div>
          <div class="phase-detail-item">
            <div class="phase-detail-dot" style="background:#60a5fa"></div>
            {ph['fours']} fours
          </div>
          <div class="phase-detail-item">
            <div class="phase-detail-dot" style="background:#00c9a7"></div>
            {ph['sixes']} sixes
          </div>
        </div>
      </div>
    </div>"""

st.markdown(f'<div class="phase-grid">{phase_html}</div>', unsafe_allow_html=True)

# ─── SECTION LABEL ────────────────────────────────────────────────────────────
st.markdown("""
<div class="section-label section-gap">
  <span class="section-label-text">vs Each Bowler — Samson's Contribution</span>
  <div class="section-label-line"></div>
</div>""", unsafe_allow_html=True)

# ─── BOWLER CARDS ─────────────────────────────────────────────────────────────
row1 = "".join(bowler_card_html(b) for b in bowlers_row1)
row2 = "".join(bowler_card_html(b) for b in bowlers_row2)
st.markdown(f"""
<div class="bowler-grid-top">{row1}</div>
<div class="bowler-grid-bot">{row2}</div>
<div class="summary-strip">
  <div class="summary-item">
    <div class="summary-val">8</div>
    <div class="summary-lbl">Dot Balls</div>
  </div>
  <div class="summary-item">
    <div class="summary-val">12</div>
    <div class="summary-lbl">Fours Hit</div>
  </div>
  <div class="summary-item">
    <div class="summary-val">4</div>
    <div class="summary-lbl">Sixes Hit</div>
  </div>
  <div class="summary-item">
    <div class="summary-val">72</div>
    <div class="summary-lbl">Boundary Runs</div>
  </div>
  <div class="summary-item">
    <div class="summary-val">25</div>
    <div class="summary-lbl">Running Runs</div>
  </div>
  <div class="summary-item">
    <div class="summary-val">7</div>
    <div class="summary-lbl">Bowlers Faced</div>
  </div>
</div>
""", unsafe_allow_html=True)

# ─── SECTION LABEL ────────────────────────────────────────────────────────────
st.markdown("""
<div class="section-label section-gap">
  <span class="section-label-text">Score Progression</span>
  <div class="section-label-line"></div>
</div>""", unsafe_allow_html=True)

# ─── SCORE PROGRESSION CHART ─────────────────────────────────────────────────
fig = go.Figure()

# Gradient area
fig.add_trace(go.Scatter(
    x=progression["Ball"], y=progression["Score"],
    fill="tozeroy",
    fillgradient=dict(
        type="vertical",
        colorscale=[[0, "rgba(245,200,66,0.18)"], [1, "rgba(245,200,66,0)"]],
    ),
    line=dict(color="rgba(0,0,0,0)"),
    showlegend=False, hoverinfo="skip",
))

# Main line
fig.add_trace(go.Scatter(
    x=progression["Ball"], y=progression["Score"],
    mode="lines+markers",
    line=dict(color="#f5c842", width=3, shape="spline", smoothing=1.0),
    marker=dict(
        color="#07090f", size=8,
        line=dict(color="#f5c842", width=2.5),
    ),
    hovertemplate="<b>Ball %{x}</b><br>Score: %{y}*<extra></extra>",
    showlegend=False,
))

# Phase boundary lines
for x_val, label, color in [(6, "PP END", "rgba(245,200,66,0.3)"), (15, "MIDDLE END", "rgba(96,165,250,0.3)")]:
    fig.add_vline(x=x_val, line=dict(color=color, width=1, dash="dot"))
    fig.add_annotation(x=x_val, y=105, text=label, showarrow=False,
                       font=dict(color=color, size=8, family="Barlow Condensed"),
                       textangle=0, xanchor="center")

# Milestone annotations
fig.add_annotation(x=26, y=53, text="<b>50</b> (26b)",
                   showarrow=True, arrowhead=0, arrowcolor="#00c9a7",
                   font=dict(color="#00c9a7", size=11, family="Barlow Condensed"),
                   ax=0, ay=-36, bgcolor="rgba(0,201,167,0.1)",
                   bordercolor="#00c9a7", borderwidth=1, borderpad=4)
fig.add_annotation(x=50, y=97, text="<b>97*</b> (50b)",
                   showarrow=True, arrowhead=0, arrowcolor="#f5c842",
                   font=dict(color="#f5c842", size=11, family="Barlow Condensed"),
                   ax=-20, ay=-36, bgcolor="rgba(245,200,66,0.1)",
                   bordercolor="#f5c842", borderwidth=1, borderpad=4)

fig.update_layout(
    paper_bgcolor="rgba(255,255,255,0.02)",
    plot_bgcolor="rgba(0,0,0,0)",
    height=210,
    margin=dict(l=48, r=20, t=24, b=36),
    xaxis=dict(
        title=dict(text="Ball", font=dict(color="#2e3d50", size=10, family="Barlow")),
        showgrid=True, gridcolor="rgba(255,255,255,0.03)",
        color="#2e3d50", tickfont=dict(color="#2e3d50", size=10, family="Barlow"),
        range=[0, 51], zeroline=False, tickmode="linear", dtick=5,
    ),
    yaxis=dict(
        title=dict(text="Runs", font=dict(color="#2e3d50", size=10, family="Barlow")),
        showgrid=True, gridcolor="rgba(255,255,255,0.03)",
        color="#2e3d50", tickfont=dict(color="#2e3d50", size=10, family="Barlow"),
        range=[0, 112], zeroline=False,
    ),
    font=dict(family="Barlow"),
    shapes=[dict(
        type="rect", xref="paper", yref="paper",
        x0=0, y0=0, x1=1, y1=1,
        line=dict(color="rgba(255,255,255,0.05)", width=1),
        fillcolor="rgba(0,0,0,0)",
    )],
)

st.plotly_chart(fig, use_container_width=True, config={"displayModeBar": False})

# ─── MILESTONES + MATCH CONTEXT ──────────────────────────────────────────────
st.markdown("""
<div class="section-label section-gap">
  <span class="section-label-text">Key Moments & Match Summary</span>
  <div class="section-label-line"></div>
</div>""", unsafe_allow_html=True)

left, right = st.columns([3, 2], gap="large")

with left:
    milestone_html = '<div class="milestone-list">'
    for dot_cls, ball_label, title, desc in milestones:
        milestone_html += f"""
        <div class="milestone">
          <div class="m-dot-wrap">
            <div class="m-dot {dot_cls}"></div>
          </div>
          <div class="m-content">
            <div class="m-ball">{ball_label}</div>
            <div class="m-title">{title}</div>
            <div class="m-desc">{desc}</div>
          </div>
        </div>"""
    milestone_html += '</div>'
    st.markdown(milestone_html, unsafe_allow_html=True)

with right:
    st.markdown("""
    <div class="quote-card">
      <div class="quote-marks">"</div>
      <div class="quote-text">
        I relied on the experience gained from many years in this format. My focus shifted
        to building a partnership and sticking to my process without thinking of doing anything
        extraordinary. This will remain one of the greatest days of my life.
      </div>
      <div class="quote-attr">— Sanju Samson, post-match</div>
    </div>""", unsafe_allow_html=True)

    st.markdown("""
    <div class="match-ctx">
      <div class="match-ctx-header">Match Result — India won by 5 wickets</div>
      <div class="match-ctx-body">
        <div class="ctx-grid">
          <div class="ctx-cell">
            <div class="ctx-lbl">Target</div>
            <div class="ctx-val">196</div>
          </div>
          <div class="ctx-cell">
            <div class="ctx-lbl">India Scored</div>
            <div class="ctx-val" style="color:#00c9a7">199/5</div>
          </div>
          <div class="ctx-cell">
            <div class="ctx-lbl">Balls to spare</div>
            <div class="ctx-val" style="color:#f5c842">4</div>
          </div>
          <div class="ctx-cell">
            <div class="ctx-lbl">Margin</div>
            <div class="ctx-val">5 wkts</div>
          </div>
        </div>
        <div class="ctx-semi">
          India advance to <strong>T20 WC 2026 Semi-Finals</strong><br>
          vs England · Wankhede, Mumbai · March 5
        </div>
      </div>
    </div>""", unsafe_allow_html=True)

# ─── FOOTER ───────────────────────────────────────────────────────────────────
st.markdown("""
<div class="dash-footer">
  <div class="footer-left">
    Data: ESPNcricinfo / ICC Official Scorecard &nbsp;·&nbsp; T20 World Cup 2026 Super Eights<br>
    Eden Gardens, Kolkata &nbsp;·&nbsp; March 1, 2026 &nbsp;·&nbsp; India 199/5 beat West Indies 195/4 by 5 wickets
  </div>
  <div class="footer-right">#TEAMINDIA · #T20WC2026</div>
</div>
""", unsafe_allow_html=True)
