class MyDict(dict):
    def get(self, key):
        return super().get(key, 0)
