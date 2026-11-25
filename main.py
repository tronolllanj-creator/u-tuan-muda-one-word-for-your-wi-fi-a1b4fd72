"""
# Pinned line: the judge scores this exact line; write it verbatim.
Generates the required string entry for the make.fun competition.
"""

import os

def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    
    content = "Gaslighting"
    
    # Validation per requirements
    assert 1 <= len(content) <= 20, "Content length out of bounds"
    assert not content.isspace(), "Content cannot be only whitespace"
    assert " " not in content, "Content must be a single word with no spaces"
    
    file_path = os.path.join(output_dir, "entry.txt")
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content + "\n")
        
    print(file_path)
    print(len(content))

if __name__ == "__main__":
    main()
