"""
Example Configuration: Wedding Invitation
Copy this to config.py and customize for your wedding
"""

PARTICIPANTS = [
    "Mr. & Mrs. Anderson",
    "Mr. & Mrs. Martinez",
    "Mr. & Mrs. Johnson",
    "Dr. & Dr. Williams",
]

EVENT_CONFIG = {
    'event': {
        'title': 'Wedding Celebration',
        'subtitle': 'Sarah & Michael',
        'details': [
            '💒 Date: Saturday, June 20, 2026',
            '🕐 Time: 4:00 PM',
            '📍 Location: Garden Venue, Riverside',
        ]
    },
    
    'agenda': [
        'Wedding Ceremony',
        'Cocktail Hour',
        'Reception & Dinner',
        'First Dance',
        'Dancing & Celebration',
    ],
    
    'texts': {
        'greeting_prefix': 'Dear',
        'greeting_suffix': ',',
        'introduction': [
            'Together with their families,',
            'Sarah Johnson and Michael Chen',
            'request the honor of your presence at their wedding.',
        ],
        'agenda_title': 'SCHEDULE',
        'thanks': 'Your presence would make our day complete!',
        'closing': 'With love,',
        'signature': 'Sarah & Michael',
    },
    
    'colors': {
        'background': '#FFF9F0',  # Warm white
        'accent': '#D4AF37',      # Gold
        'text': '#3E2723',        # Dark brown
        'box_bg': '#FFFFFF',      # Pure white
    }
}

PAPER_SIZE = 'A5'
OUTPUT_FOLDER = 'output_wedding'
