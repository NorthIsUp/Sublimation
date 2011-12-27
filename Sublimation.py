import sublime_plugin
from sublimation import block_select


class BlockSelectCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        block_select.block_select(self, edit)
