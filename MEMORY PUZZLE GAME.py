import tkinter as tk
from tkinter import messagebox
import random

class MemoryGame:
    def __init__(self, root, rows=3, cols=2):  
        self.root, self.rows, self.cols = root, rows, cols
        self.n = rows * cols
        self.cards = self._make_cards()
        self.first = None
        self.matched = set()
        self.btns = []
        for r in range(rows):
            row = []
            for c in range(cols):
                i = r * cols + c
                b = tk.Button(root, text="", width=6, height=3,
                              font=("Segoe UI Emoji", 20),
                              command=lambda i=i: self.on_click(i))
                b.grid(row=r, column=c, padx=4, pady=4)
                row.append(b)
            self.btns.append(row)
        tk.Button(root, text="Restart", command=self.restart).grid(row=rows, column=0, columnspan=cols, sticky="we")

    def _make_cards(self):
        pool = ["🍎","🍇","🍒","🍓","🍊","🍉","🍍"]
        need = self.n // 2
        deck = pool[:need] * 2
        random.shuffle(deck)
        return deck

    def on_click(self, i):
        if i in self.matched: return
        btn = self.btns[i // self.cols][i % self.cols]
        if btn["text"]: return  
        btn["text"] = self.cards[i]
        if self.first is None:
            self.first = i
            return
        if self.first == i: return
        i1, i2 = self.first, i
        if self.cards[i1] == self.cards[i2]:
            self.matched.update((i1, i2))
            self.first = None
            if len(self.matched) == self.n:
                messagebox.showinfo("You win!", "All pairs found 🎉")
        else:
            self.root.after(700, lambda: (self.hide(i1), self.hide(i2)))
            self.first = None

    def hide(self, i):
        self.btns[i // self.cols][i % self.cols]["text"] = ""

    def restart(self):
        random.shuffle(self.cards)
        self.first = None
        self.matched.clear()
        for b in sum(self.btns, []):
            b.config(text="")

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Memory Game 3x2")
    MemoryGame(root)
    root.mainloop()
