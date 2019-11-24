import getpass
import gkeepapi
import os
import sys
import dateutil.parser
import click


PathSeparator = os.path.sep
WorkingDir = os.getcwd()

assert WorkingDir.rpartition(PathSeparator)[2] == "iCloud Notes", 'Working dir must be "iCloud Notes"!'

keep = gkeepapi.Keep()

login = input("Login (Google account email):")
password = getpass.getpass()
try:
    success = keep.login(login, password)
    assert success
except Exception as e:
    print(f"Failed to login! {e}")
    sys.exit()

keep.sync()
notes = []
for root, folders, files in os.walk(WorkingDir + PathSeparator):
    for fname in files:
        label = root.split(PathSeparator)[-2]
        name = root.split(PathSeparator)[-1]
        date = fname.replace(name + '-', "").replace(".txt", "").replace("_", ":")
        if "Attachments" not in root:
            if os.path.basename(__file__) not in fname:
                with open(f"{root}{PathSeparator}{fname}", encoding="utf-8") as file:
                    text = file.read()
                    text = text.partition('\n')[2]  # drop first line (header)
                    notes.append((label, name, date, text))
        else:  # add attachments to last note
            # not implemented in gkeepapi yet
            continue
prev_len = len(keep.all())
if len(notes):
    if input(f"Found {len(notes)} notes. Do you want to push them into Google Keep? (Y\\n)") == 'Y':
        try:
            with click.progressbar(notes) as bar:
                for label, name, date, text in bar:
                    keep_label = keep.findLabel(label)
                    new_note = keep.createNote(name, text)
                    new_note.labels.add(keep_label if keep_label else keep.createLabel(label))
                    try:
                        new_note.timestamps.created = dateutil.parser.parse(date)
                    except:
                        pass  # don't bother, if couldn't parse date
                    keep.sync(())
            print(f"\n{len(keep.all()) - prev_len} notes successfully imported")
        except Exception as e:
            print(e)
            cnt = len(keep.all()) - prev_len
            if cnt:
                input(f"Only {cnt} notes were successfully imported")
else:
    print(f"Notes not found")

