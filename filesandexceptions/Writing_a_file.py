from pathlib import Path

# path = Path("filesandexceptions/prog.txt")
# path.write_text("I love programming.")


contents = "I love programming.\n"
contents += "I love creating new games.\n"
contents += "I also love finding meaning in large datasets.\n"

path = Path("filesandexceptions/prog.txt")
path.write_text(contents)