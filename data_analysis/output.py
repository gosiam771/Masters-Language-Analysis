def save_results(output_file, result):
    with open(output_file, "a", encoding="utf-8") as f:
        f.write(f'{result}\n\n')