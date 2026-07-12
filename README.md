# 🎪 The Number Festival

A cute browser-based number-catching game built with Python and Pygame, converted to run in the browser using [Pygbag](https://github.com/pygame-web/pygbag).

**[▶ Play it here]([https://goldfish.github.io/number-festival]/)** | **[Play on itch.io](https://goldofish.itch.io/the-number-festival)**

This is my first game — a first draft, and I'd genuinely appreciate feedback on anything: bugs, balance, art, vibe, whatever comes to mind.

## How to Play

Catch the falling numbers to fill the garden for the festival! Each level has a different rule for which numbers to grab:

- 🌱 **Level 1** — Catch only **EVEN** numbers
- 🌸 **Level 2** — Catch only **ODD** numbers
- 🔮 **Level 3** — Catch only **PRIME** numbers

**Controls:**
- `←` / `→` — Move
- `Space` — Start a level
- `Enter` — Play again (after winning)
- `Esc` / `Q` — Quit

Reach 10 points to clear each level.

## Tech Stack

- **Python 3.13** + **Pygame** for the core game
- **Pygbag** to compile to WebAssembly for browser play
- **asyncio** for the browser-compatible game loop

## Running Locally

```bash
pip install pygbag
python -m pygbag .
```

Then open `http://localhost:8000` in your browser.

## Credits

- Code & art: me
- Music: *hot_spring_town.ogg* by Kistol (open-source, used with credit)
- AI assistance was used to help debug and fix issues in the code

## Feedback

If you play it and have thoughts — bugs, ideas, general impressions — please open an [Issue](../../issues) or drop a comment on the [itch.io page](https://goldofish.itch.io/the-number-festival). Every bit of feedback helps!
