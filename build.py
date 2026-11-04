"""Build the Basketball GM 2027 draft class file from prospects.json.

Usage:  .venv/bin/python -I build.py
Writes: draft-class-2027.json (latest) and builds/draft-class-2027-<date>.json

prospects.json fields (one object per prospect):
  rank          board order; drives the ratings level (1 = best)
  name, pos     pos is one of PG SG SF PF C (or G, GF, F, FC)
  hgt_in, weight, age_nov2026, team, international (bool)
  tags          space-separated archetype tags, see TAGS below
  image         filename in headshots/raw (processed copy lives in headshots/final as .webp)
  background    transparent | plain | busy
  hometown, born ("YYYY" or "YYYY-MM-DD", optional)
  injury        null or {"type": "Torn ACL", "gamesRemaining": 60}
  status        active | withdrawn   (withdrawn players are left out of the file)
  notes         free text (sources, why something changed)
"""
import base64, datetime, json, math, os

HERE = os.path.dirname(os.path.abspath(__file__))
KEYS = ["stre","spd","jmp","endu","ins","dnk","ft","fg","tp","oiq","diq","drb","pss","reb"]
BASE = {  # typical prospect levels by position (before tags)
 "PG": dict(stre=40,spd=68,jmp=55,endu=45,ins=35,dnk=40,ft=55,fg=50,tp=48,oiq=40,diq=35,drb=60,pss=58,reb=35),
 "SG": dict(stre=43,spd=62,jmp=55,endu=45,ins=38,dnk=48,ft=55,fg=50,tp=50,oiq=40,diq=36,drb=52,pss=45,reb=38),
 "SF": dict(stre=48,spd=56,jmp=54,endu=45,ins=42,dnk=55,ft=50,fg=47,tp=44,oiq=40,diq=38,drb=45,pss=40,reb=45),
 "PF": dict(stre=55,spd=48,jmp=50,endu=45,ins=50,dnk=58,ft=45,fg=45,tp=38,oiq=38,diq=40,drb=38,pss=35,reb=55),
 "C":  dict(stre=62,spd=40,jmp=45,endu=40,ins=55,dnk=62,ft=40,fg=42,tp=25,oiq=36,diq=42,drb=30,pss=32,reb=62),
}
BASE["G"], BASE["GF"], BASE["F"], BASE["FC"] = BASE["PG"], BASE["SG"], BASE["SF"], BASE["PF"]
TAGS = {
 "shooter": dict(tp=14,ft=12,fg=8),
 "scorer": dict(fg=8,ins=6,oiq=6,ft=4),
 "slasher": dict(dnk=10,spd=5,jmp=4,ins=4),
 "athlete": dict(spd=8,jmp=12,dnk=6,endu=4),
 "strong": dict(stre=14,ins=4,reb=3),
 "handler": dict(drb=10,pss=3),
 "passer": dict(pss=12,oiq=5,drb=3),
 "iq": dict(oiq=8,diq=6),
 "defender": dict(diq=12,spd=2),
 "rimprot": dict(diq=12,jmp=8,reb=5),
 "rebounder": dict(reb=12,stre=4),
 "post": dict(ins=12,stre=4),
}

def hgt_rating(inches):  # same formula as BBGM's heightToRating
    return max(0, min(100, round(100 * (inches - 66) / (93 - 66))))

def ovr(r):  # same formula as BBGM's basketball ovr
    x = (0.159*(r["hgt"]-47.5)+0.0777*(r["stre"]-50.2)+0.123*(r["spd"]-50.8)+0.051*(r["jmp"]-48.7)
         +0.0632*(r["endu"]-39.9)+0.0126*(r["ins"]-42.4)+0.0286*(r["dnk"]-49.5)+0.0202*(r["ft"]-47.0)
         +0.0726*(r["tp"]-47.1)+0.133*(r["oiq"]-46.8)+0.159*(r["diq"]-46.7)+0.059*(r["drb"]-54.8)
         +0.062*(r["pss"]-51.3)+0.01*(r["fg"]-47.0)+0.01*(r["reb"]-51.4)+48.5)
    if x >= 68: f = 8
    elif x >= 50: f = 4 + (x-50)*4/18
    elif x >= 42: f = -5 + (x-42)*9/8
    elif x >= 31: f = -5 - (42-x)*5/11
    else: f = -10
    return round(x + f)

def target_ovr(rank, age):
    # weak class: #1 ~48, #30 ~42, #60 ~38; older players are more developed now
    rank = max(1, rank)
    base = 48 - 6 * math.log(rank) / math.log(30) if rank <= 30 else 42 - 4 * (rank - 30) / 30
    return base + 0.9 * (age - 19.5)

def ratings_for(pos, inches, tags, tgt):
    r = dict(BASE[pos])
    for t in tags.split():
        for k, v in TAGS.get(t, {}).items():
            r[k] += v
    hg = hgt_rating(inches)
    best = None
    for off in range(-40, 41):
        cand = {k: max(1, min(100, r[k] + off)) for k in KEYS}
        cand["hgt"] = hg
        d = abs(ovr(cand) - tgt)
        if best is None or d < best[0]:
            best = (d, cand)
    return best[1]

def main():
    prospects = json.load(open(os.path.join(HERE, "prospects.json")))
    active = sorted([p for p in prospects if p.get("status", "active") == "active"], key=lambda p: p["rank"])
    players, missing = [], []
    for i, pr in enumerate(active, 1):
        age = pr["age_nov2026"]
        r = ratings_for(pr["pos"], pr["hgt_in"], pr.get("tags", ""), target_ovr(i, age))
        r.update(season=2027, pos=pr["pos"], locked=False)
        born_year = int(2026.84 - age)
        b = pr.get("born")
        if b and str(b)[:4].isdigit():
            born_year = int(str(b)[:4])
        first, last = pr["name"].split(" ", 1)
        p = {
            "firstName": first, "lastName": last, "tid": -2,
            "hgt": pr["hgt_in"], "weight": pr["weight"], "pos": pr["pos"],
            "born": {"year": born_year, "loc": pr.get("hometown") or ""},
            "college": "" if pr.get("international") else pr["team"],
            "draft": {"year": 2027, "round": 0, "pick": 0, "tid": -1, "originalTid": -1},
            "ratings": [r],
        }
        inj = pr.get("injury")
        if inj and inj.get("type"):
            p["injury"] = {"type": inj["type"], "gamesRemaining": int(inj.get("gamesRemaining", 0))}
        img = pr.get("image")
        webp = os.path.join(HERE, "headshots", "final", os.path.splitext(img)[0] + ".webp") if img else None
        if webp and os.path.exists(webp):
            p["imgURL"] = "data:image/webp;base64," + base64.b64encode(open(webp, "rb").read()).decode()
        else:
            missing.append(pr["name"])
        players.append(p)
    out = {"version": 74, "startingSeason": 2027, "players": players}
    os.makedirs(os.path.join(HERE, "builds"), exist_ok=True)
    today = datetime.date.today().isoformat()
    for path in [os.path.join(HERE, "draft-class-2027.json"),
                 os.path.join(HERE, "builds", f"draft-class-2027-{today}.json")]:
        with open(path, "w") as f:
            json.dump(out, f, ensure_ascii=False)
    print(f"{len(players)} players written ({len(prospects) - len(active)} withdrawn/excluded)")
    for p in players[:5] + players[-3:]:
        print(f'  {p["firstName"]} {p["lastName"]:<22} ovr {ovr(p["ratings"][0])}')
    if missing:
        print("MISSING IMAGES:", ", ".join(missing))

if __name__ == "__main__":
    main()
