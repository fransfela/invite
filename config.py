"""
Configuration File for Invitation Cards
Edit this file to customize your event invitations
"""

# ============================================
# PARTICIPANTS
# ============================================
# Add or modify participant names here
PARTICIPANTS = [
    "Part1",
    "Part2",
    "Part3",
    "Part4",
    "Part5",
    "Part6",
    "Part7",
    "Part8",
]

# ============================================
# EVENT DETAILS
# ============================================
EVENT_CONFIG = {
    'event': {
        'title': 'Honey Sensory Test',
        'subtitle': '& Lunch Gathering',
        'details': [
            '📅 Date: Friday, November 1, 2025',
            '🕐 Time: 11:00 AM - 2:00 PM',
            '📍 Location: My Place - Sensory Lab',
        ]
    },
    
    'agenda': [
        'Short Briefing',
        'Sensory Evaluation',
        'Lunch Together',
        'Dhuhr Prayer in Congregation',
        'Casual Conversation',
    ],
    
    'texts': {
        'greeting_prefix': 'Dear',
        'greeting_suffix': ',',
        'introduction': [
            'We are delighted to invite you to join us for an exciting',
            'honey sensory evaluation session followed by lunch.',
        ],
        'agenda_title': 'AGENDA',
        'thanks': 'We look forward to your presence and valuable insights!',
        'closing': 'Warm regards,',
        'signature': 'The Organizing Team',
    },
    
    'colors': {
        'background': '#FFF8E7',  # Warm cream
        'accent': '#D4A574',      # Honey gold
        'text': '#2C1810',        # Dark brown
        'box_bg': '#FFFFFF',      # White box
    }
}

# ============================================
# PAPER SIZE SETTINGS
# ============================================
# Choose from: 'A4', 'A5', 'A6', 'LETTER', 'CARD_5X7', 'SQUARE'
# Or use custom size: (width, height) in pixels at 300 DPI
PAPER_SIZE = 'A5'

# Custom size example (uncomment to use):
# PAPER_SIZE = (1500, 2100)  # Custom 5x7 inches

# ============================================
# OUTPUT SETTINGS
# ============================================
OUTPUT_FOLDER = 'output'
