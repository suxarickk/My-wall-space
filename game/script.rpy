## My Wall-Space — главный скрипт, точка входа
## Engine: Ren'Py 8.x

init python:
    config.window_title  = "My Wall-Space"
    config.screen_width  = 1280
    config.screen_height = 720
    config.save_directory = "my-wall-space"

label start:
    $ holy_lumins = 5
    $ dark_lumins  = 5
    $ r_hp         = 120
    $ r_max_hp     = 120
    $ r_lvl        = 1
    jump prologue
