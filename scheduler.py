import schedule
import time
import csv
from zoom import ZoomOpener


FILENAME = "some.csv"


def parse_csv(filename):
    with open(f"{filename}", "r") as csv_file:
        csvreader = csv.reader(csv_file)
        # fields = next(csvreader)
        data = [_ for _ in csvreader]
        return data


def set_schedule():
    # very clunky way of doing it, refactor at all costs
    links_to_open = [item[1] for item in parse_csv(FILENAME)]
    dates_at_which_to_open = [item[2].split(" ")[0] for item in parse_csv(FILENAME)]
    hours_at_which_to_open = [item[2].split(" ")[1] for item in parse_csv(FILENAME)]
    scheduled_times = list(zip(dates_at_which_to_open, hours_at_which_to_open))

    for index, day in enumerate(scheduled_times):
        if day[0] == "monday":
            schedule.every().monday.at(day[1]).do(
                ZoomOpener(links_to_open[index]).open_link
            )

        if day[0] == "tuesday":
            schedule.every().tuesday.at(day[1]).do(
                ZoomOpener(links_to_open[index]).open_link
            )

        if day[0] == "wednesday":
            schedule.every().wednesday.at(day[1]).do(
                ZoomOpener(links_to_open[index]).open_link
            )

        if day[0] == "thursday":
            schedule.every().thursday.at(day[1]).do(
                ZoomOpener(links_to_open[index]).open_link
            )

        if day[0] == "friday":
            schedule.every().friday.at(day[1]).do(
                ZoomOpener(links_to_open[index]).open_link
            )

        if day[0] == "saturday":
            schedule.every().saturday.at(day[1]).do(
                ZoomOpener(links_to_open[index]).open_link
            )

    return


if __name__ == "__main__":
    set_schedule()
    while True:
        schedule.run_pending()
        time.sleep(1)
