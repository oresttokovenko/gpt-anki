import os
from pathlib import Path

output_deck_name = "test"

deck_dir: str = Path("deck")
output_file_path: str = deck_dir / f"{output_deck_name}.apkg"
print(output_file_path)

if os.path.isfile(output_file_path):
    print("found it")
else:
    print("not found")
