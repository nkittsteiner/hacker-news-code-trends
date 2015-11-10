## Hacker News Code Trends

## Features

- Generate code trends based on YC Hacker News [site][ychn].

## Prerequisites

- Python [site][python]
- Python Requests [site][requests]
- Docker if you want to run this on a container

## Instructions

1. Install version 372 of MzScheme. (Don't use the latest version. Versions after 372 made lists immutable.)
2. Get http://ycombinator.com/arc/arc3.tar and untar it.
3. Type mzscheme -m -f as.scm and you should get an Arc prompt.
4. If you ^C an Arc program, you'll get the Scheme REPL. Use (tl) to get back to the Arc REPL.
5. If you have questions or suggestions, post them on the [forum][arc-forum].

## Docker

[ychn]: http://news.ycombinator.com
[python]: https://www.python.org/downloads/
[requests]: http://docs.python-requests.org/en/latest/
[docker]: https://www.docker.com/