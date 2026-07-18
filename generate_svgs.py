import os
import base64

def generate_svg(mode="dark"):
    if mode == "dark":
        bg = "#030303"
        panel_bg = "#09090b"
        border = "#27272a"
        text_primary = "#ffffff"
        text_secondary = "#a1a1aa"
        text_accent = "#a855f7" # Purple
        text_accent_2 = "#8b5cf6"
        icon_color = "#a1a1aa"
        skill_border = "#27272a"
        skill_bg = "#09090b"
    else:
        bg = "#ffffff"
        panel_bg = "#f4f4f5"
        border = "#e4e4e7"
        text_primary = "#09090b"
        text_secondary = "#52525b"
        text_accent = "#9333ea"
        text_accent_2 = "#7e22ce"
        icon_color = "#52525b"
        skill_border = "#e4e4e7"
        skill_bg = "#ffffff"

    img_path = "gitpic.png"
    if os.path.exists(img_path):
        with open(img_path, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
            img_href = f"data:image/png;base64,{encoded_string}"
    else:
        img_href = "https://via.placeholder.com/400x500/09090b/a855f7?text=Your+Portrait+Image"

    # SVG canvas dimensions
    width = 1180
    height = 680

    code_snippet_left = [
        "function build() {",
        "  while (learning) {",
        "    grow();",
        "    build();",
        "    inspire();",
        "  }",
        "}",
        "",
        "const vision = ",
        '  "impact through code";',
        "",
        "let's create //",
        "  something ",
        "  meaningful;"
    ]

    code_lines_svg = ""
    for i, line in enumerate(code_snippet_left):
        line = line.replace(" ", "&#160;")
        code_lines_svg += f'<text x="40" y="{120 + i*18}" font-family="monospace" font-size="12" fill="{text_secondary}" opacity="0.3">{line}</text>\n'

    info_items = [
        ("Location", "Bangalore, India", "M12 2C8.13 2 5 5.13 5 9c0 5.25 7 13 7 13s7-7.75 7-13c0-3.87-3.13-7-7-7zm0 9.5c-1.38 0-2.5-1.12-2.5-2.5s1.12-2.5 2.5-2.5 2.5 1.12 2.5 2.5-1.12 2.5-2.5 2.5z"),
        ("Education", "Presidency University", "M12 3L1 9l4 2.18v6L12 21l7-3.82v-6l2-1.09V17h2V9L12 3zm6.82 6L12 12.72 5.18 9 12 5.28 18.82 9zM17 15.99l-5 2.73-5-2.73v-3.72L12 15l5-2.73v3.72z"),
        ("Current Focus", "Building AI-powered products", "M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm0 18c-4.41 0-8-3.59-8-8s3.59-8 8-8 8 3.59 8 8-3.59 8-8 8zm0-14c-3.31 0-6 2.69-6 6s2.69 6 6 6 6-2.69 6-6-2.69-6-6-6zm0 10c-2.21 0-4-1.79-4-4s1.79-4 4-4 4 1.79 4 4-1.79 4-4 4zm0-6c-1.1 0-2 .9-2 2s.9 2 2 2 2-.9 2-2-.9-2-2-2z"),
        ("Building", "Smart Campus Buddy, Career Forge & more", "M22.7 19l-9.1-9.1c.9-2.3.4-5-1.5-6.9-2-2-5-2.4-7.4-1.3L9 6 6 9 1.6 4.7C.5 7.1.9 10.1 2.9 12.1c1.9 1.9 4.6 2.4 6.9 1.5l9.1 9.1c.4.4 1 .4 1.4 0l2.3-2.3c.5-.4.5-1.1.1-1.4z"),
        ("Portfolio", "shanmukhchennuboina.dev", "M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-1 17.93c-3.95-.49-7-3.85-7-7.93 0-.62.08-1.21.21-1.79L9 15v1c0 1.1.9 2 2 2v1.93zm6.9-2.54c-.26-.81-1-1.39-1.9-1.39h-1v-3c0-.55-.45-1-1-1H8v-2h2c.55 0 1-.45 1-1V7h2c1.1 0 2-.9 2-2v-.41c2.93 1.19 5 4.06 5 7.41 0 2.08-.8 3.97-2.1 5.39z"),
        ("Email", "shanmukh.chennuboina@gmail.com", "M20 4H4c-1.1 0-1.99.9-1.99 2L2 18c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 4l-8 5-8-5V6l8 5 8-5v2z")
    ]

    info_svg = ""
    for i, (label, val, path) in enumerate(info_items):
        y = 230 + (i * 32)
        val_color = text_accent_2 if label == "Portfolio" else text_primary
        info_svg += f'''
        <g transform="translate(540, {y})">
            <path d="{path}" fill="{icon_color}" transform="scale(0.8) translate(0, -12)" />
            <text x="30" y="0" font-family="'Inter', sans-serif" font-size="14" fill="{text_secondary}">{label}</text>
            <text x="200" y="0" font-family="'Inter', sans-serif" font-size="14" font-weight="500" fill="{val_color}">{val}</text>
        </g>
        '''

    skills = [
        ("Python", "#3776AB"), ("C++", "#00599C"), ("JavaScript", "#F7DF1E"), ("TypeScript", "#3178C6"), ("FastAPI", "#009688"),
        ("React", "#61DAFB"), ("Next.js", "#ffffff" if mode=="dark" else "#000000"), ("Node.js", "#339933"), ("TailwindCSS", "#06B6D4"), ("Supabase", "#3ECF8E"),
        ("TensorFlow", "#FF6F00"), ("PyTorch", "#EE4C2C"), ("Docker", "#2496ED"), ("AWS", "#FF9900"), ("Git", "#F05032"), ("Linux", "#FCC624")
    ]
    
    skills_svg = ""
    row_gap = 42
    col_gap = 120
    for i, (skill, color) in enumerate(skills):
        row = i // 5
        col = i % 5
        x = 540 + (col * col_gap)
        y = 480 + (row * row_gap)
        width_skill = 105
        if len(skill) > 9: width_skill = 120
        if col == 4: x = 540 + (3 * col_gap) + 130 # Adjust last column
        
        skills_svg += f'''
        <g transform="translate({x}, {y})">
            <rect width="{width_skill}" height="32" rx="16" fill="{skill_bg}" stroke="{skill_border}" stroke-width="1" />
            <circle cx="16" cy="16" r="4" fill="{color}" />
            <text x="30" y="21" font-family="'Inter', sans-serif" font-size="13" font-weight="500" fill="{text_secondary}">{skill}</text>
        </g>
        '''

    socials = [
        ("GitHub", "M12 2C6.477 2 2 6.477 2 12c0 4.42 2.865 8.166 6.839 9.489.5.092.682-.217.682-.482 0-.237-.008-.866-.013-1.7-2.782.603-3.369-1.34-3.369-1.34-.454-1.156-1.11-1.462-1.11-1.462-.908-.62.069-.608.069-.608 1.003.07 1.531 1.03 1.531 1.03.892 1.529 2.341 1.087 2.91.831.092-.646.35-1.086.636-1.336-2.22-.253-4.555-1.11-4.555-4.943 0-1.091.39-1.984 1.03-2.682-.103-.253-.447-1.27.098-2.646 0 0 .84-.269 2.75 1.025A9.578 9.578 0 0112 6.836c.85.004 1.705.114 2.504.336 1.909-1.294 2.747-1.025 2.747-1.025.546 1.376.202 2.394.1 2.646.64.699 1.026 1.591 1.026 2.682 0 3.841-2.337 4.687-4.565 4.935.359.309.678.919.678 1.852 0 1.336-.012 2.415-.012 2.743 0 .267.18.578.688.48C19.138 20.161 22 16.416 22 12c0-5.523-4.477-10-10-10z"),
        ("LinkedIn", "M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433c-1.144 0-2.063-.926-2.063-2.065 0-1.138.92-2.063 2.063-2.063 1.14 0 2.064.925 2.064 2.063 0 1.139-.925 2.065-2.064 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z"),
        ("Portfolio", "M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-1 17.93c-3.95-.49-7-3.85-7-7.93 0-.62.08-1.21.21-1.79L9 15v1c0 1.1.9 2 2 2v1.93zm6.9-2.54c-.26-.81-1-1.39-1.9-1.39h-1v-3c0-.55-.45-1-1-1H8v-2h2c.55 0 1-.45 1-1V7h2c1.1 0 2-.9 2-2v-.41c2.93 1.19 5 4.06 5 7.41 0 2.08-.8 3.97-2.1 5.39z"),
        ("Email", "M20 4H4c-1.1 0-1.99.9-1.99 2L2 18c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 4l-8 5-8-5V6l8 5 8-5v2z")
    ]
    
    socials_svg = ""
    for i, (name, path) in enumerate(socials):
        x = 200 + (i * 220)
        socials_svg += f'''
        <g transform="translate({x}, 640)" style="cursor:pointer;">
            <path d="{path}" fill="{text_accent}" transform="scale(0.8) translate(0, -12)" />
            <text x="30" y="0" font-family="'Inter', sans-serif" font-size="14" font-weight="500" fill="{text_secondary}">{name}</text>
        </g>
        '''

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}">
    <defs>
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&amp;display=swap');
            text {{ font-family: 'Inter', -apple-system, sans-serif; }}
        </style>
        
        <linearGradient id="purpleGradient" x1="0%" y1="0%" x2="100%" y2="0%">
            <stop offset="0%" stop-color="{text_accent}" />
            <stop offset="100%" stop-color="{text_accent_2}" />
        </linearGradient>

        <radialGradient id="portraitGlow" cx="50%" cy="50%" r="50%">
            <stop offset="0%" stop-color="{text_accent}" stop-opacity="0.3" />
            <stop offset="100%" stop-color="transparent" />
        </radialGradient>
        
        <clipPath id="panelClip">
            <rect width="1170" height="600" rx="16" />
        </clipPath>
    </defs>

    <!-- Base Background -->
    <rect width="{width}" height="{height}" fill="{bg}" />
    
    <!-- Main Panel -->
    <g transform="translate(5, 5)">
        <rect width="1170" height="600" rx="16" fill="{panel_bg}" stroke="{border}" stroke-width="1.5" />
        
        <g clip-path="url(#panelClip)">
            <!-- Left Side Glow & Code -->
            <circle cx="250" cy="300" r="300" fill="url(#portraitGlow)" />
            {code_lines_svg}
            
            <!-- Window Controls -->
            <g transform="translate(25, 25)">
                <circle cx="0" cy="0" r="6" fill="#FF5F56" />
                <circle cx="20" cy="0" r="6" fill="#FFBD2E" />
                <circle cx="40" cy="0" r="6" fill="#27C93F" />
            </g>

            <!-- Floating Japanese Text -->
            <text x="250" y="520" text-anchor="middle" font-size="20" font-weight="600" fill="{text_accent}" opacity="0.8" letter-spacing="4">未来をコードする</text>
            <text x="250" y="540" text-anchor="middle" font-size="12" font-weight="500" fill="{text_secondary}" opacity="0.6" letter-spacing="6">CODE THE FUTURE</text>
            
            <!-- Portrait Image -->
            <image href="{img_href}" x="30" y="0" width="450" height="550" preserveAspectRatio="xMidYMid slice" opacity="0.9" />

            <!-- Floating brackets -->
            <text x="440" y="100" font-family="monospace" font-size="24" fill="{text_accent}" opacity="0.5">&lt;/&gt;</text>
            <text x="380" y="400" font-family="monospace" font-size="24" fill="{text_accent}" opacity="0.5">&lt;!&gt;</text>
            
            <!-- Divider Line -->
            <line x1="500" y1="50" x2="500" y2="550" stroke="{border}" stroke-width="1" />

            <!-- Right Side Content -->
            <!-- Greeting -->
            <text x="540" y="80" font-size="24" font-weight="600" fill="{text_primary}">Hi there 👋</text>
            
            <!-- Name -->
            <text x="540" y="130" font-size="48" font-weight="800" fill="{text_primary}">I'm <tspan fill="url(#purpleGradient)">Shanmukh</tspan></text>
            
            <!-- Roles Terminal -->
            <text x="540" y="175" font-family="monospace" font-size="16" fill="{text_secondary}">
                &gt; <tspan fill="{text_accent}">AI Engineer</tspan> | Developer | Problem Solver <tspan fill="{text_accent}">█</tspan>
            </text>
            
            <!-- Info List -->
            {info_svg}

            <!-- Skills Section -->
            <text x="540" y="450" font-size="14" font-weight="600" fill="{text_secondary}">Skills &amp; Technologies</text>
            {skills_svg}
        </g>
    </g>

    <!-- Footer Social Links -->
    {socials_svg}

</svg>'''
    
    with open(f"readme_{mode}.svg", "w", encoding="utf-8") as f:
        f.write(svg)

generate_svg("dark")
print("Generated exactly matching SVG layout as readme_dark.svg")
