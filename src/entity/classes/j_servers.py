class JServers:
    def __init__(self, savers):
        self.severs = savers

    def prints(self):
        all_id = []
        for page in self.severs:
            all_id = page.have_id()
        print(f'Все ID: {all_id}.')

    def deletes(self, id):
        for page in self.severs:
            page.delete(id)
