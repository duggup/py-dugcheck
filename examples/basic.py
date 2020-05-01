from dugcheck import Dugcheck

dug = Dugcheck()

@dug.question("822b757a")
def solution_251421(request):
    return {
        "max": 3
    }

dug.run(host="0.0.0.0", port=3003)
