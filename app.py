"""
app.py — Divyal Padalkar DevOps Portfolio  (FIXED VERSION)
Run: streamlit run app.py
"""

import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path
from data import (
    PROFILE, STATS, SKILLS, EXPERIENCE,
    EDUCATION, PROJECTS, CERTIFICATIONS,
    PIPELINE_STAGES
)

# ─── Page Config ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Divyal Padalkar | DevOps Engineer",
    page_icon="⚙️",
    layout="wide",
    initial_sidebar_state="collapsed",
    menu_items={"Get Help": None, "Report a bug": None, "About": None},
)

# ─── Load CSS ─────────────────────────────────────────────────────────────────
css_path = Path("styles/style.css")
css_content = ""
if css_path.exists():
    with open(css_path) as f:
        css_content = f.read()
    st.markdown(f"<style>{css_content}</style>", unsafe_allow_html=True)

# ─── Helper: load resume bytes ────────────────────────────────────────────────
def get_resume_bytes():
    resume_path = Path(PROFILE["resume_file"])
    if resume_path.exists():
        with open(resume_path, "rb") as f:
            return f.read()
    return None

# ─── Key fix: render loop-built HTML via components.html (bypasses sanitizer) ─
def html_block(html: str, height: int = 400):
    full = f"""<!DOCTYPE html><html><head>
    <meta charset="utf-8">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@300;400;500;700&family=Syne:wght@400;600;700;800&display=swap" rel="stylesheet">
    <style>
    {css_content}
    *{{margin:0;padding:0;box-sizing:border-box;}}
    body{{background:transparent;color:var(--text-primary);font-family:var(--font-display);}}
    </style></head><body>{html}</body></html>"""
    components.html(full, height=height, scrolling=False)

# ═══════════════════════════════════════════════════════════════════════════════
# TOP NAV
# ═══════════════════════════════════════════════════════════════════════════════
st.markdown("""
<nav class="top-nav">
  <div class="nav-brand">⚙️ &nbsp;divyal.dev</div>
  <div class="nav-links">
    <a href="#about">About</a>
    <a href="#skills">Skills</a>
    <a href="#experience">Experience</a>
    <a href="#projects">Projects</a>
    <a href="#pipeline">Pipeline</a>
    <a href="#contact">Contact</a>
  </div>
</nav>
""", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════════════════
# HERO
# ═══════════════════════════════════════════════════════════════════════════════
st.markdown("""
<section id="hero">
<div class="hero-section">
  <div class="hero-bg"></div>
  <div class="hero-grid-overlay"></div>
  <div class="hero-tag">🟢 &nbsp;Available for DevOps / SRE Roles &nbsp;·&nbsp; Pune, India</div>
  <h1 class="hero-name">Divyal<br><span>Padalkar</span></h1>
  <p class="hero-tagline">&gt; DevOps Engineer · DevSecOps · AIOps · SRE</p>
  <p class="hero-summary">
    Automating Infrastructure. Securing Pipelines. Building Reliable Delivery Systems.<br>
    3rd-year B.E. Computer Engineering student specializing in cloud-native DevOps —
    currently interning at Hisan Labs, building automation across CI/CD, Kubernetes,
    Prometheus, and ELK Stack on AWS.
  </p>
  <div class="hero-cta">
    <a class="btn-primary" href="#projects">🚀 &nbsp;View Projects</a>
    <a class="btn-outline" href="#contact">✉️ &nbsp;Contact Me</a>
    <a class="btn-outline" href="#resume">📄 &nbsp;Download Resume</a>
  </div>
</div>
</section>
""", unsafe_allow_html=True)

# ── Stats ─────────────────────────────────────────────────────────────────────
stats_inner = ""
for s in STATS:
    stats_inner += f"""
    <div class="stat-card">
      <div class="stat-icon">{s['icon']}</div>
      <div class="stat-value">{s['value']}</div>
      <div class="stat-label">{s['label']}</div>
    </div>"""
html_block(f'<div class="stats-row">{stats_inner}</div>', height=140)

# ═══════════════════════════════════════════════════════════════════════════════
# ABOUT
# ═══════════════════════════════════════════════════════════════════════════════
st.markdown('<div id="about"></div>', unsafe_allow_html=True)
st.markdown("""
<div class="section-wrap">
  <div class="section-label">// 01</div>
  <h2 class="section-title">About Me</h2>
  <hr class="section-divider">
</div>
""", unsafe_allow_html=True)

col_a, col_b = st.columns([3, 2], gap="large")
with col_a:
    st.markdown(f"""
    <p style="font-size:0.95rem;color:var(--text-secondary);line-height:1.9;margin-bottom:1.25rem;">
    {PROFILE['summary']}
    </p>
    <div class="edu-card">
      <div>
        <div class="edu-name">{EDUCATION['institution']}</div>
        <div class="edu-affil">{EDUCATION['affiliation']}</div>
        <div class="edu-degree">🎓 {EDUCATION['degree']}</div>
      </div>
      <div class="edu-meta">
        <div class="edu-period">{EDUCATION['period']}</div>
        <div class="edu-loc">📍 {EDUCATION['location']}</div>
      </div>
    </div>
    """, unsafe_allow_html=True)

with col_b:
    st.markdown("""
    <div class="terminal-widget">
      <div class="terminal-header">
        <div class="terminal-dot" style="background:#ff5f57"></div>
        <div class="terminal-dot" style="background:#febc2e"></div>
        <div class="terminal-dot" style="background:#28c840"></div>
        <span style="color:var(--text-dim);font-size:0.72rem;margin-left:0.5rem">divyal@devops ~ bash</span>
      </div>
      <div class="terminal-body">
        <div class="terminal-line">
          <span class="terminal-prompt">divyal@devops:~$</span>
          <span class="terminal-cmd">whoami</span>
        </div>
        <div class="terminal-out terminal-success">Divyal Padalkar // DevOps Engineer</div>
        <br>
        <div class="terminal-line">
          <span class="terminal-prompt">divyal@devops:~$</span>
          <span class="terminal-cmd">kubectl get pods --all-namespaces</span>
        </div>
        <div class="terminal-out">NAMESPACE&nbsp;&nbsp;NAME&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;STATUS</div>
        <div class="terminal-out terminal-success">prod&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;api-server-x4k2p&nbsp;&nbsp;Running ✓</div>
        <div class="terminal-out terminal-success">prod&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;worker-z9m3q&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Running ✓</div>
        <div class="terminal-out terminal-success">monitor&nbsp;&nbsp;&nbsp;prometheus-7qn2x&nbsp;&nbsp;Running ✓</div>
        <br>
        <div class="terminal-line">
          <span class="terminal-prompt">divyal@devops:~$</span>
          <span class="terminal-cmd">terraform plan</span>
        </div>
        <div class="terminal-out terminal-success">Plan: 5 to add, 0 to change, 0 to destroy.</div>
        <br>
        <div class="terminal-line">
          <span class="terminal-prompt">divyal@devops:~$</span>
          <span class="terminal-cmd blink">_</span>
        </div>
      </div>
    </div>
    """, unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════════════════
# SKILLS
# ═══════════════════════════════════════════════════════════════════════════════
st.markdown('<div id="skills"></div>', unsafe_allow_html=True)
st.markdown("""
<div class="section-wrap">
  <div class="section-label">// 02</div>
  <h2 class="section-title">Skills &amp; Tools</h2>
  <hr class="section-divider">
</div>
""", unsafe_allow_html=True)

skills_inner = ""
for category, tools in SKILLS.items():
    tags_html = "".join(f'<span class="skill-tag">{t}</span>' for t in tools)
    skills_inner += f"""
    <div class="skill-category">
      <div class="skill-cat-title">{category}</div>
      <div class="skill-tags">{tags_html}</div>
    </div>"""
html_block(f'<div class="skills-grid">{skills_inner}</div>', height=480)

# ═══════════════════════════════════════════════════════════════════════════════
# EXPERIENCE
# ═══════════════════════════════════════════════════════════════════════════════
st.markdown('<div id="experience"></div>', unsafe_allow_html=True)
st.markdown("""
<div class="section-wrap">
  <div class="section-label">// 03</div>
  <h2 class="section-title">Experience</h2>
  <hr class="section-divider">
</div>
""", unsafe_allow_html=True)

timeline_inner = ""
for exp in EXPERIENCE:
    dot_class = "timeline-dot current" if exp["type"] == "current" else "timeline-dot"
    bullets_html = "".join(f"<li>{b}</li>" for b in exp["bullets"])
    tags_html = "".join(f'<span class="exp-tag">{t}</span>' for t in exp["tags"])
    role_prefix = "🟢 " if exp["type"] == "current" else ""
    timeline_inner += f"""
    <div class="timeline-item">
      <div class="{dot_class}"></div>
      <div class="timeline-card">
        <div class="timeline-header">
          <div class="timeline-company">{exp['company']}</div>
          <div class="timeline-period">{exp['period']}</div>
        </div>
        <div class="timeline-role">{role_prefix}{exp['role']} · {exp['location']}</div>
        <ul class="timeline-bullets">{bullets_html}</ul>
        <div class="timeline-tags">{tags_html}</div>
      </div>
    </div>"""
html_block(f'<div class="timeline">{timeline_inner}</div>', height=580)

# ═══════════════════════════════════════════════════════════════════════════════
# PROJECTS
# ═══════════════════════════════════════════════════════════════════════════════
st.markdown('<div id="projects"></div>', unsafe_allow_html=True)
st.markdown("""
<div class="section-wrap">
  <div class="section-label">// 04</div>
  <h2 class="section-title">Projects</h2>
  <hr class="section-divider">
</div>
""", unsafe_allow_html=True)

def build_project_cards(proj_list):
    html = '<div class="projects-grid">'
    for p in proj_list:
        stack_tags = "".join(f'<span class="stack-tag">{t}</span>' for t in p["stack"])
        concepts = " · ".join(p["concepts"])
        card_class = "project-card highlight" if p.get("highlight") else "project-card"
        github_btn = (
            f'<a class="project-btn project-btn-github" href="{p["github"]}" target="_blank">🔗 GitHub</a>'
            if p.get("github") else ""
        )
        live_btn = (
            f'<a class="project-btn project-btn-github" href="{p["live"]}" target="_blank">🌐 Live</a>'
            if p.get("live") else ""
        )
        html += f"""
        <div class="{card_class}">
          <div class="project-title">{p['title']}</div>
          <div class="project-impact">📈 {p['impact']}</div>
          <p class="project-desc">{p['description']}</p>
          <div class="project-concepts">Concepts: {concepts}</div>
          <div class="project-stack">{stack_tags}</div>
          <div class="project-actions">{github_btn}{live_btn}</div>
        </div>"""
    html += "</div>"
    return html

featured = [p for p in PROJECTS if p.get("highlight")]
other    = [p for p in PROJECTS if not p.get("highlight")]

st.markdown("""<p style="font-family:var(--font-mono);font-size:0.72rem;color:var(--cyan);
letter-spacing:0.1em;text-transform:uppercase;margin-bottom:0.5rem;">⭐ Featured</p>
""", unsafe_allow_html=True)
html_block(build_project_cards(featured), height=660)

st.markdown("""<p style="font-family:var(--font-mono);font-size:0.72rem;color:var(--text-dim);
letter-spacing:0.1em;text-transform:uppercase;margin:1.5rem 0 0.5rem;">More Projects</p>
""", unsafe_allow_html=True)
html_block(build_project_cards(other), height=660)

# ═══════════════════════════════════════════════════════════════════════════════
# PIPELINE
# ═══════════════════════════════════════════════════════════════════════════════
st.markdown('<div id="pipeline"></div>', unsafe_allow_html=True)
st.markdown("""
<div class="section-wrap">
  <div class="section-label">// 05</div>
  <h2 class="section-title">Continuous Automation</h2>
  <hr class="section-divider">
</div>
""", unsafe_allow_html=True)

pipeline_stages_html = ""
for i, stage in enumerate(PIPELINE_STAGES):
    pipeline_stages_html += f"""
    <div class="pipeline-stage">
      <div class="stage-icon-wrap">{stage['icon']}</div>
      <div class="stage-label">{stage['label']}</div>
      <div class="stage-desc">{stage['desc']}</div>
    </div>"""
    if i < len(PIPELINE_STAGES) - 1:
        pipeline_stages_html += '<div class="pipeline-arrow">›</div>'

pipeline_full = f"""
<div class="pipeline-section">
  <p style="font-size:0.9rem;color:#8ba3c7;line-height:1.8;max-width:600px;margin-bottom:0.5rem;">
    My engineering philosophy: every change flows through an automated, secure, observable pipeline —
    from the first commit to production monitoring, with zero manual steps between stages.
  </p>
  <div class="pipeline-stages">{pipeline_stages_html}</div>
</div>"""
html_block(pipeline_full, height=280)

# ═══════════════════════════════════════════════════════════════════════════════
# CERTIFICATIONS
# ═══════════════════════════════════════════════════════════════════════════════
st.markdown("""
<div class="section-wrap">
  <div class="section-label">// 06</div>
  <h2 class="section-title">Certifications</h2>
  <hr class="section-divider">
</div>
""", unsafe_allow_html=True)

cert_inner = ""
for c in CERTIFICATIONS:
    cert_inner += f"""
    <div class="cert-card">
      <div class="cert-icon">🎓</div>
      <div>
        <div class="cert-name">{c['name']}</div>
        <div class="cert-issuer">{c['issuer']}</div>
      </div>
    </div>"""
html_block(f'<div class="cert-grid">{cert_inner}</div>', height=110)

# ═══════════════════════════════════════════════════════════════════════════════
# RESUME
# ═══════════════════════════════════════════════════════════════════════════════
st.markdown('<div id="resume"></div>', unsafe_allow_html=True)
st.markdown("""
<div class="section-wrap">
  <div class="section-label">// 07</div>
  <h2 class="section-title">Resume</h2>
  <hr class="section-divider">
</div>
""", unsafe_allow_html=True)

st.markdown(f"""
<div class="resume-card">
  <div class="resume-facts">
    <div class="resume-fact"><span class="resume-fact-icon">👤</span><div><strong>Divyal Padalkar</strong> — DevOps / SRE Engineer</div></div>
    <div class="resume-fact"><span class="resume-fact-icon">📍</span><div>Pune, Maharashtra, India</div></div>
    <div class="resume-fact"><span class="resume-fact-icon">🎓</span><div>B.E. Computer Engineering · SPPU · 2027</div></div>
    <div class="resume-fact"><span class="resume-fact-icon">💼</span><div>DevOps Intern @ Hisan Labs (Feb 2026 – Present)</div></div>
    <div class="resume-fact"><span class="resume-fact-icon">🛠️</span><div>Docker · Kubernetes · Terraform · Ansible · GitHub Actions · ELK Stack</div></div>
    <div class="resume-fact"><span class="resume-fact-icon">☁️</span><div>AWS · GCP · Azure</div></div>
  </div>
</div>
""", unsafe_allow_html=True)

st.markdown("<div style='margin-top:1.5rem'></div>", unsafe_allow_html=True)
resume_bytes = get_resume_bytes()
if resume_bytes:
    st.download_button(
        label="⬇️  Download Resume (PDF)",
        data=resume_bytes,
        file_name="Divyal_Padalkar_Resume.pdf",
        mime="application/pdf",
    )
else:
    st.markdown("""
    <div style="background:var(--bg-card);border:1px dashed var(--border);border-radius:8px;
    padding:1rem 1.5rem;font-family:var(--font-mono);font-size:0.8rem;color:var(--text-dim);">
    ⚠️ &nbsp;Place your resume PDF at
    <code style="color:var(--cyan)">assets/Divyal_Padalkar_Resume.pdf</code> to enable download.
    </div>
    """, unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════════════════
# CONTACT
# ═══════════════════════════════════════════════════════════════════════════════
st.markdown('<div id="contact"></div>', unsafe_allow_html=True)
st.markdown("""
<div class="section-wrap">
  <div class="section-label">// 08</div>
  <h2 class="section-title">Let's Connect</h2>
  <hr class="section-divider">
  <p style="font-size:0.95rem;color:var(--text-secondary);line-height:1.8;max-width:550px;margin-bottom:0.5rem;">
    I'm actively looking for <strong style="color:var(--text-primary)">DevOps / SRE / DevSecOps</strong>
    internships and fresher roles. If you're building reliable systems and want someone who cares deeply
    about automation and observability — let's talk.
  </p>
</div>
""", unsafe_allow_html=True)

contact_html = f"""
<div class="contact-grid">
  <a class="contact-card" href="mailto:{PROFILE['email']}">
    <div class="contact-icon">✉️</div>
    <div class="contact-label">Email</div>
    <div class="contact-value">{PROFILE['email']}</div>
  </a>
  <a class="contact-card" href="{PROFILE['github']}" target="_blank">
    <div class="contact-icon">🐙</div>
    <div class="contact-label">GitHub</div>
    <div class="contact-value">github.com/divyal27</div>
  </a>
  <a class="contact-card" href="{PROFILE['linkedin']}" target="_blank">
    <div class="contact-icon">💼</div>
    <div class="contact-label">LinkedIn</div>
    <div class="contact-value">Divyal Padalkar</div>
  </a>
  <a class="contact-card" href="tel:{PROFILE['phone']}">
    <div class="contact-icon">📱</div>
    <div class="contact-label">Phone</div>
    <div class="contact-value">{PROFILE['phone']}</div>
  </a>
</div>"""
html_block(contact_html, height=200)

# ─── Footer ───────────────────────────────────────────────────────────────────
st.markdown("""
<div class="portfolio-footer">
  Built with <span>⚙️ precision</span> by Divyal Padalkar &nbsp;·&nbsp;
  <span>DevOps · DevSecOps · AIOps</span> &nbsp;·&nbsp; Pune, India
</div>
""", unsafe_allow_html=True)

