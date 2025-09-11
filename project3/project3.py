import os
from PIL import Image
from concurrent.futures import ThreadPoolExecutor

# --------- IMAGE OPERATIONS ---------
def resize_image(img, size):
    return img.resize(size)

def convert_grayscale(img):
    return img.convert("L")

def rotate_image(img, angle):
    return img.rotate(angle, expand=True)

# --------- PROCESS FUNCTION ---------
def process_image(filepath, output_dir, operations):
    try:
        img = Image.open(filepath)
        filename = os.path.basename(filepath)

        # Apply each operation in sequence
        for op in operations:
            if op["type"] == "resize":
                img = resize_image(img, op["size"])
                filename = f"resized_{filename}"
            elif op["type"] == "grayscale":
                img = convert_grayscale(img)
                filename = f"gray_{filename}"
            elif op["type"] == "rotate":
                img = rotate_image(img, op["angle"])
                filename = f"rotated_{filename}"

        # Save output
        os.makedirs(output_dir, exist_ok=True)
        output_path = os.path.join(output_dir, filename)
        img.save(output_path)
        print(f"✅ Processed: {filename}")

    except Exception as e:
        print(f"❌ Error processing {filepath}: {e}")

# --------- BATCH PROCESSING ---------
def batch_process(input_dir, output_dir, operations):
    supported_ext = (".jpg", ".jpeg", ".png")
    files = [os.path.join(input_dir, f) for f in os.listdir(input_dir) if f.lower().endswith(supported_ext)]

    if not files:
        print("❌ No image files found in input directory.")
        return

    print(f"📂 Found {len(files)} images. Processing...")

    # Concurrent processing
    with ThreadPoolExecutor() as executor:
        for filepath in files:
            executor.submit(process_image, filepath, output_dir, operations)

# --------- CLI MENU ---------
def main():
    print("=== Image Processing Utility ===")
    input_dir = input("Enter input directory path: ").strip()
    output_dir = input("Enter output directory path: ").strip()

    operations = []

    print("\nSelect operations to apply (multiple allowed).")
    print("1. Resize Images")
    print("2. Convert to Grayscale")
    print("3. Rotate Images")
    print("4. Done selecting")
    
    while True:
        choice = input("Enter choice: ").strip()
        if choice == "1":
            width = int(input("Enter new width: "))
            height = int(input("Enter new height: "))
            operations.append({"type": "resize", "size": (width, height)})
        elif choice == "2":
            operations.append({"type": "grayscale"})
        elif choice == "3":
            angle = int(input("Enter rotation angle (e.g., 90): "))
            operations.append({"type": "rotate", "angle": angle})
        elif choice == "4":
            break
        else:
            print("❌ Invalid choice.")

    if not operations:
        print("❌ No operations selected. Exiting.")
        return

    batch_process(input_dir, output_dir, operations)


if __name__ == "__main__":
    main()
