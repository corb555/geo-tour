import argparse
import os
import re
import glob
import sys

# Configuration
MASTER_FILENAME = "snippets_combined.html"
ENCODING = "utf-8"

# --- TEMPLATES ---

# The HTML Header allows the combined file to be viewed pleasantly in a browser
HTML_HEADER = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Tour Snippet Editor</title>
    <style>
        body { font-family: sans-serif; background-color: #f0f2f5; padding: 20px; max-width: 900px; margin: 0 auto; }
        .instruction { background: #fff3cd; border: 1px solid #ffeeba; padding: 15px; margin-bottom: 30px; border-radius: 5px;}
        .snippet-wrapper {
            background: #fff;
            border: 1px solid #ccc;
            margin-bottom: 30px;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
            border-radius: 8px;
            overflow: hidden;
        }
        .snippet-header {
            background: #2c3e50;
            color: #fff;
            padding: 10px 15px;
            font-weight: bold;
            font-family: monospace;
            display: flex;
            justify-content: space-between;
        }
        .snippet-content {
            padding: 20px;
            border-top: 1px solid #eee;
        }
        /* Simulate the tour panel context */
        .tour-topic-label { font-size: 0.8em; text-transform: uppercase; color: #888; margin-bottom: 5px; font-weight: 700; }
    </style>
</head>
<body>
    <div class="instruction">
        <strong>EDITING MODE:</strong><br>
        1. Edit the content inside the white boxes below.<br>
        2. Do NOT modify the gray header bars or the HTML comments surrounding them.<br>
        3. Save this file.<br>
        4. Run <code>python html_snippets.py --split</code> to update the individual files.
    </div>
"""

HTML_FOOTER = """
</body>
</html>
"""

# Regex pattern to find snippets in the combined file
# Captures: Group 1 (Filename), Group 2 (Content)
SPLIT_PATTERN = re.compile(
    r'<!-- START_FILE: (.*?) -->.*?<div class="snippet-content">\n(.*?)\n\s*</div>.*?<!-- END_FILE -->',
    re.DOTALL
)

def combine_snippets(directory="."):
    """Reads all .html files and creates the master file."""

    # Get all HTML files, excluding the master file itself
    files = sorted(glob.glob(os.path.join(directory, "*.html")))
    files = [f for f in files if os.path.basename(f) != MASTER_FILENAME]

    if not files:
        print(f"❌ No HTML files found in '{directory}'")
        return

    print(f"📦 Combining {len(files)} files into '{MASTER_FILENAME}'...")

    with open(MASTER_FILENAME, 'w', encoding=ENCODING) as master:
        master.write(HTML_HEADER)

        for filepath in files:
            filename = os.path.basename(filepath)

            with open(filepath, 'r', encoding=ENCODING) as f:
                content = f.read().strip()

            # We wrap the content in comments AND a div structure.
            # The comments are for the parser. The divs are for the human editor.
            block = f"""
    <!-- START_FILE: {filename} -->
    <div class="snippet-wrapper">
        <div class="snippet-header">FILE: {filename}</div>
        <div class="snippet-content">
{content}
        </div>
    </div>
    <!-- END_FILE -->
"""
            master.write(block)

        master.write(HTML_FOOTER)

    print(f"✅ Success! Open '{MASTER_FILENAME}' in your browser or editor.")


def split_snippets(source_file):
    """Reads the master file and overwrites individual files."""

    if not os.path.exists(source_file):
        print(f"❌ Error: Combined file '{source_file}' not found.")
        return

    print(f"✂️  Splitting '{source_file}' back into individual files...")

    with open(source_file, 'r', encoding=ENCODING) as f:
        full_html = f.read()

    # Find all matches
    matches = SPLIT_PATTERN.findall(full_html)

    if not matches:
        print("⚠️  No snippets found. Did you modify the comment markers?")
        return

    count = 0
    for filename, content in matches:
        # Clean up whitespace slightly, but preserve internal formatting
        # We strip the newline added by the wrapper div
        clean_content = content.strip()

        # Add a trailing newline which is standard for text files
        clean_content += "\n"

        with open(filename, 'w', encoding=ENCODING) as out:
            out.write(clean_content)

        print(f"   -> Updated: {filename}")
        count += 1

    print(f"✅ Processed {count} files.")


def main():
    parser = argparse.ArgumentParser(description="Manage MapLibre Tour HTML snippets.")
    group = parser.add_mutually_exclusive_group(required=True)

    group.add_argument('--combine', action='store_true',
                       help="Merge all *.html files in the current folder into one editable view.")

    group.add_argument('--split', action='store_true',
                       help=f"Read '{MASTER_FILENAME}' and overwrite individual files.")

    args = parser.parse_args()

    if args.combine:
        combine_snippets()
    elif args.split:
        split_snippets(MASTER_FILENAME)

if __name__ == "__main__":
    main()