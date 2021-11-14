import cx_Freeze

executables = [cx_Freeze.Executable("40-converting to executable.py")]

cx_Freeze.setup(
    name = "Slither",
    options = {"build_exe" : 
                {"packages" : ["pygame"], 
                "include_files" : 
                    ["apple2.png", "snakehead2.png"]}},
    description = "Slither Game Tutorial",
    executables = executables
)