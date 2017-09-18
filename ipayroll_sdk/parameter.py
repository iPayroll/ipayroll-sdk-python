class PageParams(object):

    DEFAULT_SIZE = 20
    DEFAULT_PAGE = 1

    def __init__(self, page=1, size=20):
        self.page = page
        self.size = size