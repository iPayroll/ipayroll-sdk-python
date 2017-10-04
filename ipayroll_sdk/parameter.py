class PageParams(object):
    DEFAULT_SIZE = 20
    DEFAULT_PAGE = 0

    def __init__(self, page=0, size=20):
        self.page = page
        self.size = size
