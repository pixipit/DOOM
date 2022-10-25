import pygame


class Input:
    val = [0, 0]
    key_downs = {
        'w': False,
        's': False,
        'a': False,
        'd': False,
        'space': False,
        'escape': False
    }

    def update(self, events):
        for key in self.key_downs:
            self.key_downs[key] = False

        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    self.key_downs["a"] = True
                    self.val[0] = -1
                if event.key == pygame.K_w:
                    self.key_downs["w"] = True
                    self.val[1] = 1
                if event.key == pygame.K_d:
                    self.val[0] = 1
                    self.key_downs['d'] = True
                if event.key == pygame.K_s:
                    self.val[1] = -1
                    self.key_downs['s'] = True
                if event.key == pygame.K_SPACE:
                    self.key_downs['space'] = True
                if event.key == pygame.K_ESCAPE:
                    self.key_downs['escape'] = True

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    self.val[0] = 0
                if event.key == pygame.K_w:
                    self.val[1] = 0
                if event.key == pygame.K_d:
                    self.val[0] = 0
                if event.key == pygame.K_s:
                    self.val[1] = 0
                if event.key == pygame.K_SPACE:
                    self.val[0] = 0