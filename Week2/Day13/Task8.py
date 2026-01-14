from pathlib import Path

folder_name = Path("../Day10")
file_name = Path('Task1.py')

join_path = folder_name.joinpath(file_name)
print(join_path)