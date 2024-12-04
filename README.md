# SkadzThemer
Catalog icon theming using [SparseRestore](https://github.com/JJTech0130/TrollRestore/tree/main/sparserestore) & [BroccoliAnalytics](https://github.com/jailbreakdotparty/BroccoliAnalytics) 

## Disclaimer
I am not responsible if you bootloop! Please follow the usage steps carefully and back up your data before using.

## Usage
1. Install `pymobiledevice3` in your Python environment.
2. Run `theme.py` with your device plugged in.
3. Follow the steps to grab and theme your asset catalogs (shown below)
4. After moving the themed catalogs to your computer, select option 2
5. Enter the path to the app's asset catalog (this can be grabbed with option 3)
6. Enter the path to the themed catalog on your computer
7. Hit Enter to apply the themed catalog
8. Reboot your device and profit!

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
2. Import an asset catalog, and a PNG icon (1024x1024 is recommended, other resolutions may cause issues)
3. Theme the catalog, and send the file to your computer
4. Continue the regular usage steps

## Credits
- [Skadz](https://github.com/skadz108) for writing this script and making [CatalogHelper](https://github.com/skadz108/CatalogHelper).
- [SparseThemer](https://github.com/haxi0/SparseThemer) for the catalog modification code used in CatalogHelper.
- [Duy Tran](https://github.com/khanhduytran0) for discovering the exploit used in BroccoliAnalytics.
- [JJTech/the TrollRestore authors](https://github.com/JJTech0130/TrollRestore) for SparseRestore and its backup code.
- [the jailbreak.party team](https://github.com/jailbreakdotparty) for assistance and testing.
