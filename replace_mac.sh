#!/bin/bash

# macOS wrapper script for text replacement
# Usage: ./replace_mac.sh <target_file>

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"

if [ -z "$1" ]; then
    echo "Usage: $0 <target_file>"
    echo "  <target_file>  - Path to the text file to modify"
    exit 1
fi

python3 "$SCRIPT_DIR/replace.py" "$1"
