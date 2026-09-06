
def lines_from(file_path: str) -> list[str]:
    """
    Reads a file and returns a list of each line with whitespace stripped.
    Returns an empty list if the file is empty.
    """
    with open(file_path, "r") as file:
        return [line for line in file]