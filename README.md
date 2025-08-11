# UNMAINTAINED
This was one of my first projects, and while it does work, I can't offer support for it any longer. The current process is very tedious and the code for both the script and helper app need some serious rewriting.

If you're interested in using SkadzThemer, please wait for v2 to release.
CatalogHelper v2 will introduce fully automatic catalog theming and extraction, and will only require one file in the SkadzThemer script to apply a full icon set.

I cannot offer an ETA on when/if v2 will release, or any technical details, however this repository and project will be updated in the event it does release.

Until then, consider this project discontinued. Original README follows below.

# SkadzThemer
Catalog icon theming using [SparseRestore](https://github.com/JJTech0130/TrollRestore/tree/main/sparserestore) & [BroccoliAnalytics](https://github.com/jailbreakdotparty/BroccoliAnalytics)

Supports iOS 17.0-17.7 and iOS 18.0-18.1 beta 4.

## Disclaimer & Limitations
**Disclaimer**

I am not responsible if you bootloop! Please follow the usage steps carefully and back up your data before using.

**Limitations**

- This can only theme User apps and removable system apps (e.g. Tips). System apps cannot be themed, as they aren't in `/var/`.
- There is no way to forcefully trigger an icon cache refresh (which is needed for custom icons to show up). On iOS 17, it sometimes refreshes after rebooting, but this can be inconsistent. iOS 18 users may be able to make custom icons show by messing with the icon customization feature (e.g. toggling between tinted and dark icons).
- Grabbing each catalog is fairly tedious

## Usage
1. Install `pymobiledevice3` in your Python environment.
2. Run `theme.py` with your device plugged in.
3. Follow the steps to grab and theme your asset catalogs (shown below)
4. After moving the themed catalogs to your computer, select option 2
5. Enter the name of the app you'd like to theme
6. Enter the path to the themed catalog on your computer
7. Hit Enter to apply the themed catalog
8. Repeat steps 4-7 for each app
9. Reboot your device and profit!

## Grabbing and theming catalogs
**Grabbing catalogs**

To grab the original catalogs, we'll use option 1 in SkadzThemer, which creates symlinks to each asset catalog in the Analytics Data menu in Settings.
This only needs to be done once, afterwards you can theme the existing copies of the catalogs.

1. Select option 1 in SkadzThemer
2. Open Settings on your device, and go to Privacy & Security > Analytics & Improvements > Analytics Data
3. Select the `Assets.car.txt` file for your app, and hit the Share icon in the corner
4. Select Messages, and drag & drop the attachment into the Files app.
5. Remove the `.txt` at the end of the file name, leaving it as a `.car` file
6. Repeat steps 3-5 for each catalog

**Theming catalogs**

The framework used to modify catalogs only works on Apple systems, so we'll sideload the [CatalogHelper](https://github.com/skadz108/CatalogHelper) app to theme the catalogs on our device.

1. Sideload the latest [CatalogHelper](https://github.com/skadz108/CatalogHelper/releases/latest) .ipa onto your device
2. Import an asset catalog, and a PNG icon
3. Theme the catalog, and send the file to your computer
4. Repeat steps 2-3 for each app's catalog
5. Continue the regular usage steps

## Credits
- [Skadz](https://github.com/skadz108) for writing this script and making [CatalogHelper](https://github.com/skadz108/CatalogHelper).
- [SparseThemer](https://github.com/haxi0/SparseThemer) & [PrivateKits](https://github.com/NSAntoine/PrivateKits/tree/haxi-test) for the catalog modification/theming code used in CatalogHelper.
- [Duy Tran](https://github.com/khanhduytran0) for discovering the exploit used to read the catalogs.
- [JJTech/the TrollRestore authors](https://github.com/JJTech0130/TrollRestore) for SparseRestore.
