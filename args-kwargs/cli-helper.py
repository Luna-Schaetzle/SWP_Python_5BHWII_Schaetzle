import os
import shutil

class CLIHelper:
    def __init__(self):
        self.commands = {
            "put": self.put,
            "copy": self.copy,
            "move": self.move,
            "rename": self.rename,
            "delete": self.delete
        }

    def process_input(self, user_input: str):
        parts = user_input.lower().split()
        command = parts[0]
        
        if command in self.commands:
            self.commands[command](*parts[1:])
        else:
            print(f"Unbekannter Befehl: {command}")

    def put(self, *args, **kwargs):
        # Beispiel: put text.txt into new folder testfolder
        if len(args) == 4 and args[1] == "into" and args[3] == "folder":
            self._create_folder(args[2])
            self._move_file(args[0], args[2])
            

    def copy(self, *args, **kwargs):
        # Beispiel: copy text.txt 10 times in folder
        if len(args) == 5 and args[3] == "in" and args[4] == "folder":
            self._create_folder(args[2])
            self._copy_file(args[0], args[2], int(args[1]))

    def move(self, *args, **kwargs):
        # Beispiel: move text.txt into folder backup
        if len(args) == 4 and args[1] == "into" and args[3] == "folder":
            self._move_file(args[0], args[2])

    def rename(self, *args, **kwargs):
        # Beispiel: rename text.txt to newtext.txt
        if len(args) == 4 and args[1] == "to":
            self._rename_file(args[0], args[3])

    def delete(self, *args, **kwargs):
        # Beispiel: delete text.txt
        if len(args) == 1:
            self._delete_file(args[0])

    def _create_folder(self, folder_name):
        def log_action(action):
            print(f"Aktion: {action}")

        if not os.path.exists(folder_name):
            os.makedirs(folder_name)
            log_action(f"Ordner {folder_name} erstellt.")
        else:
            log_action(f"Ordner {folder_name} existiert bereits.")

    def _move_file(self, file_name, folder_name):
        def log_action(action):
            print(f"Aktion: {action}")

        if os.path.exists(file_name):
            shutil.move(file_name, os.path.join(folder_name, file_name))
            log_action(f"Datei {file_name} nach {folder_name} verschoben.")
        else:
            log_action(f"Datei {file_name} existiert nicht.")

    def _copy_file(self, file_name, folder_name, times):
        def log_action(action):
            print(f"Aktion: {action}")

        if os.path.exists(file_name):
            for i in range(1, times + 1):
                new_file_name = f"{i}_{file_name}"
                shutil.copy(file_name, os.path.join(folder_name, new_file_name))
                log_action(f"Datei {file_name} als {new_file_name} kopiert.")
        else:
            log_action(f"Datei {file_name} existiert nicht.")

    def _rename_file(self, old_name, new_name):
        def log_action(action):
            print(f"Aktion: {action}")

        if os.path.exists(old_name):
            os.rename(old_name, new_name)
            log_action(f"Datei {old_name} in {new_name} umbenannt.")
        else:
            log_action(f"Datei {old_name} existiert nicht.")

    def _delete_file(self, file_name):
        def log_action(action):
            print(f"Aktion: {action}")

        if os.path.exists(file_name):
            os.remove(file_name)
            log_action(f"Datei {file_name} gelöscht.")
        else:
            log_action(f"Datei {file_name} existiert nicht.")

# Beispielverwendung
cli_helper = CLIHelper()

# Beispielbefehle
cli_helper.process_input("put text.txt into new folder testfolder")
#cli_helper.process_input("copy text.txt 5 times in folder backupfolder")
#cli_helper.process_input("move text.txt into folder new_folder")
#cli_helper.process_input("rename text.txt to new_text.txt")
#cli_helper.process_input("delete text.txt")
