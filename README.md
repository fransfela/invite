# 📨 INVITE: **INstant Visual Invitation Text Editor**

Auto-fit invitation card generator with responsive sizing - create beautiful, compact invitation cards that automatically adjust to your content.

![Python](https://img.shields.io/badge/python-3.7+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

---

## ✨ Features

- **Auto-Fit Height** - Card height automatically adjusts to content (no wasted space!)
- **Responsive Width** - Choose from A4, A5, A6, Letter, or custom sizes
- **Batch Generation** - Create unlimited cards at once
- **Easy Config** - Single file configuration
- **High Quality** - 300 DPI PNG output, print-ready
- **Zero Setup** - Just edit config and run!

---

## 🚀 Quick Start

### 1. Install
```bash
pip install Pillow
```

### 2. Edit `config.py`
```python
PARTICIPANTS = ["John Doe", "Jane Smith", "Alice Brown"]
PAPER_SIZE = 'A5'  # Choose: A4, A5, A6, LETTER

EVENT_CONFIG = {
    'event': {
        'title': 'Your Event Title',
        'details': [
            '📅 Date: November 15, 2025',
            '🕐 Time: 2:00 PM',
            '📍 Location: Your Venue',
        ]
    },
    # ... more config
}
```

### 3. Generate!
```bash
python generate.py
```

✅ **Done!** Find your cards in the `output/` folder.

---

## 📐 Auto-Fit Magic

### Traditional vs INVITE

**Traditional Fixed Height:**
```
┌─────────────┐
│   Content   │
│             │
│             │  ← Wasted space
│             │
└─────────────┘
1748 × 2480 px
```

**INVITE Auto-Fit:**
```
┌─────────────┐
│   Content   │
│             │
└─────────────┘ ← Perfect fit!
1748 × 1212 px (51% shorter!)
```

**Result:**
- A6 width: 1240 × **842** px
- A5 width: 1748 × **1212** px
- A4 width: 2480 × **1707** px

Height automatically calculated based on your content!

---

## 🎨 Customization

### Choose Width
```python
PAPER_SIZE = 'A5'     # Standard (recommended)
PAPER_SIZE = 'A4'     # Large/formal
PAPER_SIZE = 'A6'     # Compact/postcard
PAPER_SIZE = 1500     # Custom width in pixels
```

### Change Colors
```python
'colors': {
    'background': '#FFF8E7',  # Warm cream
    'accent': '#D4A574',      # Honey gold
    'text': '#2C1810',        # Dark brown
}
```

### Modify Agenda
```python
'agenda': [
    'Registration',
    'Opening Ceremony',
    'Main Event',
    'Lunch',
    'Closing',
]
```

---

## 💡 Examples

Check the `examples/` folder for ready-to-use templates:
- **Wedding** - Elegant formal invitations
- **Birthday** - Fun party cards
- **Corporate** - Professional meeting invites

```bash
# Use a template
cp examples/wedding_config.py config.py
python generate.py
```

---

## 📁 Project Structure

```
invite/
├── invitation_generator_autofit.py  # Core engine
├── generate.py                      # Run this!
├── config.py                        # Edit this!
├── requirements.txt                 # Dependencies
├── README.md                        # This file
├── START_HERE.md                    # Quick guide
├── examples/                        # Templates
│   ├── wedding_config.py
│   ├── birthday_config.py
│   └── corporate_config.py
└── output/                          # Generated cards
```

---

## 🎯 Why INVITE?

| Feature | INVITE | Traditional Tools |
|---------|--------|-------------------|
| Auto-fit height | ✅ Yes | ❌ No |
| Batch processing | ✅ Unlimited | ⚠️ Manual |
| Responsive sizing | ✅ Perfect | ❌ Fixed |
| Open source | ✅ Free | ⚠️ Varies |
| Customization | ✅ Full control | ⚠️ Limited |
| Print quality | ✅ 300 DPI | ⚠️ Varies |

---

## 🤝 Contributing

Contributions welcome! Feel free to:
- Report bugs
- Suggest features
- Submit pull requests
- Share your templates

---

## 📝 License

MIT License - free to use, modify, and distribute.

---

## 🙏 Acknowledgments

Built with:
- [Pillow](https://python-pillow.org/) - Python Imaging Library
- Love for efficient, beautiful design ❤️

---

## 📧 Support

Questions? Ideas? Open an issue or start a discussion!

---

**INVITE** - *Because your invitations deserve better than wasted space* ✨

⭐ **Star this repo if you find it useful!**
