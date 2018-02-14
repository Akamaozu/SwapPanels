from fman import DirectoryPaneCommand

class SwapPanel(DirectoryPaneCommand):
    def __call__(self):
        panes = self.pane.window.get_panes()

        lpane = panes[0]
        lpane_path = lpane.get_path()
        lpane_selection = lpane.get_selected_files()

        rpane = panes[1]
        rpane_path = rpane.get_path()
        rpane_selection = rpane.get_selected_files()

        lpane.set_path( rpane_path )
        rpane.set_path( lpane_path )

        if( lpane_selection ):
            for url in lpane_selection:
                rpane.toggle_selection( url )

        if( rpane_selection ):
            for url in rpane_selection:
                lpane.toggle_selection( url )