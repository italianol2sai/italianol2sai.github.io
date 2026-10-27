def rosa(labels=("N","E","S","O"), size=260, color="#15803D"):
    n,e,s,o = labels
    return f'''<svg viewBox="-160 -135 320 270" width="{size}" height="{size}" role="img" aria-label="rosa dei venti" style="max-width:100%">
<g fill="{color}"><polygon points="0,-95 14,-14 0,0"/><polygon points="0,95 -14,14 0,0"/><polygon points="95,0 14,14 0,0"/><polygon points="-95,0 -14,-14 0,0"/></g>
<g fill="#cbd5c0"><polygon points="0,-95 -14,-14 0,0"/><polygon points="0,95 14,14 0,0"/><polygon points="95,0 14,-14 0,0"/><polygon points="-95,0 -14,14 0,0"/>
<polygon points="45,-45 8,-2 2,-8"/><polygon points="-45,45 -8,2 -2,8"/><polygon points="45,45 2,8 8,2"/><polygon points="-45,-45 -2,-8 -8,-2"/></g>
<g font-family="Trebuchet MS,Arial" font-weight="bold" font-size="19" fill="currentColor" text-anchor="middle">
<text x="0" y="-104">{n}</text><text x="0" y="122">{s}</text><text x="122" y="7">{e}</text><text x="-122" y="7">{o}</text></g></svg>'''
