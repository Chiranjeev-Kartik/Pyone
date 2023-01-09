import tkinter as tk
import time

class Stopwatch(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self._start = 0.0
        self._elapsedtime = 0.0
        self._running = 0
        self.timestr = tk.StringVar()
        self.makeWidgets()

    def makeWidgets(self):
        l = tk.Label(self, textvariable=self.timestr)
        self._setTime(self._elapsedtime)
        l.pack(fill=tk.X, expand=tk.NO, pady=2, padx=2)

    def _update(self):
        self._elapsedtime = time.time() - self._start
        self._setTime(self._elapsedtime)
        self._timer = self.after(50, self._update)

    def _setTime(self, elap):
        minutes = int(elap/60)
        seconds = int(elap - minutes*60.0)
        hseconds = int((elap - minutes*60.0 - seconds)*100)
        self.timestr.set('%02d:%02d:%02d' % (minutes, seconds, hseconds))

    def Start(self):
        if not self._running:
            self._start = time.time() - self._elapsedtime
            self._update()
            self._running = 1

    def Stop(self):
        if self._running:
            self.after_cancel(self._timer)
            self._elapsedtime = time.time() - self._start
            self._setTime(self._elapsedtime)
            self._running = 0

    def Reset(self):
        self._start = time.time()
        self._elapsedtime = 0.0
        self._setTime(self._elapsedtime)

def main():
    root = tk.Tk()
    sw = Stopwatch(root)
    sw.pack(side=tk.TOP)

    tk.Button(root, text='Start', command=sw.Start).pack(side=tk.LEFT)
    tk.Button(root, text='Stop', command=sw.Stop).pack(side=tk.LEFT)
    tk.Button(root, text='Reset', command=sw.Reset).pack(side=tk.LEFT)
    tk.Button(root, text='Quit', command=root.quit).pack(side=tk.LEFT)

    root.mainloop()

if __name__ == '__main__':
    main()