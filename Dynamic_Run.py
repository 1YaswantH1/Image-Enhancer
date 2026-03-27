import subprocess
import os

print("Choose input type:")
print("1 → Single Image")
print("2 → Folder of Images")

choice = input("Enter 1 or 2: ").strip()

# -----------------------------
# Get Input Path
# -----------------------------
if choice == "1":
    input_path = input("Enter image file path: ").strip()
    if not os.path.isfile(input_path):
        print("Error: File does not exist")
        exit()

elif choice == "2":
    input_path = input("Enter folder path: ").strip()
    if not os.path.isdir(input_path):
        print("Error: Folder does not exist")
        exit()

else:
    print("Invalid choice")
    exit()

input_path = os.path.abspath(input_path)
print("\nInput Path:", input_path)

# -----------------------------
# RealESRGAN Setup
# -----------------------------
realesrgan_path = os.getcwd()
venv_python = f"{realesrgan_path}/venv/bin/python"

output_folder = os.path.join(realesrgan_path, "results")

# Create output folder if not exists
os.makedirs(output_folder, exist_ok=True)

# -----------------------------
# Run RealESRGAN
# -----------------------------
print("\nRunning RealESRGAN Noise Removal...")

subprocess.run(
    [
        venv_python,
        "inference_realesrgan.py",
        "-n",
        "RealESRGAN_x4plus",
        "-i",
        input_path,
        "-o",
        output_folder,
        "--fp32",
    ],
    cwd=realesrgan_path,
)

print("\nNoise Removal Completed Successfully")
print("📁 Output saved in:", output_folder)
