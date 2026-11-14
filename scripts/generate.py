"""Generate Sierra Byrd's Paper Signal profile artwork from a small JSON config."""
from __future__ import annotations
import argparse
import json
import os
import urllib.request
from pathlib import Path
from xml.sax.saxutils import escape

ROOT = Path(__file__).resolve().parent.parent
ASSETS = ROOT / "assets"
PAPER, INK, BLUE, CORAL, LIME, MUTED = "#f3eedf", "#171717", "#2348f5", "#ff6559", "#c8ef54", "#6d685f"
DEMO = {"public_repos": 0, "followers": 0, "stars": 0, "repos": []}


def config() -> dict:
    return json.loads((ROOT / "config.json").read_text(encoding="utf-8"))


def api(url: str) -> object:
    headers = {"Accept": "application/vnd.github+json", "User-Agent": "sierra-profile"}
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        headers["Authorization"] = f"Bearer {token}"
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, timeout=25) as response:
        import json as json_module
        return json_module.load(response)


def collect(username: str, featured: list[str]) -> dict:
    user = api(f"https://api.github.com/users/{username}")
    repos = api(f"https://api.github.com/users/{username}/repos?per_page=100&sort=updated")
    if not isinstance(user, dict) or not isinstance(repos, list):
        raise RuntimeError("Unexpected response from GitHub")
    originals = [r for r in repos if not r.get("fork")]
    names = {r.get("name", "").lower(): r for r in originals}
    missing = [name for name in featured if name.lower() not in names]
    if missing:
        raise RuntimeError("Featured public repositories not found: " + ", ".join(missing))
    selected = [names[name.lower()] for name in featured]
    return {"public_repos": user.get("public_repos", len(repos)), "followers": user.get("followers", 0),
            "stars": sum(r.get("stargazers_count", 0) for r in originals), "repos": selected}


def short(value: object, size: int) -> str:
    text = " ".join(str(value or "").split())
    return text if len(text) <= size else text[:size - 1].rstrip() + "…"


def styles() -> str:
    # Keep all profile artwork fully legible in GitHub's static SVG renderer.
    return f""".serif{{font-family:Georgia,'Times New Roman',serif;fill:{INK}}}.sans{{font-family:'Trebuchet MS',Arial,sans-serif;fill:{INK}}}.mono{{font-family:ui-monospace,Consolas,monospace;fill:{MUTED}}}.caps{{font-size:10px;font-weight:700;letter-spacing:2px}}"""


def cover_svg(cfg: dict) -> str:
    service_nodes = []
    for i, service in enumerate(cfg["services"][:4]):
        x = 49 + (i % 2) * 215
        y = 265 + (i // 2) * 32
        color = BLUE if i % 2 == 0 else CORAL
        service_nodes.append(f'<text x="{x}" y="{y}" class="sans" font-size="11" font-weight="700"><tspan fill="{color}">0{i+1}.</tspan> {escape(service)}</text>')
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="900" height="340" viewBox="0 0 900 340" role="img" aria-label="Sierra Byrd, full-stack software engineer">
<defs><style>{styles()}</style><pattern id="grain" width="17" height="17" patternUnits="userSpaceOnUse"><circle cx="2" cy="4" r=".45" fill="{INK}" opacity=".14"/><circle cx="12" cy="13" r=".35" fill="{INK}" opacity=".1"/></pattern></defs>
<rect width="900" height="340" rx="5" fill="{PAPER}"/><rect width="900" height="340" rx="5" fill="url(#grain)"/><path d="M25 39h850M25 315h850" stroke="{INK}" stroke-width="1.4"/>
<text x="26" y="27" class="sans caps">INDEPENDENT ENGINEERING PROFILE</text><text x="874" y="27" text-anchor="end" class="sans caps">SELECTED WORK / @{escape(cfg['username'].upper())}</text>
<g class="intro"><text x="39" y="111" class="serif" font-size="70" font-weight="700" letter-spacing="-4">{escape(cfg['name'])}</text><rect x="42" y="129" width="420" height="8" fill="{BLUE}" class="wipe"/><text x="42" y="169" class="sans" font-size="15" font-weight="700">{escape(cfg['role'])}</text><text x="42" y="199" class="serif" font-size="18" font-style="italic">“{escape(short(cfg['statement'], 58))}”</text><text x="42" y="230" class="mono" font-size="11">{escape(cfg['location'])}  /  {escape(cfg['website'])}</text>{''.join(service_nodes)}</g>
<path d="M548 71h309v225H548z" fill="{INK}"/><path d="M571 94h263v179H571z" fill="{CORAL}"/>
<g class="mark"><circle cx="703" cy="184" r="72" fill="{LIME}"/><path d="M648 188c31-72 78-76 111-12M647 201c30 32 75 39 112 4" fill="none" stroke="{INK}" stroke-width="8" stroke-linecap="round"/><text x="703" y="201" text-anchor="middle" class="serif" font-size="58" font-weight="700">{escape(cfg['monogram'])}</text></g>
<text x="703" y="290" text-anchor="middle" class="sans caps" font-size="9" fill="{PAPER}"><tspan fill="{PAPER}">PRODUCT / SYSTEMS / EXPERIENCE</tspan></text>
<rect x="744" y="56" width="96" height="25" rx="13" fill="{BLUE}"/><text x="792" y="73" text-anchor="middle" class="sans caps" font-size="8" fill="{PAPER}"><tspan fill="{PAPER}">WORK</tspan></text>
</svg>'''


def folio_svg(cfg: dict) -> str:
    projects = cfg.get("projects", [])[:3]
    palette = [BLUE, CORAL, LIME]
    project_nodes = []
    for i, project in enumerate(projects):
        y = 150 + i * 88
        color = palette[i]
        project_nodes.append(f'''<g class="intro" style="animation-delay:{.1+i*.1:.2f}s"><text x="40" y="{y}" class="serif" font-size="25" font-weight="700">0{i+1}</text><rect x="88" y="{y-22}" width="5" height="34" fill="{color}"/><text x="110" y="{y-4}" class="sans" font-size="14" font-weight="700">{escape(short(project.get('name'), 25))}</text><text x="110" y="{y+18}" class="mono" font-size="9">{escape(short(project.get('description'), 42))}</text><text x="476" y="{y+18}" text-anchor="end" class="mono" font-size="8">{escape(short(project.get('label'), 23))}</text></g>''')
    practices = [
        ("PRODUCT ENGINEERING", "Full-stack apps, APIs, auth and data"),
        ("BUSINESS SYSTEMS", "CRM, lead intelligence and automation"),
        ("COMMERCE & UX", "Storefronts, 3D and product experiences"),
        ("QUALITY & DELIVERY", "Testing, accessibility and deployment"),
    ]
    practice_nodes = []
    for i, (heading, detail) in enumerate(practices):
        y = 112 + i * 67
        practice_nodes.append(f'<text x="550" y="{y}" class="sans caps" fill="{LIME}"><tspan fill="{LIME}">0{i+1} / {escape(heading)}</tspan></text><text x="550" y="{y+22}" class="mono" font-size="10" fill="{PAPER}"><tspan fill="{PAPER}">{escape(detail)}</tspan></text>')
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="900" height="460" viewBox="0 0 900 460" role="img" aria-label="Selected engineering work and technical focus">
<defs><style>{styles()}</style><pattern id="dots" width="13" height="13" patternUnits="userSpaceOnUse"><circle cx="2" cy="2" r="1" fill="{INK}" opacity=".16"/></pattern></defs>
<rect width="900" height="460" rx="5" fill="{PAPER}"/><rect x="515" width="385" height="460" fill="{INK}"/><rect x="515" width="385" height="460" fill="url(#dots)" opacity=".6"/>
<text x="39" y="47" class="sans caps">01 / SELECTED ENGINEERING</text><text x="476" y="47" text-anchor="end" class="mono" font-size="10">PRIVATE PRODUCT BUILDS</text><line x1="39" y1="62" x2="476" y2="62" stroke="{INK}"/>
<text x="39" y="105" class="serif" font-size="34" font-weight="700">Flagship products.</text>{''.join(project_nodes)}
<text x="548" y="47" class="sans caps" fill="{LIME}"><tspan fill="{LIME}">02 / ENGINEERING PRACTICE</tspan></text><line x1="548" y1="62" x2="829" y2="62" stroke="{LIME}"/>{''.join(practice_nodes)}
<rect x="548" y="385" width="281" height="42" fill="{LIME}"/><text x="564" y="403" class="sans caps">PRIVATE PRODUCT BUILDS</text><text x="564" y="419" class="sans" font-size="11" font-weight="700">Recover Revenue  ·  NextRole</text>
<text x="39" y="433" class="mono" font-size="9">Private systems are documented separately; source code and credentials stay private.</text>
</svg>'''


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--demo", action="store_true", help="offline generation using configured copy")
    args = parser.parse_args()
    cfg = config()
    username = os.environ.get("GH_USERNAME") or os.environ.get("GITHUB_REPOSITORY_OWNER") or cfg["username"]
    cfg["username"] = username
    if not args.demo:
        collect(username, cfg.get("featured_repos", []))
    ASSETS.mkdir(exist_ok=True)
    (ASSETS / "cover.svg").write_text(cover_svg(cfg), encoding="utf-8")
    (ASSETS / "folio.svg").write_text(folio_svg(cfg), encoding="utf-8")
    print(f"Generated Paper Signal assets for @{username}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
