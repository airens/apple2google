# Apple2Google notes converter
This script converts notes from Apple devices (iPhone, iPad, iMac) to Google Keep format (Android devices and other).

## Conversion info and limitations
1. This version of the script can't attach any media data to the notes due to the [gkeepapi](https://github.com/kiwiz/gkeepapi) limitations
2. Checklists will be just raw text, because of Apple exporting it's data in completely simplified format
3. Folders from Apple's notes will be replaced by Google's tags
4. Note's headers for Google Keep will be created from the first lines of Apple's notes  


## Getting notes data from Apple's iCloud:
1. Go to <https://appleid.apple.com/> 
2. In `Data & Privacy` section follow the `Manage Your Data and Privacy` link
3. In `Manage your data` section click on `Request a copy of your data`
4. Select `iCloud Notes` and click `Continue`
5. Push `Complete request`
6. Wait for Apple to send you email with the confirmation that your data is ready (it can take several days) and download it from the <https://appleid.apple.com/> site

## Conversion
1. Unpack the `iCloud Notes.zip` archive and put `convert.py` into the `iCloud Notes` folder
2. Install Python packages from `requirements.txt`, if needed
3. Run the script by the command `python convert.py` and follow the instructions
