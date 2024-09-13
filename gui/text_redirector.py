class TextRedirector(object):
    def __init__(self, widget, tag):
        self.widget = widget
        self.tag = tag
    
    def write(self, string):
        self.widget.configure(state="normal")
        self.widget.tag_configure(self.tag, justify="center")
        self.widget.insert("end", string, (self.tag))
        self.widget.see("end")
        self.widget.configure(state="disabled")
    
    def flush(self):
        pass