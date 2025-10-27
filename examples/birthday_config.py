"""
Example Configuration: Birthday Party Invitation
Copy this to config.py and customize for your birthday party
"""

PARTICIPANTS = [
    "Emma Thompson",
    "Liam Wilson",
    "Olivia Davis",
    "Noah Martinez",
    "Ava Garcia",
]

EVENT_CONFIG = {
    'event': {
        'title': 'Birthday Celebration',
        'subtitle': "Let's Party!",
        'details': [
            '🎂 Date: Saturday, December 15, 2025',
            '🕐 Time: 3:00 PM - 7:00 PM',
            '📍 Location: Community Center Hall',
        ]
    },
    
    'agenda': [
        'Welcome & Icebreaker Games',
        'Birthday Cake Cutting',
        'Entertainment Show',
        'Dinner Buffet',
        'Gift Exchange & Fun',
    ],
    
    'texts': {
        'greeting_prefix': 'Hey',
        'greeting_suffix': '!',
        'introduction': [
            "You're invited to celebrate an amazing birthday!",
            "Join us for food, fun, and fantastic memories.",
        ],
        'agenda_title': 'PARTY SCHEDULE',
        'thanks': "Can't wait to celebrate with you!",
        'closing': 'See you there,',
        'signature': 'The Birthday Crew',
    },
    
    'colors': {
        'background': '#FFE5E5',  # Light pink
        'accent': '#FF69B4',      # Hot pink
        'text': '#4A0E4E',        # Purple
        'box_bg': '#FFFFFF',      # White
    }
}

PAPER_SIZE = 'A6'  # Smaller card for casual party
OUTPUT_FOLDER = 'output_birthday'
