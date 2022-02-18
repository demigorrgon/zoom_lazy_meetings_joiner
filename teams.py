import webbrowser
from zoom import ZoomOpener


class TeamsOpener(ZoomOpener):
    def open_link(self):
        webbrowser.open(self.link)
        return

    def reconnect(self):
        self.open_link()
        return

    def join(self):
        # fish for join now button with pyautogui
        pass
