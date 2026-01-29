# Portfolio - Marie-Ange KUITCHE

A modern, responsive portfolio website showcasing my skills, projects, and professional experience as a Full Stack Developer & QA Test Automation Engineer.

## 🚀 Features

- **Modern Design**: Sleek, professional interface with smooth animations
- **Responsive**: Fully optimized for desktop, tablet, and mobile devices
- **Interactive**: WebGL background animations and custom cursor effects
- **Dark Mode**: Toggle between light and dark themes
- **Project Showcase**: Detailed project cards with modals for extended information
- **PDF Viewer**: Embedded certifications and CV viewer
- **Performance**: Optimized loading and lazy-loading for assets

## 🛠️ Tech Stack

- **Backend**: Python, Flask
- **Frontend**: HTML5, CSS3, JavaScript (ES6+)
- **Graphics**: Three.js for WebGL effects
- **Icons**: Font Awesome 6
- **Fonts**: Google Fonts (Inter, Space Grotesk)
- **Deployment**: Google Cloud Platform (GCP)

## 📦 Installation

### Prerequisites

- Python 3.8+
- pip
- Git

### Local Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/N377Y/portfolio.git
   cd portfolio
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On macOS/Linux
   # or
   venv\Scripts\activate  # On Windows
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   python main.py
   ```

5. **Open in browser**
   Navigate to `http://127.0.0.1:5003`

## 🚀 Deployment to Google Cloud Platform

### Using Cloud Run

1. **Install gcloud CLI**
   ```bash
   # Follow instructions at: https://cloud.google.com/sdk/docs/install
   ```

2. **Initialize gcloud**
   ```bash
   gcloud init
   gcloud auth login
   ```

3. **Set your project**
   ```bash
   gcloud config set project YOUR_PROJECT_ID
   ```

4. **Deploy to Cloud Run**
   ```bash
   gcloud run deploy portfolio \
     --source . \
     --platform managed \
     --region europe-west1 \
     --allow-unauthenticated
   ```

### Using App Engine

1. **Create app.yaml**
   ```yaml
   runtime: python39
   entrypoint: gunicorn -b :$PORT main:app
   ```

2. **Deploy**
   ```bash
   gcloud app deploy
   ```

## 📁 Project Structure

```
portfolio/
├── main.py                 # Flask application entry point
├── config.py              # Configuration settings
├── requirements.txt       # Python dependencies
├── Dockerfile            # Docker configuration for deployment
├── .dockerignore         # Docker ignore rules
├── .gitignore            # Git ignore rules
├── README.md             # This file
├── static/
│   ├── css/
│   │   └── style.css     # Main stylesheet
│   ├── js/
│   │   └── script.js     # JavaScript functionality
│   ├── images/
│   │   ├── profile.png   # Profile photo
│   │   └── ...
│   ├── projets/
│   │   └── ...           # Project images
│   ├── certifications/
│   │   └── ...           # PDF certifications
│   └── cv/
│       └── CV_Marie-Ange_KUITCHE.pdf
└── templates/
    └── index.html        # Main HTML template
```

## 🎨 Customization

### Update Personal Information

Edit `main.py` and modify the `portfolio_data` dictionary:

```python
portfolio_data = {
    'name': 'Your Name',
    'title': 'Your Title',
    'bio': 'Your bio...',
    # ... more fields
}
```

### Add Projects

Add new projects to the `projects` array in `main.py`:

```python
{
    'title': 'Project Name',
    'description': 'Short description',
    'tech': ['Python', 'React'],
    'color': '#667eea',
    'image': '/static/projets/project.png',
    'github': 'https://github.com/...',
    'demo': 'https://...',
    'details': {
        'objectif': '...',
        'features': [...],
        'challenges': [...],
        'results': '...'
    }
}
```

### Change Colors

Update CSS variables in `static/css/style.css`:

```css
:root {
    --primary: #6366f1;
    --secondary: #8b5cf6;
    --accent: #ec4899;
    /* ... */
}
```

## 🔧 Environment Variables

For production deployment, set these environment variables:

```bash
FLASK_ENV=production
SECRET_KEY=your-secret-key-here
PORT=8080
```

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 👤 Author

**Marie-Ange KUITCHE**

- Email: marie-ange.kuitche@groupe-esigelec.org
- GitHub: [@N377Y](https://github.com/N377Y)
- LinkedIn: [Marie-Ange Kuitche](https://www.linkedin.com/in/marie-ange-nelly-kuitche-megouo-a49974226/)

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

## ⭐ Show your support

Give a ⭐️ if you like this project!

---

*Built with ❤️ using Flask, Three.js, and modern web technologies*

