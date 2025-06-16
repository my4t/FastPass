
EXCLUDED_PREFIXES = (
    "android",
    "androidx",
    "javax",
    "kotlin",
    "kotlinx",
    "io",
    "okhttp3",
    "com.google",
    "com.microsoft",
    "com.reactnativecommunity",
    "pushnotification",
)

def extract_libs(decompiled_dir):

    package_set = set()

    
    smali_dirs = [d for d in decompiled_dir.iterdir() if d.is_dir() and d.name.startswith("smali")]

    for smali_dir in smali_dirs:
        for path in smali_dir.rglob("*"):
            if path.is_dir():
                parts = path.relative_to(smali_dir).parts
                if len(parts) >= 3:
                    package = ".".join(parts[:3])
                    if not package.startswith(EXCLUDED_PREFIXES):
                        package_set.add(package)

    return sorted(package_set)


def extract_nativelibs(decompiled_path):
    lib_dir = decompiled_path / "lib"
    so_files = set()

    if not lib_dir.exists():
        print("[i] No lib/ folder found. Skipping native libraries.")
        return []

    for so_file in lib_dir.rglob("*.so"):
        so_files.add(so_file.name.split('.')[0])

    return sorted(so_files)

def detect_framework(packages, nativelibs):
    
    for i in packages:
        if "reactnative" in i and ("libreactnative" in nativelibs or "libreact_utils" in nativelibs):
            return "React Native"

        if "flutter" in i and "libflutter" in nativelibs:
            return "Flutter"
        
    return "No Framework or other one"