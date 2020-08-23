import cx_Freeze

executables = [cx_Freeze.Executable("manav.py")]

cx_Freeze.setup(
    name="space invaders",
    option={"build_exe":{"packages":["pygame"],"incluade_files":["avatar.png","gaming.png","backgroung.wav","explosion.wav","laser.wav","misc.png","screenshot.png","sprint.png"]}},
    description = "space invaders",
    executables = executables
    )


    

