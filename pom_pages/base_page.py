class BasePage:
    def __init__(self, browser):
        self.browser = browser

    def load(self, url):
        self.browser.get(url)

        if self.browser.current_url != url:
            raise Exception('The page that was loaded is not the correct one, please re-run the test')


