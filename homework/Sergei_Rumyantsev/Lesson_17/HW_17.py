import argparse
import os


def search_in_file(file_path: str, search_text: str):
    results = []
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        for line_number, line in enumerate(f, start=1):
            if search_text in line:
                words = line.strip().split()
                indices = [
                    i for i, word in enumerate(words) if search_text in word
                    ]

                for idx in indices:
                    start = max(idx - 5, 0)
                    end = min(idx + 6, len(words))
                    snippet = " ".join(words[start:end])
                    results.append((line_number, snippet))
    return results


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('filepath', type=str, help='File_path')
    parser.add_argument('--text', type=str, required=True, help='Searched_text')
    args = parser.parse_args()

    log_dir = args.filepath
    search_text = args.text

    if not os.path.isdir(log_dir):
        print(f"Ошибка: {log_dir} не является папкой")
        return

    for filename in os.listdir(log_dir):
        file_path = os.path.join(log_dir, filename)

        if not os.path.isfile(file_path):
            continue

        results = search_in_file(file_path, search_text)
        if results:
            for line_number, snippet in results:
                print(f"""
                      File Name: '{filename}', 
                      line number: '{line_number}' 
                      and snippet: '{snippet}'
                      """)


if __name__ == "__main__":
    main()
