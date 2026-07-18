import base64
import os
import json

def generate_svg():
    bg = "#020617" # Pure black boot background
    panel = "#0B1120"
    border = "rgba(255,255,255,0.08)"
    text_primary = "#F8FAFC"
    text_muted = "#94A3B8"
    accent_1 = "#7C3AED"
    accent_2 = "#8B5CF6"
    accent_3 = "#22D3EE"
    
    width = 1180
    height = 640

    img_path = "assets/hero.png"
    img_href = ""
    if os.path.exists(img_path):
        with open(img_path, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
            img_href = f"data:image/png;base64,{encoded_string}"

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
    
    skill_colors = {
        "Next.js": "#ffffff"
    }

    # Time calculations (Laser starts at 3.5s, ends at 5.3s, covers 710px)
    # Velocity = 710 / 1.8 = 394.4 px/s
    def get_reveal_time(y_pos):
        return 3.5 + (y_pos / 394.4)

    skills_svg = ""
    for i, (skill, color) in enumerate(skills):
        row = 0
        if i < 5:
            row = 0
            col = i
        elif i < 10:
            row = 1
            col = i - 5
        else:
            row = 2
            col = i - 10
            
        x = 510 + (col * 130)
        y = 440 + (row * 45)
        if row == 2:
            x = 510 + (col * 110)

        width_skill = 115
        if skill in ["TailwindCSS", "TensorFlow", "JavaScript", "TypeScript"]: width_skill = 125
        if skill in ["Git", "Linux", "AWS"]: width_skill = 90
        
        icon_path = icon_paths.get(skill, "")
        fill_color = skill_colors.get(skill, color)
        
        reveal_time = get_reveal_time(y)

        skills_svg += f'''
        <g transform="translate({x}, {y})" class="skill" opacity="0">
            <animate attributeName="opacity" values="0;1" dur="0.3s" begin="{reveal_time}s" fill="freeze" />
            <animateTransform attributeName="transform" type="scale" values="0.9;1" dur="0.3s" begin="{reveal_time}s" fill="freeze" additive="sum" />
            <rect width="{width_skill}" height="34" rx="8" fill="transparent" stroke="{border}" stroke-width="1" class="skill-rect" />
            <g transform="translate(12, 9) scale(0.65)">
                <path d="{icon_path}" fill="{fill_color}" />
            </g>
            <text x="36" y="22" font-family="'Inter', sans-serif" font-size="13" font-weight="500" fill="{text_muted}">{skill}</text>
        </g>
        '''

    socials = [
        ("GitHub", "M12 2C6.477 2 2 6.477 2 12c0 4.42 2.865 8.166 6.839 9.489.5.092.682-.217.682-.482 0-.237-.008-.866-.013-1.7-2.782.603-3.369-1.34-3.369-1.34-.454-1.156-1.11-1.462-1.11-1.462-.908-.62.069-.608.069-.608 1.003.07 1.531 1.03 1.531 1.03.892 1.529 2.341 1.087 2.91.831.092-.646.35-1.086.636-1.336-2.22-.253-4.555-1.11-4.555-4.943 0-1.091.39-1.984 1.03-2.682-.103-.253-.447-1.27.098-2.646 0 0 .84-.269 2.75 1.025A9.578 9.578 0 0112 6.836c.85.004 1.705.114 2.504.336 1.909-1.294 2.747-1.025 2.747-1.025.546 1.376.202 2.394.1 2.646.64.699 1.026 1.591 1.026 2.682 0 3.841-2.337 4.687-4.565 4.935.359.309.678.919.678 1.852 0 1.336-.012 2.415-.012 2.743 0 .267.18.578.688.48C19.138 20.161 22 16.416 22 12c0-5.523-4.477-10-10-10z", accent_2, "https://github.com/shanmukh-dotcom"),
        ("LinkedIn", "M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433c-1.144 0-2.063-.926-2.063-2.065 0-1.138.92-2.063 2.063-2.063 1.14 0 2.064.925 2.064 2.063 0 1.139-.925 2.065-2.064 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z", accent_3, "https://www.linkedin.com/in/shanmukha-chennuboina-7a61073a9/"),
        ("Portfolio", "M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-1 17.93c-3.95-.49-7-3.85-7-7.93 0-.62.08-1.21.21-1.79L9 15v1c0 1.1.9 2 2 2v1.93zm6.9-2.54c-.26-.81-1-1.39-1.9-1.39h-1v-3c0-.55-.45-1-1-1H8v-2h2c.55 0 1-.45 1-1V7h2c1.1 0 2-.9 2-2v-.41c2.93 1.19 5 4.06 5 7.41 0 2.08-.8 3.97-2.1 5.39z", accent_1, "https://github.com/shanmukh-dotcom/prof-portfollio-"),
        ("Email", "M20 4H4c-1.1 0-1.99.9-1.99 2L2 18c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 4l-8 5-8-5V6l8 5 8-5v2z", accent_3, "mailto:chennuboinashanmukh2007@gmail.com")
    ]
    
    socials_svg = ""
    for i, (name, path, color, link) in enumerate(socials):
        x = 220 + (i * 220)
        reveal_time = get_reveal_time(660) + (i * 0.15) # Fading upward one by one
        socials_svg += f'''
        <a href="{link}" target="_blank">
            <g transform="translate({x}, 660)" class="social" opacity="0">
                <animate attributeName="opacity" values="0;1" dur="0.4s" begin="{reveal_time}s" fill="freeze" />
                <animateTransform attributeName="transform" type="translate" values="0,10; 0,0" dur="0.4s" begin="{reveal_time}s" fill="freeze" additive="sum" />
                <path d="{path}" fill="{color}" transform="scale(0.8) translate(0, -12)" class="social-icon" />
                <text x="30" y="0" font-family="'Inter', sans-serif" font-size="16" font-weight="500" fill="{text_muted}" class="social-text">{name}</text>
            </g>
        </a>
        '''

    info_rows = [
        ("Location", "Bangalore, India", "M12 2C8.13 2 5 5.13 5 9c0 5.25 7 13 7 13s7-7.75 7-13c0-3.87-3.13-7-7-7zm0 9.5c-1.38 0-2.5-1.12-2.5-2.5s1.12-2.5 2.5-2.5 2.5 1.12 2.5 2.5-1.12 2.5-2.5 2.5z", False),
        ("Education", "Presidency University", "M12 3L1 9l4 2.18v6L12 21l7-3.82v-6l2-1.09V17h2V9L12 3zm6.82 6L12 12.72 5.18 9 12 5.28 18.82 9z", False),
        ("Current Focus", "Building AI-powered products", "M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm0 18c-4.41 0-8-3.59-8-8s3.59-8 8-8 8 3.59 8 8-3.59 8-8 8zm0-14c-3.31 0-6 2.69-6 6s2.69 6 6 6 6-2.69 6-6-2.69-6-6-6zm0 10c-2.21 0-4-1.79-4-4s1.79-4 4-4 4 1.79 4 4-1.79 4-4 4zm0-6c-1.1 0-2 .9-2 2s.9 2 2 2 2-.9 2-2-.9-2-2-2z", False),
        ("Building", "Smart Campus Buddy, Career Forge &amp; more", "M22.7 19l-9.1-9.1c.9-2.3.4-5-1.5-6.9-2-2-5-2.4-7.4-1.3L9 6 6 9 1.6 4.7C.5 7.1.9 10.1 2.9 12.1c1.9 1.9 4.6 2.4 6.9 1.5l9.1 9.1c.4.4 1 .4 1.4 0l2.3-2.3c.5-.4.5-1.1.1-1.4z", False),
        ("Portfolio", "shanmukhchennuboina.dev", "M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-1 17.93c-3.95-.49-7-3.85-7-7.93 0-.62.08-1.21.21-1.79L9 15v1c0 1.1.9 2 2 2v1.93zm6.9-2.54c-.26-.81-1-1.39-1.9-1.39h-1v-3c0-.55-.45-1-1-1H8v-2h2c.55 0 1-.45 1-1V7h2c1.1 0 2-.9 2-2v-.41c2.93 1.19 5 4.06 5 7.41 0 2.08-.8 3.97-2.1 5.39z", True),
        ("Email", "shanmukh.chennuboina@gmail.com", "M20 4H4c-1.1 0-1.99.9-1.99 2L2 18c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 4l-8 5-8-5V6l8 5 8-5v2z", False)
    ]
    
    info_svg = ""
    for i, (label, val, path, highlight) in enumerate(info_rows):
        y_pos = i * 32
        info_reveal_time = get_reveal_time(140 + y_pos) + (i * 0.12)
        val_color = accent_2 if highlight else text_muted
        info_svg += f'''
        <g transform="translate(0, {y_pos})" opacity="0">
            <animate attributeName="opacity" values="0;1" dur="0.3s" begin="{info_reveal_time}s" fill="freeze" />
            <path d="{path}" fill="{text_muted}" opacity="0.8" transform="scale(0.8) translate(0, -12)"/>
            <text x="25" y="0" font-size="14" fill="{text_muted}">{label}</text>
            <text x="160" y="0" font-size="14" font-weight="500" fill="{val_color}">{val}</text>
        </g>
        '''

    boot_logs = [
        "INITIALIZING AI PROFILE...",
        "Loading assets...",
        "Building interface...",
        "Loading portrait...",
        "Rendering components...",
        "Verifying modules...",
        "Establishing connection...",
        "READY"
    ]
    
    boot_svg = ""
    for i, log in enumerate(boot_logs):
        t = 0.5 + (i * 0.3)
        boot_svg += f'''
        <text x="40" y="{40 + i * 25}" font-family="monospace" font-size="14" fill="#22D3EE" opacity="0">
            {log}
            <animate attributeName="opacity" values="0;1;1;0.2" keyTimes="0;0.1;0.9;1" dur="{3.5 - t}s" begin="{t}s" fill="freeze" />
        </text>
        '''

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height + 70}" width="{width}" height="{height + 70}">
    <defs>
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&amp;display=swap');
            text {{ font-family: 'Inter', -apple-system, sans-serif; }}
            .social {{ cursor: pointer; }}
            .social:hover .social-icon, .social:hover .social-text {{ fill: {accent_2}; filter: drop-shadow(0 0 5px {accent_2}); transition: all 0.3s; }}
            .skill {{ cursor: pointer; }}
            .skill:hover .skill-rect {{ stroke: {accent_2}; fill: rgba(255,255,255,0.03); transition: all 0.3s; }}
        </style>
        
        <linearGradient id="gradientName" x1="0%" y1="0%" x2="100%" y2="0%">
            <stop offset="0%" stop-color="{accent_1}" />
            <stop offset="50%" stop-color="{accent_2}" />
            <stop offset="100%" stop-color="{accent_3}" />
            <animate attributeName="x1" values="-100%;100%" dur="18s" repeatCount="indefinite" />
            <animate attributeName="x2" values="0%;200%" dur="18s" repeatCount="indefinite" />
        </linearGradient>

        <linearGradient id="borderShimmer" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" stop-color="transparent" />
            <stop offset="50%" stop-color="rgba(255,255,255,0.15)" />
            <stop offset="100%" stop-color="transparent" />
        </linearGradient>
        
        <clipPath id="panelClip">
            <rect width="1180" height="600" rx="24" />
        </clipPath>
        
        <clipPath id="laserReveal">
            <rect x="0" y="0" width="{width}" height="0">
                <animate attributeName="height" values="0;710" dur="1.8s" begin="3.5s" fill="freeze" />
            </rect>
        </clipPath>
        
        <filter id="cyanGlow" x="-20%" y="-20%" width="140%" height="140%">
            <feGaussianBlur stdDeviation="4" result="blur" />
            <feMerge>
                <feMergeNode in="blur" />
                <feMergeNode in="SourceGraphic" />
            </feMerge>
        </filter>
        
        <filter id="portraitBlur">
            <feGaussianBlur stdDeviation="10">
                <animate attributeName="stdDeviation" values="10;0" dur="1s" begin="3.8s" fill="freeze" />
            </feGaussianBlur>
        </filter>
    </defs>

    <!-- Base Canvas Background -->
    <rect width="{width}" height="{height + 70}" fill="{bg}" />
    
    <!-- Boot Sequence Terminal -->
    <g>
        {boot_svg}
        <!-- Blinking cursor -->
        <rect x="0" y="0" width="8" height="15" fill="#22D3EE" opacity="0">
            <animate attributeName="opacity" values="0;1;0" dur="0.8s" repeatCount="indefinite" />
            <animate attributeName="x" values="240;165;210;200;225;210;250;90" keyTimes="0;0.125;0.25;0.375;0.5;0.625;0.75;1" dur="2.4s" begin="0.5s" fill="freeze" />
            <animate attributeName="y" values="30;55;80;105;130;155;180;205" keyTimes="0;0.125;0.25;0.375;0.5;0.625;0.75;1" dur="2.4s" begin="0.5s" fill="freeze" />
            <animate attributeName="opacity" values="1;0" dur="0.1s" begin="3.5s" fill="freeze" />
        </rect>
    </g>

    <!-- The Revealed UI -->
    <g clip-path="url(#laserReveal)">
        <!-- Glassmorphism Panel -->
        <g transform="translate(0, 10)">
            <rect width="1180" height="600" rx="24" fill="{panel}" stroke="{accent_1}" stroke-width="1" stroke-opacity="0.5" />
            
            <!-- Border Shimmer -->
            <rect width="1180" height="600" rx="24" fill="transparent" stroke="url(#borderShimmer)" stroke-width="1.5">
                <animate attributeName="stroke-dasharray" values="0 4000; 4000 0" dur="15s" repeatCount="indefinite" />
            </rect>
            
            <g clip-path="url(#panelClip)">
                <!-- Left Panel Boundary -->
                <g>
                    <g filter="url(#portraitBlur)">
                        <animateTransform attributeName="transform" type="translate" values="0,0; 0,-5; 0,0" dur="15s" repeatCount="indefinite" />
                        <image href="{img_href}" x="-20" y="-20" width="510" height="640" preserveAspectRatio="xMidYMid slice" />
                    </g>
                    <line x1="472" y1="0" x2="472" y2="600" stroke="{border}" stroke-width="1" />
                </g>

                <!-- Text Content -->
                <g transform="translate(510, 50)">
                    <text x="0" y="0" font-size="22" font-weight="600" fill="{text_primary}" opacity="0">
                        Hi there 👋
                        <animate attributeName="opacity" values="0;1" dur="0.4s" begin="{get_reveal_time(50)}s" fill="freeze" />
                    </text>
                    
                    <g opacity="0">
                        <animate attributeName="opacity" values="0;1" dur="0.6s" begin="{get_reveal_time(100)}s" fill="freeze" />
                        <animateTransform attributeName="transform" type="translate" values="0,8; 0,0" dur="0.6s" begin="{get_reveal_time(100)}s" fill="freeze" />
                        <text x="0" y="50" font-size="52" font-weight="800" fill="url(#textGradient)">I'm Shanmukh</text>
                        <text x="0" y="50" font-size="52" font-weight="800" fill="white" opacity="0.8">I'm </text>
                    </g>
                    
                    <!-- Animated Typewriter with Border Box (starts after laser scan finishes ~ 5.3s) -->
                    <g opacity="0">
                        <animate attributeName="opacity" values="0;1" dur="0.2s" begin="5.5s" fill="freeze" />
                        <rect x="0" y="75" width="480" height="36" rx="6" fill="transparent" stroke="{border}" stroke-width="1.5" />
                        <text x="15" y="98" font-family="monospace" font-size="16" fill="{text_muted}">
                            &gt; 
                            <tspan fill="{accent_2}">
                                <animate attributeName="opacity" values="0;1" dur="0.1s" begin="5.8s" fill="freeze" />
                                AI Engineer | Developer | Problem Solver 
                            </tspan>
                            <tspan fill="{accent_2}">
                                <animate attributeName="opacity" values="1;0;1" dur="0.8s" repeatCount="indefinite" />
                                █
                            </tspan>
                        </text>
                    </g>
                    
                    <!-- Info Grid -->
                    <g transform="translate(0, 140)">
                        {info_svg}
                    </g>
                    
                    <text x="0" y="345" font-size="13" font-weight="500" fill="{text_muted}" opacity="0">
                        Skills &amp; Technologies
                        <animate attributeName="opacity" values="0;1" dur="0.3s" begin="{get_reveal_time(345)}s" fill="freeze" />
                    </text>
                </g>
                
                {skills_svg}
            </g>
        </g>

        {socials_svg}
    </g>

    <!-- The Laser -->
    <rect x="0" y="0" width="{width}" height="2" fill="#22D3EE" filter="url(#cyanGlow)" opacity="0">
        <animate attributeName="opacity" values="0;1;1;0" keyTimes="0;0.05;0.95;1" dur="1.9s" begin="3.5s" fill="freeze" />
        <animate attributeName="y" values="0;710" dur="1.8s" begin="3.5s" fill="freeze" />
    </rect>
    
</svg>'''
    
    with open("assets/background.svg", "w", encoding="utf-8") as f:
        f.write(svg)

generate_svg()
print("Generated assets/background.svg successfully")
