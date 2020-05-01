from dugcheck import Dugcheck

dug = Dugcheck()

@dug.question("max-number")
def solution_max_number(inp):
    max_number = max(inp["numbers"])
    return {
        "max": max_number
    }

dug.run(host="0.0.0.0", port=3003)
