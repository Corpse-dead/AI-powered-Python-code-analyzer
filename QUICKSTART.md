# 🚀 Quick Start Guide

## Installation & Setup

### 1. Clone or Download the Project
```bash
git clone <your-repo-url>
cd aiml
```

### 2. Create Virtual Environment (Recommended)
```bash
python -m venv .venv
```

### 3. Activate Virtual Environment

**Windows:**
```bash
.venv\Scripts\activate
```

**Mac/Linux:**
```bash
source .venv/bin/activate
```

### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

### 5. Run the Application
```bash
python app.py
```

### 6. Open in Browser
Navigate to: **http://localhost:8000**

---

## 📝 How to Use

### Method 1: Upload a File
1. Click "Choose File" button
2. Select a Python (.py) file
3. Click "Analyze File"
4. View results!

### Method 2: Paste Code
1. Copy your Python code
2. Paste it into the text area
3. Click "Analyze Code"
4. View results!

---

## 🧪 Test the Application

Run the test suite:
```bash
python test_app.py
```

Or try analyzing the example file:
```bash
# Upload examples/sample_code.py through the web interface
```

---

## 📊 Understanding Results

### Quality Score (0-100)
- **90-100 (A)**: Excellent code
- **80-89 (B)**: Good code
- **70-79 (C)**: Acceptable
- **60-69 (D)**: Needs work
- **0-59 (F)**: Major issues

### Key Metrics
- **Cyclomatic Complexity**: Lower is better (<10 is good)
- **Maintainability Index**: Higher is better (>50 is good)
- **Comment Ratio**: 10-30% is ideal

---

## 🛠️ Troubleshooting

### Port Already in Use
If port 8000 is busy, edit `app.py` and change:
```python
uvicorn.run(app, host="0.0.0.0", port=8001, reload=True)
```

### Module Not Found Errors
Make sure you activated the virtual environment and installed dependencies:
```bash
.venv\Scripts\activate
pip install -r requirements.txt
```

---

## 📸 Screenshots for GitHub

When adding to GitHub, consider taking screenshots of:
1. Main interface (upload section)
2. Analysis results with good code
3. Analysis results showing suggestions
4. The metrics dashboard

---

## 🎓 For Your Resume/Portfolio

Highlight these features:
- ✅ Machine Learning integration (scikit-learn)
- ✅ Full-stack development (FastAPI + JavaScript)
- ✅ RESTful API design
- ✅ Code analysis algorithms
- ✅ Responsive web design
- ✅ Software engineering best practices

---

## 🚀 Next Steps

1. **Add to GitHub**
   ```bash
   git init
   git add .
   git commit -m "Initial commit: Smart Code Review Assistant"
   git remote add origin <your-repo-url>
   git push -u origin main
   ```

2. **Customize**
   - Update README.md with your name/info
   - Add screenshots
   - Modify ML model training data
   - Add more analysis features

3. **Deploy** (Optional)
   - Deploy to Heroku, Railway, or Render
   - Share live demo link in README

---

**Need Help?** Check the main [README.md](README.md) for detailed information.
