from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but they might need fine-tuning.
build_exe_options = {
    "packages": ["tkinter", "customtkinter", "difflib", "datetime", "teste"],
	"include_files": ["orange.json", "images"]
    
}

setup(
    name="chatbot",
    version="0.1",
    description="chatbot NUGEP!",
    options={"build_exe": build_exe_options},
    executables=[Executable("bot.py", base="gui")],
)