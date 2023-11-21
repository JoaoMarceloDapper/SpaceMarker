#pip install cx_freeze
import cx_Freeze
executables =[
    cx_Freeze.Executable(script="SpaceMarker.py", icon="space.png")
]
cx_Freeze.setup(
    name = "Space Marker",
    options={
        "build_exe":{
            "packages":["pygame","json","tkinter"],
            "include_files":["bg.jpg",
                            "space.png",
                            "readme.md" ,
                            "Space_Machine_Power.mp3"
                            ]
        }
    }, executables = executables
)
