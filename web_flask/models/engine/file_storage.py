class FileStorage:
    # ... (your existing code)

    def close(self):
        """
        Calls reload() method for deserializing the JSON file to objects.
        """
        self.reload()
