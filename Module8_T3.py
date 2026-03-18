from pathlib import Path
import sys
from colorama import Fore, Style, init


def print_directory_tree(path: Path, prefix: str = "") -> None:
    """
    Рекурсивно виводить структуру директорії.
    """
    try:
        items = sorted(path.iterdir(), key=lambda item: (item.is_file(), item.name.lower()))
    except PermissionError:
        print(f"{prefix}{Fore.RED}[Permission denied]{Style.RESET_ALL}")
        return

    for index, item in enumerate(items):
        is_last = index == len(items) - 1
        connector = "┗ " if is_last else "┣ "
        next_prefix = prefix + ("  " if is_last else "┃ ")

        if item.is_dir():
            print(f"{prefix}{connector}{Fore.BLUE}📂 {item.name}{Style.RESET_ALL}")
            print_directory_tree(item, next_prefix)
        else:
            print(f"{prefix}{connector}{Fore.GREEN}📜 {item.name}{Style.RESET_ALL}")


def main() -> None:
    """
    Перевіряє аргументи командного рядка та запускає виведення структури директорії.
    """
    init(autoreset=True)

    if len(sys.argv) != 2:
        print(f"{Fore.RED}Usage: python hw03.py /path/to/directory{Style.RESET_ALL}")
        return

    directory_path = Path(sys.argv[1])

    if not directory_path.exists():
        print(f"{Fore.RED}Error: path does not exist.{Style.RESET_ALL}")
        return

    if not directory_path.is_dir():
        print(f"{Fore.RED}Error: the specified path is not a directory.{Style.RESET_ALL}")
        return

    print(f"{Fore.YELLOW}📦 {directory_path.name}{Style.RESET_ALL}")
    print_directory_tree(directory_path)


if __name__ == "__main__":
    main()
