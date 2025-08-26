from datetime import datetime, timezone

# Helper function to get current timestamp
def time_stamp(fmt: str = "utc")-> datetime:
    if fmt == "utc":
        return datetime.now(timezone.utc)
    return datetime.now()  # local time

