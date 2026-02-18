def clean_transcript(text):
    lines = text.split(".")
    filtered = []

    for line in lines:
        line = line.strip()

        # remove very short dialogue fragments
        if len(line.split()) < 4:
            continue

        # remove repeated phrases
        if filtered and line == filtered[-1]:
            continue

        filtered.append(line)

    return ". ".join(filtered)