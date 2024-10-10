class CacheLayer:
    def __init__(self):
        self.cache = {}

    def get(self, key):
        """Retrieve an item from the cache by key."""
        return self.cache.get(key)

    def set(self, key, value):
        """Store an item in the cache with the specified key."""
        self.cache[key] = value

    def clear(self):
        """Clear the entire cache."""
        self.cache.clear()

    def contains(self, key):
        """Check if the cache contains the specified key."""
        return key in self.cache