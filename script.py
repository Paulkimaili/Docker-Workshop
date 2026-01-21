from pathlib import path

current_dir=Path.cwd()
current_file=path(__file__).name

print(f"Files in  {current_dir}:")

for filepath i current_dir.iterdir():
    if filepath.name==current_file:
        continue

    print(f" -{Filepath.name}")

    if filepath.is_file():
        content=filepath.read_text