# Kaidi Zhang - Personal Website

A modern, responsive personal website showcasing my academic journey, skills, and experiences as a Data Science student at the University of Michigan. Built with Flask and automatically deployed to GitHub Pages.

![Website Live](https://img.shields.io/badge/Website-Live-brightgreen?logo=github)
![Python](https://img.shields.io/badge/Python-3.8.1+-blue?logo=python)
![Flask](https://img.shields.io/badge/Flask-3.1.2-lightgrey?logo=flask)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3.0-purple?logo=bootstrap)
![GitHub Pages](https://img.shields.io/badge/Deployed%20on-GitHub%20Pages-blue?logo=github)
![License](https://img.shields.io/badge/License-MIT-yellow)

## 🌟 Project Overview

This personal website serves as a comprehensive digital portfolio, featuring a clean and modern design with a blue/light color scheme. Built with Python Flask for development and automatically converted to static files for GitHub Pages deployment.

**🌐 Live Website:** [https://zkaidi19.github.io](https://zkaidi19.github.io)

The site combines the power of Flask templating for easy development with the simplicity of static hosting for reliable deployment.

### ✨ Key Features

- **Responsive Design**: Mobile-first approach with Bootstrap 5
- **Modern UI/UX**: Clean, professional design with smooth animations
- **Fast Performance**: Optimized static files with CDN resources
- **SEO Friendly**: Semantic HTML structure and meta tags
- **Accessible**: WCAG compliant design principles
- **GitHub Pages**: Automatic deployment and hosting
- **Static API**: JSON resume data available at `/api/resume.json`

## 🏗️ Project Architecture

### System Architecture Diagram

```
┌─────────────────────────────────────────────────────────┐
│                    CLIENT SIDE                          │
├─────────────────────────────────────────────────────────┤
│  Web Browser                                            │
│  ├── HTML5 (Semantic Structure)                         │
│  ├── CSS3 (Custom Styling + Bootstrap 5)                │
│  ├── JavaScript (ES6+ Interactive Features)             │
│  └── Font Awesome Icons + Google Fonts                  │
└─────────────────────────────────────────────────────────┘
                              │
                         HTTP/HTTPS
                              │
┌─────────────────────────────────────────────────────────┐
│                   SERVER SIDE                           │
├─────────────────────────────────────────────────────────┤
│  Flask Application (Python)                             │
│  ├── Route Handlers                                     │
│  ├── Template Rendering (Jinja2)                        │
│  ├── Static File Serving                                │
│  ├── API Endpoints                                      │
│  └── Configuration Management                           │
└─────────────────────────────────────────────────────────┘
                              │
                        File System
                              │
┌─────────────────────────────────────────────────────────┐
│                 DATA & ASSETS                           │
├─────────────────────────────────────────────────────────┤
│  ├── Templates/ (Jinja2 HTML Templates)                 │
│  ├── Static/                                            │
│  │   ├── CSS/ (Custom Stylesheets)                      │
│  │   ├── JS/ (Interactive Scripts)                      │
│  │   └── Images/ (Future Assets)                        │
│  └── Configuration Files                                │
└─────────────────────────────────────────────────────────┘
```

### 📁 Directory Structure

```
zkaidi19.github.io/
│
├── 📄 app.py                 # Main Flask application
├── 📄 requirements.txt       # Python dependencies
├── 📄 README.md             # Project documentation
│
├── 📁 templates/            # Jinja2 HTML templates
│   ├── 📄 base.html         # Base template with navigation
│   ├── 📄 index.html        # Home page
│   ├── 📄 about.html        # About page
│   ├── 📄 education.html    # Education page
│   ├── 📄 activities.html   # Activities page
│   ├── 📄 skills.html       # Skills page
│   └── 📄 contact.html      # Contact page
│
└── 📁 static/               # Static assets
    ├── 📁 css/
    │   └── 📄 style.css     # Custom CSS styling
    ├── 📁 js/
    │   └── 📄 script.js     # Interactive JavaScript
    └── 📁 images/           # Image assets (future)
```

## 🛠️ Tech Stack

### Backend Technologies
- **Python 3.8+**: Core programming language
- **Flask 3.0.0**: Lightweight web framework
- **Jinja2**: Template engine for dynamic HTML
- **Werkzeug**: WSGI toolkit
- **Gunicorn**: Production WSGI server

### Frontend Technologies
- **HTML5**: Semantic markup structure
- **CSS3**: Modern styling with custom properties
- **JavaScript ES6+**: Interactive functionality
- **Bootstrap 5.3.0**: Responsive framework
- **Font Awesome 6.4.0**: Icon library
- **Google Fonts (Inter)**: Typography

### Development Tools
- **Python Virtual Environment**: Dependency isolation
- **Flask Development Server**: Local testing
- **pytest**: Testing framework
- **Black**: Code formatting
- **Flake8**: Code linting

### Design & UX
- **Mobile-First Design**: Responsive across all devices
- **Accessibility**: WCAG 2.1 compliance
- **Performance**: Optimized loading and animations
- **SEO**: Search engine optimization

## 🚀 Installation & Setup

### Prerequisites
- Python 3.8.1 or higher
- [uv](https://docs.astral.sh/uv/) (modern Python package manager)
- Git

### Local Development Setup

1. **Clone the Repository**
   ```bash
   git clone https://github.com/zkaidi19/zkaidi19.github.io.git
   cd zkaidi19.github.io
   ```

2. **Install uv (if not already installed)**
   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   source $HOME/.local/bin/env  # Add to PATH
   ```

3. **Install Dependencies**
   ```bash
   uv sync  # Creates virtual environment and installs all dependencies
   ```

4. **Run the Application**
   ```bash
   uv run python app.py
   # Or use the convenience script
   uv run python run.py
   ```

5. **Access the Website**
   Open your browser and navigate to: `http://localhost:5000`

### Development Workflow

**For Local Development:**
```bash
# Start Flask development server
uv run python run.py dev
# Visit: http://localhost:5000
```

**For Static Site Generation:**
```bash
# Generate static files for GitHub Pages
uv run python build_static.py
# Files created in /docs directory

# Test static files locally (optional)
cd docs && python -m http.server 8000
# Visit: http://localhost:8000
```

**Development vs Production:**
- **Development**: Use Flask server for live editing and debugging
- **Production**: Static files automatically deployed to GitHub Pages

### Production Deployment

#### Using Gunicorn (Recommended)
```bash
uv run gunicorn --bind 0.0.0.0:5000 app:app
```

#### Using Docker (Optional)
```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
```

## 📋 Features & Pages

### 🏠 Home Page (`/`)
- **Hero Section**: Introduction with key statistics
- **Quick Overview**: Snapshot of education, activities, and skills
- **Call-to-Action**: Contact information and links

### 👤 About Page (`/about`)
- **Personal Story**: Detailed background and journey
- **Interests**: Data science, ice skating, cultural arts
- **Statistics**: Location, languages, programming skills

### 🎓 Education Page (`/education`)
- **University of Michigan**: Current Data Science program
- **UM-SJTU Joint Institute**: International experience
- **Skyline High School**: Academic achievements and AP courses
- **Academic Highlights**: GPA, coursework, and achievements

### ⭐ Activities Page (`/activities`)
- **Ice Skating Instructor**: Teaching experience and skills
- **rXn Dance Group**: Cultural performances and teamwork
- **Community Service**: Charity work and volunteer experience

### 🔧 Skills Page (`/skills`)
- **Programming Languages**: Python and C++ proficiency
- **Language Skills**: English and Mandarin fluency
- **Technical Skills**: Data analysis, statistics, algorithms
- **Soft Skills**: Teaching, creativity, cultural awareness

### 📬 Contact Page (`/contact`)
- **Contact Information**: Email, LinkedIn, location
- **Contact Form**: Interactive form with validation
- **Response Times**: Expected communication timelines
- **Availability**: Open opportunities and interests

### 🔌 API Endpoint (`/api/resume`)
- **JSON Format**: Structured resume data
- **Programmatic Access**: For integrations and applications
- **Complete Data**: All resume information in machine-readable format

## 🎨 Design System

### Color Palette
- **Primary Blue**: `#2563eb` - Main brand color
- **Light Blue**: `#dbeafe` - Accent and backgrounds
- **Gray Scale**: `#f8fafc` to `#0f172a` - Text and UI elements
- **Status Colors**: Success (`#10b981`), Warning (`#f59e0b`), etc.

### Typography
- **Font Family**: Inter (Google Fonts)
- **Font Weights**: 300, 400, 500, 600, 700
- **Responsive Scaling**: Fluid typography across devices

### Components
- **Navigation**: Fixed top navigation with smooth scrolling
- **Cards**: Consistent card design with hover effects
- **Buttons**: Primary and outline button styles
- **Forms**: Floating labels with validation
- **Animations**: Smooth transitions and scroll animations

## ⚡ Performance Features

### Frontend Optimizations
- **Lazy Loading**: Images and non-critical resources
- **CSS Optimization**: Custom properties and efficient selectors
- **JavaScript**: Modern ES6+ with performance best practices
- **Caching**: Browser caching for static assets

### Backend Optimizations
- **Static File Serving**: Efficient asset delivery
- **Template Caching**: Jinja2 template optimization
- **Compression**: Gzip compression for production
- **CDN Integration**: Bootstrap and Font Awesome via CDN

## 🧪 Testing

### Running Tests
```bash
# Run all tests
uv run pytest

# Run with coverage
uv run pytest --cov=app

# Run specific test file
uv run pytest tests/test_routes.py
```

### Test Coverage
- **Route Testing**: All endpoints tested
- **Template Rendering**: Template functionality verified
- **API Testing**: JSON endpoint validation
- **Form Validation**: Contact form testing

## 🚀 GitHub Pages Deployment

This website is configured for automatic deployment to GitHub Pages using the special repository naming convention `{username}.github.io`.

### Automatic Deployment Process

1. **Push Changes**: Commit and push changes to the `main` branch
2. **GitHub Actions**: Automatically builds static files using `build_static.py`
3. **Deploy**: Static files are deployed to GitHub Pages
4. **Live**: Website is available at `https://zkaidi19.github.io`

### Manual Build (Optional)

You can also build static files locally:

```bash
# Generate static files
uv run python build_static.py

# Files will be created in root directory
```

### GitHub Pages Configuration

For `{username}.github.io` repositories, **no configuration is needed!** GitHub automatically:
- Serves files from the root directory
- Updates the site when you push to the `main` branch
- Makes your site available at `https://zkaidi19.github.io`

The site will automatically update whenever you push changes to the main branch!

## 📈 Future Enhancements

### Planned Features
- **Blog Section**: Technical articles and insights
- **Project Portfolio**: Showcase of data science projects
- **Resume Download**: PDF generation and download
- **Dark Mode**: Theme switching capability
- **Multi-language**: Chinese language support

### Technical Improvements
- **Database Integration**: Store contact form submissions
- **Email Service**: Automated contact form responses
- **Analytics**: Google Analytics integration
- **SEO Enhancement**: Advanced meta tags and structured data
- **PWA Features**: Service worker and offline capability

## 🤝 Contributing

While this is a personal website, contributions for improvements are welcome!

### How to Contribute
1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Make your changes and test thoroughly
4. Commit your changes: `git commit -m 'Add feature'`
5. Push to the branch: `git push origin feature-name`
6. Submit a pull request

### Code Standards
- Follow PEP 8 for Python code
- Use consistent indentation (4 spaces)
- Add comments for complex functionality
- Test all changes before submitting

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📞 Contact Information

**Kaidi Zhang**
- 📧 Email: [zkaidi@umich.edu](mailto:zkaidi@umich.edu)
- 💼 LinkedIn: [kaidi-zhang-6a862a2b0](https://www.linkedin.com/in/kaidi-zhang-6a862a2b0/)
- 📍 Location: Ann Arbor, Michigan 48103

## 🙏 Acknowledgments

- **University of Michigan**: For providing excellent education and opportunities
- **Bootstrap Team**: For the responsive framework
- **Flask Community**: For the lightweight and powerful web framework
- **Font Awesome**: For the comprehensive icon library
- **Google Fonts**: For the beautiful Inter typography

---

**Built with ❤️ by Kaidi Zhang | Data Science Student at University of Michigan**