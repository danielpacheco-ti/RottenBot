from threads.driver_threads import DriverThreads
from crawler.crawler_instagram import CrawlerInsta
from settings import SIMILAR_ARTISTS
from util.general import General


class RottenThreads(object):
    def __init__(self):
        self.driver = DriverThreads().get_driver()
        self.crawler = CrawlerInsta()
        self.tolls = General()
        print("Iniciando o processo")

    def start_crawler(self):
        self.tolls.login(self.driver)
        for artist in SIMILAR_ARTISTS:
            get_followers = self.crawler.start(self.driver, artist)
