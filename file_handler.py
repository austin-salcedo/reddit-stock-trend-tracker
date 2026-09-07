from pathlib import Path

def lines_from(file_path: Path) -> list[str]:
    """
    Reads a file and returns a list of each line.
    Returns an empty list if the file is empty.
    """
    with open(file_path, "r") as file:
        return [line for line in file]