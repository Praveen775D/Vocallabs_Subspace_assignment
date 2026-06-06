import time


def retry(
    func,
    retries=3,
    delay=1
):

    for attempt in range(retries):

        try:

            return func()

        except Exception:

            if attempt < retries - 1:

                time.sleep(delay)

    raise Exception(
        "Maximum retries exceeded"
    )