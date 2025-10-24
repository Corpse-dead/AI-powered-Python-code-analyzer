// API base URL
const API_BASE = '';

// Upload and analyze file
async function uploadFile() {
    const fileInput = document.getElementById('fileInput');
    const file = fileInput.files[0];
    
    if (!file) {
        alert('Please select a Python file first!');
        return;
    }
    
    if (!file.name.endsWith('.py')) {
        alert('Please select a Python (.py) file!');
        return;
    }
    
    showLoading();
    
    const formData = new FormData();
    formData.append('file', file);
    
    try {
        const response = await fetch(`${API_BASE}/api/analyze`, {
            method: 'POST',
            body: formData
        });
        
        if (!response.ok) {
            throw new Error('Analysis failed');
        }
        
        const data = await response.json();
        displayResults(data);
    } catch (error) {
        alert('Error analyzing code: ' + error.message);
        hideLoading();
    }
}

// Analyze pasted code
async function analyzeText() {
    const codeInput = document.getElementById('codeInput');
    const code = codeInput.value.trim();
    
    if (!code) {
        alert('Please paste some Python code first!');
        return;
    }
    
    showLoading();
    
    try {
        const response = await fetch(`${API_BASE}/api/analyze-text`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ code })
        });
        
        if (!response.ok) {
            throw new Error('Analysis failed');
        }
        
        const data = await response.json();
        displayResults(data);
    } catch (error) {
        alert('Error analyzing code: ' + error.message);
        hideLoading();
    }
}

// Display analysis results
function displayResults(data) {
    hideLoading();
    
    const resultsDiv = document.getElementById('results');
    resultsDiv.style.display = 'block';
    
    // Update quality score
    const qualityScore = data.overall_score || data.ml_prediction?.quality_score || 0;
    document.getElementById('qualityScore').textContent = qualityScore.toFixed(1);
    document.getElementById('scoreGrade').textContent = `Grade: ${data.ml_prediction?.rating || '-'}`;
    
    // Update code metrics
    const metricsHtml = [];
    const metrics = data.metrics;
    
    if (metrics.error) {
        metricsHtml.push(`<li style="color: red;">❌ ${metrics.error}: ${metrics.message}</li>`);
    } else {
        metricsHtml.push(`<li><strong>Lines of Code:</strong> ${metrics.lines_of_code}</li>`);
        metricsHtml.push(`<li><strong>Logical Lines:</strong> ${metrics.logical_lines}</li>`);
        metricsHtml.push(`<li><strong>Comments:</strong> ${metrics.comments}</li>`);
        metricsHtml.push(`<li><strong>Comment Ratio:</strong> ${(metrics.comment_ratio * 100).toFixed(1)}%</li>`);
        metricsHtml.push(`<li><strong>Functions:</strong> ${metrics.num_functions}</li>`);
        metricsHtml.push(`<li><strong>Classes:</strong> ${metrics.num_classes}</li>`);
    }
    
    document.getElementById('codeMetrics').innerHTML = metricsHtml.join('');
    
    // Update ML prediction
    const mlHtml = [];
    const ml = data.ml_prediction;
    
    mlHtml.push(`<li><strong>Quality Score:</strong> ${ml.quality_score}/100</li>`);
    mlHtml.push(`<li><strong>Prediction:</strong> ${ml.prediction.replace('_', ' ')}</li>`);
    mlHtml.push(`<li><strong>Confidence:</strong> ${ml.confidence}%</li>`);
    mlHtml.push(`<li><strong>Grade:</strong> ${ml.rating}</li>`);
    
    if (!metrics.error) {
        mlHtml.push(`<li><strong>Avg Complexity:</strong> ${metrics.avg_complexity}</li>`);
        mlHtml.push(`<li><strong>Maintainability:</strong> ${metrics.maintainability_index}</li>`);
    }
    
    document.getElementById('mlPrediction').innerHTML = mlHtml.join('');
    
    // Update suggestions
    const suggestionsHtml = data.suggestions.map(s => `<li>${s}</li>`).join('');
    document.getElementById('suggestions').innerHTML = suggestionsHtml || '<li>No suggestions - looks good!</li>';
    
    // Update code smells
    const smells = metrics.code_smells || [];
    const smellsHtml = smells.length > 0 
        ? smells.map(s => `<li>⚠️ ${s}</li>`).join('')
        : '<li>✅ No code smells detected!</li>';
    document.getElementById('codeSmells').innerHTML = smellsHtml;
    
    // Scroll to results
    resultsDiv.scrollIntoView({ behavior: 'smooth' });
}

// Show loading spinner
function showLoading() {
    document.getElementById('loading').style.display = 'block';
    document.getElementById('results').style.display = 'none';
}

// Hide loading spinner
function hideLoading() {
    document.getElementById('loading').style.display = 'none';
}

// Test API connection on page load
window.addEventListener('load', async () => {
    try {
        const response = await fetch(`${API_BASE}/api/health`);
        const data = await response.json();
        console.log('API Status:', data);
    } catch (error) {
        console.warn('API connection issue:', error);
    }
});
