import os


class PathUtils:
    def __init__(self):
        self.BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    @property
    def config_path(self):
        return os.path.join(self.BASE_PATH, 'config')

    @property
    def testcasedata_path(self):
        return os.path.join(self.BASE_PATH, 'test_case_data')

    @property
    def log_path(self):
        return os.path.join(self.BASE_PATH, 'log')

    @property
    def report_path(self):
        return os.path.join(self.BASE_PATH, 'report')

    @property
    def case_path(self):
        return os.path.join(self.BASE_PATH, 'test_case')
