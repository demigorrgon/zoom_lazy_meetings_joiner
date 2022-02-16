import webbrowser
import re


class ZoomOpener:
    def __init__(self, link: str):
        self.link = link

    def open_link(self):
        """
        zoom conference id is everything after "?confno" till ?pwd
        conference password - ?pwd till the end of the string
        to use zoommtg url gotta replace "?pwd" with "&pwd"
        """
        r = re.compile(r"[0-9]{10,12}")
        get_conf_id = r.findall(self.link)
        get_password = self.link.split("?pwd=")
        construct_proper_string = (
            f"zoommtg://zoom.us/join?confno={get_conf_id[0]}&pwd={get_password[1]}"
        )
        webbrowser.open(construct_proper_string)
        return

    def reconnect(self):
        self.open_link()
        return


# z = ZoomOpener("https://zoom.us/j/3700022521?pwd=aWh5T2UzaVF4Nm14S1FEdFNJejJSUT09")
# z.open_link()
