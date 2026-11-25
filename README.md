# Advent of Code

My solutions to [Advent of Code](https://adventofcode.com), the yearly puzzle event, in plain Python: standard library only, formatted and linted with [ruff](https://docs.astral.sh/ruff/).

The goal is to work through every year one puzzle at a time, starting with the oldest one I haven't finished.

## Layout

```
aoc.py              # helper: what's available, what's done, and a new day's files
2022/day N/*.ipynb  # 2022, solved in Jupyter notebooks (imported from an older repo)
2023/day_NN.py      # one script per day
2025/day_NN.py
```

Each solution reads its puzzle input from the `.txt` file with the same name, next to it (`2025/day_01.py` reads `2025/day_01.txt`). Inputs are not committed: Advent of Code [asks people not to share them](https://adventofcode.com/about#faq_copying). The 2022 and 2023 inputs were committed before that rule and are still in the repo.

## Setup

You need [uv](https://docs.astral.sh/uv/). It installs the right Python (3.14) by itself.

```bash
uv sync                      # create .venv with ruff and pre-commit
uv run pre-commit install    # run ruff on every commit
```

## `aoc.py`: see what's left and set up a day

```bash
uv run aoc.py              # every year: number of puzzles, files here, your stars, oldest unfinished year
uv run aoc.py 2024         # one year, day by day, and the next day to do
uv run aoc.py 2024 7       # create 2024/day_07.py and download 2024/day_07.txt
```

- Every year from 2015 to 2024 has 25 puzzles. From 2025 on, there are 12. During December, only the days already unlocked count. Puzzles unlock at midnight US Eastern time.
- Creating a day never overwrites an existing solution or input, so it's safe to run again.
- `aoc.py` counts `YEAR/day_NN.py` files. It doesn't see the 2022 notebooks, so without the cookie 2022 looks untouched. With the cookie, your stars on adventofcode.com are what count.
- The new file is a template with a `test_data` string for the puzzle's example, `part_1` / `part_2`, and asserts to fill in.

### Your session cookie

Your stars and your puzzle inputs belong to your adventofcode.com account, so `aoc.py` needs your `session` cookie to read them:

1. Log in at [adventofcode.com](https://adventofcode.com).
2. Open the browser's DevTools → Application (Storage in Firefox) → Cookies → `https://adventofcode.com`, and copy the value of `session`.
3. Export it in your shell (add it to `~/.zshrc` to keep it):

   ```bash
   export AOC_SESSION=<your cookie>
   ```

Without it, `aoc.py` still works, but it can only go by the files in this repo, and it won't download inputs. The cookie expires after a while. When that happens, downloads fail with HTTP 400 and the script says the cookie is invalid or expired: copy a fresh one.

## Running a solution

```bash
uv run 2025/day_01.py
```

Scripts find their input relative to their own file, so they run from any folder. The 2022 notebooks open in Jupyter. Day 9 also needs numpy and matplotlib:

```bash
uv run --with jupyter --with numpy --with matplotlib jupyter lab 2022
```

## Workflow

- Every puzzle gets its own branch and pull request.
- CI (GitHub Actions) runs `ruff format --check` and `ruff check` on every pull request. `main` is protected: a change goes in only through a PR whose check passed.
- The pre-commit hook runs the same checks before each commit, using the same ruff version (locked in `uv.lock`). It fixes what it can and stops the commit so you can review the change.
- To run the checks by hand:

  ```bash
  uv run ruff format
  uv run ruff check
  ```
