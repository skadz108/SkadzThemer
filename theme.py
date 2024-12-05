import platform
import sys

from sparserestore import backup, perform_restore
from sparserestore.restore import restore_file
from pymobiledevice3.services.installation_proxy import InstallationProxyService
from pymobiledevice3.services.diagnostics import DiagnosticsService
from pymobiledevice3.exceptions import NoDeviceConnectedError
from pymobiledevice3.lockdown import create_using_usbmux
from pathlib import Path

def exit(code=0):
    if platform.system() == "Windows" and getattr(sys, "frozen", False) and hasattr(sys, "_MEIPASS"):
        input("Press Enter to exit...")

    sys.exit(code)

try:
    lockdown = create_using_usbmux()
except NoDeviceConnectedError:
        print("No device connected!")
        print("Please connect your device and try again.")
        exit(1)

def get_nice_ios_version_string():
    os_names = {
        "iPhone": "iOS",
        "iPad": "iPadOS",
        "iPod": "iOS",
        "AppleTV": "tvOS",
        "Watch": "watchOS",
        "AudioAccessory": "HomePod Software Version",
        "RealityDevice": "visionOS",
    }
    device_class = lockdown.get_value(key="DeviceClass")
    product_version = lockdown.get_value(key="ProductVersion")
    os_name = (os_names[device_class] + " " + product_version) if device_class in os_names else ""
    return os_name
    
def create_catalog_symlinks():
    apps = InstallationProxyService(lockdown).get_apps(calculate_sizes=False, application_type="User")
    catalog_backup = []
    catalog_backup.append(backup.Directory("", "SysContainerDomain-../../../../../../../../var/mobile/Library/Logs/RTCReporting/"))
    for key, value in apps.items():
        if isinstance(value, dict) and "Path" in value:
            app_path = Path(value["Path"])
            catalog_path = Path.joinpath(app_path, 'Assets.car').as_posix()
            app_name = Path(catalog_path).parent.name.replace('.app', '')
#            print(f"app path: {app_path.as_posix()}")
#            print(f"app name: {app_name}")
#            print(catalog_path)
            catalog_backup.append(backup.SymbolicLink("", f"SysContainerDomain-../../../../../../../../var/mobile/Library/Logs/RTCReporting/{app_name}-Assets.car.txt", f"{catalog_path}"))
#    print(catalog_backup)
    return catalog_backup
    
def apply_catalog():
    target_path = input("Enter the path to the asset catalog on your iDevice: ")
    parts = target_path.split('/')

    restore_path = '/'.join(parts[:-1]) + '/'
    restore_name = parts[-1]

    input_catalog_path = input("Enter the path to your themed asset catalog: ")

    input(f"Press Enter to overwrite {restore_name} with {Path(input_catalog_path).name}...")

    restore_file(fp=input_catalog_path, restore_path=restore_path, restore_name=restore_name)

def grab_catalog_path():
    apps = InstallationProxyService(lockdown).get_apps(calculate_sizes=False, application_type="User")
    app = input("Enter the bundle name of the app: ")
    if not app.endswith(".app"):
        app += ".app"
    for key, value in apps.items():
        if isinstance(value, dict) and "Path" in value:
            app_path = Path(value["Path"])
            catalog_path = Path.joinpath(app_path, 'Assets.car').as_posix()
            if app_path.name.lower() == app.lower():
                print(f"Successfully grabbed path to {app.replace('.app', '')}'s asset catalog!\nCatalog path: {catalog_path}")
                return
            # print(f"app path: {app_path.as_posix()}")
            # print(catalog_path)

def menu():
    print(f"""
                  SkadzThemer v1.0
              Brought to you by Skadz

      Connected to {lockdown.get_value(key="DeviceName")} ({get_nice_ios_version_string()})
        
         === Please select an option. ===
    """)
    print("""
      [1] : Create symlinks to asset catalogs
      [2] : Apply themed asset catalog
      [3] : Grab path to app's asset catalog
            
      [0] : Exit
    """)
    option = None
    try:
        user_input = input('Enter a number: ')
        if user_input.strip():
            option = int(float(user_input))
        else:
            input("Please select an option. Press Enter to continue.")
            menu()
    except ValueError:
        input("Please enter a valid number. Press Enter to continue.")
        menu()

    if option is not None:
        if option == 1:
            back = backup.Backup(files=create_catalog_symlinks())
            perform_restore(back, reboot=False)
        elif option == 2:
            apply_catalog()
        elif option == 3:
            grab_catalog_path()
        elif option == 0:
            print("Thanks for using SkadzThemer!")
            exit()
        else:
            input("Please select a valid option. Press Enter to continue.")
            menu()

menu()
