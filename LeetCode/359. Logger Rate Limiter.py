class Logger(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.msg_dict = {}

    def shouldPrintMessage(self, timestamp, message):
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        :type timestamp: int
        :type message: str
        :rtype: bool
        """

        if timestamp < self.msg_dict.get(message, 0):
            return False
        self.msg_dict[message] = timestamp + 10
        return True


test = Logger()
print(test.shouldPrintMessage(1, "foo"))
print(test.shouldPrintMessage(2, "bar"))
print(test.shouldPrintMessage(3, "foo"))
print(test.shouldPrintMessage(8, "bar"))
print(test.shouldPrintMessage(10, "foo"))
print(test.shouldPrintMessage(11, "foo"))