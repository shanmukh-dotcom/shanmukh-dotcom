document.addEventListener("DOMContentLoaded", () => {
    
    // Boot sequence orchestration
    const bootLogs = [
        "INITIALIZING AI PROFILE...",
        "Loading assets...",
        "Building interface...",
        "Loading portrait...",
        "Rendering components...",
        "Verifying modules...",
        "Establishing connection...",
        "READY"
    ];
    
    const terminal = document.getElementById("boot-terminal");
    const laser = document.getElementById("laser");
    const mainContent = document.getElementById("main-content");
    const glassPanel = document.getElementById("glass-panel");
    const bootOverlay = document.getElementById("boot-overlay");
    const typeWriterBox = document.getElementById("terminal-box");
    
    let logDelay = 500;
    
    bootLogs.forEach((log, index) => {
        setTimeout(() => {
            const p = document.createElement("p");
            p.textContent = log;
            terminal.appendChild(p);
            
            if (index === bootLogs.length - 1) {
                // "READY" appeared
                setTimeout(() => {
                    terminal.style.opacity = "0.2";
                    startLaserScan();
                }, 300);
            }
        }, logDelay);
        logDelay += 300;
    });
    
    function startLaserScan() {
        // Show main content, but hidden via clip-path in CSS initially
        mainContent.classList.add("scanning");
        laser.style.display = "block";
        
        // Laser animates down in CSS
        setTimeout(() => {
            // Scan finished
            laser.style.display = "none";
            bootOverlay.style.display = "none";
            mainContent.classList.remove("scanning");
            mainContent.classList.add("booted");
            
            // Start main typing animation
            typeWriterBox.style.opacity = "1";
            startMainTyping();
            
            createParticles();
        }, 1800); // laser duration 1.8s
    }

    // Main Typing Animation
    function startMainTyping() {
        const typeTarget = document.getElementById("typewriter");
        const roles = ["AI Engineer", "Developer", "Problem Solver", "Open Source Builder"];
        let roleIndex = 0;
        let charIndex = 0;
        let isDeleting = false;

        function type() {
            const currentRole = roles[roleIndex];
            
            if (isDeleting) {
                typeTarget.textContent = currentRole.substring(0, charIndex - 1);
                charIndex--;
            } else {
                typeTarget.textContent = currentRole.substring(0, charIndex + 1);
                charIndex++;
            }

            let typeSpeed = isDeleting ? 50 : 100;

            if (!isDeleting && charIndex === currentRole.length) {
                typeSpeed = 2000;
                isDeleting = true;
            } else if (isDeleting && charIndex === 0) {
                isDeleting = false;
                roleIndex = (roleIndex + 1) % roles.length;
                typeSpeed = 500;
            }

            setTimeout(type, typeSpeed);
        }
        
        type();
    }
    
    function createParticles() {
        const body = document.body;
        for (let i = 0; i < 20; i++) {
            const particle = document.createElement("div");
            particle.className = "cyan-particle";
            particle.style.left = Math.random() * 100 + "vw";
            particle.style.top = Math.random() * 100 + "vh";
            particle.style.animationDelay = Math.random() * 2 + "s";
            body.appendChild(particle);
        }
    }
});