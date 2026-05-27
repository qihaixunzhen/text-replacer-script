import sys
import os

def load_config(config_path):
    rules = []
    with open(config_path, 'r', encoding='utf-8') as f:
        for line_num, line in enumerate(f, 1):
            line = line.strip()
            if not line or '>' not in line:
                continue
            # Split only on the first '>' to support cases where B contains '>'
            sep = line.index('>')
            find = line[:sep]
            replace = line[sep + 1:]
            if find:
                rules.append((find, replace))
    return rules


def apply_replacements(file_path, rules):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    for find, replace in rules:
        content = content.replace(find, replace)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)


def main():
    # Default config path relative to script location
    script_dir = os.path.dirname(os.path.abspath(__file__))
    default_config = os.path.join(script_dir, 'config.txt')

    if len(sys.argv) < 2:
        print("Usage: python replace.py <target_file> [config_file]")
        print("  <target_file>  - Path to the text file to modify")
        print("  [config_file]  - Path to config file (default: config.txt in same directory)")
        sys.exit(1)

    target_file = sys.argv[1]
    config_file = sys.argv[2] if len(sys.argv) > 2 else default_config

    if not os.path.exists(target_file):
        print(f"Error: Target file '{target_file}' not found.")
        sys.exit(1)

    if not os.path.exists(config_file):
        print(f"Error: Config file '{config_file}' not found.")
        sys.exit(1)

    rules = load_config(config_file)

    if not rules:
        print("Warning: No valid replacement rules found in config file.")
        sys.exit(0)

    print(f"Applying {len(rules)} replacement rules to '{target_file}'...")
    apply_replacements(target_file, rules)
    print("Done.")


if __name__ == '__main__':
    main()
