W,H=1080,1350; N=8; TY=1150
INK='#141414'; BLUE='#1f5fd6'; AMB='#e08a00'; PUR='#7a3bd6'; GRN='#1f9d55'; RED='#c8102e'; BG='#f3efe6'
svg=[]; html=[]
def X(i,x): return (i-1)*W+x
def st(cx,cy,col,r=18,w=8): svg.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="#fff" stroke="{col}" stroke-width="{w}"/>')
def ichg(cx,cy,r=30): svg.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="#fff" stroke="{INK}" stroke-width="9"/>')
def txt(x,y,s,cls,anchor='start'): svg.append(f'<text x="{x}" y="{y}" class="{cls}" text-anchor="{anchor}">{s}</text>')
OUT={'w':('WON',GRN),'m':('MIXED','#8a8170'),'f':('FLOPPED',RED)}
def chip(x,y,k):
    t,c=OUT[k]; w=len(t)*15+28
    svg.append(f'<rect x="{x}" y="{y-24}" width="{w}" height="34" rx="6" fill="{c}"/><text x="{x+w/2}" y="{y}" class="chip" text-anchor="middle">{t}</text>')
def panel(i,inner,top=90): html.append(f'<div class="panel" style="left:{X(i,84)}px;top:{top}px">{inner}</div>')
def foot(i,label): html.append(f'<div class="foot" style="left:{X(i,84)}px"><span>{label}</span><span>{i} / 8</span></div>')

# trunk
svg.append(f'<path d="M{X(1,130)} {TY} H{X(8,330)}" stroke="{INK}" stroke-width="22" stroke-linecap="round" fill="none"/>')

# 1 cover
panel(1,'''<div class="eyebrow"><b>Deconstructed</b>Product strategy</div>
<h1>Ten years of Jio,<br><i>drawn as a metro map.</i></h1>
<p class="body">One main line: the connection. Three branch lines tried to go beyond it. Not all of them still run.</p>''')
html.append(f'''<div class="legend" style="left:{X(1,84)}px;top:720px">
<div class="lh">KEY</div>
<div><i style="background:{INK};height:14px"></i><span><b>Main line</b> · the SIM</span></div>
<div><i style="background:{BLUE}"></i><span><b>Bundle</b> · put it inside the plan</span></div>
<div><i style="background:{PUR}"></i><span><b>Build</b> · make your own app</span></div>
<div><i style="background:{AMB}"></i><span><b>Buy</b> · rent what users want</span></div>
</div>''')
ichg(X(1,130),TY,34); txt(X(1,130),TY+8,'J','roundel','middle')
txt(X(1,190),TY-36,'MAIN LINE · THE CONNECTION','lbl')
txt(X(1,996),TY+80,'RIDE THE LINE →','cue','end')

# 2 origin
panel(2,'''<div class="kicker">Stop 01 · 2016</div>
<h2>Price mattered. <i>The slot mattered more.</i></h2>
<p class="body">Most Indian phones were dual-SIM. So nobody had to give up their number. They just filled the empty slot with a free Jio SIM. <b>About 100 million users in roughly 170 days.</b></p>''')
html.append(f'''<div class="tray" style="left:{X(2,170)}px;top:640px">
<div class="slot old"><div class="sim"></div><span>SIM 1 · OLD NUMBER</span></div>
<div class="slot new"><div class="sim jio"></div><span>SIM 2 · JIO, FREE</span></div></div>''')
svg.append(f'<path d="M{X(2,710)} 960 V{TY}" stroke="{INK}" stroke-width="6" stroke-dasharray="2 14" stroke-linecap="round"/>')
ichg(X(2,710),TY); txt(X(2,710),TY+70,'FREE SIM','lbl','middle')
html.append(f'<div class="rule" style="left:{X(2,84)}px;top:1010px">Rule 1 · slot into a habit that already exists</div>')
foot(2,'STOP 01 · THE EMPTY SLOT')

# 3 consolidation
panel(3,'''<div class="kicker">Stop 02 · 2016–2019</div>
<h2>About a dozen operators went in. <i>Three came out.</i></h2>
<p class="body">With three players, matching a rival's tariff hike is the rational move. In July 2024 Jio raised prices 12–27%, lost ~10.9M connections, <b>and still made ~5% more.</b></p>''')
for k,(nm,fate) in enumerate([('Telenor','sold to Airtel'),('Aircel','bankrupt'),('RCom','shut voice'),('Vodafone + Idea','merged')]):
    x=X(3,150+k*230)
    if k<3:
        svg.append(f'<path d="M{x} 700 V940" stroke="#b5ad9c" stroke-width="16" stroke-linecap="round"/><path d="M{x-30} 952 H{x+30}" stroke="{RED}" stroke-width="10" stroke-linecap="round"/>')
    else:
        svg.append(f'<path d="M{x-40} 700 V780 Q{x-40} 820 {x} 840 Q{x+40} 820 {x+40} 780 V700 M{x} 840 V940" stroke="#b5ad9c" stroke-width="16" fill="none" stroke-linecap="round"/>')
    txt(x,680,nm,'lblg','middle'); txt(x,1000,fate.upper(),'fate','middle')
ichg(X(3,800),TY); txt(X(3,800),TY+70,'3 PLAYERS','lbl','middle')
html.append(f'<div class="rule" style="left:{X(3,84)}px;top:1040px">Rule 2 · pricing power came from market structure</div>')
foot(3,'STOP 02 · CONSOLIDATION')

# 4 recharge screen
panel(4,'''<div class="kicker">Stop 03 · Every 28 days</div>
<h2>The busiest station isn't an app. <i>It's the recharge screen.</i></h2>''')
html.append(f'''<div class="side" style="left:{X(4,84)}px;top:560px">
<p class="body" style="margin:0">About <b>90%</b> of Indian connections are prepaid. Plans expire every 28, 56 or 84 days, so users keep coming back to pay.</p>
<p class="big">It isn't sold to anyone. <i>It's where everything else is sold.</i></p></div>''')
html.append(f'''<div class="phone" style="left:{X(4,640)}px;top:520px">
<div class="notch"></div>
<div class="ph-t">Your plan expires in <b>2 days</b></div>
<div class="ph-btn">Recharge</div>
<div class="ph-s">ALSO ON THIS SCREEN</div>
<div class="ph-r"><i style="background:{AMB}"></i>Streaming</div>
<div class="ph-r"><i style="background:{PUR}"></i>Shopping</div>
<div class="ph-r"><i style="background:{BLUE}"></i>Home broadband</div>
<div class="ph-r ai"><i style="background:{INK}"></i>AI, next?</div></div>''')
svg.append(f'<path d="M{X(4,800)} 1090 V{TY}" stroke="{INK}" stroke-width="10"/>')
ichg(X(4,800),TY); txt(X(4,800),TY+70,'MYJIO','lbl','middle')
foot(4,'STOP 03 · THE RECHARGE SCREEN')

# branch helper
def branch(i,col,stations,top,label):
    bx=X(i,170); x0=X(i,60)
    svg.append(f'<path d="M{x0} {TY} Q{bx} {TY} {bx} {TY-90} V{top}" stroke="{col}" stroke-width="18" fill="none" stroke-linecap="round"/>')
    txt(bx+40,TY-40,label,'lblc','start')
    return bx

# 5 bundle
panel(5,f'''<div class="kicker" style="color:{BLUE}">Bundle line · ride the connection</div>
<h2>Put it inside the plan, and it <i>mostly works.</i></h2>
<p class="body">These win when the alternative is nothing: a 2G phone, no home broadband. The one flop was a smartphone that needed buyers to prefer it.</p>''')
bx=branch(5,BLUE,None,610,'')
for k,(nm,yr,o) in enumerate([('JioTV','2016','w'),('JioPhone','2017','w'),('JioFiber','2019','m'),('JioPhone Next','2021','f'),('AirFiber','2023','w'),('JioBharat','2023','w')]):
    y=1010-k*78; st(bx,y,BLUE); txt(bx+48,y+12,nm,'stn'); txt(X(5,620),y+10,yr,'yr'); chip(X(5,720),y+10,o)
foot(5,'BUNDLE LINE · 4 WON · 1 MIXED · 1 FLOPPED')

# 6 build
panel(6,f'''<div class="kicker" style="color:{PUR}">Build line · make your own app</div>
<h2>Build a standalone app, and <i>the trains stop coming.</i></h2>
<p class="quote">Distribution gets an app installed. Only preference gets it opened again tomorrow.</p>''')
bx=branch(6,PUR,None,640,'')
svg.append(f'<path d="M{bx-36} 628 H{bx+36}" stroke="{PUR}" stroke-width="12" stroke-linecap="round"/>')
txt(bx,600,'END OF LINE','fate','middle')
for k,(nm,yr,o) in enumerate([('JioChat','2015','f'),('JioMeet','2020','f'),('JioPages','2020','f'),('JioMart','2020','m')]):
    y=1000-k*100; st(bx,y,PUR); txt(bx+48,y+12,nm,'stn'); txt(X(6,450),y+10,yr,'yr'); chip(X(6,540),y+10,o)
jx=X(6,900); jy=700
svg.append(f'<path d="M{X(6,700)} {jy} H{jx}" stroke="{GRN}" stroke-width="8" stroke-dasharray="4 14" stroke-linecap="round"/>')
svg.append(f'<path d="M{X(6,690)} 690 L{X(6,706)} {jy} L{X(6,690)} 710" stroke="{GRN}" stroke-width="0"/>')
ichg(jx,jy,34); txt(jx,jy+9,'W','roundel','middle')
html.append(f'<div class="xfer" style="left:{X(6,700)}px;top:740px"><b>Change here for WhatsApp</b>In 2020 Jio sold ~10% of itself to Meta, and JioMart launched inside WhatsApp, the messenger JioChat was built to rival. It stopped building habit and <u>started renting it.</u></div>')
foot(6,'BUILD LINE · 0 WON · 1 MIXED · 3 FLOPPED')

# 7 buy
panel(7,f'''<div class="kicker" style="color:{AMB}">Buy line · rent what's scarce</div>
<h2>Buy something scarce, and <i>the platforms fill up.</i></h2>
<p class="body">Music isn't scarce: every app licenses the same songs. Live IPL is in one place. Jio didn't build a reason to subscribe. <b>It bought one.</b></p>''')
bx=branch(7,AMB,None,720,'')
st(bx,990,AMB); txt(bx+48,1002,'JioSaavn','stn'); txt(bx+48,1040,'2018','yr'); chip(X(7,400),1040,'m')
ichg(bx,760,32); txt(bx+52,772,'JioHotstar','stn'); txt(bx+52,810,'2023–25','yr'); chip(X(7,400),810,'w')
cx0=X(7,580); base=1060; vals=[(50,"Feb '25"),(100,'Mar'),(200,'Apr'),(300,"Jun '25")]
svg.append(f'<rect x="{cx0+80}" y="640" width="320" height="{base-640}" fill="url(#hatch)"/><text x="{cx0+80}" y="628" class="ipl">IPL 2025</text>')
for k,(v,l) in enumerate(vals):
    h=v/300*340; x=cx0+k*100; c=AMB if k==3 else '#c9b48a'
    svg.append(f'<rect x="{x}" y="{base-h}" width="72" height="{h}" rx="6" fill="{c}"/>')
    txt(x+36,base-h-12,f'{v}M','bv','middle'); txt(x+36,base+34,l,'yr','middle')
txt(cx0,base+70,'Subscribers incl. bundled plans','tiny')
foot(7,'BUY LINE · 1 WON · 1 MIXED')

# 8 AI fork
panel(8,'''<div class="kicker">Next stop · AI</div>
<h2>The line forks. <i>Which way does Jio go?</i></h2>''')
fx=X(8,330)
svg.append(f'<path d="M{fx} {TY} Q{fx+120} {TY} {fx+120} {TY-120} V760" stroke="{PUR}" stroke-width="14" fill="none" stroke-dasharray="26 18" stroke-linecap="round"/>')
svg.append(f'<path d="M{fx} {TY} H{X(8,960)}" stroke="{BLUE}" stroke-width="14" stroke-dasharray="26 18" stroke-linecap="round"/>')
ichg(fx,TY,34)
st(fx+120,760,PUR,22); st(X(8,960),TY,BLUE,22)
html.append(f'<div class="fork" style="left:{X(8,500)}px;top:690px;border-color:{PUR}"><b style="color:{PUR}">BUILD</b>A Jio AI app, fighting ChatGPT, Gemini and Meta AI for daily habit. Another JioMeet?</div>')
html.append(f'<div class="fork" style="left:{X(8,500)}px;top:930px;border-color:{BLUE}"><b style="color:{BLUE}">BUNDLE · BUY</b>Sell the recharge screen to whoever wins AI.</div>')
html.append(f'''<div class="board" style="left:{X(8,84)}px;top:380px">
<div class="bl">THE ONE-LINE READ</div>
<div class="bt">Jio sells distribution <span>and buys preference.</span></div>
<div class="bs">The telecom arm still earns ~95% of Jio's EBITDA. The market is pricing the main line.</div></div>''')
txt(X(8,996),TY+80,'FULL MAP · LINK IN COMMENTS ↓','cue','end')
foot(8,'PRIYANSHU MOHANTY · DECONSTRUCTED')

page=f'''<!DOCTYPE html><html><head><meta charset="utf-8"><title>The Jio Line - LinkedIn carousel</title><style>
@import url('https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&family=JetBrains+Mono:wght@500;700;800&family=Outfit:wght@400;500;600;700;800&display=swap');
*{{margin:0;padding:0;box-sizing:border-box}}
body{{background:#222}}
#frame{{width:{W}px;height:{H}px;position:relative;overflow:hidden}}
#canvas{{position:absolute;left:0;top:0;width:{W*N}px;height:{H}px;background:{BG};font-family:'Outfit',sans-serif;color:{INK}}}
#canvas::before{{content:"";position:absolute;inset:0;opacity:.16;background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='200' height='200'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='.9' numOctaves='3'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)'/%3E%3C/svg%3E")}}
.grid{{position:absolute;inset:0;background-image:radial-gradient(#d9d2c3 1.6px,transparent 2px);background-size:36px 36px;opacity:.7}}
svg.map{{position:absolute;left:0;top:0}}
.panel{{position:absolute;width:912px}}
.eyebrow{{font-family:'JetBrains Mono';font-size:22px;font-weight:700;letter-spacing:4px;text-transform:uppercase}}
.eyebrow b{{background:{INK};color:#f2b134;padding:4px 12px;margin-right:12px}}
.kicker{{font-family:'JetBrains Mono';font-size:22px;letter-spacing:4px;font-weight:800;text-transform:uppercase;color:#8a8170}}
h1,h2{{font-family:'Instrument Serif';font-weight:400;letter-spacing:-2px}}
h1{{font-size:116px;line-height:.98;margin-top:60px}}
h2{{font-size:80px;line-height:1.02;margin-top:18px}}
h1 i,h2 i{{color:{RED}}}
.body{{font-size:31px;line-height:1.42;margin-top:26px;color:#3a3326}}
.body b{{color:{INK}}}
.quote{{font-family:'Instrument Serif';font-style:italic;font-size:46px;line-height:1.12;margin-top:26px;padding-left:26px;border-left:8px solid {PUR}}}
.foot{{position:absolute;bottom:44px;width:912px;display:flex;justify-content:space-between;font-family:'JetBrains Mono';font-size:19px;letter-spacing:3px;color:#8a8170;font-weight:700}}
text.lbl{{font:800 22px 'JetBrains Mono';letter-spacing:3px;fill:{INK}}}
text.lblg{{font:700 26px 'Outfit';fill:#6f6757}}
text.fate{{font:800 18px 'JetBrains Mono';letter-spacing:2px;fill:{RED}}}
text.cue{{font:800 24px 'JetBrains Mono';letter-spacing:4px;fill:{INK}}}
text.roundel{{font:800 30px 'Outfit';fill:{INK}}}
text.stn{{font:700 34px 'Outfit';fill:{INK}}}
text.yr{{font:500 22px 'JetBrains Mono';fill:#8a8170;letter-spacing:1px}}
text.chip{{font:800 17px 'JetBrains Mono';fill:#fff;letter-spacing:2px}}
text.ipl{{font:800 20px 'JetBrains Mono';fill:{RED};letter-spacing:3px}}
text.bv{{font:400 38px 'Instrument Serif';fill:{INK}}}
text.tiny{{font:500 18px 'JetBrains Mono';fill:#8a8170}}
.legend{{position:absolute;width:640px;background:#fffdf7;border:3px solid {INK};border-radius:14px;padding:26px 30px;display:grid;gap:16px;font-size:28px}}
.legend .lh{{font:800 18px 'JetBrains Mono';letter-spacing:4px;color:#8a8170}}
.legend div{{display:flex;align-items:center;gap:18px}}
.legend i{{display:inline-block;width:70px;height:12px;border-radius:8px}}
.tray{{position:absolute;display:flex;gap:30px}}
.slot{{width:340px;height:300px;border-radius:24px;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:20px;font:700 20px 'JetBrains Mono';letter-spacing:2px}}
.slot.old{{background:#2b2b2b;color:#bdb5a3}}.slot.new{{background:{INK};color:#f2b134;outline:5px solid {INK};outline-offset:6px}}
.sim{{width:120px;height:154px;border-radius:12px;background:#5a5a5a;clip-path:polygon(28% 0,100% 0,100% 100%,0 100%,0 22%);position:relative}}
.sim::after{{content:"";position:absolute;left:28px;top:50px;width:64px;height:52px;border-radius:8px;background:#b9b9b9}}
.sim.jio{{background:#1e2a78}}.sim.jio::after{{background:linear-gradient(135deg,#f5d77a,#d4a73a,#f0cf6c)}}
.rule{{position:absolute;background:{INK};color:#f3efe6;font:700 22px 'JetBrains Mono';letter-spacing:1px;padding:12px 18px;border-radius:8px}}
.side{{position:absolute;width:520px}}
.big{{font-family:'Instrument Serif';font-size:56px;line-height:1.05;margin-top:36px;letter-spacing:-1px}}
.big i{{color:{RED}}}
.phone{{position:absolute;width:320px;height:570px;border-radius:44px;background:{INK};padding:50px 22px 24px;box-shadow:0 30px 50px rgba(0,0,0,.25)}}
.phone .notch{{position:absolute;top:16px;left:50%;width:90px;height:16px;margin-left:-45px;border-radius:10px;background:#333}}
.phone>div:not(.notch){{background:#fffdf7}}
.ph-t{{border-radius:18px 18px 0 0;padding:24px 20px 10px;font-size:24px;line-height:1.25}}
.ph-btn{{padding:0 20px 20px;}}
.ph-btn::before{{content:"Recharge";display:block;background:#f2b134;border-radius:12px;padding:14px;text-align:center;font-weight:800;font-size:26px}}
.ph-btn{{font-size:0}}
.ph-s{{padding:14px 20px 6px;font:800 15px 'JetBrains Mono';letter-spacing:3px;color:#8a8170;border-top:2px dashed #d6cebf}}
.ph-r{{padding:12px 20px;font-size:23px;font-weight:600;display:flex;align-items:center;gap:14px}}
.ph-r i{{width:16px;height:16px;border-radius:50%}}
.ph-r.ai{{border-radius:0 0 18px 18px;padding-bottom:22px;font-style:italic}}
.xfer{{position:absolute;width:320px;font-size:22px;line-height:1.38;color:#3a3326;background:#fffdf7;border:3px solid {GRN};border-radius:14px;padding:18px 20px}}
.xfer b{{display:block;font:800 17px 'JetBrains Mono';letter-spacing:2px;color:{GRN};text-transform:uppercase;margin-bottom:8px}}
.fork{{position:absolute;width:500px;background:#fffdf7;border:4px solid;border-radius:14px;padding:20px 24px;font-size:26px;line-height:1.35}}
.fork b{{display:block;font:800 18px 'JetBrains Mono';letter-spacing:3px;margin-bottom:6px}}
.board{{position:absolute;width:912px;background:{INK};border-radius:16px;padding:28px 34px;color:#f3efe6}}
.board .bl{{font:800 18px 'JetBrains Mono';letter-spacing:4px;color:#f2b134}}
.board .bt{{font-family:'Instrument Serif';font-size:58px;line-height:1.05;margin-top:8px}}
.board .bt span{{font-style:italic;color:#f2b134}}
.board .bs{{font-size:24px;color:#bdb5a3;margin-top:12px}}
</style></head><body><div id="frame"><div id="canvas"><div class="grid"></div>
<svg class="map" width="{W*N}" height="{H}" viewBox="0 0 {W*N} {H}"><defs><pattern id="hatch" width="22" height="22" patternUnits="userSpaceOnUse" patternTransform="rotate(45)"><rect width="10" height="22" fill="rgba(200,16,46,.08)"/></pattern></defs>{''.join(svg)}</svg>
{''.join(html)}</div></div></body></html>'''
open('carousel/carousel.html','w').write(page)
