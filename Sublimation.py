import sublime
sublime.log_commands(True)

import sublime_plugin
from sublimation import block_select
from sublimation import json_plist_toggle
from sublimation import update_api_docs


class BlockSelectCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        block_select.block_select(self, edit)


class JsonPlistToggleCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        json_plist_toggle.json_plist_toggle(self, edit)


class UpdateApiDoc(sublime_plugin.TextCommand):
    def run(self, edit):
        print "running"

        update_api_docs.update_api_docs(self)
