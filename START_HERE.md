# 🚀 START HERE

Welcome to the Invitation Card Generator!

## ⚡ Quick Start (3 Steps)

### Step 1: Install Dependency
```bash
pip install Pillow
```

### Step 2: Edit `config.py`
```python
# Line 12-21: Add your participants
PARTICIPANTS = [
    "John Doe",
    "Jane Smith",
    # Add more...
]

# Line 27-33: Update event details
'title': 'Your Event Title',
'details': [
    '📅 Date: Your Date',
    '🕐 Time: Your Time',
    '📍 Location: Your Location',
]

# Line 65: Choose width
PAPER_SIZE = 'A5'  # Options: A4, A5, A6, LETTER
```

### Step 3: Generate Cards
```bash
python generate_autofit.py
```

✅ Done! Find your cards in `output/` folder!

---

## 📋 Two Versions Available

### ⭐ Version 1: Auto-Fit Height (RECOMMENDED)
**Run:** `python generate_autofit.py`

✅ Height adjusts to content  
✅ No wasted white space  
✅ Compact and efficient  
✅ ~51% shorter than fixed size  

**Result:**
- A5 width → 1748 × **1212** px (compact!)
- Perfect fit for your content

### Version 2: Fixed Standard Size
**Run:** `python generate.py`

✅ Standard paper sizes  
✅ Traditional format  

**Result:**
- A5 size → 1748 × 2480 px (full A5)

---

## 🎨 Quick Customization

### Change Colors
```python
# In config.py, line 59-64
'colors': {
    'background': '#FFF8E7',  # Your color
    'accent': '#D4A574',      # Your color
    'text': '#2C1810',        # Your color
}
```

### Change Size
```python
# Line 65
PAPER_SIZE = 'A4'  # Larger
PAPER_SIZE = 'A6'  # Smaller
PAPER_SIZE = 1500  # Custom width (pixels)
```

### Modify Agenda
```python
# Line 36-42
'agenda': [
    'Your Item 1',
    'Your Item 2',
    'Your Item 3',
    # Add or remove as needed
],
```

---

## 📚 Documentation

- **README_AUTOFIT.md** - Complete auto-fit guide
- **QUICKSTART.md** - 5-minute quick start
- **README.md** - Full documentation
- **VISUAL_GUIDE.md** - Visual walkthrough
- **TECHNICAL.md** - Technical deep dive

---

## 💡 Examples Included

Check the `examples/` folder:
- `wedding_config.py` - Wedding invitation
- `birthday_config.py` - Birthday party
- `corporate_config.py` - Corporate meeting

Copy any example to `config.py` and run!

---

## 🎯 What You'll Get

**Input:**
```python
PARTICIPANTS = ["Alice", "Bob", "Charlie"]
PAPER_SIZE = 'A5'
```

**Output:**
```
output/
├── Alice_invitation_A5.png
├── Bob_invitation_A5.png
└── Charlie_invitation_A5.png
```

All cards are:
- ✅ 300 DPI (print-ready)
- ✅ PNG format (high quality)
- ✅ Auto-fit height (no waste)
- ✅ Responsive width (scales perfectly)

---

## 🔥 Pro Tips

1. **Test with one participant first**
   ```python
   PARTICIPANTS = ["Test User"]
   ```
   
2. **Try different sizes**
   ```bash
   python demo_autofit.py  # Compare A6, A5, A4
   ```

3. **Use examples as templates**
   ```bash
   cp examples/wedding_config.py config.py
   ```

---

## ❓ Need Help?

**Issue:** Cards don't generate  
**Fix:** Make sure Pillow is installed: `pip install Pillow`

**Issue:** Want to change layout  
**Fix:** Edit `invitation_generator_autofit.py`

**Issue:** Need different paper size  
**Fix:** Change `PAPER_SIZE` in config.py

---

## 🎊 That's It!

You're ready to generate beautiful invitation cards!

**Next step:** Edit `config.py` and run `python generate_autofit.py`

🎉 **Happy card making!**
