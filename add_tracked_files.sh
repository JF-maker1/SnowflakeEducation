#!/bin/bash
while read -r file; do
    git add "$file"
done < tracked_files.txt
