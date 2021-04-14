def parse_export(export):
    parsed = []
    for line in export.splitlines():
        parsed.append(
            line.split("\t")
        )
    return parsed
