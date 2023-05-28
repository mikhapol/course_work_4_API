class JServers:
    def __init__(self, savers):
        self.severs = savers

    def prints_id(self):
        all_id = []
        for page in self.severs:
            all_id = page.have_id()
        print(f'Все ID: {all_id}.')

    def del_id(self, id):
        for page in self.severs:
            page.delete(id)
