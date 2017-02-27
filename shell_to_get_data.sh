#!/bin/bash
find . -type f -name data_clinical* -exec head -1 {} + > condensed_files.txt