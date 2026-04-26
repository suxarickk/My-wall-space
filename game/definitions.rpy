## ============================================================
## РЕСУРСЫ — образы и трансформации
## ============================================================

# ── ФОНЫ ─────────────────────────────────────────────────────
image bg_darkness = "images/bg/bg_darkness.jpg"
image bg_room     = "images/bg/bg_room.jpg"

# ── СПРАЙТЫ ──────────────────────────────────────────────────
image runfell     = "images/sprites/runfell.jpg"
image lifarsiy    = "images/sprites/lifarsiy.jpg"
image jermyn      = "images/sprites/jermyn.jpg"
image idzuki      = "images/sprites/idzuki.jpg"
image bezzezelint = "images/sprites/bezzezelint.jpg"

# ── UI ХОТСПОТЫ (заглушки — цветные прямоугольники) ──────────
image hotspot_idle  = Solid("#6644aa")
image hotspot_hover = Solid("#aa88ff")

# ── ТРАНСФОРМАЦИИ ────────────────────────────────────────────
transform left_pos:
    xalign 0.15 yalign 1.0

transform center_pos:
    xalign 0.5  yalign 1.0

transform right_pos:
    xalign 0.85 yalign 1.0

transform lifarsiy_appear:
    alpha 0.0
    xalign 0.78 yalign 0.95
    ease 1.8 alpha 1.0

transform fadein_slow:
    alpha 0.0
    ease 1.0 alpha 1.0
