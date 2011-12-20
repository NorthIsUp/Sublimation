# -*- coding: utf-8 -*-
import sublime


def block_select(self, edit):
    sel = self.view.sel()
    view = self.view

    if len(sel) == 1:
        is_block = False
    else:
        is_block = True

    a = view.rowcol(sel[0].begin())
    b = view.rowcol(sel[-1].end())

    sel.clear()

    pt_start = min(a[1], b[1])
    pt_end = max(a[1], b[1])

    if is_block:
        x = a[0]
        y = b[0]
        start = self.view.text_point(x, pt_start)
        end = self.view.text_point(y, pt_end)
        sel.add(sublime.Region(start, end))
    else:
        for x in xrange(a[0], b[0] + 1):
            start = self.view.text_point(x, pt_start)
            end = self.view.text_point(x, pt_end)
            sel.add(sublime.Region(start, end))
