def copy_file(command: str) -> None:
    parts = command.split()
    if len(parts) == 3 and parts[0] == "cp":
        if not parts[2] == parts[1]:
            try:
                with (open(parts[1])
                      as source_file, open(parts[2], "w") as destination_file):
                    destination_file.write(source_file.read())
            except FileNotFoundError:
                return
