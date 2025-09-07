#!/usr/bin/env python3
"""
Static Site Generator for Kaidi Zhang's Personal Website
Converts Flask templates to static HTML files for GitHub Pages deployment
"""

import os
import shutil
import json
from pathlib import Path
from app import app

def create_output_directory():
    """Create and clean the output directory"""
    # For {username}.github.io repos, GitHub Pages serves from root directory
    output_dir = Path('.')  # Current directory (root)
    
    # Clean up any existing HTML files (but keep source files)
    html_files = ['index.html', 'about.html', 'education.html', 'activities.html', 'skills.html', 'contact.html', '404.html']
    for html_file in html_files:
        html_path = output_dir / html_file
        if html_path.exists():
            html_path.unlink()
    
    # Clean up API directory if it exists
    api_dir = output_dir / 'api'
    if api_dir.exists():
        shutil.rmtree(api_dir)
    
    # Create API directory
    api_dir.mkdir(exist_ok=True)
    
    return output_dir

def copy_static_files(output_dir):
    """Static files are already in the right place - no need to copy for root deployment"""
    # For root deployment, static files are already in /static directory
    # No copying needed since we're generating HTML files in the same directory
    print("ℹ️  Static files already in correct location (/static)")

def generate_static_pages(output_dir):
    """Generate static HTML pages from Flask routes"""
    
    # Routes to generate static files for
    routes = [
        ('/', 'index.html'),
        ('/about', 'about.html'),
        ('/education', 'education.html'),
        ('/activities', 'activities.html'),
        ('/skills', 'skills.html'),
        ('/contact', 'contact.html'),
    ]
    
    with app.test_client() as client:
        for route, filename in routes:
            print(f"Generating {filename} from {route}...")
            
            # Get the rendered HTML
            response = client.get(route)
            
            if response.status_code == 200:
                # Process the HTML to fix paths for static hosting
                html_content = response.get_data(as_text=True)
                
                # Fix static file paths (remove Flask url_for calls)
                html_content = html_content.replace('href="/static/', 'href="static/')
                html_content = html_content.replace('src="/static/', 'src="static/')
                
                # Write to file
                output_file = output_dir / filename
                with open(output_file, 'w', encoding='utf-8') as f:
                    f.write(html_content)
                
                print(f"✅ Generated {filename}")
            else:
                print(f"❌ Failed to generate {filename} (status: {response.status_code})")

def generate_api_data(output_dir):
    """Generate static JSON files for API endpoints"""
    
    with app.test_client() as client:
        # Generate resume API data
        print("Generating resume.json from /api/resume...")
        response = client.get('/api/resume')
        
        if response.status_code == 200:
            # Create api directory
            api_dir = output_dir / 'api'
            api_dir.mkdir(exist_ok=True)
            
            # Write JSON data
            with open(api_dir / 'resume.json', 'w', encoding='utf-8') as f:
                f.write(response.get_data(as_text=True))
            
            print("✅ Generated api/resume.json")
        else:
            print(f"❌ Failed to generate resume.json (status: {response.status_code})")

def create_github_pages_config(output_dir):
    """Create configuration files for GitHub Pages"""
    
    # Create .nojekyll to prevent Jekyll processing
    nojekyll_file = output_dir / '.nojekyll'
    nojekyll_file.touch()
    
    # Create CNAME file if custom domain is needed (optional)
    # cname_file = output_dir / 'CNAME'
    # with open(cname_file, 'w') as f:
    #     f.write('your-custom-domain.com')
    
    print("✅ Created GitHub Pages configuration files")

def create_404_page(output_dir):
    """Create a custom 404 page"""
    
    html_404 = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Page Not Found - Kaidi Zhang</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="static/css/style.css">
</head>
<body>
    <div class="container-fluid vh-100 d-flex align-items-center justify-content-center">
        <div class="text-center">
            <div class="error-icon mb-4">
                <i class="fas fa-exclamation-triangle fa-5x text-warning"></i>
            </div>
            <h1 class="display-1 fw-bold text-primary">404</h1>
            <h2 class="mb-4">Page Not Found</h2>
            <p class="lead mb-4">Sorry, the page you're looking for doesn't exist.</p>
            <a href="index.html" class="btn btn-primary btn-lg">
                <i class="fas fa-home me-2"></i>Go Home
            </a>
        </div>
    </div>
</body>
</html>"""
    
    with open(output_dir / '404.html', 'w', encoding='utf-8') as f:
        f.write(html_404)
    
    print("✅ Created 404.html page")

def update_contact_form():
    """Update contact form to work without backend"""
    print("ℹ️  Note: Contact form will show demo message since no backend is available in static hosting")

def main():
    """Main build function"""
    print("🏗️  Building Static Site for GitHub Pages")
    print("=" * 50)
    
    # Create output directory
    output_dir = create_output_directory()
    print(f"📁 Created output directory: {output_dir}")
    
    # Copy static files
    copy_static_files(output_dir)
    print("📦 Copied static files")
    
    # Generate HTML pages
    generate_static_pages(output_dir)
    
    # Generate API data as static JSON
    generate_api_data(output_dir)
    
    # Create GitHub Pages configuration
    create_github_pages_config(output_dir)
    
    # Create 404 page
    create_404_page(output_dir)
    
    # Note about contact form
    update_contact_form()
    
    print("\n" + "=" * 50)
    print("✅ Static site generation complete!")
    print(f"📂 Files generated in: {output_dir.absolute()}")
    print("\n🚀 Deployment Instructions:")
    print("1. Commit and push all changes to your repository:")
    print("   git add .")
    print("   git commit -m 'Deploy personal website'")
    print("   git push origin main")
    print("2. Your site will be automatically available at: https://zkaidi19.github.io")
    print("3. No GitHub Pages configuration needed for {username}.github.io repos!")
    print("\n💡 The site will automatically update when you push changes!")

if __name__ == '__main__':
    main()
