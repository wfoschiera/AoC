"""Advent of Code helper: what is available, what is done, and a new day's files.

    python aoc.py            # every year: puzzles available, files here, your stars
    python aoc.py 2022       # one year, day by day, and the next day to do
    python aoc.py 2022 7     # create 2022/day_07.py and download 2022/day_07.txt

Existing files are never overwritten. Stars and inputs need your adventofcode.com
`session` cookie in the AOC_SESSION environment variable; without it, only the
files in this repo are shown.
"""

import argparse
import os
import re
import sys
import urllib.error
import urllib.request
from datetime import datetime, timedelta, timezone
from pathlib import Path
from string import Template

ROOT = Path(__file__).parent
FIRST_YEAR = 2015
AOC_URL = "https://adventofcode.com"
# AoC asks automated tools to identify themselves.
USER_AGENT = "github.com/wfoschiera/AoC aoc.py"
# Puzzles unlock at midnight US Eastern time (UTC-5 in December).
AOC_TZ = timezone(timedelta(hours=-5))

DAY_TEMPLATE = Template('''\
"""Advent of Code $year, day $day: $url"""

from pathlib import Path

INPUT = Path(__file__).with_suffix(".txt")

test_data = """\\
"""


def parse(data: str) -> list[str]:
    return data.splitlines()


def part_1(data: str):
    raise NotImplementedError


def part_2(data: str):
    raise NotImplementedError


if __name__ == "__main__":
    # PART 1
    # TEST
    res = part_1(test_data)
    print(res)
    # assert res == ...

    # RESULT
    # res = part_1(INPUT.read_text())
    # print(res)

    # PART 2
    # TEST
    # res = part_2(test_data)
    # print(res)
    # assert res == ...

    # RESULT
    # res = part_2(INPUT.read_text())
    # print(res)
''')


def now() -> datetime:
    return datetime.now(AOC_TZ)


def latest_year(today: datetime) -> int:
    return today.year if today.month == 12 else today.year - 1


def puzzle_count(year: int) -> int:
    # 25 puzzles a year until 2024, 12 from 2025 on.
    return 12 if year >= 2025 else 25


def available_days(year: int, today: datetime) -> int:
    if year == today.year and today.month == 12:
        return min(today.day, puzzle_count(year))
    return puzzle_count(year)


def day_files(year: int, day: int) -> tuple[Path, Path]:
    solution = ROOT / str(year) / f"day_{day:02d}.py"
    return solution, solution.with_suffix(".txt")


def fetch(path: str, session: str) -> str:
    request = urllib.request.Request(
        AOC_URL + path,
        headers={"Cookie": f"session={session}", "User-Agent": USER_AGENT},
    )
    with urllib.request.urlopen(request, timeout=30) as response:
        return response.read().decode()


def logged_in(html: str) -> bool:
    return "/auth/login" not in html


def stars_per_year(session: str) -> dict[int, int] | None:
    """Stars per year from /events; None when the cookie was not accepted."""
    html = fetch("/events", session)
    if not logged_in(html):
        return None
    stars = {}
    for event in html.split('class="eventlist-event"')[1:]:
        event = event.split("</div>")[0]
        year = re.search(r"\[(\d{4})\]", event)
        count = re.search(r"(\d+)\*", event)
        if year:
            stars[int(year.group(1))] = int(count.group(1)) if count else 0
    return stars


def stars_per_day(session: str, year: int) -> dict[int, int] | None:
    """Stars per day from the year's calendar; None when the cookie was not accepted."""
    html = fetch(f"/{year}", session)
    if not logged_in(html):
        return None
    labels = re.findall(r'aria-label="Day (\d+)(?:, (one|two) stars?)?"', html)
    return {int(day): {"one": 1, "two": 2}.get(count, 0) for day, count in labels}


def read_stars(reader, session: str, *args) -> dict[int, int] | None:
    if not session:
        print("(set AOC_SESSION to see your stars; showing the files in this repo)\n")
        return None
    try:
        stars = reader(session, *args)
    except urllib.error.URLError as error:
        print(f"(could not read your stars: {error}; showing the files in this repo)\n")
        return None
    if stars is None:
        print("(AOC_SESSION was not accepted; showing the files in this repo)\n")
    return stars


def show_years(session: str, today: datetime) -> None:
    stars = read_stars(stars_per_year, session)
    unfinished = None
    print("year  puzzles  files  stars")
    for year in range(FIRST_YEAR, latest_year(today) + 1):
        days = available_days(year, today)
        files = sum(day_files(year, day)[0].exists() for day in range(1, days + 1))
        if stars is None:
            star_text, started, done = "?", files > 0, files == days
        else:
            got = stars.get(year, 0)
            star_text, started, done = f"{got}/{2 * days}", got > 0, got == 2 * days
        print(f"{year}  {days:>7}  {files:>5}  {star_text:>5}")
        if started and not done and unfinished is None:
            unfinished = year
    if unfinished:
        print(f"\noldest unfinished year: {unfinished}  ->  python aoc.py {unfinished}")


def show_year(year: int, session: str, today: datetime) -> None:
    stars = read_stars(stars_per_day, session, year)
    next_day = None
    print(f"{year}  {AOC_URL}/{year}")
    print("day  file  input  stars")
    for day in range(1, available_days(year, today) + 1):
        solution, puzzle_input = day_files(year, day)
        if stars is None:
            star_text, done = "?", solution.exists()
        else:
            got = stars.get(day, 0)
            star_text, done = "*" * got or "-", got == 2
        if not done and next_day is None:
            next_day = day
        file_text = "yes" if solution.exists() else "-"
        input_text = "yes" if puzzle_input.exists() else "-"
        print(f"{day:>3}  {file_text:>4}  {input_text:>5}  {star_text:>5}")
    if next_day:
        print(f"\nnext day: {next_day}  ->  python aoc.py {year} {next_day}")
    else:
        print("\nall done")


def create_day(year: int, day: int, session: str) -> int:
    solution, puzzle_input = day_files(year, day)
    solution.parent.mkdir(exist_ok=True)
    url = f"{AOC_URL}/{year}/day/{day}"

    if solution.exists():
        print(f"kept      {solution.relative_to(ROOT)} (already exists)")
    else:
        solution.write_text(DAY_TEMPLATE.substitute(year=year, day=day, url=url))
        print(f"created   {solution.relative_to(ROOT)}")

    if puzzle_input.exists():
        print(f"kept      {puzzle_input.relative_to(ROOT)} (already exists)")
    elif not session:
        print(
            f"skipped   {puzzle_input.relative_to(ROOT)}: set AOC_SESSION to download"
        )
    else:
        try:
            puzzle_input.write_text(fetch(f"/{year}/day/{day}/input", session))
        except urllib.error.HTTPError as error:
            hint = {
                400: "AOC_SESSION is invalid or expired",
                404: "the puzzle is not unlocked yet",
            }.get(error.code, error.reason)
            print(
                f"failed    {puzzle_input.relative_to(ROOT)}: HTTP {error.code}, {hint}"
            )
            return 1
        except urllib.error.URLError as error:
            print(f"failed    {puzzle_input.relative_to(ROOT)}: {error.reason}")
            return 1
        print(f"fetched   {puzzle_input.relative_to(ROOT)}")

    print(f"puzzle    {url}")
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument("year", type=int, nargs="?")
    parser.add_argument("day", type=int, nargs="?")
    args = parser.parse_args(argv)
    today = now()
    session = os.environ.get("AOC_SESSION", "").strip()

    if args.year is None:
        show_years(session, today)
        return 0
    if not FIRST_YEAR <= args.year <= latest_year(today):
        parser.error(
            f"Advent of Code years go from {FIRST_YEAR} to {latest_year(today)}"
        )
    if args.day is None:
        show_year(args.year, session, today)
        return 0
    days = available_days(args.year, today)
    if not 1 <= args.day <= days:
        parser.error(f"{args.year} has days 1 to {days}")
    return create_day(args.year, args.day, session)


if __name__ == "__main__":
    sys.exit(main())
