## ============================================================
## РЕСУРСЫ — заглушки и определения изображений
## Когда добавишь PNG/JPG, Ren'Py подхватит их автоматически
## ============================================================

# ── ФОНЫ ─────────────────────────────────────────────────────
image bg_darkness = "images/bg/bg_darkness.jpg"
image bg_room     = "images/bg/bg_room.jpg"
# Если файл не найден — показываем цветной прямоугольник
image bg_darkness_solid = Solid("#0a0008")
image bg_room_solid     = Solid("#1a1a2e")

# ── СПРАЙТЫ ──────────────────────────────────────────────────
image runfell   = "images/sprites/runfell.jpg"
image lifarsiy  = "images/sprites/lifarsiy.jpg"
image jermyn    = "images/sprites/jermyn.jpg"
image idzuki    = "images/sprites/idzuki.jpg"
image bezzezelint = "images/sprites/bezzezelint.jpg"

# ── UI / ХОТСПОТЫ ────────────────────────────────────────────
# Прозрачные кнопки для point-and-click (заглушки — цветные квадраты)
image hotspot_idle  = Solid("#6644aa44", xsize=60, ysize=60)
image hotspot_hover = Solid("#aa88ff88", xsize=60, ysize=60)

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

transform fadein:
    alpha 0.0
    ease 1.0 alpha 1.0
