
class ToDoList (object):

	def __init__(self,):
		self.todo = ''

	def create (self,todo_content):
		self.todo_content = todo_content
		self.todo += todo_content + '\n'

	def list(self):
		return (self.todo)




'''
emeka = ToDoList()
emeka.create('i am frustrated')
emeka.create('i am frustrated')
emeka.create('i am frustrated')
emeka.list()'''

