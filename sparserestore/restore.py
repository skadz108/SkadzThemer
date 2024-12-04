from . import backup
from pymobiledevice3.lockdown import create_using_usbmux
from pymobiledevice3.services.mobilebackup2 import Mobilebackup2Service
from tempfile import TemporaryDirectory
from pathlib import Path

def restore_file(fp: str, restore_path: str, restore_name: str):
    contents = open(fp, "rb").read()

    back = backup.Backup(files=[
        backup.Directory("", "RootDomain", owner=33, group=33),
        backup.Directory("Library", "RootDomain", owner=33, group=33),
        backup.Directory("Library/Preferences", "RootDomain", owner=33, group=33),
        backup.ConcreteFile("Library/Preferences/sparsetemp", "RootDomain", owner=33, group=33, contents=contents),
        backup.Directory("", f"SysContainerDomain-../../../../../../../../var/.backup.i{restore_path}", owner=33, group=33),
        backup.ConcreteFile("", f"SysContainerDomain-../../../../../../../../var/.backup.i{restore_path}{restore_name}", owner=33, group=33, contents=contents),
            backup.Directory("", "SysContainerDomain-../../../../../../../../var/.backup.i/var/root/Library/Preferences/sparsetemp", owner=33, group=33),
    ])

    with TemporaryDirectory() as backup_dir:
        backup_dir_path = Path(backup_dir)
        back.write_to_directory(backup_dir_path)
        
        lockdown = create_using_usbmux()
        with Mobilebackup2Service(lockdown) as mb:
            mb.restore(backup_dir, system=True, reboot=False, copy=False, source=".")
