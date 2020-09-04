def finder(paths, files):
    files_table = {}

    for name in files:
        files_table[name] = None

    matches = []

    for path in paths:
        if path.split("/")[-1] in files_table:
            matches.append(path)

    return matches


if __name__ == "__main__":
    paths = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    files = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(paths, files))
