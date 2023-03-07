from rentomatic.responses import ResponseSuccess


def room_list_use_case(repo, request):
    result = repo.list()
    return ResponseSuccess(result)
