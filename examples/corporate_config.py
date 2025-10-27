"""
Example Configuration: Corporate Meeting Invitation
Copy this to config.py and customize for your business meeting
"""

PARTICIPANTS = [
    "John Smith - CEO",
    "Sarah Johnson - CFO",
    "Michael Chen - CTO",
    "Emily Rodriguez - VP Sales",
    "David Lee - VP Marketing",
]

EVENT_CONFIG = {
    'event': {
        'title': 'Quarterly Business Review',
        'subtitle': 'Q4 2025',
        'details': [
            '📅 Date: Wednesday, October 30, 2025',
            '🕐 Time: 9:00 AM - 12:00 PM',
            '📍 Location: Conference Room A, HQ Building',
        ]
    },
    
    'agenda': [
        'Opening Remarks & Objectives',
        'Q4 Performance Review',
        'Strategic Planning Session',
        'Department Updates',
        'Action Items & Next Steps',
    ],
    
    'texts': {
        'greeting_prefix': 'Dear',
        'greeting_suffix': ',',
        'introduction': [
            'You are cordially invited to attend our quarterly',
            'business review meeting to discuss performance and strategy.',
        ],
        'agenda_title': 'MEETING AGENDA',
        'thanks': 'Your participation and insights are valuable to our success.',
        'closing': 'Best regards,',
        'signature': 'Executive Team',
    },
    
    'colors': {
        'background': '#F5F5F5',  # Light gray
        'accent': '#2E5090',      # Corporate blue
        'text': '#1A1A1A',        # Almost black
        'box_bg': '#FFFFFF',      # White
    }
}

PAPER_SIZE = 'LETTER'  # US standard for business
OUTPUT_FOLDER = 'output_corporate'
