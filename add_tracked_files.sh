#!/bin/bash
while read -r file; do
    if [[ -n "$file" ]]; then  # Ignoruje prázdné řádky
        git add "$file"
    fi
done < tracked_files.txt
