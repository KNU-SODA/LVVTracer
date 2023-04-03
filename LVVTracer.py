class LVVTracer():
    def __init__(self, target: str):
        pass


    def __enter__(self) -> Any:
        pass

    def __exit__(self, exc_tp: Type, exc_value: BaseException,
                 exc_traceback: TracebackType) -> Optional[bool]:
        # Note: we must return a non-True value here,
        # such that we re-raise all exceptions
        if self.is_internal_error(exc_tp, exc_value, exc_traceback):
            return False  # internal error
        else:
            return None  # all ok

    def getLVVmap() -> dict:
        return None
