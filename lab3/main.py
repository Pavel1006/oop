import os
from datetime import datetime

class File:
    def __init__(self, filepath):
        self.filepath = filepath
        self.filename = os.path.basename(filepath)
        self.extension = os.path.splitext(filepath)[1]
        self.creation_time = datetime.fromtimestamp(os.path.getctime(filepath))
        self.last_modified_time = datetime.fromtimestamp(os.path.getmtime(filepath))
        self._snapshot_time = self.last_modified_time

    def info(self):
        return f"Filename: {self.filename}\nExtension: {self.extension}\nCreation Date: {self.creation_time}\nLast Modified Date: {self.last_modified_time}"

    def is_changed(self):
        current_modified_time = datetime.fromtimestamp(os.path.getmtime(self.filepath))
        return current_modified_time > self._snapshot_time

    def commit(self):
        self._snapshot_time = datetime.fromtimestamp(os.path.getmtime(self.filepath))


class ImageFile(File):
    def info(self):
        base_info = super().info()
        dimensions = "800x600" if self.extension in [".png", ".jpg"] else "N/A"  # Simulating dimensions
        return f"{base_info}\nDimensions: {dimensions}"


class TextFile(File):
    def info(self):
        base_info = super().info()
        with open(self.filepath, 'r') as file:
            content = file.read()
        lines = len(content.splitlines())
        words = len(content.split())
        characters = len(content)
        return f"{base_info}\nLine Count: {lines}\nWord Count: {words}\nCharacter Count: {characters}"


class ProgramFile(File):
    def info(self):
        base_info = super().info()
        with open(self.filepath, 'r') as file:
            content = file.readlines()
        class_count = sum(1 for line in content if line.strip().startswith("class "))
        method_count = sum(1 for line in content if line.strip().startswith("def "))
        return f"{base_info}\nLine Count: {len(content)}\nClass Count: {class_count}\nMethod Count: {method_count}"


class DocumentChangeDetectionSystem:
    def __init__(self, folder_path):
        self.folder_path = folder_path
        self.files = []
        self.scan_folder()

    def scan_folder(self):
        self.files = []
        for root, _, filenames in os.walk(self.folder_path):
            for filename in filenames:
                filepath = os.path.join(root, filename)
                extension = os.path.splitext(filepath)[1]

                if extension in [".png", ".jpg"]:
                    self.files.append(ImageFile(filepath))
                elif extension == ".txt":
                    self.files.append(TextFile(filepath))
                elif extension in [".py", ".java"]:
                    self.files.append(ProgramFile(filepath))
                else:
                    self.files.append(File(filepath))

    def commit(self):
        for file in self.files:
            file.commit()
        print("Snapshot updated. All files marked as clean.")

    def info(self, filename):
        for file in self.files:
            if file.filename == filename:
                print(file.info())
                return
        print("File not found.")

    def status(self):
        for file in self.files:
            status = "Changed" if file.is_changed() else "Unchanged"
            print(f"{file.filename}: {status}")

    def run(self):
        while True:
            command = input("Enter command (git commit, git info <filename>, git status, git exit): ").strip()
            if command == "git commit":
                self.commit()
            elif command.startswith("info"):
                _, filename = command.split(" ", 1)
                self.info(filename)
            elif command == "git status":
                self.status()
            elif command == "git exit":
                print("Exiting program.")
                break
            else:
                print("Invalid command.")


if __name__ == "__main__":
    folder_path = "./monitor_folder"  # Specify the folder to monitor
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)  # Create the folder if it doesn't exist

    system = DocumentChangeDetectionSystem(folder_path)
    system.run()
