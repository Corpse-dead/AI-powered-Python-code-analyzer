# 🤖 Smart Code Review Assistant

An AI-powered Python code analyzer that uses machine learning to evaluate code quality, detect code smells, and provide actionable improvement suggestions.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-0.104+-green.svg)
![ML](https://img.shields.io/badge/ML-scikit--learn-orange.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

## 🌐 Live Demo
> **Coming Soon!** Deploy to Railway, Render, or Heroku - see [DEPLOYMENT.md](DEPLOYMENT.md)

## 🌟 Features

- **📊 Static Code Analysis**: Comprehensive metrics including cyclomatic complexity, maintainability index, and Halstead metrics
- **🤖 ML-Powered Quality Prediction**: Machine learning model trained to predict code quality scores
- **🔍 Code Smell Detection**: Automatically detects common anti-patterns and code smells
- **💡 Smart Suggestions**: Provides actionable recommendations for code improvement
- **🎨 Beautiful Web Interface**: Modern, responsive UI for easy code submission and result visualization
- **📈 Detailed Metrics**: Lines of code, complexity, documentation ratio, and more

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/AI-powered-Python-code-analyzer.git
cd AI-powered-Python-code-analyzer
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
python app.py
```

4. Open your browser and navigate to:
```
http://localhost:8000
```

## 📖 Usage

### Web Interface

1. **Upload a File**: Click "Choose File" and select a Python (.py) file
2. **Paste Code**: Copy and paste your Python code directly into the text area
3. **View Results**: Get instant feedback with quality scores, metrics, and suggestions

### API Endpoints

#### Analyze Uploaded File
```bash
curl -X POST "http://localhost:8000/api/analyze" \
  -F "file=@your_code.py"
```

#### Analyze Code Text
```bash
curl -X POST "http://localhost:8000/api/analyze-text" \
  -H "Content-Type: application/json" \
  -d '{"code": "def hello(): print(\"Hello, World!\")"}'
```

#### Health Check
```bash
curl "http://localhost:8000/api/health"
```

## 🏗️ Project Structure

```
smart-code-review/
├── app.py                 # FastAPI application entry point
├── src/
│   ├── __init__.py
│   ├── code_analyzer.py   # Static code analysis module
│   └── ml_models.py       # ML-based quality prediction
├── static/
│   ├── index.html         # Web interface
│   ├── styles.css         # Styling
│   └── script.js          # Frontend logic
├── requirements.txt       # Python dependencies
└── README.md             # This file
```

## 🎯 Metrics Explained

### Code Metrics
- **Lines of Code (LOC)**: Total lines including comments and blanks
- **Logical Lines**: Actual code lines (excluding comments/blanks)
- **Comment Ratio**: Percentage of comments in code
- **Cyclomatic Complexity**: Measure of code complexity
- **Maintainability Index**: Overall code maintainability (0-100)

### Quality Score
The ML model assigns a quality score (0-100) based on:
- Code structure and organization
- Naming conventions
- Documentation quality
- Complexity metrics
- Best practices adherence

### Letter Grades
- **A (85-100)**: Excellent code quality
- **B (70-84)**: Good code with minor improvements needed
- **C (55-69)**: Acceptable code, some refactoring recommended
- **D (40-54)**: Poor code, significant improvements needed
- **F (0-39)**: Very poor code, major refactoring required

## 🔧 Technology Stack

- **Backend**: FastAPI (Python web framework)
- **ML/AI**: scikit-learn, RandomForest classifier
- **Code Analysis**: Radon, AST, Pylint
- **Frontend**: HTML5, CSS3, Vanilla JavaScript
- **API**: RESTful API with JSON responses

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 Future Enhancements

- [ ] Support for additional programming languages (JavaScript, Java, etc.)
- [ ] Integration with GitHub for automatic PR reviews
- [ ] Custom rule configuration
- [ ] Historical analysis and trend tracking
- [ ] VS Code extension
- [ ] Docker containerization
- [ ] Advanced NLP models (CodeBERT, GraphCodeBERT)

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👨‍💻 Author

Created by a CS student passionate about AI/ML and code quality!

## 🙏 Acknowledgments

- FastAPI for the excellent web framework
- scikit-learn for ML capabilities
- Radon for code metrics
- The Python community for amazing tools and libraries

## 📧 Contact

Questions or suggestions? Feel free to open an issue or reach out!

---

⭐ If you find this project useful, please consider giving it a star on GitHub!
