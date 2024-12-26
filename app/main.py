def main() -> None:
    file_name = input("Enter name of the file: ")
    if not file_name.endswith(".txt"):
        file_name += ".txt"
    content = []
    while True:
        line = input("Enter new line of content: ")
        if line.lower() == "stop":
            break
        content.append(line)
    with open(file_name, "w") as file:
        file.write("\n".join(content))

    file.close()


if __name__ == "__main__":
    main()
