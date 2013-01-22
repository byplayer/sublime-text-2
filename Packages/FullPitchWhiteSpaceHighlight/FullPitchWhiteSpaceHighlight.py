#!/usr/bin/python
# -*- coding: utf8 -*-
import sublime
import sublime_plugin

class FullPitchWhiteSpaceHighlightListener(sublime_plugin.EventListener):
    # highlight full-pitch white spaces
    def highlight_fullpitch_spaces(self, view):
        if view.settings().get('fullwhitespace_viewable') == True:
            view.add_regions('FullPitchWhiteSpaceHighlight',
                             view.find_all(u'　+'),
                             "entity.name.class",
                             sublime.DRAW_OUTLINED)
        else:
            view.erase_regions('FullPitchWhiteSpaceHighlight')
    # Called after changes have been made to a view.
    # @override
    def on_modified(self, view):
        self.highlight_fullpitch_spaces(view)

    # Called when a view gains input focus.
    # @override
    def on_activated(self, view):
        self.highlight_fullpitch_spaces(view)

    # Called when the file is finished loading.
    # @override
    def on_load(self, view):
        self.highlight_fullpitch_spaces(view)
