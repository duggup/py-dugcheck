[![Build Status](https://travis-ci.org/duggup/py-dugcheck.svg?branch=master)](https://travis-ci.org/duggup/py-dugcheck)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/2f20647a28534955828d897776821efe)](https://www.codacy.com/manual/duggup/py-dugcheck?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=duggup/py-dugcheck&amp;utm_campaign=Badge_Grade)

py-dugcheck
---

py-dugcheck is a Python based code evaluator for [Duggup's Coding Questions](https://duggup.com/q).

# Installing

```
pip install dugcheck
```

# Coding solution for the question `max-number`

```py
from dugcheck import Dugcheck

dug = Dugcheck()

@dug.question("max-number")
def solution_max_number(inp):
    max_number = max(inp["numbers"])
    return {
        "max": max_number
    }

dug.run(host="0.0.0.0", port=3003)
```
