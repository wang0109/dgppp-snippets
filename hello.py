import sublime
import sublime_plugin


# Use console: view.run_command('example') run this within
# Sublime.. example -> ExampleCommond is auto-deduced somehow..
# It does: Go to file begin and insert hello world...
class ExampleCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        self.view.insert(edit, 0, "Hello, World!")
