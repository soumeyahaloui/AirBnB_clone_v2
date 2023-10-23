class DBStorage:
    # ... (your existing code)

    def close(self):
        """
        Calls remove() method on the private session attribute (self.__session)
        or close() on the class Session.
        """
        self.__session.close()
