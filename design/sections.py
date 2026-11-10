"""Generates the principle chips and the toolbox/certifications panel (dark + light), animated, no external resources."""
import pathlib
OUT = pathlib.Path(__file__).resolve().parent.parent / "assets"
FONT = "ui-sans-serif,-apple-system,BlinkMacSystemFont,'Segoe UI',Inter,Helvetica,Arial,sans-serif"
MONO = "ui-monospace,'SF Mono',SFMono-Regular,Menlo,Consolas,monospace"
TH = {
  "dark": dict(bg1="#060a14", bg2="#0d1530", border="#1f2a44", chip="#101a33", chipb="#2a3757", text="#e9eef8", sub="#8e9ab5", accent="#FF9900", green="#30D158", gray="#5b6782"),
  "light": dict(bg1="#f7f9fc", bg2="#eef2f9", border="#d5dcea", chip="#ffffff", chipb="#d0d8e8", text="#0b1220", sub="#56627c", accent="#C25E00", green="#1f9d47", gray="#8a95ad"),
}
ICONS = {  # 22px, centered at 0,0, stroked
  "lock": '<rect x="-8" y="-2" width="16" height="12" rx="3"/><path d="M-5 -2 V-6 a5 5 0 0 1 10 0 V-2"/>',
  "shield": '<path d="M0 -11 L9 -7 V0 C9 6 5 10 0 12 C-5 10 -9 6 -9 0 V-7 Z"/><path d="M-4 0 L4 0"/>',
  "eye": '<path d="M-11 0 C-7 -7 7 -7 11 0 C7 7 -7 7 -11 0 Z"/><circle cx="0" cy="0" r="3"/>',
  "home": '<path d="M-10 -1 L0 -10 L10 -1"/><path d="M-7 -3 V9 H7 V-3"/>',
}

def chips(t):
    c = TH[t]; W, H = 1200, 120
    items = [("lock", "LEAST PRIVILEGE", "one model, nothing else"), ("shield", "FAIL CLOSED", "unknown means no"),
             ("eye", "AI OUTPUT IS UNTRUSTED", "every claim is checked"), ("home", "DATA STAYS HOME", "the AI never sees a salary")]
    cw, gap = 276, 16; x0 = (W - (4 * cw + 3 * gap)) / 2
    g = ""
    for i, (ic, title, sub) in enumerate(items):
        x = x0 + i * (cw + gap)
        g += f'''<g transform="translate({x} 22)">
  <rect width="{cw}" height="76" rx="18" class="chip"/>
  <rect width="{cw}" height="76" rx="18" class="lit" style="animation-delay:{i*0.9:.1f}s"/>
  <g transform="translate(34 38)" class="ic" style="animation-delay:{i*0.9:.1f}s">{ICONS[ic]}</g>
  <text x="62" y="35" class="tt">{title}</text><text x="62" y="56" class="ss">{sub}</text></g>'''
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-label="Least privilege. Fail closed. AI output is untrusted. Data stays home.">
<style>
.chip{{fill:{c['chip']};stroke:{c['chipb']};stroke-width:1.2}}
.lit{{fill:none;stroke:{c['accent']};stroke-width:1.6;opacity:0;animation:lit 3.6s ease-in-out infinite}}
.ic{{fill:none;stroke:{c['sub']};stroke-width:1.8;stroke-linecap:round;stroke-linejoin:round;animation:ic 3.6s ease-in-out infinite}}
.tt{{font:700 13px {MONO};letter-spacing:.12em;fill:{c['text']}}}
.ss{{font:400 13px {FONT};fill:{c['sub']}}}
@keyframes lit{{0%,100%{{opacity:0}}12%,30%{{opacity:1}}45%{{opacity:0}}}}
@keyframes ic{{0%,100%{{stroke:{c['sub']}}}12%,30%{{stroke:{c['accent']}}}45%{{stroke:{c['sub']}}}}}
@media (prefers-reduced-motion:reduce){{*{{animation:none!important}}}}
</style>{g}</svg>'''

def stack(t):
    c = TH[t]; W = 1200
    rows = [("WORKING WITH", ["Python", "TypeScript", "React", "AWS", "Amazon Bedrock", "AWS Lambda", "Strands Agents", "Microsoft Entra ID", "Splunk", "Git"], "on"),
            ("LEARNING NOW", ["Terraform", "AWS IAM", "Okta", "PowerShell", "Palantir Foundry"], "soft"),
            ("CERTIFIED", ["CompTIA Security+", "GIAC GFACT", "GIAC GSEC", "GIAC GCIH"], "cert"),
            ("IN PROGRESS", ["Microsoft SC-300"], "prog"),
            ("EDUCATION", [("BS IT Management, WGU (2025)", "cert"), ("SANS Cyber Academy Fellow, Cybersecurity (2026)", "cert"), ("MS Cybersecurity, Georgia Tech (2028)", "prog")], "mixed")]
    y = 34; body = ""; k = 0
    for label, items, row_kind in rows:
        body += f'<text x="40" y="{y+21}" class="lab">{label}</text>'
        x = 210
        for it in items:
            it, kind = it if isinstance(it, tuple) else (it, row_kind)
            w = 20 + len(it) * 7.3
            if x + w > W - 40: x = 210; y += 46
            dot = {"on": c['accent'], "soft": c['gray'], "cert": c['green'], "prog": c['gray']}[kind]
            pulse = ' class="pulse"' if kind == "prog" else ""
            body += f'<g transform="translate({x:.0f} {y})"><rect width="{w+16:.0f}" height="32" rx="16" class="pill" style="animation-delay:{k*0.12:.2f}s"/><circle cx="16" cy="16" r="4" fill="{dot}"{pulse}/><text x="28" y="21" class="pt">{it}</text></g>'
            x += w + 16 + 10; k += 1
        y += 58
    H = y + 6
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-label="Toolbox and certifications">
<defs><linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{c['bg1']}"/><stop offset="1" stop-color="{c['bg2']}"/></linearGradient></defs>
<style>
.lab{{font:700 12px {MONO};letter-spacing:.18em;fill:{c['sub']}}}
.pill{{fill:{c['chip']};stroke:{c['chipb']};stroke-width:1.1;opacity:0;animation:in .6s ease-out forwards}}
.pt{{font:500 14px {FONT};fill:{c['text']}}}
.pulse{{animation:pulse 1.8s ease-in-out infinite}}
@keyframes in{{to{{opacity:1}}}}
@keyframes pulse{{50%{{opacity:.25}}}}
@media (prefers-reduced-motion:reduce){{*{{animation:none!important}}.pill{{opacity:1}}}}
</style>
<rect x="1" y="1" width="{W-2}" height="{H-2}" rx="20" fill="url(#bg)" stroke="{c['border']}"/>
{body}</svg>'''

for t in TH:
    (OUT / f"principles-{t}.svg").write_text(chips(t))
    (OUT / f"stack-{t}.svg").write_text(stack(t))
print("ok")
