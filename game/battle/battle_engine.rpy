## ============================================================
## СИСТЕМА БОЯ — My Wall-Space
## Стиль: Deltarune (пошаговый, ACT-действия, Люмины)
## ============================================================

init python:

    class BattleManager:
        """Ядро боевой системы. Управляет Люминами, HP и ходами."""

        def __init__(self):
            self.holy  = store.holy_lumins
            self.dark  = store.dark_lumins
            self.r_hp  = store.r_hp
            self.turn  = 1
            self.log   = []

        def can_use(self, cost_holy, cost_dark):
            return self.holy >= cost_holy and self.dark >= cost_dark

        def spend(self, cost_holy, cost_dark):
            if self.can_use(cost_holy, cost_dark):
                self.holy -= cost_holy
                self.dark  -= cost_dark
                return True
            return False

        def regen(self, amount_holy=1, amount_dark=1):
            self.holy = min(10, self.holy + amount_holy)
            self.dark  = min(10, self.dark  + amount_dark)

        def take_damage(self, dmg):
            self.r_hp = max(0, self.r_hp - dmg)
            self.log.append(f"РАнфи получил {dmg} урона. HP: {self.r_hp}")

        def sync(self):
            store.holy_lumins = self.holy
            store.dark_lumins  = self.dark
            store.r_hp         = self.r_hp

    # Способности РАнфи (Уровень 1, доступные в прологе)
    ABILITIES = {
        "echo_strike": {
            "name": "Эхо-удар",
            "cost_holy": 1, "cost_dark": 0,
            "power": 15,
            "desc": "Резонанс гитарной струны — точечный удар звуком."
        },
        "dark_pulse": {
            "name": "Тёмный импульс",
            "cost_holy": 0, "cost_dark": 2,
            "power": 22,
            "desc": "Волна тёмных люминов, дестабилизирующая врага."
        },
        "soul_shield": {
            "name": "Щит Души",
            "cost_holy": 2, "cost_dark": 1,
            "power": 0,
            "desc": "Защитный барьер. Снижает урон на 40% на 1 ход."
        },
        "emocore": {
            "name": "ЭмокОр",
            "cost_holy": 3, "cost_dark": 3,
            "power": 45,
            "desc": "Синергия РАнфи + БеззесЕлинт. Гитарная ярость + теневой взрыв."
        },
    }


# ── Экран битвы ───────────────────────────────────────────────
screen battle_hud(bm):
    frame:
        background "#000000bb"
        xalign 0.5 yalign 0.95
        xsize 900
        padding (20, 10)
        has hbox spacing 30

        # HP
        vbox:
            text "HP" color "#ff6677" size 14
            text "[bm.r_hp]/[store.r_max_hp]" color "#ffaaaa" size 18

        # Святые Люмины
        vbox:
            text "☀ Святые" color "#ffffaa" size 14
            text "[bm.holy]/10" color "#ffff88" size 18

        # Тёмные Люмины
        vbox:
            text "☽ Тёмные" color "#aaaaff" size 14
            text "[bm.dark]/10" color "#aaaaff" size 18

        # Ход
        vbox:
            text "Ход" color "#cccccc" size 14
            text "[bm.turn]" color "#ffffff" size 18

screen battle_actions(bm):
    frame:
        background "#00000099"
        xalign 0.5 yalign 0.88
        xsize 860
        padding (16, 10)
        has hbox spacing 20

        textbutton "⚔ АТАКА":
            action Return("attack")
            text_color "#ffcccc"

        textbutton "✦ ACT":
            action Return("act")
            text_color "#ccffcc"

        textbutton "⚡ СПОСОБНОСТЬ":
            action Return("ability")
            text_color "#ccccff"

        textbutton "🛡 ЗАЩИТА":
            action Return("defend")
            text_color "#ffeeaa"
