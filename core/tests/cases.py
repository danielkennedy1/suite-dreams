import datetime

class Cases(object):
    def __init__(self):
        self.validation_test_cases = [
            # TODO: add validation error messages to these tests
            # (fields to modify, values to put in these fields, expected code from ValidationError)
            (["date"], ["2024-01-32"], "invalid_date"),
            (["organiser"], [""], "empty_organiser"),
            (["title"], [""], "empty_title"),
            (["details"], [""], "empty_details"),
            (["start_time"], ["7:00"], "start_too_early"),
            (["end_time"], ["17:01"], "end_too_late"),
            (["start_time", "end_time"], ["11:00", "10:00"], "start_after_end"),
            (["organiser"], ["a" * 101], "organiser_too_long"),
            (["title"], ["a" * 101], "title_too_long"),
            (["date"], [(datetime.datetime.now() - datetime.timedelta(days=1)).date().strftime("%Y-%m-%d")], "booking_in_past"),
            (["date"], [(datetime.datetime.now() - datetime.timedelta(days=2)).date().strftime("%Y-%m-%d")], "booking_in_past"),
            (["date"], [(datetime.datetime.now() - datetime.timedelta(days=300)).date().strftime("%Y-%m-%d")], "booking_in_past"),
            (["start_time", "end_time", ], ["09:00", "10:01"], "booking_overlaps"),
            (["start_time", "end_time", ], ["09:00", "11:00"], "booking_overlaps"),
            (["start_time", "end_time", ], ["09:00", "11:01"], "booking_overlaps"),
            (["start_time", "end_time", ], ["10:00", "11:00"], "booking_overlaps"),
            (["start_time", "end_time", ], ["10:00", "11:01"], "booking_overlaps"),
            (["start_time", "end_time", ], ["10:30", "12:00"], "booking_overlaps")
        ]