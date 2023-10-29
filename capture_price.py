import tkinter as tk
from PIL import Image, ImageDraw, ImageTk
from tkinter import filedialog

class CapturePrice:
    def __init__(self, screenshot_path):
        self.root = tk.Tk()
        self.root.title("Capture price interface")

        # Load the screenshot
        self.screenshot = Image.open(screenshot_path)
        self.screenshot_copy = self.screenshot.copy()

        # Create a scrollable canvas
        self.canvas_frame = tk.Frame(self.root)
        self.canvas_frame.pack(fill=tk.BOTH, expand=True)

        self.canvas = tk.Canvas(self.canvas_frame, width=self.screenshot.width, height=750)
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.scrollbar = tk.Scrollbar(self.canvas_frame, command=self.canvas.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.canvas.config(yscrollcommand=self.scrollbar.set)
        self.canvas.bind("<Configure>", self.on_canvas_configure)

        self.photo = ImageTk.PhotoImage(self.screenshot)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.photo)

        # Initialize drawing variables
        self.start_x = None
        self.start_y = None
        self.selection = None
        self.rect = None

        # Add a button to capture the selected area
        tk.Button(self.root, text="Capture Selection", command=self.capture_selection).pack()

        # Start listening for mouse events
        self.canvas.bind("<ButtonPress-1>", self.on_press)
        self.canvas.bind("<B1-Motion>", self.on_drag)
        self.canvas.bind("<ButtonRelease-1>", self.on_release)

    def on_canvas_configure(self, event):
        # Update the canvas scroll region when the canvas size changes
        self.canvas.config(scrollregion=self.canvas.bbox("all"))

    def on_press(self, event):
        self.start_x = self.canvas.canvasx(event.x)
        self.start_y = self.canvas.canvasy(event.y)

        if self.rect:
            self.canvas.delete(self.rect)
        
        self.rect = self.canvas.create_rectangle(self.start_x, self.start_y, self.start_x, self.start_y, outline="red")

    def on_drag(self, event):
        cur_x = self.canvas.canvasx(event.x)
        cur_y = self.canvas.canvasy(event.y)

        self.canvas.coords(self.rect, self.start_x, self.start_y, cur_x, cur_y)

    def on_release(self, event):
        end_x = self.canvas.canvasx(event.x)
        end_y = self.canvas.canvasy(event.y)

        # Ensure that the end coordinates are within the bounds of the screenshot
        end_x = min(max(end_x, 0), self.screenshot.width)
        end_y = min(max(end_y, 0), self.screenshot.height)

        # Capture the selected area
        selected_area = self.screenshot_copy.crop((self.start_x, self.start_y, end_x, end_y))
        self.selection = (self.start_x, self.start_y, end_x, end_y)
        
        # Save the selected area as an image
        file_path = "results/price_test.png"
        if file_path:
            selected_area.save(file_path)
            print(f"Selected area saved as '{file_path}'")

    def capture_selection(self):
        # Capture the selection and display it in a new window
        selected_area = self.screenshot.crop((self.start_x, self.start_y, self.canvas.canvasx(self.rect[2]), self.canvas.canvasy(self.rect[3])))
        selected_area.show()

    def run(self):
        self.root.mainloop()
