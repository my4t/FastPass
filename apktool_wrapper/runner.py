
import subprocess


def run_apktool(apk_path, output_dir, apktool_path):
    try:
        subprocess.run(["java", "-jar", apktool_path, "d", apk_path, "-o", output_dir, "-f"], stdout=subprocess.DEVNULL, check=True)
        print("Decompiling...")
        print(f"Decompiled APK to {output_dir}")
    except subprocess.CalledProcessError as e:
        print(f"Error running apktool: {e}")

