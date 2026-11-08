"""Generates assets/hero-dark.svg and assets/hero-light.svg (animated, no external resources).
A person, a server and an AI agent travel toward an identity gate: two pass, the agent with no owner is stopped."""
import pathlib

THEMES = {
    "dark": dict(tag1="#FF9900", tag2="#FFC266", bg1="#060a14", bg2="#0d1530", border="#1f2a44", grid="#3b4a72", text="#f5f7fb", sub="#9aa6c0",
                 node="#0f1830", nodeStroke="#3a4766", icon="#d7deec", chip="#141d36"),
    "light": dict(tag1="#C25E00", tag2="#E68A00", bg1="#f7f9fc", bg2="#e9eef7", border="#d5dcea", grid="#9aa8c7", text="#0b1220", sub="#4a5670",
                  node="#ffffff", nodeStroke="#c3cbdc", icon="#1d2740", chip="#ffffff"),
}
ORANGE, GREEN, RED, BLUE = "#FF9900", "#30D158", "#FF453A", "#4C8DFF"
DUR = 7.5
FONT = "ui-sans-serif,-apple-system,BlinkMacSystemFont,'Segoe UI',Inter,Helvetica,Arial,sans-serif"
MONO = "ui-monospace,'SF Mono',SFMono-Regular,Menlo,Consolas,monospace"

# icons drawn around (0,0), ~ 26px
HUMAN = '<circle cx="0" cy="-6" r="6"/><path d="M-11 12 C-11 2 -5 -1 0 -1 C5 -1 11 2 11 12 Z"/>'
SERVER = ('<rect x="-11" y="-12" width="22" height="9" rx="2.5"/><rect x="-11" y="-1" width="22" height="9" rx="2.5"/>'
          '<rect x="-11" y="10" width="22" height="3" rx="1.5" opacity=".5"/>')
AGENT = ('<rect x="-12" y="-9" width="24" height="19" rx="6"/><rect x="-1" y="-15" width="2" height="6" rx="1"/>'
         '<circle cx="0" cy="-16" r="2.2"/>')

def entity(cls, icon, y, label, eyes=False):
    eye = ('<circle cx="-5" cy="0" r="2.3" class="eye"/><circle cx="5" cy="0" r="2.3" class="eye"/>' if eyes else "")
    return f'''
  <g class="{cls}" transform="translate(0 {y})">
    <g class="mv">
      <circle cx="650" cy="0" r="27" class="node"/>
      <circle cx="650" cy="0" r="27" class="ring"/>
      <g transform="translate(650 0)" class="ico">{icon}{eye}</g>
      <text x="650" y="44" class="lbl">{label}</text>
    </g>
  </g>'''

def svg(t):
    c = THEMES[t]
    grid = "".join(f'<line x1="{x}" y1="0" x2="{x}" y2="400"/>' for x in range(0, 1300, 40)) + \
           "".join(f'<line x1="0" y1="{y}" x2="1300" y2="{y}"/>' for y in range(0, 401, 40))
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 400" width="1200" height="400" role="img" aria-label="Tyler Bynum. Identity is the new perimeter. Securing humans, machines and AI agents.">
<defs>
  <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{c['bg1']}"/><stop offset="1" stop-color="{c['bg2']}"/></linearGradient>
  <linearGradient id="tag" x1="0" x2="1"><stop offset="0" stop-color="{c['tag1']}"/><stop offset="1" stop-color="{c['tag2']}"/></linearGradient>
  <radialGradient id="glow" cx="0.5" cy="0.5" r="0.5"><stop offset="0" stop-color="{ORANGE}" stop-opacity=".35"/><stop offset="1" stop-color="{ORANGE}" stop-opacity="0"/></radialGradient>
  <linearGradient id="fadeL" x1="0" x2="1"><stop offset="0" stop-color="{c['bg1']}"/><stop offset=".55" stop-color="{c['bg1']}" stop-opacity="0"/></linearGradient>
  <linearGradient id="fadeV" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{c['bg1']}" stop-opacity=".9"/><stop offset=".25" stop-color="{c['bg1']}" stop-opacity="0"/><stop offset=".75" stop-color="{c['bg2']}" stop-opacity="0"/><stop offset="1" stop-color="{c['bg2']}" stop-opacity=".95"/></linearGradient>
  <clipPath id="card"><rect x="1" y="1" width="1198" height="398" rx="20"/></clipPath>
</defs>
<style>
  .grid line{{stroke:{c['grid']};stroke-width:1;opacity:.16}}
  .gridmove{{animation:grid 4s linear infinite}}
  @keyframes grid{{to{{transform:translateX(-40px)}}}}
  .eyebrow{{font:600 13px {MONO};letter-spacing:.22em;fill:{c['tag1']}}}
  .name{{font:700 62px {FONT};letter-spacing:-.035em;fill:{c['text']}}}
  .tag{{font:650 30px {FONT};letter-spacing:-.02em;fill:url(#tag)}}
  .sub{{font:400 17px {FONT};fill:{c['sub']}}}
  .cursor{{fill:{ORANGE};animation:blink 1.1s steps(1) infinite}}
  @keyframes blink{{50%{{opacity:0}}}}
  .node{{fill:{c['node']};stroke:{c['nodeStroke']};stroke-width:1.5}}
  .ring{{fill:none;stroke-width:2.5;opacity:0}}
  .ico{{fill:{c['icon']}}}
  .eye{{fill:{BLUE}}}
  .lbl{{font:600 11px {MONO};letter-spacing:.14em;fill:{c['sub']};text-anchor:middle}}
  .gate{{fill:none;stroke:{ORANGE};stroke-width:3}}
  .gatecore{{fill:{ORANGE};opacity:.9}}
  .gatetxt{{font:700 11px {MONO};letter-spacing:.2em;fill:{ORANGE};text-anchor:middle}}
  .chip rect{{fill:{c['chip']};stroke:{RED};stroke-width:1.5}}
  .chip text{{font:700 12px {MONO};letter-spacing:.12em;fill:{RED}}}
  .ok rect{{fill:{c['chip']};stroke:{GREEN};stroke-width:1.5}}
  .ok text{{font:700 12px {MONO};letter-spacing:.12em;fill:{GREEN}}}

  .a .mv,.b .mv{{animation:pass {DUR}s cubic-bezier(.45,0,.25,1) infinite}}
  .b .mv{{animation-delay:-{DUR/3:.2f}s}}
  .c .mv{{animation:block {DUR}s cubic-bezier(.45,0,.25,1) infinite;animation-delay:-{2*DUR/3:.2f}s}}
  .a .ring,.b .ring{{animation:okring {DUR}s linear infinite}}
  .b .ring{{animation-delay:-{DUR/3:.2f}s}}
  .c .ring{{animation:badring {DUR}s linear infinite;animation-delay:-{2*DUR/3:.2f}s}}
  .chip{{animation:chip {DUR}s linear infinite;animation-delay:-{2*DUR/3:.2f}s;opacity:0}}
  .gateflash{{animation:flash {DUR}s linear infinite;animation-delay:-{2*DUR/3:.2f}s}}
  .halo{{animation:halo 3s ease-in-out infinite;transform-origin:905px 200px}}
  .scan{{animation:scan 2.4s ease-in-out infinite}}

  @keyframes pass{{0%{{transform:translateX(0);opacity:0}}8%{{opacity:1}}42%{{transform:translateX(196px)}}54%{{transform:translateX(196px)}}90%{{transform:translateX(470px);opacity:1}}100%{{transform:translateX(490px);opacity:0}}}}
  @keyframes block{{0%{{transform:translateX(0);opacity:0}}8%{{opacity:1}}42%{{transform:translateX(196px)}}46%{{transform:translateX(188px)}}49%{{transform:translateX(196px)}}52%{{transform:translateX(190px)}}55%,84%{{transform:translateX(196px);opacity:1}}96%,100%{{transform:translateX(184px);opacity:0}}}}
  @keyframes okring{{0%,45%{{opacity:0;stroke:{GREEN}}}50%,92%{{opacity:1;stroke:{GREEN}}}100%{{opacity:0;stroke:{GREEN}}}}}
  @keyframes badring{{0%,44%{{opacity:0;stroke:{RED}}}48%,86%{{opacity:1;stroke:{RED}}}96%,100%{{opacity:0;stroke:{RED}}}}}
  @keyframes chip{{0%,47%{{opacity:0;transform:translateY(6px)}}52%,84%{{opacity:1;transform:translateY(0)}}94%,100%{{opacity:0}}}}
  @keyframes flash{{0%,44%{{stroke:{ORANGE}}}47%,84%{{stroke:{RED}}}92%,100%{{stroke:{ORANGE}}}}}
  @keyframes halo{{0%,100%{{opacity:.55;transform:scale(1)}}50%{{opacity:1;transform:scale(1.08)}}}}
  @keyframes scan{{0%,100%{{transform:translateY(-70px);opacity:0}}20%,80%{{opacity:1}}50%{{transform:translateY(70px)}}}}
  @media (prefers-reduced-motion:reduce){{*{{animation:none!important}}.mv{{opacity:1}}.chip{{opacity:1}}}}
</style>
<g clip-path="url(#card)">
  <rect width="1200" height="400" fill="url(#bg)"/>
  <g class="grid"><g class="gridmove">{grid}</g></g>
  <rect width="1200" height="400" fill="url(#fadeV)"/>
  <rect width="1200" height="400" fill="url(#fadeL)"/>

  <!-- identity gate -->
  <ellipse class="halo" cx="905" cy="200" rx="90" ry="150" fill="url(#glow)"/>
  <rect class="gate gateflash" x="893" y="66" width="24" height="270" rx="12"/>
  <rect class="gatecore scan" x="899" y="185" width="12" height="30" rx="6"/>
  <text x="905" y="56" class="gatetxt">IDENTITY GATE</text>
  {entity("a", HUMAN, 114, "HUMAN")}
  {entity("b", SERVER, 200, "SERVICE")}
  {entity("c", AGENT, 286, "AI AGENT", eyes=True)}
  <g class="chip"><rect x="934" y="271" width="226" height="30" rx="15"/><text x="1047" y="291" text-anchor="middle">DENIED · NO HUMAN OWNER</text></g>

  <!-- words -->
  <text x="64" y="112" class="eyebrow">IAM · AI AGENT SECURITY · SECOPS</text>
  <text x="62" y="186" class="name">Tyler Bynum</text>
  <text x="64" y="236" class="tag">Identity is the new perimeter.</text>
  <text x="64" y="276" class="sub">Securing humans, machines and AI agents.</text>
  <text x="64" y="302" class="sub">Least privilege, a human owner, and a full audit trail.</text>
</g>
<rect x="1" y="1" width="1198" height="398" rx="20" fill="none" stroke="{c['border']}"/>
</svg>'''

out = pathlib.Path(__file__).resolve().parent.parent / "assets"
for t in THEMES:
    (out / f"hero-{t}.svg").write_text(svg(t))
    print("wrote", out / f"hero-{t}.svg")
