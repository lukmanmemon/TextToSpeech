from cx_Freeze import setup, Executable

setup ( 
    name = "Text to speech",
    version = "1.0",
    description = "A text to speech application",
    executables = [Executable("main.py", target_name="TextToSpeech.exe")]
)