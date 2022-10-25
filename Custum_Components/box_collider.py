from component import Component


class BoxCollider(Component):
    on_trigger_entry = None

    def __init__(self, size=None, offset=[0, 0]):
        self.size = [0,0]
        self.offset = [0, 0]
        self.overwrite = False
        if size is None:
            self.overwrite = True
            return
        self.size = size
        self.offset = offset
        self.overwrite = False

    def start(self):
        if not self.overwrite:
            return
        self.size = self.game_object.size
        self.offset = [-self.size[0]/2, -self.size[1]/2]
