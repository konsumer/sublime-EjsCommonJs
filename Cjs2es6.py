import sublime
import sublime_plugin
import re

regexE = r"(const|var|let) (.+) *= *require *\((.+)\)"
regexC = r"import (.+) *from *(.+)"

class Cjs2es6Command(sublime_plugin.TextCommand):
    def run(self, edit):
        selection = self.view.sel()
        for region in selection:
            region_text = self.view.substr(region)
            self.view.replace(edit, region, re.sub(regexE, "import \\2 from \\3", region_text, 0, re.MULTILINE))

class Es62cjsCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        selection = self.view.sel()
        for region in selection:
            region_text = self.view.substr(region)
            self.view.replace(edit, region, re.sub(regexC, "const \\1 = require(\\2)", region_text, 0, re.MULTILINE))
