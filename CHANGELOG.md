# 2027 Draft Class — Changelog

Newest first. Each daily check adds an entry, even when nothing changed.

## 2026-11-04 — College fix
- Arafan Diané (Houston), Massamba Diop (Gonzaga), Miles Sadler (West Virginia), Obinna Ekezie Jr. (Louisville), Zvonimir Ivisic (Illinois) and Johann Grünloh (Virginia) had `international: true`, so BBGM showed "College: None". That flag is only for pro-club players, so it is now false for all six and their colleges show.

## 2026-11-04 — Daily update
The class now has 69 active prospects (77 entries, 8 withdrawn). Ranks are the median of current boards: [ESPN](https://www.espn.com/nba/story/_/id/49101766/2027-nba-mock-draft-no-1-pick-options-top-players-race-picks), [CBS](https://www.cbssports.com/nba/news/2027-nba-mock-draft-tyran-stokes-jordan-smith-jr-stefan-joksimovic/) (Oct 17), [No Ceilings](https://www.noceilingsnba.com/p/2027-nba-mock-draft-v1) (Oct 14), B/R [big board](https://bleacherreport.com/articles/25474454-2027-nba-draft-big-board-top-100-player-rankings) and [mock](https://bleacherreport.com/articles/25461538-our-2027-nba-mock-draft-already-stacked-pro-ready-talent), and [FanSided](https://fansided.com/nba/2027-nba-draft-big-board-top-60-prospects-for-the-new-cycle), plus the previous (Tankathon) order for existing players. Tankathon's 2027 pages returned 404 today.

### Withdrawn
- **Solo Ball** (UConn): wrist surgery and a medical redshirt for 2026-27, so he returns to UConn in 2027-28. [NBC Sports](https://www.nbcsports.com/mens-college-basketball/news/uconns-solo-ball-will-take-a-medical-redshirt-and-miss-next-season-after-undergoing-wrist-surgery)
- **Nikolas Khamenia, Cayden Boozer, Elliot Cadeau, Tomislav Ivisic**: on none of the five full top-60 boards.
- **Klark Riethauser, JT Toppin, Matas Vokietaitis**: each on only one of the five boards (B/R board, B/R mock and ESPN respectively).
- Tomislav Ivisic note: the boards list his twin **Zvonimir** (now added) rather than Tomislav.

### Added (17; each is in the top 60 of 2+ outlets; headshots from ESPN unless noted)
- #7 Colben Landrew (UConn SF): No Ceilings 10, B/R 11, FanSided 10, ESPN 33
- #19 Caleb Gaskins (Miami PF): ESPN 11, No Ceilings 12, B/R 26, FanSided 26. Photo from the [Miami roster](https://miamihurricanes.com/sports/mbball/roster/player/caleb-gaskins), with the background removed.
- #21 Arafan Diané (Houston C): No Ceilings 9, CBS 14, FanSided 21, B/R 34. Photo from the [Houston roster](https://uhcougars.com/sports/mens-basketball/roster/arafan-dian/10147), with the background removed.
- #22 Abdou Toure (Arkansas SG): No Ceilings 7, FanSided 19, B/R 25
- #25 Austin Goosby (Texas SG): ESPN 13, FanSided 23, No Ceilings 24
- #29 Na'jai Hines (UConn C): FanSided 16, B/R 24, No Ceilings 26
- #30 Bryson Howard (Duke SG): B/R 10, FanSided 12, No Ceilings 40
- #45 Massamba Diop (Gonzaga C): FanSided 34, B/R 35, ESPN 41
- #50 Miles Sadler (West Virginia PG): No Ceilings 23, FanSided 27
- #55 Maximo Adams (North Carolina SF): B/R 30, FanSided 31
- #56 Obinna Ekezie Jr. (Louisville C): No Ceilings 33, ESPN 34
- #57 Jaxon Richardson (Alabama SF): ESPN 22, FanSided 35. Birth date not found, so his age is an estimate.
- #60 Deron Rippey Jr. (Duke PG): FanSided 33, No Ceilings 46
- #61 Zvonimir Ivisic (Illinois C): B/R mock 44, FanSided 47
- #64 Jacob Cofie (USC PF): ESPN 50, B/R mock 51
- #67 Johann Grünloh (Virginia C): FanSided 52, B/R 58
- #68 John Blackwell (Duke SG): B/R mock 56, ESPN 60

### Rank changes (consensus moves; other one-to-five-spot shifts come from the additions)
- Up: Braylon Mullins 13 → 6, Motiejus Krivas 22 → 9, Patrick Ngongba II 14 → 11, Luigi Suigo 20 → 16, Matt Able 37 → 32, Dame Sarr 44 → 36, Pryce Sandfort 52 → 47.
- Down: Baba Oladotun 7 → 18, Cameron Williams 9 → 20, Hugo Yimga-Moukouri 10 → 27, Tounde Yessoufou 18 → 35, Davis Fogle 25 → 42, Billy Richmond III 26 → 43, Milan Momcilovic 30 → 53, Andrej Stojakovic 40 → 63, Paul McNeil Jr. 39 → 69. Each is ranked well below his old spot on most boards.
- Brandon McCoy Jr. 8 → 10 after his ACL tear. The post-injury boards have him at No Ceilings 13 and outside CBS's top 27.

### Injuries
- New: **Brandon McCoy Jr.**, Torn ACL, 82 games. Tore his right ACL on Michigan's Europe tour and will miss 2026-27. [ESPN](https://www.espn.com/mens-college-basketball/story/_/id/49795307/michigan-5-star-freshman-brandon-mccoy-jr-knee-miss-season)
- New: **David Mirković**, Broken Foot, 20 games. Recovering from August foot-fracture surgery, then had an appendectomy Nov 1. Missed the Nov 2 opener and is targeting about mid-December. [SI](https://www.si.com/college/illinois/basketball/illinois-basketball-david-mirkovic-undergoes-appendectomy)
- JT Toppin (now withdrawn): his ACL rehab is noted (return expected Jan–Feb). [HoopsHQ](https://www.hoopshq.com/players/injury-watch-college-basketball)
- Checked with no change: [Covers injury report](https://www.covers.com/sport/basketball/ncaab/injuries) (Thiam questionable with an illness, a minor issue, so not recorded). JJ Andrews' wrist fracture is from Dec 2025 and has healed.

### Other fixes
- process.py: new optional `"crop": "square"` for tight portraits whose shoulders fill the frame (used for Diané). Without it the waist-up crop cut him off at the chin.
- Dash Daniels' team (SE Melbourne Phoenix) is confirmed correct. [SEM Phoenix](https://www.semphoenix.com.au/news/daniels-set-to-dash-to-phoenix-for-nbl27)

## 2026-11-04 — Baba Oladotun headshot
- Swapped Oladotun's tightly cropped Maryland roster photo for his 247Sports head-and-shoulders portrait, with the background removed. ESPN still has no photo for him (ESPN id 5210434).

## 2026-11-04 — Initial build
- 60 prospects, ordered by Tankathon's 2027 mock draft and cross-checked against the FanSided top 60, ESPN, CBS, SI and Bleacher Report boards.
- Headshots: 54 ESPN transparent PNGs; Ohio State, Maryland, EuroLeague, ABA League, Nanterre 92, Élan Chalon and SE Melbourne Phoenix official photos for the rest. Plain backgrounds (Thompson, Oladotun, Riethauser) were removed with rembg.
- No injuries recorded.
