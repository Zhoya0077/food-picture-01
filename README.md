# food-picture-01 — Steaming Ramen

A close-up photograph of a bowl of ramen, made to make you hungry on
first sight: rich broth glistening under warm light, a halved soft egg
with a jammy yolk, spring onions and chilli oil, and noodles lifted
high with chopsticks while steam curls up from the bowl.

## How it runs

`main.py` (Python 3.13, standard library only) copies `entry.png` to
`$MAKEFUN_OUTPUT_DIR/entry.png` (default `/output/entry.png`). It
refuses to run if the image is over the 1 MiB cap, and it reads the
output back to confirm the bytes are identical to the source.

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## Files

- `entry.png` — the ramen photograph (JPEG bytes, 1024×683, 144,615 bytes)
- `main.py` — the program that writes the picture to the output directory
- `LICENSE` — MIT
