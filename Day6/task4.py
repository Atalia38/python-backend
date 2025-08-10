
class EmptyTextError(Exception):
    """Raised when a text file has no usable content."""

def read_first_line(path: str) -> str:
    try:
        with open(path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line:
                    return line
        raise EmptyTextError("File has no non-empty lines.")
    except FileNotFoundError:
        return "Error: file not found."
    except UnicodeDecodeError:
        return "Error: wrong encoding (try UTF-8)."
    finally:
        pass  
print(read_first_line("missing.txt"))  
