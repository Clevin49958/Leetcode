import logging


def insert_sort_local(arr: list, map=lambda x:x, start=0, end=None) -> list:
    """
    Sort the array in place in ascending order

    Args:
        arr (list[T]): array to sort
        map (func(T):numeric, optional): map object to comporable value. Defaults to lambdax:x.
        start (int): start index. Defaults to 0
        end (int): end index (exclusive). Defaults to last index of array

    Returns:
        list: sorted original array
    """
    if end is None: 
        end = len(arr)
    for i in range(start + 1, end):
        cache = map(arr[i])
        if cache < map(arr[i-1]):
            loc = i - 1
            while loc > start and cache < map(arr[loc - 1]):
                loc -= 1
            arr[loc], arr[loc + 1:i + 1] = arr[i], arr[loc:i]
    return arr

logging.basicConfig(level=logging.INFO)
_logger = logging.getLogger(__name__)
def test_local(func, *params, expand=False, sol=None, pause=None) -> None:
    for idx, s in enumerate(params):
        _logger.info(f"Test case %d: %s", idx + 1, s)
        if pause is not None and (idx == pause or idx == len(params) + pause):
            input("Set a breakpoint to debug...")
        res = func(*s) if expand else func(s)
        _logger.info(f"Test obtained: %s", res)
        if sol:
            # _logger.info(f"Test result: {res == sol[idx]}")
            assert res == sol[idx]
        print()

if __name__ == "__main__":
    test_local(insert_sort_local, [3,4,6,5,1,2])