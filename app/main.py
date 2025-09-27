def copy_file(command: str) -> None:
    split_command = command.split(" ")
    if len(split_command) == 3 and split_command[0] == "cp":
        if not split_command[2] == split_command[1]:
            try:
                with (open(split_command[1])
                      as src, open(split_command[2], "w") as dst):
                    dst.write(src.read())
            except FileNotFoundError:
                return
