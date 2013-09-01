import sublime, sublime_plugin

def Hide(self, edit):
    return self.view.fold(self.view.find_all('(\/\*\*(([^\*]|\*[^\/]|``[^`])*)\*\/)'))


def Show(self, edit):
    return self.view.unfold(self.view.find_all('(\/\*\*(([^\*]|\*[^\/]|``[^`])*)\*\/)'))


class DocularToggleCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        if Hide(self, edit) is False:
            Show(self, edit)
