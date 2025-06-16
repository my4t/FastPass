import sys, os, tempfile
from pathlib import Path
from apktool_wrapper.runner import run_apktool
from analyzer.arch import *
from analyzer.defense import *
import argparse

decompiled_path = Path(os.path.join(tempfile.gettempdir(), "decompiledAPK"))
libraries = set()
nativelibs = set()

def is_apk_file(file_path):
    return os.path.isfile(file_path) and file_path.lower().endswith('.apk')

def main():

    parser = argparse.ArgumentParser(description="Process some inputs.")
    parser.add_argument('-a', '--apk', required=True, help='Path to APK')
    parser.add_argument('-p', '--path', required=True, help='Path to Apktool Jar file')

    args = parser.parse_args()
    apk_path = args.apk
    apktool_path = args.path

    if not is_apk_file(args.apk):
        print("Error: The provided file is not a valid .apk file.")
        sys.exit(1)

    print(f"APK file received: {apk_path}")

    run_apktool(Path(apk_path), decompiled_path, Path(apktool_path))

    libraries = extract_libs(decompiled_path)
    print("[+] Libraries List Extracted!")
    
    nativelibs = extract_nativelibs(decompiled_path)
    print("[+] Native Libraries Extracted!")
    

    framework = detect_framework(libraries, nativelibs)

    print(f"[+] The app used {framework} framework.")
    print()

    print("Bypass Root Detection with these scripts. (if require)")
    print("######################################################")
    for i in check_rootlibs(libraries):
        print(f"frida --codeshare {i} -U -f [package_name]")
    
    print()

    print("Bypass ssl pinning with these scripts. (if require)")
    print("######################################################")
    ssl_bypass(framework)


    

if __name__ == "__main__":
    main()
