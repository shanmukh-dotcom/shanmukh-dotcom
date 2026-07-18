import urllib.request
import json
import re

slugs = {
    "Python": "python",
    "C++": "cplusplus",
    "JavaScript": "javascript",
    "TypeScript": "typescript",
    "FastAPI": "fastapi",
    "React": "react",
    "Next.js": "nextdotjs",
    "Node.js": "nodedotjs",
    "TailwindCSS": "tailwindcss",
    "Supabase": "supabase",
    "TensorFlow": "tensorflow",
    "PyTorch": "pytorch",
    "Docker": "docker",
    "AWS": "amazonaws",
    "Git": "git",
    "Linux": "linux"
}

icon_paths = {}

for name, slug in slugs.items():
    url = f"https://raw.githubusercontent.com/simple-icons/simple-icons/develop/icons/{slug}.svg"
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response:
            svg_content = response.read().decode('utf-8')
            # Extract path d="..."
            match = re.search(r'<path[^>]*d="([^"]+)"', svg_content)
            if match:
                icon_paths[name] = match.group(1)
            else:
                print(f"No path found for {name}")
    except Exception as e:
        print(f"Failed to fetch {name}: {e}")

with open("icon_paths.json", "w") as f:
    json.dump(icon_paths, f, indent=4)

print("Icons fetched successfully.")
