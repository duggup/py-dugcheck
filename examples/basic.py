# encoding=utf-8
import logging

import pytest
from dugcheck import Dugcheck

logger = logging.getLogger(__name__)

dug = Dugcheck()

@dug.question("question-id")
def solution_251421(request):
    return {
        "max": 3
    }

dug.run(host="0.0.0.0", port=3003)
