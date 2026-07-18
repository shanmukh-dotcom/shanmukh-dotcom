import json
import os

def build_web():
    try:
        with open("icon_paths.json", "r") as f:
            icon_paths = json.load(f)
    except:
        icon_paths = {}

    skills = [
        ("Python", "#3776AB"), ("C++", "#00599C"), ("JavaScript", "#F7DF1E"), ("TypeScript", "#3178C6"),
        ("FastAPI", "#009688"), ("React", "#61DAFB"), ("Next.js", "#FFFFFF"), ("Node.js", "#339933"), 
        ("TailwindCSS", "#06B6D4"), ("Supabase", "#3ECF8E"), ("TensorFlow", "#FF6F00"), 
        ("PyTorch", "#EE4C2C"), ("Docker", "#2496ED"), ("AWS", "#FF9900"), ("Git", "#F05032"), ("Linux", "#FCC624")
    ]
    
    skills_html = ""
    for skill, color in skills:
        path = icon_paths.get(skill, "")
        skills_html += f'''
                        <div class="skill-pill">
                            <svg width="14" height="14" viewBox="0 0 24 24" fill="{color}"><path d="{path}"/></svg>
                            {skill}
                        </div>'''

    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Shanmukh - Portfolio</title>
    <link rel="stylesheet" href="styles.css">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
</head>
<body>
    <div class="banner-container">
        <!-- Main Glassmorphism Panel -->
        <div class="glass-panel">
            <!-- Left Side: Portrait & Ambiance -->
            <div class="left-panel">
                <img src="assets/hero.png" alt="Shanmukh Portrait" class="portrait-img">
            </div>

            <!-- Right Side: Terminal Info -->
            <div class="right-panel">
                <div class="window-controls">
                    <span class="dot close"></span>
                    <span class="dot min"></span>
                    <span class="dot max"></span>
                </div>

                <div class="content-wrapper">
                    <p class="greeting">Hi there 👋</p>
                    <h1 class="name">I'm <span class="gradient-text">Shanmukh</span></h1>
                    
                    <div class="terminal-typing">
                        <span class="prompt">&gt; </span>
                        <span class="typewriter" id="typewriter"></span>
                        <span class="cursor">█</span>
                    </div>

                    <div class="info-grid">
                        <div class="info-row">
                            <span class="info-label">
                                <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2C8.13 2 5 5.13 5 9c0 5.25 7 13 7 13s7-7.75 7-13c0-3.87-3.13-7-7-7zm0 9.5c-1.38 0-2.5-1.12-2.5-2.5s1.12-2.5 2.5-2.5 2.5 1.12 2.5 2.5-1.12 2.5-2.5 2.5z"/></svg>
                                Location
                            </span>
                            <span class="info-val">Bangalore, India</span>
                        </div>
                        <div class="info-row">
                            <span class="info-label">
                                <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M12 3L1 9l4 2.18v6L12 21l7-3.82v-6l2-1.09V17h2V9L12 3zm6.82 6L12 12.72 5.18 9 12 5.28 18.82 9z"/></svg>
                                Education
                            </span>
                            <span class="info-val">Presidency University</span>
                        </div>
                        <div class="info-row">
                            <span class="info-label">
                                <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm0 18c-4.41 0-8-3.59-8-8s3.59-8 8-8 8 3.59 8 8-3.59 8-8 8zm0-14c-3.31 0-6 2.69-6 6s2.69 6 6 6 6-2.69 6-6-2.69-6-6-6zm0 10c-2.21 0-4-1.79-4-4s1.79-4 4-4 4 1.79 4 4-1.79 4-4 4zm0-6c-1.1 0-2 .9-2 2s.9 2 2 2 2-.9 2-2-.9-2-2-2z"/></svg>
                                Current Focus
                            </span>
                            <span class="info-val">Building AI-powered products</span>
                        </div>
                        <div class="info-row">
                            <span class="info-label">
                                <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M22.7 19l-9.1-9.1c.9-2.3.4-5-1.5-6.9-2-2-5-2.4-7.4-1.3L9 6 6 9 1.6 4.7C.5 7.1.9 10.1 2.9 12.1c1.9 1.9 4.6 2.4 6.9 1.5l9.1 9.1c.4.4 1 .4 1.4 0l2.3-2.3c.5-.4.5-1.1.1-1.4z"/></svg>
                                Building
                            </span>
                            <span class="info-val">Smart Campus Buddy, Career Forge &amp; more</span>
                        </div>
                        <div class="info-row">
                            <span class="info-label">
                                <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-1 17.93c-3.95-.49-7-3.85-7-7.93 0-.62.08-1.21.21-1.79L9 15v1c0 1.1.9 2 2 2v1.93zm6.9-2.54c-.26-.81-1-1.39-1.9-1.39h-1v-3c0-.55-.45-1-1-1H8v-2h2c.55 0 1-.45 1-1V7h2c1.1 0 2-.9 2-2v-.41c2.93 1.19 5 4.06 5 7.41 0 2.08-.8 3.97-2.1 5.39z"/></svg>
                                Portfolio
                            </span>
                            <span class="info-val highlight">shanmukhchennuboina.dev</span>
                        </div>
                        <div class="info-row">
                            <span class="info-label">
                                <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M20 4H4c-1.1 0-1.99.9-1.99 2L2 18c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 4l-8 5-8-5V6l8 5 8-5v2z"/></svg>
                                Email
                            </span>
                            <span class="info-val">shanmukh.chennuboina@gmail.com</span>
                        </div>
                    </div>

                    <div class="skills-heading">Skills &amp; Technologies</div>
                    <div class="skills-section">
                        {skills_html}
                    </div>
                </div>
            </div>
        </div>

        <!-- Social Icons Footer Outside the Panel -->
        <div class="socials">
            <a href="https://github.com/shanmukh-dotcom" target="_blank" class="social-link" style="color: #8B5CF6">
                <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2C6.477 2 2 6.477 2 12c0 4.42 2.865 8.166 6.839 9.489.5.092.682-.217.682-.482 0-.237-.008-.866-.013-1.7-2.782.603-3.369-1.34-3.369-1.34-.454-1.156-1.11-1.462-1.11-1.462-.908-.62.069-.608.069-.608 1.003.07 1.531 1.03 1.531 1.03.892 1.529 2.341 1.087 2.91.831.092-.646.35-1.086.636-1.336-2.22-.253-4.555-1.11-4.555-4.943 0-1.091.39-1.984 1.03-2.682-.103-.253-.447-1.27.098-2.646 0 0 .84-.269 2.75 1.025A9.578 9.578 0 0112 6.836c.85.004 1.705.114 2.504.336 1.909-1.294 2.747-1.025 2.747-1.025.546 1.376.202 2.394.1 2.646.64.699 1.026 1.591 1.026 2.682 0 3.841-2.337 4.687-4.565 4.935.359.309.678.919.678 1.852 0 1.336-.012 2.415-.012 2.743 0 .267.18.578.688.48C19.138 20.161 22 16.416 22 12c0-5.523-4.477-10-10-10z"/></svg>
                <span class="social-text">GitHub</span>
            </a>
            <a href="https://www.linkedin.com/in/shanmukha-chennuboina-7a61073a9/" target="_blank" class="social-link" style="color: #22D3EE">
                <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor"><path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433c-1.144 0-2.063-.926-2.063-2.065 0-1.138.92-2.063 2.063-2.063 1.14 0 2.064.925 2.064 2.063 0 1.139-.925 2.065-2.064 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z"/></svg>
                <span class="social-text">LinkedIn</span>
            </a>
            <a href="https://github.com/shanmukh-dotcom/prof-portfollio-" target="_blank" class="social-link" style="color: #7C3AED">
                <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-1 17.93c-3.95-.49-7-3.85-7-7.93 0-.62.08-1.21.21-1.79L9 15v1c0 1.1.9 2 2 2v1.93zm6.9-2.54c-.26-.81-1-1.39-1.9-1.39h-1v-3c0-.55-.45-1-1-1H8v-2h2c.55 0 1-.45 1-1V7h2c1.1 0 2-.9 2-2v-.41c2.93 1.19 5 4.06 5 7.41 0 2.08-.8 3.97-2.1 5.39z"/></svg>
                <span class="social-text">Portfolio</span>
            </a>
            <a href="mailto:shanmukh.chennuboina@gmail.com" target="_blank" class="social-link" style="color: #22D3EE">
                <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor"><path d="M20 4H4c-1.1 0-1.99.9-1.99 2L2 18c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 4l-8 5-8-5V6l8 5 8-5v2z"/></svg>
                <span class="social-text">Email</span>
            </a>
        </div>
    </div>

    <script src="script.js"></script>
</body>
</html>'''

    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html)

    print("index.html successfully updated")

build_web()
