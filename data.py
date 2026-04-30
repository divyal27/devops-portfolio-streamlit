# ============================================================
# data.py — Edit all personal content here
# ============================================================

PROFILE = {
    "name": "Divyal Padalkar",
    "headline": "DevOps Engineer · DevSecOps · AIOps",
    "tagline": "Automating Infrastructure. Securing Pipelines. Building Reliable Delivery Systems.",
    "summary": (
        "3rd-year B.E. Computer Engineering student (SPPU, graduating 2027) specializing in "
        "DevOps, SRE, and Cloud Engineering. Currently interning as a DevOps Engineer at Hisan Labs, "
        "automating infrastructure with Ansible, GitHub Actions, ELK Stack, Prometheus, and Kubernetes "
        "on AWS. Built end-to-end projects using Docker, Kubernetes, Terraform, ArgoCD, and cloud "
        "platforms — focusing on reliability, monitoring, and secure CI/CD. Open to DevOps / SRE / "
        "DevSecOps roles in Pune."
    ),
    "location": "Pune, Maharashtra, India",
    "email": "888divyal.3@gmail.com",
    "phone": "+91 7498841528",
    "github": "https://github.com/divyal27",
    "linkedin": "https://linkedin.com/in/divyal-padalkar",  # UPDATE with your actual LinkedIn URL
    "resume_file": "assets/Divyal_Padalkar_Resume.pdf",  # Place your resume PDF in assets/
}

STATS = [
    {"label": "Projects Built", "value": "6+", "icon": "🚀"},
    {"label": "Pipelines Automated", "value": "10+", "icon": "⚙️"},
    {"label": "Tools Mastered", "value": "25+", "icon": "🛠️"},
    {"label": "Cloud Platforms", "value": "3", "icon": "☁️"},
]

SKILLS = {
    "☁️ Cloud": ["GCP", "AWS", "Azure"],
    "📦 Containers & Orchestration": ["Docker", "Kubernetes", "Helm"],
    "🔄 CI/CD": ["GitHub Actions", "Jenkins", "GitLab CI", "ArgoCD"],
    "🏗️ IaC & Config": ["Terraform", "Ansible"],
    "📊 Monitoring & Observability": ["Prometheus", "Grafana", "AWS CloudWatch", "Datadog", "ELK Stack"],
    "🔐 DevSecOps": ["Bandit", "SAST", "SonarQube", "Trivy"],
    "🤖 AIOps": ["Dynatrace", "LogicMonitor", "Moogsoft", "Splunk ITSI"],
    "💻 Languages": ["Python", "Bash", "YAML", "Java"],
    "🖥️ OS & VCS": ["Linux", "GitHub", "GitLab", "Git"],
}

EXPERIENCE = [
    {
        "company": "Hisan Labs Pvt Ltd",
        "role": "DevOps Intern",
        "location": "Pune",
        "period": "Feb 2026 – Present",
        "type": "current",
        "bullets": [
            "Automated server configuration and environment consistency across staging and production by implementing Ansible playbooks.",
            "Reduced MTTR by ~35% across 3 services by configuring ELK Stack alerting and Prometheus rules, cutting average incident resolution from 40 min to 26 min.",
            "Facilitated Pre-production Acceptance Testing by designing GitHub Actions workflows that validate code quality before deployment.",
        ],
        "tags": ["Ansible", "ELK Stack", "Prometheus", "Kubernetes", "GitHub Actions", "AWS"],
    },
    {
        "company": "Widesoftech Pvt. Ltd.",
        "role": "Full Stack Web Development Intern",
        "location": "Pune",
        "period": "Jan 2026 – Feb 2026",
        "type": "past",
        "bullets": [
            "Built and deployed InternMeets (internmeets.com), a live student internship platform serving real users, contributing Frontend and Backend features within a team over 1 month.",
            "Gained production experience working on a fully functional live product, handling real-world deployment and debugging in a professional team environment.",
        ],
        "tags": ["Full Stack", "Production Deployment", "Team Collaboration"],
    },
]

EDUCATION = {
    "institution": "Genba Sopanrao Moze College of Engineering",
    "affiliation": "Affiliated to Savitribai Phule Pune University (SPPU)",
    "degree": "B.E. Computer Engineering",
    "period": "2023 – 2027",
    "location": "Pune, Maharashtra",
}

PROJECTS = [
    {
        "title": "AIOps Log Analyzer",
        "impact": "Reduced troubleshooting time by ~30% across 3 application domains",
        "description": (
            "Engineered automated monitoring using Python and FastAPI with ELK Stack centralized "
            "logging. Built an intelligent log analysis pipeline that detects anomalies and routes "
            "alerts to reduce manual triage effort."
        ),
        "stack": ["Python", "FastAPI", "Docker", "ELK Stack", "Prometheus", "Grafana"],
        "concepts": ["AIOps", "Log Aggregation", "Alerting", "Observability", "Containerization"],
        "github": "https://github.com/divyal27",  # UPDATE with specific repo URL
        "live": "",  # Add live URL if available
        "highlight": True,
    },
    {
        "title": "UI Chatbot — DevSecOps Pipeline",
        "impact": "Reduced manual infrastructure tasks by ~40%, blocked vulnerable builds automatically",
        "description": (
            "Built a full DevSecOps pipeline on AWS using GitHub Actions with Trivy container "
            "scanning and SonarQube static analysis security gates. Vulnerable builds are blocked "
            "before reaching production."
        ),
        "stack": ["Python", "Docker", "GitHub Actions", "Trivy", "SonarQube", "AWS EC2"],
        "concepts": ["DevSecOps", "SAST", "Container Security", "CI/CD Gates", "AWS"],
        "github": "https://github.com/divyal27",  # UPDATE with specific repo URL
        "live": "",
        "highlight": True,
    },
    {
        "title": "E-commerce Microservices Platform",
        "impact": "Zero-downtime releases with ~35% faster release cycles",
        "description": (
            "Provisioned 5+ microservices on AWS using Terraform for infrastructure and ArgoCD "
            "for GitOps-based continuous deployment. Achieved zero-downtime rolling releases and "
            "dramatically accelerated release velocity."
        ),
        "stack": ["Docker", "Kubernetes", "Terraform", "AWS", "GitHub Actions", "ArgoCD"],
        "concepts": ["GitOps", "Microservices", "IaC", "Zero-Downtime Deploy", "Orchestration"],
        "github": "https://github.com/divyal27",  # UPDATE with specific repo URL
        "live": "",
        "highlight": True,
    },
    {
        "title": "Weather DevOps Flask App",
        "impact": "End-to-end containerized deployment with automated CI/CD pipeline",
        "description": (
            "Developed and deployed a Flask weather application with a complete DevOps pipeline — "
            "containerized with Docker, deployed via automated CI/CD, and monitored for reliability."
        ),
        "stack": ["Python", "Flask", "Docker", "GitHub Actions", "AWS"],
        "concepts": ["Containerization", "CI/CD", "Cloud Deploy", "Flask"],
        "github": "https://github.com/divyal27/weather-devops-flask",  # UPDATE if different
        "live": "",
        "highlight": False,
    },
    {
        "title": "Flask URL Shortener — DevSecOps",
        "impact": "Security-hardened URL shortener with integrated SAST scanning",
        "description": (
            "Built a URL shortener service with a full DevSecOps pipeline including static analysis, "
            "container vulnerability scanning, and automated deployment — focusing on security at "
            "every stage of the delivery pipeline."
        ),
        "stack": ["Python", "Flask", "Docker", "Trivy", "SonarQube", "GitHub Actions"],
        "concepts": ["DevSecOps", "SAST", "Security Gates", "CI/CD"],
        "github": "https://github.com/divyal27/flask-url-shortener-devsecops",  # UPDATE if different
        "live": "",
        "highlight": False,
    },
    {
        "title": "Self-Healing CI/CD Pipeline",
        "impact": "Automated failure detection and recovery in CI/CD workflows",
        "description": (
            "Implemented self-healing mechanisms in a CI/CD pipeline for a Flask URL shortener — "
            "automatically detecting failures, triggering rollbacks, and notifying teams, minimizing "
            "human intervention in incident response."
        ),
        "stack": ["Python", "Flask", "Docker", "GitHub Actions", "Bash"],
        "concepts": ["Self-Healing", "Automated Rollback", "Resilience", "SRE"],
        "github": "https://github.com/divyal27/self-healing-ci-cd-flask-url-shortener",  # UPDATE if different
        "live": "",
        "highlight": False,
    },
]

CERTIFICATIONS = [
    {"name": "Claude Code in Action", "issuer": "Anthropic Education"},
    {"name": "Building with the Claude API", "issuer": "Anthropic Education"},
]

PIPELINE_STAGES = [
    {"icon": "📝", "label": "Code", "desc": "Write clean, reviewed code"},
    {"icon": "🔨", "label": "Build", "desc": "Compile & package artifacts"},
    {"icon": "🧪", "label": "Test", "desc": "Automated test suites"},
    {"icon": "🔐", "label": "Secure", "desc": "SAST, DAST, container scan"},
    {"icon": "📦", "label": "Containerize", "desc": "Docker image build & push"},
    {"icon": "🚀", "label": "Deploy", "desc": "GitOps / ArgoCD / K8s"},
    {"icon": "📊", "label": "Monitor", "desc": "Prometheus, Grafana, ELK"},
    {"icon": "🔁", "label": "Improve", "desc": "Feedback loop & iteration"},
]
