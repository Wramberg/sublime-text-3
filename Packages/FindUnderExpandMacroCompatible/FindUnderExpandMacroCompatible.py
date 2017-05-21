import sublime
import sublime_plugin

class FindUnderExpandMacroCompatible(sublime_plugin.TextCommand):
    def run(self, edit):
        win = sublime.active_window()
        win.run_command("find_under_expand")
