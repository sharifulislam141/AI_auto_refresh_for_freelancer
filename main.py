import pyautogui
import time
import random
import google.generativeai as genai
import json
from PIL import Image

# === Gemini API Setup ===
with open('config.json', 'r') as f:
    config = json.load(f)
API_KEY = config.get('api_key')
genai.configure(api_key=API_KEY)

# === Screen Info ===
screen_width, screen_height = pyautogui.size()
print(f"[+] Screen size: {screen_width}x{screen_height}")

def take_screenshot(filename="screen.png"):
    pyautogui.screenshot(filename)
    return filename

def get_clickable_boxes(image_path):
    model = genai.GenerativeModel("gemini-1.5-flash")
    prompt = f"""
    This is a screenshot of my {screen_width}x{screen_height} screen.
    Identify clickable elements (buttons, links, menus).
    Return a JSON list with bounding boxes in format:
    [
      {{"label": "Button", "x1": int, "y1": int, "x2": int, "y2": int}}
    ]
    Only return JSON.
    """

    # Open with PIL instead of raw file object
    img = Image.open(image_path)

    response = model.generate_content(
        [prompt, img],
        generation_config=genai.GenerationConfig(response_mime_type="application/json")
    )

    try:
        return json.loads(response.text)
    except Exception as e:
        print("[!] JSON parsing failed:", e)
        print("Raw response:", response.text)
        return []


def human_like_move_click(x, y):
    cx, cy = pyautogui.position()
    steps = random.randint(6, 12)
    for i in range(steps):
        nx = cx + (x - cx) * (i+1)/steps + random.randint(-2, 2)
        ny = cy + (y - cy) * (i+1)/steps + random.randint(-2, 2)
        pyautogui.moveTo(nx, ny, duration=random.uniform(0.05, 0.2))
    time.sleep(random.uniform(0.3, 1.0))
    pyautogui.click(x, y)

def random_scroll():
    scroll_amount = random.choice([-500, -200, -100, 100, 200, 400])
    pyautogui.scroll(scroll_amount)
    print(f"[+] Scrolled {scroll_amount}")
    time.sleep(random.uniform(0.5, 2.5))

def work_on_tab():
    screenshot_path = take_screenshot()
    boxes = get_clickable_boxes(screenshot_path)

    if not boxes:
        print("[!] No clickable elements found.")
        return

    img_file = Image.open(screenshot_path)

    for _ in range(random.randint(2, 4)):
        box = random.choice(boxes)
        x1, y1, x2, y2 = box["x1"], box["y1"], box["x2"], box["y2"]

        rx = random.randint(x1, x2)
        ry = random.randint(y1, y2)

        print(f"[+] Clicking {box['label']} at ({rx},{ry})")

        time.sleep(random.uniform(6, 300))
        human_like_move_click(rx, ry)

        if random.random() < 0.4:
            random_scroll()

        if random.random() < 0.3:
            idle = random.uniform(50, 120)
            print(f"[+] Idle {idle:.1f} sec")
            time.sleep(idle)

def switch_tab():
    print("[+] Switching to next tab with Ctrl+Tab")
    pyautogui.hotkey("ctrl", "tab")
    time.sleep(random.uniform(2, 4))  # delay after switching

# === Infinite Loop ===
while True:
    time.sleep(5)
    work_on_tab()
    switch_tab()
