class MessageClass(object):

    def __init__(self, content, *args, **kw):
        # Initialize any variables you need from the input you get
        self.content = content

    def do_work(self):
        # Do some calculations here
        # returns a tuple ((1,2,3, ), (4,5,6,))
        result = {"message":{"text" : self.content}} # final result
        return result

class KeyboardClass(object):
	def __init__(self, *args, **kw):
		pass

	def do_work(self):
		result = { "type" : "buttons", "buttons" : ["선택 1", "선택 2", "선택 3"]}
		return result