import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path
from data import (
    PROFILE,
    STATS,
    SKILLS,
    EXPERIENCE,
    EDUCATION,
    PROJECTS,
    CERTIFICATIONS,
    PIPELINE_STAGES,
)

st.set_page_config(
    page_title="Divyal Padalkar | DevOps Portfolio",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed",
)

def load_css():
    css_file = Path("styles/style.css")
    if css_file.exists():
        st.markdown(f"<style>{css_file.read_text()}</style>", unsafe_allow_html=True)

def get_resume_bytes():
    resume_path = Path(PROFILE.get("resume_file", ""))
    if resume_path.exists():
        return resume_path.read_bytes()
    return None

def badge(text):
    return f"<span class='pill'>{text}</span>"

def social_button(label, url, kind="ghost"):
    return f"<a class='btn {kind}' href='{url}' target='_blank'>{label}</a>"

def section_title(eyebrow, title, desc=""):
    st.markdown(
        f"""
        <div class="section-head">
            <div class="eyebrow">{eyebrow}</div>
            <h2>{title}</h2>
            <p>{desc}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

def render_metric_cards():
    html = "<div class='stats-grid'>"
    for item in STATS:
        html += f"""
        <div class='stat-card'>
            <div class='stat-icon'>{item['icon']}</div>
            <div class='stat-value'>{item['value']}</div>
            <div class='stat-label'>{item['label']}</div>
        </div>
        """
    html += "</div>"
    st.markdown(html, unsafe_allow_html=True)

def render_skill_groups():
    html = "<div class='skills-grid'>"
    for category, tools in SKILLS.items():
        html += f"""
        <div class='skill-card'>
            <div class='skill-title'>{category}</div>
            <div class='skill-tags'>
                {''.join([badge(tool) for tool in tools])}
            </div>
        </div>
        """
    html += "</div>"
    st.markdown(html, unsafe_allow_html=True)

def render_experience():
    html = "<div class='timeline'>"
    for exp in EXPERIENCE:
        tags = "".join([badge(tag) for tag in exp.get("tags", [])])
        bullets = "".join([f"<li>{b}</li>" for b in exp.get("bullets", [])])
        current = "Current" if exp.get("type") == "current" else "Past"
        html += f"""
        <div class='timeline-item'>
            <div class='timeline-dot'></div>
            <div class='timeline-card'>
                <div class='timeline-top'>
                    <div>
                        <h3>{exp['role']}</h3>
                        <div class='timeline-company'>{exp['company']} · {exp['location']}</div>
                    </div>
                    <div class='timeline-period'>{exp['period']} · {current}</div>
                </div>
                <ul class='timeline-list'>{bullets}</ul>
                <div class='timeline-tags'>{tags}</div>
            </div>
        </div>
        """
    html += "</div>"
    st.markdown(html, unsafe_allow_html=True)

def render_projects(projects):
    html = "<div class='projects-grid'>"
    for p in projects:
        stack = "".join([badge(s) for s in p.get("stack", [])[:6]])
        concepts = "".join([badge(c) for c in p.get("concepts", [])[:4]])
        live_btn = f"<a class='btn ghost' href='{p['live']}' target='_blank'>Live Demo</a>" if p.get("live") else ""
        github_btn = f"<a class='btn primary' href='{p['github']}' target='_blank'>GitHub</a>" if p.get("github") else ""
        html += f"""
        <div class='project-card'>
            <div class='project-top'>
                <div class='project-kicker'>Project</div>
                <div class='project-impact'>{p['impact']}</div>
            </div>
            <h3>{p['title']}</h3>
            <p>{p['description']}</p>
            <div class='label'>Tech Stack</div>
            <div class='project-tags'>{stack}</div>
            <div class='label'>Concepts</div>
            <div class='project-tags'>{concepts}</div>
            <div class='project-actions'>
                {github_btn}
                {live_btn}
            </div>
        </div>
        """
    html += "</div>"
    st.markdown(html, unsafe_allow_html=True)

def render_pipeline():
    html = "<div class='pipeline-grid'>"
    for step in PIPELINE_STAGES:
        html += f"""
        <div class='pipe-card'>
            <div class='pipe-icon'>{step['icon']}</div>
            <div class='pipe-title'>{step['label']}</div>
            <div class='pipe-desc'>{step['desc']}</div>
        </div>
        """
    html += "</div>"
    st.markdown(html, unsafe_allow_html=True)

def render_certifications():
    html = "<div class='cert-grid'>"
    for cert in CERTIFICATIONS:
        html += f"""
        <div class='cert-card'>
            <div class='cert-name'>{cert['name']}</div>
            <div class='cert-issuer'>{cert['issuer']}</div>
        </div>
        """
    html += "</div>"
    st.markdown(html, unsafe_allow_html=True)

load_css()
resume_bytes = get_resume_bytes()

st.markdown(
    f"""
    <div class='topbar'>
        <div class='brand'>
            <div class='brand-mark'>DP</div>
            <div>
                <div class='brand-name'>{PROFILE['name']}</div>
                <div class='brand-role'>{PROFILE['headline']}</div>
            </div>
        </div>
        <div class='top-links'>
            <a href="{PROFILE['github']}" target="_blank">GitHub</a>
            <a href="{PROFILE['linkedin']}" target="_blank">LinkedIn</a>
            <a href="mailto:{PROFILE['email']}">Email</a>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

left, right = st.columns([1.25, 0.75], gap="large")

with left:
    st.markdown(
        f"""
        <div class='hero-card'>
            <div class='eyebrow'>Available for DevOps / SRE internships</div>
            <h1>{PROFILE['tagline']}</h1>
            <p class='hero-copy'>{PROFILE['summary']}</p>
            <div class='hero-meta'>
                <span>{PROFILE['location']}</span>
                <span>{PROFILE['email']}</span>
            </div>
            <div class='hero-actions'>
                {social_button("View GitHub", PROFILE["github"], "primary")}
                {social_button("Connect LinkedIn", PROFILE["linkedin"], "ghost")}
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with right:
    st.markdown(
        """
        <div class='spotlight-card'>
            <div class='spotlight-label'>Focus Areas</div>
            <div class='spotlight-list'>
                <div>CI/CD Automation</div>
                <div>Kubernetes & Docker</div>
                <div>Cloud Infrastructure</div>
                <div>Monitoring & Observability</div>
                <div>DevSecOps Pipelines</div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

render_metric_cards()

tabs = st.tabs(["Projects", "Skills", "Experience", "Pipeline", "Education & Certs"])

with tabs[0]:
    section_title(
        "Selected Work",
        "Projects that show real DevOps thinking",
        "Built around automation, cloud deployment, observability, security, and release engineering."
    )
    featured = [p for p in PROJECTS if p.get("highlight")]
    others = [p for p in PROJECTS if not p.get("highlight")]
    if featured:
        st.markdown("<div class='subhead'>Featured Projects</div>", unsafe_allow_html=True)
        render_projects(featured)
    if others:
        st.markdown("<div class='subhead'>More Projects</div>", unsafe_allow_html=True)
        render_projects(others)

with tabs[1]:
    section_title(
        "Tool Stack",
        "Skills grouped like an engineering stack",
        "Clearer than a badge wall and easier for recruiters to scan."
    )
    render_skill_groups()

with tabs[2]:
    section_title(
        "Journey",
        "Experience that connects projects to impact",
        "Focused on automation, reliability, and practical cloud work."
    )
    render_experience()

with tabs[3]:
    section_title(
        "Delivery Flow",
        "How I think about shipping systems",
        "From commit to monitoring, every stage should be automated, secure, and observable."
    )
    render_pipeline()

with tabs[4]:
    section_title(
        "Foundation",
        "Education and certifications",
        "Academic base plus continuous learning in DevOps, cloud, and AI tooling."
    )
    edu = EDUCATION
    st.markdown(
        f"""
        <div class='edu-card'>
            <h3>{edu['degree']}</h3>
            <div class='edu-inst'>{edu['institution']}</div>
            <div class='edu-meta'>{edu['affiliation']} · {edu['period']} · {edu['location']}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    render_certifications()

section_title(
    "Contact",
    "Open to internships, trainee roles, and DevOps opportunities",
    "Best suited for cloud, DevOps, SRE, platform engineering, and DevSecOps-focused teams."
)

cta1, cta2, cta3 = st.columns(3)

with cta1:
    st.markdown(
        f"""
        <div class='contact-card'>
            <div class='contact-title'>Email</div>
            <div class='contact-value'>{PROFILE['email']}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with cta2:
    st.markdown(
        f"""
        <div class='contact-card'>
            <div class='contact-title'>GitHub</div>
            <div class='contact-value'><a href="{PROFILE['github']}" target="_blank">{PROFILE['github']}</a></div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with cta3:
    st.markdown(
        f"""
        <div class='contact-card'>
            <div class='contact-title'>LinkedIn</div>
            <div class='contact-value'><a href="{PROFILE['linkedin']}" target="_blank">Profile</a></div>
        </div>
        """,
        unsafe_allow_html=True,
    )

if resume_bytes:
    st.download_button(
        "Download Resume",
        data=resume_bytes,
        file_name="Divyal_Padalkar_Resume.pdf",
        mime="application/pdf",
        use_container_width=False,
    )
else:
    st.info("Add your resume PDF at assets/Divyal_Padalkar_Resume.pdf to enable resume download.")

st.markdown(
    """
    <div class='footer-note'>
        Built with Streamlit · Designed as a fresher-friendly DevOps portfolio with a product-style UI.
    </div>
    """,
    unsafe_allow_html=True,
)
