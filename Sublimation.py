import sublime_plugin
from sublimation import block_select
from sublimation import json_plist_toggle
import sublime
sublime.log_commands(True)


class BlockSelectCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        block_select.block_select(self, edit)


class JsonPlistToggleCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        json_plist_toggle.json_plist_toggle(self, edit)


class TestWindowCommand(sublime_plugin.WindowCommand):
    def foo(*args, **kwargs):
        pass

    def run(self):
        self.window.show_quick_panel(["1", "2", "3"], self.foo)


