import datetime
from freezegun import freeze_time


class Cases(object):
    @freeze_time("0420-01-01" + " 09:00:00")
    def __init__(self):
        self.validation_test_cases = [
            # (fields, values, error_code, error_message

            (["date"], ["2024-01-32"], "invalid_date", ""),
            (["organiser"], [""], "empty_organiser",
             "organiser cannot be empty"),
            (["title"], [""], "empty_title", "title cannot be empty"),
            (["details"], [""], "empty_details", "details cannot be empty"),
            (["start_time"], ["7:00"], "start_too_early",
             "Booking starts too early. Opening hours: 9:00 - 17:00"),
            (["end_time"], ["17:01"], "end_too_late",
             "Booking ends too late. Opening hours: 9:00 - 17:00"),
            (["start_time", "end_time"], ["11:00", "10:00"], "start_after_end",
             "Booking start time cannot be after booking end time"),
            (["organiser"], ["a" * 101], "organiser_too_long",
             "organiser cannot be longer than 100 characters"),
            (["title"], ["a" * 101], "title_too_long",
             "title cannot be longer than 100 characters"),
            (["date"], [(datetime.datetime.now() - datetime.timedelta(days=1)
                         ).date().strftime("%Y-%m-%d")], "booking_in_past", "Bookings must be in the future"),
            (["date"], [(datetime.datetime.now() - datetime.timedelta(days=2)
                         ).date().strftime("%Y-%m-%d")], "booking_in_past", "Bookings must be in the future"),
            (["date"], [(datetime.datetime.now() - datetime.timedelta(days=300)
                         ).date().strftime("%Y-%m-%d")], "booking_in_past", "Bookings must be in the future"),
            (["start_time", "end_time", ], ["09:00", "10:01"],
             "booking_overlaps", "is already booked during this time"),
            (["start_time", "end_time", ], ["09:00", "11:00"],
             "booking_overlaps", "is already booked during this time"),
            (["start_time", "end_time", ], ["09:00", "11:01"],
             "booking_overlaps", "is already booked during this time"),
            (["start_time", "end_time", ], ["10:00", "11:00"],
             "booking_overlaps", "is already booked during this time"),
            (["start_time", "end_time", ], ["10:00", "11:01"],
             "booking_overlaps", "is already booked during this time"),
            (["start_time", "end_time", ], ["10:30", "12:00"],
             "booking_overlaps", "is already booked during this time")
        ]
