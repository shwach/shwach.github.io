"""Builds index.html (Korean) and en/index.html (English) from the data below.

Run from the repo root:  python3 _build/build.py
Edit GAMES / TEXT here, never the generated HTML.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
YT = 'https://www.youtube.com/@doggguggu'
MAIL = 'doggguggu@gmail.com'

# (icon, iOS id, Play package, {lang: (name, subtitle_or_genre, description)})
FEATURED = [
    ('guild.jpg', 6779811440, 'com.idle.guild', 'Idle RPG', {
        'ko': ('Idle Guild', '방치형 길드 키우기', '길드원을 던전에 파견하면 알아서 싸우고, 명성과 장비를 모아 옵니다. 앱을 꺼 둔 동안에도 모험은 계속돼요.'),
        'en': ('Idle Guild', 'Dungeon Text RPG', 'Send your guild members into dungeons and they fight on their own, bringing back fame and gear. The adventure goes on even while the app is closed.'),
    }),
    ('blade.jpg', 6811132548, 'com.blade.smith', 'Idle Crafting RPG', {
        'ko': ('Idle Blade Smith', '방치형 대장간: 검 만들기', '광석을 캐고 쇠를 녹여 칼날과 손잡이를 조합하세요. 완성한 검을 기사에게 들려 던전으로 보내고, 가져온 재료로 더 좋은 검을 만듭니다.'),
        'en': ('Idle Blade Smith', 'Forge RPG', 'Mine ore, smelt iron, and combine blades and hilts into swords. Arm your knights, send them into dungeons, and forge even better blades from the loot they bring back.'),
    }),
    ('farm.jpg', 6774788641, 'com.farm.trade', 'Idle Farming', {
        'ko': ('Lazy Farm', '누워서 농장', '누워서 쉬는 동안에도 농장은 자라요. 작물 18가지와 일하는 동물들, 자유 배치 농장을 갖춘 귀여운 픽셀 방치형 농장 게임.'),
        'en': ('Lazy Farm', 'Cozy Pixel Farming', 'Lie back and let your farm grow. A cozy pixel-art idle farming game with 18 crops, hard-working animals and a farm you lay out your way.'),
    }),
]

# (icon, iOS id or None, Play package or None, genre, {lang: (name, description)})
GAMES = [
    ('split.jpg', 6806672427, 'com.split.squad', 'Idle RPG', {
        'ko': ('4분할 원정대', '기사, 도적, 마법사, 사제 네 영웅이 화면을 넷으로 나눠 동시에 던전을 오르는 방치형 RPG.'),
        'en': ('Split Squad', 'A knight, rogue, mage and priest each climb their own dungeon at once in this four-way split-screen idle RPG.'),
    }),
    ('meteor.png', 6813854627, 'com.spell.tower', 'Planet Defense', {
        'ko': ('메테오 브레이커: 행성 디펜스', '우주에 홀로 뜬 작은 행성이 되어 소행성과 혜성, UFO를 요격하세요. 부순 광석으로 판마다 강화를 고르는 디펜스.'),
        'en': ('Meteor Breaker: Planet Defense', 'You are a tiny planet alone in space. Shoot down asteroids, comets and UFOs, and spend the ore on upgrades each run.'),
    }),
    ('arena.png', None, 'com.arena.manager', 'Management', {
        'ko': ('투기장 매니저: 검투사 키우기', '축구 감독 게임처럼 즐기는 2:2 투기장 경영. 영웅을 영입하고 전투 규칙을 직접 짜서 레전드 리그로.'),
        'en': ('Arena Manager: Gladiator RPG', 'Run a 2v2 arena club like a football manager. Scout heroes, write their battle rules and climb to the Legend league.'),
    }),
    ('branch.jpg', 6801756977, 'com.branch.four', 'Simulation', {
        'ko': ('제4지사: 던전시설관리공단', '용사가 부수고 간 던전은 누가 치울까요? 21종족 직원의 근무표를 짜는 던전 관리 행정 시뮬레이션.'),
        'en': ('Branch 4: Dungeon Idle Manager', 'The heroes break it, you clean it up. Schedule a staff of 21 fantasy races in this dungeon facility management sim.'),
    }),
    ('ember.jpg', 6799284115, 'com.hero.cart', 'Dark Fantasy Idle RPG', {
        'ko': ('불씨지기: 방치형 다크판타지 RPG', '재가 된 왕국의 마지막 불씨를 지키세요. 불이 타는 동안 기사는 홀로 길을 걷고, 몬스터를 베고, 보스에게 덤빕니다.'),
        'en': ('Emberkeeper: Idle Knight RPG', 'Keep the last ember of a fallen kingdom alive. While the fire burns, your knight walks on alone, cutting down monsters and taking on bosses.'),
    }),
    ('healer.jpg', 6792133086, 'com.healer.simulator', 'Healing Simulation', {
        'ko': ('힐러 키우기', '딜은 파티가, 생존은 당신이. 레이드 힐러의 긴장감을 모바일 터치로 옮긴 실시간 힐링 시뮬레이션.'),
        'en': ('Healer Simulator', 'Your party deals the damage. Your job is to keep everyone alive in this real-time raid healing sim built for touch.'),
    }),
    ('fantasy.jpg', 6808270586, 'com.fantasyshop.simulator', 'Shop Simulation', {
        'ko': ('판타지 상점 시뮬레이터', '오크, 엘프, 드래곤 손님에게 물건을 팔고 거스름돈까지 정확히 계산하는 판타지 잡화점 경영.'),
        'en': ('Fantasy Shop Simulator', 'Serve orcs, elves and dragons, pick their orders off the shelf and count out exact change in your own fantasy shop.'),
    }),
    ('pigeon.jpg', 6809312191, 'com.pigeon.robot', 'Idle Bakery', {
        'ko': ('로봇 vs 비둘기: 방치형 빵집', '중고 로봇 제빵사와 함께 빵을 굽고, 빵을 노리는 동네 비둘기를 쫓아내는 방치형 빵집.'),
        'en': ('Robot vs Pigeons: Idle Bakery', 'Bake bread with a second-hand robot baker and shoo away the neighborhood pigeons who want it all.'),
    }),
    ('sword.png', None, 'com.pull.sword', 'Idle Clicker', {
        'ko': ('칼뽑기 - 방치형 검 키우기', '바위에 박힌 칼을 탭으로 뽑아 보세요. 녹슨 부엌칼일까, 엑스칼리버일까? 아기자기한 방치형 클리커.'),
        'en': ('Pull the Sword: Idle Clicker', 'Tap to pull the sword from the stone. Will it be a rusty kitchen knife or Excalibur? A cozy idle clicker.'),
    }),
    ('mage.jpg', 6781848358, None, 'Idle RPG', {
        'ko': ('Idle Mage Academy', '입학 꼴찌 낙제생에서 대마법사까지. 웹소설 감성 텍스트 로그로 즐기는 방치형 마법사 키우기.'),
        'en': ('Idle Mage Academy', 'Rise from the academy\'s worst dropout to archmage, told through a web-novel style text log.'),
    }),
    ('deep.jpg', 6787365168, None, 'Idle Fishing', {
        'ko': ('Deep Idle - 방치형 심해 낚시', '낚싯줄을 깊은 바다로 내리면 수심대마다 물고기가 걸려요. 도감을 채우고 수족관을 키우세요.'),
        'en': ('Deep Idle', 'Drop your line into the deep sea and fish bite at every depth. Fill your collection and grow your aquarium.'),
    }),
    ('lotto.png', 6772916627, None, 'Tycoon', {
        'ko': ('복권 가게 시뮬레이터', '복권 가게 사장이 되어 복권을 팔고, 추첨을 기다리고, 가게를 키우는 방치형 경영 시뮬레이션.'),
        'en': ('Lottery Shop Simulator', 'Run your own lottery shop. Sell tickets, wait for the draw and grow your store in this idle tycoon game.'),
    }),
    ('dungeon15.png', 6772534621, 'com.pomodoro.dungeon', 'Survival Action', {
        'ko': ('15분 던전', '15분 동안 끝없이 몰려오는 몬스터를 버텨 내세요. 무기는 저절로 공격하고, 진화와 합체로 판마다 새로운 빌드를 만듭니다.'),
        'en': ('15-Minute Dungeon', 'Survive 15 minutes against endless monster waves. Your weapons fire on their own, so evolve and fuse them into a new build every run.'),
    }),
    ('queue.jpg', 6776687466, 'com.queue.up', 'Casual', {
        'ko': ('Queue Up! - 줄서기 게임', '가장 빨리 빠지는 줄을 골라 계산대를 통과하세요! 새치기꾼을 막고 옆 줄로 갈아타는 코믹 픽셀 줄서기 게임.'),
        'en': ('Queue Up!', 'Pick the line that moves fastest, block the line cutters and hop lanes in this comic pixel queueing game.'),
    }),
]

TEXT = {
    'ko': {
        'lang': 'ko', 'root': '', 'store': 'kr', 'hl': 'ko',
        'title': 'GGU Games | 인디 모바일 게임 스튜디오',
        'meta': 'GGU Games는 매일 손이 가는 방치형 모바일 게임을 만드는 인디 게임 스튜디오입니다. Idle Guild, Idle Blade Smith, Lazy Farm.',
        'home': 'GGU Games 홈', 'switch': ('EN', 'en/'),
        'lead': 'GGU Games는 하루 5분, 매일 손이 가는 작은 모바일 게임을 만드는 인디 스튜디오입니다. Idle Guild, Idle Blade Smith, Lazy Farm까지. 앱을 꺼 둬도 계속 자라는 방치형 게임을 iOS와 Android에 선보입니다.',
        'cta1': '게임 보러가기 →', 'cta2': '▶ 플레이 영상',
        'feat_desc': 'GGU를 대표하는 방치형 게임 3종. App Store와 Google Play에서 무료로 플레이하세요.',
        'games_desc': '경영, 디펜스, 캐주얼까지. 직접 기획하고 개발한 GGU의 게임들.',
        'icon': '아이콘',
        'studio': [
            '<strong>GGU Games</strong>는 기획부터 개발, 출시와 업데이트까지 직접 하는 작은 인디 게임 스튜디오입니다.',
            '우리는 거창한 대작보다 <strong>출퇴근길, 쉬는 시간, 잠들기 전</strong>에 꺼내 드는 게임을 만듭니다. 짧게 즐겨도 재밌고, 오래 하면 더 깊어지는 게임이 목표예요.',
            '새로운 게임 개발 과정과 플레이 영상은 YouTube 채널에서 가장 먼저 공개됩니다.',
        ],
        'stats': ['출시 게임', '대표작', 'App Store, Google Play', '계속 만드는 중'],
        'values': [
            '하루 5분이면 충분한 플레이. 짧은 세션으로도 확실한 재미를 줍니다.',
            '귀여운 픽셀 아트와 캐릭터로 한눈에 알아보는 GGU만의 감성.',
            '작게 만들고 빠르게 출시하고, 플레이어 피드백으로 계속 개선합니다.',
        ],
        'contact': '게임 문의, 버그 제보, 제휴 제안 모두 환영합니다.',
        'mail_btn': '✉ 이메일 보내기', 'yt_btn': '▶ YouTube 구독',
    },
    'en': {
        'lang': 'en', 'root': '../', 'store': 'us', 'hl': 'en',
        'title': 'GGU Games | Indie Mobile Game Studio',
        'meta': 'GGU Games is an indie studio making idle mobile games you come back to every day. Idle Guild, Idle Blade Smith, Lazy Farm.',
        'home': 'GGU Games home', 'switch': ('KO', '../'),
        'lead': 'GGU Games is an indie studio making small mobile games you come back to every day. From Idle Guild and Idle Blade Smith to Lazy Farm, our idle games keep growing even when the app is closed, on iOS and Android.',
        'cta1': 'See our games →', 'cta2': '▶ Gameplay videos',
        'feat_desc': 'The three idle games that define GGU. Play free on the App Store and Google Play.',
        'games_desc': 'Management, tower defense, casual and more. Every game designed and built by GGU.',
        'icon': 'icon',
        'studio': [
            '<strong>GGU Games</strong> is a small indie game studio that handles everything from game design and development to launch and updates.',
            'We skip the blockbusters and make games you pull out <strong>on your commute, on a break, or before bed</strong>. Fun in five minutes, deeper the longer you play.',
            'New games, dev updates and gameplay videos land on our YouTube channel first.',
        ],
        'stats': ['Games released', 'Flagship titles', 'App Store, Google Play', 'Still building'],
        'values': [
            'Five minutes a day is enough. Short sessions that still feel rewarding.',
            'Cute pixel art and characters with a look that is unmistakably GGU.',
            'Build small, ship fast, and keep improving with player feedback.',
        ],
        'contact': 'Questions, bug reports and partnership ideas are all welcome.',
        'mail_btn': '✉ Send an email', 'yt_btn': '▶ Subscribe on YouTube',
    },
}


def store_links(t, ios, play, cls):
    out = ''
    if ios:
        out += f'<a class="{cls} ios" href="https://apps.apple.com/{t["store"]}/app/id{ios}" target="_blank" rel="noopener"> App Store</a>'
    if play:
        out += f'<a class="{cls} play" href="https://play.google.com/store/apps/details?id={play}&amp;hl={t["hl"]}" target="_blank" rel="noopener">▶ Google Play</a>'
    return out


def feat_html(t, i, g):
    icon, ios, play, genre, loc = g
    name, sub, desc = loc[t['lang']]
    return f'''        <article class="feat">
          <div class="feat-art"><span class="feat-no">0{i + 1}</span><img src="{t['root']}icons/{icon}" alt="{name} {t['icon']}"></div>
          <div class="feat-body">
            <p class="feat-genre">{genre}</p>
            <h3>{name}</h3>
            <p class="feat-ko">{sub}</p>
            <p class="feat-desc">{desc}</p>
            <div class="store-row">{store_links(t, ios, play, 'store-btn')}</div>
          </div>
        </article>
'''


def card_html(t, g):
    icon, ios, play, genre, loc = g
    name, desc = loc[t['lang']]
    return f'''        <article class="card">
          <div class="card-top">
            <img src="{t['root']}icons/{icon}" alt="{name} {t['icon']}" loading="lazy">
            <div>
              <p class="card-genre">{genre}</p>
              <h3>{name}</h3>
            </div>
          </div>
          <p>{desc}</p>
          <div class="store-row">{store_links(t, ios, play, 'store-link')}</div>
        </article>
'''


def page(t):
    r = t['root']
    icons = ''.join(f'<img src="{r}icons/{g[0]}" alt="">' for g in FEATURED + GAMES)
    total = len(FEATURED) + len(GAMES)
    url = 'https://shwach.github.io/' + ('en/' if t['lang'] == 'en' else '')
    favicon = "data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'%3E%3Ccircle cx='50' cy='50' r='50'/%3E%3Ctext x='50' y='66' font-family='Impact,Arial Narrow,sans-serif' font-size='44' font-weight='700' fill='white' text-anchor='middle'%3EGGU%3C/text%3E%3C/svg%3E"
    return f'''<!DOCTYPE html>
<!-- Generated by _build/build.py. Edit that file, not this one. -->
<html lang="{t['lang']}">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{t['title']}</title>
  <meta name="description" content="{t['meta']}">
  <link rel="canonical" href="{url}">
  <link rel="alternate" hreflang="ko" href="https://shwach.github.io/">
  <link rel="alternate" hreflang="en" href="https://shwach.github.io/en/">
  <meta property="og:title" content="GGU Games">
  <meta property="og:description" content="{t['meta']}">
  <meta property="og:image" content="https://shwach.github.io/icons/guild.jpg">
  <link rel="icon" href="{favicon}">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Anton&family=Noto+Sans+KR:wght@400;500;700;900&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="{r}style.css">
</head>
<body>

  <!-- Header -->
  <header>
    <div class="wrap nav">
      <a class="brand" href="#top" aria-label="{t['home']}">
        <span class="logo">GGU</span>
        <span class="brand-name">GGU GAMES</span>
      </a>
      <ul class="nav-links">
        <li class="sec"><a href="#featured">Featured</a></li>
        <li class="sec"><a href="#games">Games</a></li>
        <li class="sec"><a href="#studio">Studio</a></li>
        <li class="sec"><a href="#contact">Contact</a></li>
        <li><a class="nav-lang" href="{t['switch'][1]}" hreflang="{t['switch'][0].lower()}">{t['switch'][0]}</a></li>
        <li><a class="nav-yt" href="{YT}" target="_blank" rel="noopener">▶ YouTube</a></li>
      </ul>
    </div>
  </header>

  <!-- Hero -->
  <div class="hero" id="top">
    <div class="hero-mark" aria-hidden="true">GGU</div>
    <div class="wrap">
      <p class="eyebrow">Indie Mobile Game Studio</p>
      <h1>Small games.<br><span class="outline">Big</span> fun.</h1>
      <p class="lead">{t['lead']}</p>
      <div class="cta-row">
        <a class="btn btn-white" href="#featured">{t['cta1']}</a>
        <a class="btn btn-ghost" href="{YT}" target="_blank" rel="noopener">{t['cta2']}</a>
      </div>
    </div>
  </div>

  <!-- Icon marquee -->
  <div class="marquee" aria-hidden="true">
    <div class="marquee-track">
      {icons}
      {icons}
    </div>
  </div>

  <!-- Featured -->
  <section id="featured">
    <div class="wrap">
      <div class="sec-head">
        <div>
          <p class="sec-num">01 — FEATURED</p>
          <h2 class="sec-title">Flagship Games</h2>
        </div>
        <p class="sec-desc">{t['feat_desc']}</p>
      </div>
      <div class="feat-grid">
{''.join(feat_html(t, i, g) for i, g in enumerate(FEATURED))}      </div>
    </div>
  </section>

  <!-- Games -->
  <section id="games" class="alt">
    <div class="wrap">
      <div class="sec-head">
        <div>
          <p class="sec-num">02 — GAMES</p>
          <h2 class="sec-title">All Games</h2>
        </div>
        <p class="sec-desc">{t['games_desc']}</p>
      </div>
      <div class="grid">
{''.join(card_html(t, g) for g in GAMES)}      </div>
    </div>
  </section>

  <!-- Studio -->
  <section id="studio">
    <div class="wrap">
      <div class="sec-head">
        <div>
          <p class="sec-num">03 — STUDIO</p>
          <h2 class="sec-title">About GGU</h2>
        </div>
      </div>
      <div class="studio">
        <div class="studio-text">
{''.join(f'          <p>{p}</p>{chr(10)}' for p in t['studio'])}        </div>
        <div class="stats">
          <div class="stat dark"><b>{total}</b><span>{t['stats'][0]}</span></div>
          <div class="stat"><b>{len(FEATURED)}</b><span>{t['stats'][1]}</span></div>
          <div class="stat"><b>2</b><span>{t['stats'][2]}</span></div>
          <div class="stat"><b>2026</b><span>{t['stats'][3]}</span></div>
        </div>
      </div>

      <div class="values">
        <div class="value">
          <h4>Bite-sized</h4>
          <p>{t['values'][0]}</p>
        </div>
        <div class="value">
          <h4>Pixel-crafted</h4>
          <p>{t['values'][1]}</p>
        </div>
        <div class="value">
          <h4>Ship fast</h4>
          <p>{t['values'][2]}</p>
        </div>
      </div>
    </div>
  </section>

  <!-- Contact -->
  <section class="contact" id="contact">
    <div class="wrap">
      <div class="logo inverse">GGU</div>
      <h2>Say hello</h2>
      <p>{t['contact']}</p>
      <a class="mail" href="mailto:{MAIL}">{MAIL}</a>
      <div class="cta-row">
        <a class="btn btn-white" href="mailto:{MAIL}">{t['mail_btn']}</a>
        <a class="btn btn-ghost" href="{YT}" target="_blank" rel="noopener">{t['yt_btn']}</a>
      </div>
    </div>
  </section>

  <!-- Footer -->
  <footer>
    <div class="wrap">
      <span class="brand-name">GGU GAMES</span>
      <nav>
        <a href="#featured">Featured</a>
        <a href="#games">Games</a>
        <a href="{YT}" target="_blank" rel="noopener">YouTube</a>
        <a href="/privacy-policy/">Privacy Policy</a>
        <a href="{t['switch'][1]}">{'English' if t['lang'] == 'ko' else '한국어'}</a>
      </nav>
      <span>© 2026 GGU Games. All rights reserved.</span>
    </div>
  </footer>

</body>
</html>
'''


if __name__ == '__main__':
    (ROOT / 'index.html').write_text(page(TEXT['ko']), encoding='utf-8')
    (ROOT / 'en').mkdir(exist_ok=True)
    (ROOT / 'en' / 'index.html').write_text(page(TEXT['en']), encoding='utf-8')
    print('built index.html, en/index.html')
