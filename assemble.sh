#!/bin/bash
# Assembles full app.py from parts
set -e
if [ -f data/app.part0 ] && [ -f data/app.part1 ] && [ -f data/app.part2 ]; then
  cat data/app.part0 data/app.part1 data/app.part2 > app.py
  chmod +x app.py
  echo "Assembled app.py ($(wc -c < app.py) bytes)"
  echo "Run: python app.py"
else
  echo "Parts missing in data/"
  exit 1
fi
