

### To move batches of files into subdirectories.... as written 25 files get moved

````
 n=0; for f in *; do d="dir$((n++ / 25))"; mkdir -p "$d"; mv -- "$f" "$d/$f"; done
````
