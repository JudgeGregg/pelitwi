import os

HOME = os.environ["HOME"]
TWISTED_DOCSOURCE_ROOT = (
    HOME + "/Projects/Python/twisource/twistedmatrix.com/documents/current/_sources"
)
print(TWISTED_DOCSOURCE_ROOT)


def handle_file(root, filename):
    if filename == "index.rst.txt":
        print("skipping: " + filename)
        return
    with open(os.path.join(root, filename)) as file_:
        lines = []
        for line in file_.readlines():
            if ":doc:" in line:
                line = handle_line_doc(line)
            line = handle_line_sphinx(line)
            if ":download:" in line:
                line = handle_line_download(line)
            if "literalinclude::" in line:
                continue
            if ":LastChanged" in line:
                continue
            if "versionadded:" in line:
                line = line.replace(".. versionadded:", "versionadded")
            if ":emphasize-lines:" in line:
                continue
            if ":caption:" in line:
                continue
            if "toctree::" in line:
                continue
            if line:
                lines.append(line)
        if ".. contents:: Table Of Contents\n" not in lines:
            lines.append("\n")
            lines.append(".. contents:: Table Of Contents\n")
        filename = filename.replace(".txt", "")
        with open(os.path.join(root, filename), "w") as file_out:
            file_out.writelines(lines)


def handle_line_doc(line):
    line = line.replace(":doc:", "")
    index = line.find("<")
    new_line = line[: index + 1] + "{filename}" + line[index + 1 :]
    index = new_line.find(">")
    line = new_line[:index] + ".rst" + new_line[index:]
    new_index = line.find("`", index)
    new_line = line[: new_index + 1] + "_" + line[new_index + 1 :]
    return new_line


def handle_line_sphinx(line):
    line = line.replace(":py:class:", "")
    line = line.replace(":py:func:", "")
    line = line.replace(":py:meth:", "")
    line = line.replace(":py:mod:", "")
    line = line.replace(":py:attr:", "")
    line = line.replace(":mod:", "")
    line = line.replace(":ref:", "")
    line = line.replace(":func:", "")
    line = line.replace(":data:", "")
    return line


def handle_line_download(line):
    line = line.replace(":download:", "")
    return line


if __name__ == "__main__":
    count = 0
    for (root, dirs, files) in os.walk(TWISTED_DOCSOURCE_ROOT):
        for filename in files:
            if filename.endswith(".rst.txt"):
                count += 1
                handle_file(root, filename)
    print(count)
