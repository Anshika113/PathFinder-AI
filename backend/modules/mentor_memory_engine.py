class MentorMemoryEngine:
    def __init__(self):
        self.memory = []

    def add_memory(self, message):
        self.memory.append(message)

    def get_memory(self):

        return self.memory