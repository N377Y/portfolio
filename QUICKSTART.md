# 🎯 Portfolio - Quick Start Guide

Welcome to your modern portfolio website! This guide will help you get started quickly.

## 🚀 Quick Start (Local Development)

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Run the application
python main.py

# 3. Open in browser
# Navigate to: http://127.0.0.1:5003
```

## 📝 Recent Updates (v2.2)

### ✅ What's New

1. **AI Coding Tools Section** 
   - Added new skills category: Claude Code, GitHub Copilot, Cursor, Gemini, GPT Codex
   - Hidden by default with "Voir plus" button

2. **Show More/Less Button**
   - Technical skills now have a toggle button
   - Reduces visual clutter on page load
   - Smooth animations for expanding/collapsing

3. **Code Cleanup**
   - Removed duplicate sections
   - All documentation files consolidated into README.md
   - Added English comments throughout the codebase
   - Removed unnecessary markdown files

4. **Deployment Ready**
   - ✅ Dockerfile for containerization
   - ✅ app.yaml for Google App Engine
   - ✅ deploy.sh script for easy GCP deployment
   - ✅ init-github.sh script for GitHub setup
   - ✅ Comprehensive DEPLOYMENT.md guide

## 🛠️ Customization

### Update Your Information

Edit `main.py` to update:
- Personal information (name, title, bio)
- Skills and proficiency levels
- Work experience
- Projects
- Contact information

### Add Your Content

1. **Profile Photo**: Replace `static/images/profile.png`
2. **CV**: Update `static/cv/CV_Marie-Ange_KUITCHE.pdf`
3. **Project Images**: Add to `static/projets/`
4. **Certifications**: Add to `static/certifications/`

## 📦 Deployment

### GitHub
```bash
./init-github.sh
# Follow the interactive prompts
```

### Google Cloud Platform
```bash
./deploy.sh
# Choose: 1) Cloud Run or 2) App Engine
```

**For detailed instructions, see [DEPLOYMENT.md](DEPLOYMENT.md)**

## 📚 Documentation

- **README.md** - Complete project documentation
- **DEPLOYMENT.md** - Deployment guide for GCP and GitHub
- **LICENSE** - MIT License

## 🎨 Features

- ✨ Modern, responsive design
- 🌓 Dark/Light mode toggle
- 🎭 WebGL background animations
- 📱 Mobile-friendly
- 🚀 Fast loading with optimizations
- 🔒 Secure (production-ready)
- ♿ Accessible keyboard navigation
- 🎯 SEO optimized

## 🐛 Need Help?

1. Check [DEPLOYMENT.md](DEPLOYMENT.md) for deployment issues
2. See [README.md](README.md) for full documentation
3. Review code comments (in English)

## 📞 Support

**Marie-Ange KUITCHE**
- Email: marie-ange.kuitche@groupe-esigelec.org
- GitHub: [@N377Y](https://github.com/N377Y)

---

**🎉 Ready to deploy your portfolio to the world!**

Start by running `python main.py` to see it locally, then use `./deploy.sh` when ready to go live!

