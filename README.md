# Divyal Padalkar — DevOps Portfolio

A futuristic, premium DevOps portfolio built with Streamlit.

## 📁 Folder Structure

```
portfolio/
├── app.py                  # Main Streamlit app (all sections)
├── data.py                 # All personal content (edit this!)
├── requirements.txt        # Python dependencies
├── styles/
│   └── style.css           # All custom CSS (futuristic dark theme)
├── assets/
│   └── Divyal_Padalkar_Resume.pdf  # Place your resume PDF here
└── .streamlit/
    └── config.toml         # Streamlit theme config
```

## ✏️ How to Customize

1. **All personal content** → Edit `data.py`
   - Update GitHub repo links for each project
   - Update LinkedIn URL
   - Edit stats, skills, certifications as needed

2. **Resume PDF** → Drop your resume at `assets/Divyal_Padalkar_Resume.pdf`

3. **Styling** → Edit `styles/style.css` for colors, fonts, spacing

## 🚀 Running Locally

```bash
pip install streamlit
streamlit run app.py
```

## ☁️ Deploy on Streamlit Community Cloud

1. Push this folder to a GitHub repo
2. Go to https://share.streamlit.io
3. Connect your GitHub repo
4. Set `app.py` as the main file
5. Deploy!

> Make sure `assets/Divyal_Padalkar_Resume.pdf` is committed to the repo.

## 🛠️ Update Project Links

In `data.py`, each project has a `github` field — replace the placeholder URLs with your actual repo links:

```python
"github": "https://github.com/divyal27/your-actual-repo-name",
```
