import datetime


class Cases(object):
    def __init__(self):
        self.validation_test_cases = [
            # (fields, values, error_code, error_message, True/False Equal/Contains)
            # why True/False? Some errors will throw the value also which we want to retain so we can't use assertEqual in those cases

            (["date"], ["2024-01-32"], "invalid_date", True),
            (["organiser"], [""], "empty_organiser",
             "organiser cannot be empty", True),
            (["title"], [""], "empty_title", "title cannot be empty", True),
            (["details"], [""], "empty_details", "details cannot be empty", True),
            (["start_time"], ["7:00"], "start_too_early",
             "Booking starts too early. Opening hours: 9:00 - 17:00", True),
            (["end_time"], ["17:01"], "end_too_late",
             "Booking starts too early. Opening hours: 9:00 - 17:00", True),
            (["start_time", "end_time"], ["11:00", "10:00"], "start_after_end",
             "Booking start time cannot be after booking end time", True),
            (["organiser"], ["a" * 101], "organiser_too_long",
             "organiser cannot be longer than 100 characters",  True),
            (["title"], ["a" * 101], "title_too_long",
             "title cannot be longer than 100 characters", True),
            (["date"], [(datetime.datetime.now() - datetime.timedelta(days=1)
                         ).date().strftime("%Y-%m-%d")], "booking_in_past", "Bookings must be in the future", True),
            (["date"], [(datetime.datetime.now() - datetime.timedelta(days=2)
                         ).date().strftime("%Y-%m-%d")], "booking_in_past", "Bookings must be in the future", True),
            (["date"], [(datetime.datetime.now() - datetime.timedelta(days=300)
                         ).date().strftime("%Y-%m-%d")], "booking_in_past", "Bookings must be in the future", True),
            (["start_time", "end_time", ], ["09:00", "10:01"],
             "booking_overlaps", "is already booked during this time", False),
            (["start_time", "end_time", ], ["09:00", "11:00"],
             "booking_overlaps", "is already booked during this time", False),
            (["start_time", "end_time", ], ["09:00", "11:01"],
             "booking_overlaps", "is already booked during this time", False),
            (["start_time", "end_time", ], ["10:00", "11:00"],
             "booking_overlaps", "is already booked during this time", False),
            (["start_time", "end_time", ], ["10:00", "11:01"],
             "booking_overlaps", "is already booked during this time", False),
            (["start_time", "end_time", ], ["10:30", "12:00"],
             "booking_overlaps", "is already booked during this time", False)
        ]
