from flask import Flask, render_template, jsonify
import os

app = Flask(__name__)

# Configuration
app.config['SECRET_KEY'] = 'your-secret-key-here'

@app.route('/')
def home():
    """Home page route"""
    return render_template('index.html')

@app.route('/about')
def about():
    """About page route"""
    return render_template('about.html')

@app.route('/education')
def education():
    """Education page route"""
    return render_template('education.html')

@app.route('/activities')
def activities():
    """Activities page route"""
    return render_template('activities.html')

@app.route('/skills')
def skills():
    """Skills page route"""
    return render_template('skills.html')

@app.route('/contact')
def contact():
    """Contact page route"""
    return render_template('contact.html')

@app.route('/api/resume')
def api_resume():
    """API endpoint to get resume data in JSON format"""
    resume_data = {
        "personal_info": {
            "name": "Kaidi Zhang",
            "email": "zkaidi@umich.edu",
            "phone": "734-730-0647",
            "location": "48103, Ann Arbor, Michigan",
            "linkedin": "https://www.linkedin.com/in/kaidi-zhang-6a862a2b0/"
        },
        "education": [
            {
                "institution": "University of Michigan – College of Literature, Science, and the Arts (LSA)",
                "location": "Ann Arbor, MI",
                "degree": "Bachelor of Science, Data Science",
                "duration": "August 2023 – May 2027",
                "coursework": [
                    "Programming and Intro Data Structures",
                    "Introduction to Statistics and Data Analysis",
                    "Linear Algebra"
                ]
            },
            {
                "institution": "University of Michigan-Shanghai Jiao Tong University Joint Institute (JI)",
                "location": "Shanghai, China",
                "courses": "Introduction to Chinese Culture, Intro to Computers and Programming",
                "duration": "May 2024 – August 2025"
            },
            {
                "institution": "Skyline High School",
                "location": "Ann Arbor, MI",
                "gpa": "3.98/4.0",
                "duration": "2019 – 2023",
                "ap_classes": [
                    "Environmental Science", "Computer Science Principles", "Chinese Language and Culture",
                    "Macroeconomics", "Calculus BC", "Computer Science A", "Chemistry",
                    "Physics C Mechanics", "Statistics", "Psychology"
                ]
            }
        ],
        "activities": [
            {
                "title": "Ice Skating Instructor I",
                "location": "Ann Arbor, MI",
                "organization": "Veterans Memorial Park",
                "duration": "Feb 2024 – Present",
                "description": [
                    "Instruct youth in skating fundamentals while supporting head coaches during weekly lessons (6 hrs/week)",
                    "Practiced teaching techniques, creativity, patience, and active listening in a dynamic class environment"
                ]
            },
            {
                "title": "Member",
                "organization": "rXn Chinese-American Co-ed Dance Group",
                "location": "Ann Arbor, MI",
                "duration": "October 2024 – Present",
                "description": [
                    "Participated in four performances in the Fall semester and ten performances in the Winter semester",
                    "rXn's performances are recognized by our use of traditional Chinese props, including a variety of fans, staffs, umbrellas, etc. to represent and honor our cultural background"
                ]
            },
            {
                "title": "Member",
                "organization": "Charity Gift Wrapping for Ann-Hua Chinese School",
                "location": "Briarwood Mall, Ann Arbor, MI",
                "duration": "November 2021",
                "description": [
                    "Collaborated with a team of eight volunteers to provide gift wrapping services at a charity booth in the mall during the holiday season",
                    "Raised hundreds of dollars to meet the goal"
                ]
            }
        ],
        "skills": {
            "programming_languages": ["C++", "Python"],
            "languages": ["Fluent in English and Mandarin"]
        }
    }
    return jsonify(resume_data)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
