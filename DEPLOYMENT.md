# 🚀 Deployment Guide

This guide provides step-by-step instructions to deploy your portfolio to Google Cloud Platform (GCP) and push it to GitHub.

## 📋 Prerequisites

Before deploying, make sure you have:

- ✅ Python 3.8+ installed
- ✅ Git installed
- ✅ A Google Cloud account ([Sign up here](https://cloud.google.com/))
- ✅ A GitHub account ([Sign up here](https://github.com/))

---

## 🐙 GitHub Setup

### Option 1: Using the automated script (Recommended)

```bash
./init-github.sh
```

Follow the interactive prompts to set up your GitHub repository.

### Option 2: Manual setup

1. **Initialize Git repository**
   ```bash
   git init
   git add .
   git commit -m "Initial commit: Portfolio website"
   ```

2. **Create a new repository on GitHub**
   - Go to [github.com/new](https://github.com/new)
   - Name it `portfolio` (or your preferred name)
   - Do NOT initialize with README
   - Click "Create repository"

3. **Push to GitHub**
   ```bash
   git remote add origin https://github.com/YOUR_USERNAME/portfolio.git
   git branch -M main
   git push -u origin main
   ```

---

## ☁️ Google Cloud Platform Deployment

### Step 1: Install Google Cloud CLI

#### macOS
```bash
# Using Homebrew
brew install --cask google-cloud-sdk
```

#### Linux
```bash
curl https://sdk.cloud.google.com | bash
exec -l $SHELL
```

#### Windows
Download and run the installer from: https://cloud.google.com/sdk/docs/install

### Step 2: Initialize gcloud

```bash
# Login to your Google account
gcloud auth login

# Initialize gcloud configuration
gcloud init

# Select or create a project
gcloud projects create portfolio-PROJECT_ID --set-as-default
# Replace PROJECT_ID with a unique identifier (e.g., portfolio-12345)
```

### Step 3: Enable Required APIs

```bash
# Enable Cloud Run API (for serverless deployment)
gcloud services enable run.googleapis.com

# Enable Cloud Build API
gcloud services enable cloudbuild.googleapis.com

# Enable App Engine API (if using App Engine)
gcloud services enable appengine.googleapis.com
```

---

## 🎯 Deployment Options

### Option A: Cloud Run (Recommended - Serverless)

**Advantages:**
- ✅ Pay only for what you use
- ✅ Automatic scaling (including to zero)
- ✅ Fast deployment
- ✅ Easy rollbacks

**Deploy using the script:**
```bash
./deploy.sh
# Choose option 1 (Cloud Run)
```

**Or deploy manually:**
```bash
gcloud run deploy portfolio \
  --source . \
  --platform managed \
  --region europe-west1 \
  --allow-unauthenticated \
  --memory 512Mi \
  --max-instances 10
```

**Custom domain (Optional):**
```bash
# Map a custom domain
gcloud run domain-mappings create \
  --service portfolio \
  --domain your-domain.com \
  --region europe-west1
```

---

### Option B: App Engine

**Advantages:**
- ✅ Managed platform
- ✅ Integrated monitoring
- ✅ Easy version management

**Deploy using the script:**
```bash
./deploy.sh
# Choose option 2 (App Engine)
```

**Or deploy manually:**
```bash
# Create App Engine application (first time only)
gcloud app create --region=europe-west

# Deploy
gcloud app deploy
```

**View your app:**
```bash
gcloud app browse
```

---

## 🔧 Configuration

### Environment Variables

For production, update these settings:

**In `main.py`:**
```python
app.config['SECRET_KEY'] = 'your-production-secret-key-here'  # Generate a strong secret
```

**For Cloud Run (using gcloud):**
```bash
gcloud run deploy portfolio \
  --set-env-vars="FLASK_ENV=production,SECRET_KEY=your-secret-key"
```

**For App Engine:**
Create an `env_variables` section in `app.yaml`:
```yaml
env_variables:
  FLASK_ENV: 'production'
  SECRET_KEY: 'your-secret-key-here'
```

### Generate a Secret Key

```python
python -c "import secrets; print(secrets.token_hex(32))"
```

---

## 📊 Monitoring & Logs

### View Logs (Cloud Run)
```bash
gcloud run services logs read portfolio --region=europe-west1
```

### View Logs (App Engine)
```bash
gcloud app logs tail -s default
```

### Access Cloud Console
Visit: https://console.cloud.google.com

---

## 🔄 Updates & Redeployment

### Update Code
```bash
# 1. Make your changes
# 2. Commit to git
git add .
git commit -m "Update portfolio"
git push

# 3. Redeploy
./deploy.sh
```

### Rollback (Cloud Run)
```bash
# List revisions
gcloud run revisions list --service=portfolio --region=europe-west1

# Rollback to previous revision
gcloud run services update-traffic portfolio \
  --to-revisions=REVISION_NAME=100 \
  --region=europe-west1
```

---

## 💰 Cost Estimation

### Cloud Run (Free Tier Generous)
- **Free Tier:** 2 million requests/month
- **After Free Tier:** ~$0.40 per million requests
- **Estimated Cost:** $0-5/month for personal portfolio

### App Engine
- **Free Tier:** 28 instance hours/day
- **After Free Tier:** Varies by instance class
- **Estimated Cost:** $0-10/month for personal portfolio

💡 **Tip:** Cloud Run is more cost-effective for low-traffic sites as it scales to zero.

---

## 🐛 Troubleshooting

### Deployment fails with "permission denied"
```bash
# Re-authenticate
gcloud auth login
gcloud auth application-default login
```

### Port binding error
Make sure your app uses `PORT` environment variable:
```python
if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 5003))
    app.run(host='0.0.0.0', port=port)
```

### Static files not loading
- For Cloud Run: Files are included in the container
- For App Engine: Check `app.yaml` handlers

### Build fails
```bash
# Clear build cache
gcloud builds list
gcloud builds cancel BUILD_ID
```

---

## 📚 Additional Resources

- [Cloud Run Documentation](https://cloud.google.com/run/docs)
- [App Engine Documentation](https://cloud.google.com/appengine/docs)
- [Flask Deployment Guide](https://flask.palletsprojects.com/en/2.3.x/deploying/)
- [GCP Pricing Calculator](https://cloud.google.com/products/calculator)

---

## ✅ Deployment Checklist

Before going live:

- [ ] Update `SECRET_KEY` to a strong random value
- [ ] Test all features locally
- [ ] Update contact information in `main.py`
- [ ] Add your CV PDF to `static/cv/`
- [ ] Add your profile photo to `static/images/`
- [ ] Test on mobile devices
- [ ] Set up custom domain (optional)
- [ ] Configure SSL (automatic with Cloud Run/App Engine)
- [ ] Set up monitoring/alerts
- [ ] Update README with live URL

---

**🎉 Congratulations! Your portfolio is now live on Google Cloud Platform!**

For support, visit the [GCP Community](https://cloud.google.com/community) or [Stack Overflow](https://stackoverflow.com/questions/tagged/google-cloud-platform).

