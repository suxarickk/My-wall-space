## ============================================================
## ПРОЛОГ — «Та же ночь»
## My Wall-Space  |  Глава 0
## ============================================================

# ── ПЕРЕМЕННЫЕ ИССЛЕДОВАНИЯ ───────────────────────────────────
default explored_guitar  = False
default explored_mirror  = False
default explored_posters = False
default explored_cat     = False
default explored_clock   = False

# ─────────────────────────────────────────────────────────────
label prologue:

    ## ── ВСТУПЛЕНИЕ: СОН ─────────────────────────────────────
    scene bg_darkness
    with fade

    play music "audio/music/etarcius_dream.ogg" fadein 2.0 loop

    "..."

    "..."

    "Ничего нет. Кроме меня — абсолютно ничего."

    "Это даже не тьма. Тьма — это что-то. Это — вообще ничто."

    "Но я слышу что-то. Нет — чувствую."

    "Это не звук и не голос. Это вибрация внутри грудной клетки. Медленная. Тёмно-бордовая."

    "..."

    "Три головы. Три пустых силуэта без лиц. Рога уходят в то место, где должно быть небо."

    r "ЭтАрциус..."

    "---"

    stop music fadeout 1.5

    ## ── ПРОБУЖДЕНИЕ ─────────────────────────────────────────
    scene bg_room
    with vpunch

    play music "audio/music/night_ambient.ogg" fadein 2.5 loop volume 0.55

    pause 0.6

    narrator "3:17 ночи."

    narrator "РАнфи сидит на кровати. Музыка в телефоне всё ещё играет — он заснул, не выключив её."

    pause 0.4

    show runfell at center_pos with dissolve

    r "..."

    r "Снова."

    pause 0.5

    r "Третью ночь подряд этот сон. Три головы. Без лиц."

    r "(тихо) ...Джермин бы сказал, что я слишком много думаю."

    narrator "Он встаёт. Спать всё равно не получится."

    narrator "РАнфи медленно осматривает комнату."

    "---"

    ## ── POINT-AND-CLICK: ОСМОТР КОМНАТЫ ─────────────────────
    $ explored_guitar  = False
    $ explored_mirror  = False
    $ explored_posters = False
    $ explored_cat     = False
    $ explored_clock   = False

    call screen room_exploration

    ## После return из экрана — переход к появлению ЛифАрсия
    jump prologue_lifarsiy


# ─────────────────────────────────────────────────────────────
## ЭКРАН POINT-AND-CLICK
# ─────────────────────────────────────────────────────────────
screen room_exploration():
    tag menu

    ## Подсказка
    frame:
        background "#00000055"
        xalign 0.5 ypos 10
        padding (20, 6)
        text "[Осмотри комнату]" color "#9988bb" size 17

    ## ── ГИТАРА (центр-лево, у тумбочки) ─────────────────────
    imagebutton:
        idle  "hotspot_idle"
        hover "hotspot_hover"
        xpos 0.34 ypos 0.72
        action [SetVariable("explored_guitar", True), Call("inspect_guitar")]
        tooltip "Осмотреть: Электрогитара"

    ## ── ЗЕРКАЛО (лево) ───────────────────────────────────────
    imagebutton:
        idle  "hotspot_idle"
        hover "hotspot_hover"
        xpos 0.18 ypos 0.44
        action [SetVariable("explored_mirror", True), Call("inspect_mirror")]
        tooltip "Осмотреть: Зеркало"

    ## ── ПОСТЕРЫ (право-верх) ─────────────────────────────────
    imagebutton:
        idle  "hotspot_idle"
        hover "hotspot_hover"
        xpos 0.64 ypos 0.14
        action [SetVariable("explored_posters", True), Call("inspect_posters")]
        tooltip "Осмотреть: Постеры"

    ## ── КОШКА (право) ────────────────────────────────────────
    imagebutton:
        idle  "hotspot_idle"
        hover "hotspot_hover"
        xpos 0.84 ypos 0.68
        action [SetVariable("explored_cat", True), Call("inspect_cat")]
        tooltip "Осмотреть: Кот"

    ## ── ЧАСЫ (центр-верх) ────────────────────────────────────
    imagebutton:
        idle  "hotspot_idle"
        hover "hotspot_hover"
        xpos 0.41 ypos 0.11
        action [SetVariable("explored_clock", True), Call("inspect_clock")]
        tooltip "Осмотреть: Часы"

    ## ── Кнопка выхода ────────────────────────────────────────
    textbutton "Лечь обратно":
        xalign 0.5 yalign 0.97
        text_color "#9977bb"
        text_hover_color "#ccaaff"
        action Return()

    ## Подсветка уже осмотренных
    if explored_guitar:
        text "✓" xpos 0.34 ypos 0.70 color "#55ff88" size 14
    if explored_mirror:
        text "✓" xpos 0.18 ypos 0.42 color "#55ff88" size 14
    if explored_posters:
        text "✓" xpos 0.64 ypos 0.12 color "#55ff88" size 14
    if explored_cat:
        text "✓" xpos 0.84 ypos 0.66 color "#55ff88" size 14
    if explored_clock:
        text "✓" xpos 0.41 ypos 0.09 color "#55ff88" size 14


# ─────────────────────────────────────────────────────────────
## ОБЪЕКТЫ
# ─────────────────────────────────────────────────────────────

label inspect_guitar:
    hide screen room_exploration
    narrator "[Осмотреть: Электрогитара]"
    narrator "Белая. Стоит у тумбочки — не на подставке, просто прислонена к стене."
    narrator "Гриф чуть потёртый. Там, где пальцы касаются чаще всего."
    r "Мы с ДжЕрмином учились брать аккорды одновременно. Он за две недели обогнал меня на месяц."
    r "(думает) ...Интересно, как он сейчас."
    call screen room_exploration
    return

label inspect_mirror:
    hide screen room_exploration
    narrator "[Осмотреть: Зеркало]"
    narrator "Он стоит напротив. Бледное лицо. Тёмные круги под глазами."
    narrator "Долго изучает своё отражение — как будто видит его впервые."
    r "(думает) ТЭлвон."
    pause 0.5
    r "(тихо) ...Этого человека больше нет."
    pause 0.4
    call screen room_exploration
    return

label inspect_posters:
    hide screen room_exploration
    narrator "[Осмотреть: Постеры]"
    narrator "Scary Birches. sMall is Prison. Несколько без подписей — просто силуэты."
    narrator "И в самом углу, почти незаметный — нарисованный от руки."
    narrator "Большая белая фигура с крыльями."
    r "(тихо) ...я сам его нарисовал. Два года назад."
    call screen room_exploration
    return

label inspect_cat:
    hide screen room_exploration
    narrator "[Осмотреть: Чёрный кот]"
    narrator "Кот смотрит на него. Не моргает."
    narrator "Слишком долго. Слишком внимательно."
    r "Ты что-то видишь?"
    pause 0.6
    narrator "Кот медленно отворачивается к стене."
    r "..."
    call screen room_exploration
    return

label inspect_clock:
    hide screen room_exploration
    narrator "[Осмотреть: Часы на стене]"
    narrator "3:21. Стрелки движутся — медленно, как будто нехотя."
    r "(думает) До рассвета три часа."
    narrator "Три часа тишины. Три часа, пока ночь не отпустит."
    call screen room_exploration
    return


# ─────────────────────────────────────────────────────────────
## ПОЯВЛЕНИЕ ЛИФАРСИЯ
# ─────────────────────────────────────────────────────────────

label prologue_lifarsiy:

    scene bg_room
    with dissolve

    show runfell at center_pos

    narrator "Он садится обратно на кровать."

    pause 0.5

    narrator "Музыка в телефоне замолкает сама."

    narrator "Это нельзя объяснить разрядом батареи — он только что смотрел: 74%."

    pause 1.0

    play sfx "audio/sfx/lifarsiy_arrive.ogg"

    narrator "Комната становится холоднее на несколько градусов."

    narrator "Это не сквозняк."

    pause 0.7

    show lifarsiy at lifarsiy_appear

    pause 1.0

    narrator "Он просто... есть."

    narrator "Как будто всегда стоял в том углу, и РАнфи просто не смотрел туда."

    r "..."

    r "(спокойно, устало) Третья ночь подряд, ЛифАрсий."

    pause 0.5

    ## ── ЛИФАРСИЙСКИЙ ЯЗЫК ────────────────────────────────────
    l "Аэ-вэрну, тариЭль сАйн..."
    l "(Я слышу тебя, дитя ночи...)"

    pause 0.3

    l "ЭлфорЭ нумерИй ко-астЭ. СонтАри РАнфи-нарИэ."
    l "(Сон приходит не просто так. Ты чувствуешь это, РАнфи.)"

    r "Знаю. Именно это меня и беспокоит."

    pause 0.4

    l "КорвелЭ, РАнфи. АстЭ-форЕль — ЭтАрциус ко'мЭн."
    l "(Будь осторожен. То, что ты видишь — ЭтАрциус зовёт.)"

    narrator "Одно из крыльев чуть шевельнулось."

    narrator "Красный глаз в нижней части крыла — с тёмным узором вокруг — смотрит прямо на него."

    r "(тихо) Зовёт... или предупреждает?"

    pause 0.8

    l "..."

    narrator "Ответа не последовало."

    pause 0.5

    narrator "ЛифАрсий начал растворяться — так же, как появился. Медленно. Без слов."

    hide lifarsiy with dissolve

    pause 1.2

    narrator "РАнфи долго смотрел на то место, где только что стоял ангел."

    r "(думает) ...Мне нужно поговорить с ДжЕрмином."

    "---"

    narrator "За окном — темнота. До утра три часа."

    narrator "РАнфи лёг обратно. Уставился в потолок."

    narrator "Спать он больше не пытался."

    pause 0.8

    "— КОНЕЦ ПРОЛОГА —"

    jump chapter_one_start
