import sys
import os

def split_legacy_file(input_path):
    if not os.path.exists(input_path):
        print(f"❌ Error: File '{input_path}' not found.")
        return

    print(f"Processing '{input_path}'...")

    current_file = None
    file_count = 0

    with open(input_path, 'r', encoding='utf-8') as f:
        for line in f:
            stripped = line.strip()

            # Check for the file delimiter
            if stripped.startswith("FILE:"):
                # Close previous file if open
                if current_file:
                    current_file.close()

                # Extract filename (remove "FILE:" and whitespace)
                filename = stripped.replace("FILE:", "").strip()

                print(f"   --> Creating: {filename}")
                current_file = open(filename, 'w', encoding='utf-8')
                file_count += 1
                continue

            # If we have an open file, write the content
            if current_file:
                # Optional: Skip blank lines at the very top of the file
                # to keep the HTML clean
                if current_file.tell() == 0 and stripped == "":
                    continue

                current_file.write(line)

    # Close the final file
    if current_file:
        current_file.close()

    print(f"✅ Done! Created {file_count} files.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python split_legacy.py <filename>")
    else:
        split_legacy_file(sys.argv[1])