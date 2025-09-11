import os
import shutil
from datetime import datetime

LOG_FILE = "last_moves.log"

# ---------- FILE TYPE MAPPING ----------
FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".pptx", ".xlsx"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov"],
    "Music": [".mp3", ".wav", ".flac"],
    "Archives": [".zip", ".rar", ".tar", ".gz"],
    "Scripts": [".py", ".js", ".java", ".c", ".cpp", ".html", ".css"],
}

# ---------- FUNCTION TO GET FOLDER NAME ----------
def get_folder_for_file(filename, date_based=False):
    ext = os.path.splitext(filename)[1].lower()

    if date_based:
        # Date-based folder: YYYY-MM
        timestamp = os.path.getmtime(filename)
        folder_name = datetime.fromtimestamp(timestamp).strftime("%Y-%m")
        return folder_name

    for folder, extensions in FILE_TYPES.items():
        if ext in extensions:
            return folder
    return "Others"

# ---------- ORGANIZER FUNCTION ----------
def organize_directory(directory, date_based=False):
    if not os.path.exists(directory):
        print("❌ Directory does not exist.")
        return

    moves = []  # track moves for undo

    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)

            # Skip if it's already inside a categorized folder
            if root != directory:
                continue

            folder_name = get_folder_for_file(file_path, date_based)
            folder_path = os.path.join(directory, folder_name)
            os.makedirs(folder_path, exist_ok=True)

            dest_path = os.path.join(folder_path, file)

            try:
                shutil.move(file_path, dest_path)
                moves.append((file_path, dest_path))
                print(f"✅ Moved: {file} → {folder_name}/")
            except Exception as e:
                print(f"❌ Error moving {file}: {e}")

    # Save moves to log for undo
    if moves:
        with open(LOG_FILE, "w") as log:
            for src, dst in moves:
                log.write(f"{src}|{dst}\n")

# ---------- UNDO FUNCTION ----------
def undo_last_organization():
    if not os.path.exists(LOG_FILE):
        print("❌ No previous organization found to undo.")
        return

    with open(LOG_FILE, "r") as log:
        moves = [line.strip().split("|") for line in log]

    for src, dst in moves:
        if os.path.exists(dst):
            os.makedirs(os.path.dirname(src), exist_ok=True)
            shutil.move(dst, src)
            print(f"🔄 Restored: {os.path.basename(dst)} → {src}")

    os.remove(LOG_FILE)  # clear log after undo
    print("✅ Undo complete! Files restored.")

# ---------- MAIN CLI ----------
def main():
    print("=== Automated File Organizer ===")
    print("1. Organize by File Type")
    print("2. Organize by Date (YYYY-MM)")
    print("3. Undo Last Organization")
    choice = input("Enter choice: ").strip()

    if choice == "1":
        directory = input("Enter directory to organize: ").strip()
        organize_directory(directory, date_based=False)
    elif choice == "2":
        directory = input("Enter directory to organize: ").strip()
        organize_directory(directory, date_based=True)
    elif choice == "3":
        undo_last_organization()
    else:
        print("❌ Invalid choice.")

if __name__ == "__main__":
    main()
