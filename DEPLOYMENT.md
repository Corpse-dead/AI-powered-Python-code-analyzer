# 🚀 Deployment Guide

This guide covers deploying the Smart Code Review Assistant to various cloud platforms.

## 📦 Quick Deploy Options

### Option 1: Railway (Recommended - Free Tier)

[![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/new)

1. Fork this repository on GitHub
2. Go to [Railway.app](https://railway.app)
3. Click "Start a New Project"
4. Select "Deploy from GitHub repo"
5. Choose your forked repository
6. Railway will auto-detect and deploy!

**Environment Setup:**
- No environment variables needed
- Auto-detects Python and installs dependencies
- Exposes port automatically

---

### Option 2: Render (Free Tier)

1. Fork this repository
2. Go to [Render.com](https://render.com)
3. Click "New" → "Web Service"
4. Connect your GitHub repository
5. Configure:
   - **Name:** `smart-code-review`
   - **Runtime:** Python 3
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `uvicorn app:app --host 0.0.0.0 --port $PORT`
6. Click "Create Web Service"

---

### Option 3: Heroku

```bash
# Install Heroku CLI first
heroku login
heroku create smart-code-review-yourname
git push heroku main
heroku open
```

**Note:** Heroku requires `Procfile` (already included)

---

### Option 4: Vercel (Serverless)

1. Install Vercel CLI: `npm i -g vercel`
2. Run: `vercel`
3. Follow prompts
4. Done!

**Note:** Create `vercel.json`:
```json
{
  "builds": [{"src": "app.py", "use": "@vercel/python"}],
  "routes": [{"src": "/(.*)", "dest": "app.py"}]
}
```

---

## 🔧 Configuration for Deployment

### Update `app.py` for Production

The app is already configured to work on any cloud platform. The key line:

```python
uvicorn.run("app:app", host="0.0.0.0", port=int(os.getenv("PORT", 8000)))
```

This uses the `PORT` environment variable that cloud platforms provide.

### Dependencies

All dependencies are in `requirements.txt`:
- FastAPI
- Uvicorn
- scikit-learn
- radon
- numpy

---

## 🌐 Custom Domain (Optional)

After deployment, you can add a custom domain:

**Railway:**
- Settings → Domains → Add Custom Domain

**Render:**
- Settings → Custom Domain → Add Domain

**Heroku:**
```bash
heroku domains:add yourdomain.com
```

---

## 📊 Monitoring & Logs

**View Logs:**
- **Railway:** Dashboard → Deployments → View Logs
- **Render:** Logs tab in dashboard
- **Heroku:** `heroku logs --tail`

---

## 🔒 Security Considerations

For production deployment:

1. **Add rate limiting:**
```python
from slowapi import Limiter
limiter = Limiter(key_func=get_remote_address)
```

2. **Add CORS restrictions:**
```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://yourdomain.com"],  # Specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

3. **Add authentication** (optional for public use)

---

## ✅ Pre-Deployment Checklist

- [x] All dependencies in `requirements.txt`
- [x] `Procfile` configured
- [x] `runtime.txt` specifies Python version
- [x] Static files properly served
- [x] CORS configured
- [x] Port configuration dynamic
- [ ] Update README with live demo link
- [ ] Test locally: `python app.py`

---

## 🎉 After Deployment

1. **Update README.md** with live demo link:
```markdown
## 🌐 Live Demo
Try it live: [https://your-app.railway.app](https://your-app.railway.app)
```

2. **Test the deployment:**
   - Visit the URL
   - Upload a test file
   - Paste code and analyze

3. **Share your project:**
   - Add deployment badge to README
   - Share on LinkedIn/Twitter
   - Add to your portfolio

---

## 🐛 Troubleshooting

**Build fails:**
- Check Python version in `runtime.txt`
- Verify all packages install locally first

**App crashes on startup:**
- Check logs for errors
- Verify PORT environment variable usage

**Static files not loading:**
- Ensure `static/` directory is included in git
- Check file paths are relative

**Import errors:**
- Add missing packages to `requirements.txt`
- Run `pip freeze > requirements.txt`

---

## 💡 Tips

- **Free tiers** are perfect for portfolio projects
- **Cold starts** may take a few seconds on free tier
- **Keep it active** - some platforms sleep after inactivity
- **Monitor usage** - stay within free tier limits

---

**Ready to deploy? Choose a platform and go live! 🚀**
