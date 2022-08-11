class CapitaliseDelimit:
    def __init__(self, string: str):
        self.string = string
        self.capitalised = ""

    def capitalise(self, delimiters: list):
        """
        'do_capitalise' called separately as it is a recursive function and the parameter 'string' it takes in is
        modified upon each invocation
        :param delimiters: list of delimiters to split and capitalise by
        :return: capitalised form of string
        """
        self.capitalised = self.__do_capitalise(self.string, delimiters)
        return self.capitalised

    @staticmethod
    def __do_capitalise(string, delimiters: list):
        """
        Recursively split string by given delimiters, then capitalise individual parts before joining them back together
        with the delimiter that the string was split by
        :param string: string to capitalise, becomes list as recursion occurs
        :param delimiters: list of delimiters to split and capitalise string by
        :return: capitalised string
        """
        if len(delimiters) == 0:
            if len(string) > 1:
                string = string.capitalize()
            else:
                string = string.capitalize()
        else:
            string = string.split(delimiters[0])
            for s in range(len(string)):
                string[s] = CapitaliseDelimit.__do_capitalise(string[s], delimiters[1:])
            string = f'{delimiters[0]}'.join(string)
        return string
