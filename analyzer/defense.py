custom_bypass = ['KishorBal/multiple-root-detection-bypass', 'fdciabdul/frida-multiple-bypass']
rootbeer_bypass = ['ub3rsick/rootbeer-root-detection-bypass', 'Zero3141/rootbeer-root-detection-bypass']
jailmonkey_bypass = ['RohindhR/react-native-jail-monkey-bypass-all-checks', 'anubi5egypt/jailmonkey-root-detection-bypass']
sslbypass_res = ['pcipolloni/universal-android-ssl-pinning-bypass-with-frida', 'Q0120S/bypass-ssl-pinning']

def check_rootlibs(libraries):
    for i in libraries:
        if "scottyab" in i:
            return rootbeer_bypass
        if "gantix" in i:
            return jailmonkey_bypass
    return custom_bypass

def ssl_bypass(framework):
    if framework == "Flutter":
        print("Try any of the methods that work for you.")
        print("================================================================================================")
        print("1. frida -U --codeshare TheDauntless/disable-flutter-tls-v1 -f [package_name]")
        print("2. Set up Proxy Droid in testing device.")
        print("3. reflutter [app.apk] and sign the generated apk file with uberapksigner.")
        print("Nothing work? Installing burp CA as system certificate in testing device and retry above methods.")
        print("================================================================================================")
    else:
        for i in sslbypass_res:
            print(f"frida -U --codeshare {i} -f [package_name]")
        