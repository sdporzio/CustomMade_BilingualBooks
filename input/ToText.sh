input=${1}
output=$(echo "$input" | cut -f 1 -d '.')

run "/Applications/calibre.app/Contents/MacOS/ebook-convert ${input} ${output}.txt"

