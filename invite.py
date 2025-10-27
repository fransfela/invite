"""
Invitation Card Generator with Auto-Fit Height
Card height automatically adjusts to content length
"""

from PIL import Image, ImageDraw, ImageFont
import os
import math

class InvitationCardGenerator:
    """
    Main class for generating responsive invitation cards
    Height automatically adjusts to content to avoid white space
    """
    
    # ===== PREDEFINED PAPER WIDTHS (height is auto-calculated) =====
    PAPER_WIDTHS = {
        'A4': 2480,      # 210 mm width
        'A5': 1748,      # 148 mm width
        'A6': 1240,      # 105 mm width
        'LETTER': 2550,  # 8.5 inches width
        'CARD_5X7': 1500, # 5 inches width
        'SQUARE': 2000,   # Square-ish width
    }
    
    def __init__(self, paper_size='A5'):
        """
        Initialize the generator with specified paper width
        Height will be calculated based on content
        
        Args:
            paper_size: Paper size name ('A4', 'A5', etc.) or custom width (int)
        """
        # Set card width
        if isinstance(paper_size, str):
            if paper_size.upper() in self.PAPER_WIDTHS:
                self.width = self.PAPER_WIDTHS[paper_size.upper()]
                self.size_name = paper_size.upper()
            else:
                raise ValueError(f"Unknown paper size: {paper_size}. Available: {list(self.PAPER_WIDTHS.keys())}")
        elif isinstance(paper_size, int):
            self.width = paper_size
            self.size_name = f"CUSTOM_{paper_size}"
        else:
            raise ValueError("paper_size must be a string or int (width)")
        
        # Height will be calculated based on content
        self.height = None
        
        # Calculate scaling factor based on A5 as reference (1748)
        reference_width = 1748
        self.scale = self.width / reference_width
        
        # Initialize scaled values
        self._init_scaled_values()
        
    def _init_scaled_values(self):
        """Calculate all scaled values based on card width"""
        s = self.scale  # Shorthand for scale
        
        # Border and spacing
        self.border_width = int(20 * s)
        self.border_thickness = max(4, int(8 * s))
        self.padding = int(80 * s)  # Reduced from 100
        self.line_spacing = int(35 * s)  # Reduced from 45
        self.section_spacing = int(60 * s)  # Reduced from 80
        
        # Font sizes (scaled)
        self.font_sizes = {
            'title': int(72 * s),
            'subtitle': int(48 * s),
            'heading': int(36 * s),
            'body': int(28 * s),
            'small': int(24 * s),
        }
        
        # Decorative elements
        self.hex_size = int(30 * s)
        
        # Box dimensions
        self.box_padding = int(30 * s)  # Reduced from 40
        self.box_line_height = int(45 * s)  # Reduced from 50
        
    def _calculate_content_height(self, config):
        """
        Calculate required height based on content
        Returns the total height needed for all content
        """
        height = 0
        
        # Top padding
        height += self.padding
        
        # Title
        height += int(self.font_sizes['title'] * 1.3)
        
        # Subtitle
        height += self.section_spacing
        
        # Greeting
        height += self.section_spacing
        
        # Introduction lines
        intro_lines = config['texts']['introduction']
        height += len(intro_lines) * self.line_spacing
        height += self.section_spacing
        
        # Event details box
        details_count = len(config['event']['details'])
        box_height = details_count * self.box_line_height + self.box_padding * 2
        height += box_height
        height += self.section_spacing
        
        # Agenda title
        height += int(self.font_sizes['heading'] * 1.5)
        
        # Agenda items
        agenda_count = len(config['agenda'])
        height += agenda_count * self.line_spacing
        height += self.section_spacing
        
        # Thank you message
        height += self.line_spacing
        height += self.section_spacing
        
        # Closing
        height += self.line_spacing * 2
        
        # Bottom padding
        height += self.padding
        
        return height
    
    def _get_font(self, size):
        """Load font with specified size, fallback to default if not available"""
        try:
            return ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf", size)
        except:
            try:
                return ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", size)
            except:
                return ImageFont.load_default()
    
    def _get_regular_font(self, size):
        """Load regular (non-bold) font"""
        try:
            return ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", size)
        except:
            return ImageFont.load_default()
    
    def _draw_centered_text(self, draw, text, y, font, color):
        """Draw text centered horizontally"""
        bbox = draw.textbbox((0, 0), text, font=font)
        text_width = bbox[2] - bbox[0]
        x = (self.width - text_width) // 2
        draw.text((x, y), text, font=font, fill=color)
        return bbox[3] - bbox[1]  # Return text height
    
    def _draw_text(self, draw, text, x, y, font, color):
        """Draw text at specified position"""
        draw.text((x, y), text, font=font, fill=color)
    
    def _draw_hexagon(self, draw, x, y, size, color, width=2):
        """Draw a hexagon shape"""
        angles = [i * 60 for i in range(6)]
        points = []
        for angle in angles:
            rad = math.radians(angle)
            px = x + size * math.cos(rad)
            py = y + size * math.sin(rad)
            points.append((px, py))
        draw.polygon(points, outline=color, width=width)
    
    def _draw_honeycomb_pattern(self, draw, accent_color):
        """Draw decorative honeycomb pattern in corners (scaled)"""
        hex_size = self.hex_size
        spacing = int(hex_size * 1.4)
        
        # Top left
        positions_tl = [
            (self.padding * 0.7, self.padding * 0.7),
            (self.padding * 0.7 + spacing, self.padding * 0.7 + spacing * 0.5),
            (self.padding * 0.7 + spacing * 2, self.padding * 0.7),
        ]
        
        # Top right
        positions_tr = [
            (self.width - self.padding * 0.7 - spacing * 2, self.padding * 0.7),
            (self.width - self.padding * 0.7 - spacing, self.padding * 0.7 + spacing * 0.5),
            (self.width - self.padding * 0.7, self.padding * 0.7),
        ]
        
        # Bottom left
        positions_bl = [
            (self.padding * 0.7, self.height - self.padding * 0.7),
            (self.padding * 0.7 + spacing, self.height - self.padding * 0.7 - spacing * 0.5),
            (self.padding * 0.7 + spacing * 2, self.height - self.padding * 0.7),
        ]
        
        all_positions = positions_tl + positions_tr + positions_bl
        
        for x, y in all_positions:
            self._draw_hexagon(draw, x, y, hex_size, accent_color, width=max(2, int(2 * self.scale)))
    
    def generate_card(self, config, participant_name, output_folder='output'):
        """
        Generate a single invitation card with auto-fit height
        
        Args:
            config: Dictionary containing event details and styling
            participant_name: Name of the participant
            output_folder: Folder to save the card
        
        Returns:
            Path to the generated card
        """
        
        # Calculate required height based on content
        self.height = self._calculate_content_height(config)
        
        # Extract configuration
        event = config['event']
        agenda = config['agenda']
        colors = config['colors']
        texts = config['texts']
        
        # Create image
        img = Image.new('RGB', (self.width, self.height), colors['background'])
        draw = ImageDraw.Draw(img)
        
        # Add decorative border
        draw.rectangle(
            [self.border_width, self.border_width, 
             self.width - self.border_width, self.height - self.border_width],
            outline=colors['accent'],
            width=self.border_thickness
        )
        
        # Add honeycomb pattern
        self._draw_honeycomb_pattern(draw, colors['accent'])
        
        # Load fonts
        fonts = {
            'title': self._get_font(self.font_sizes['title']),
            'subtitle': self._get_font(self.font_sizes['subtitle']),
            'heading': self._get_font(self.font_sizes['heading']),
            'body': self._get_regular_font(self.font_sizes['body']),
            'small': self._get_regular_font(self.font_sizes['small']),
        }
        
        # Current Y position
        y_pos = self.padding
        
        # === TITLE ===
        self._draw_centered_text(draw, event['title'], y_pos, fonts['title'], colors['accent'])
        y_pos += int(self.font_sizes['title'] * 1.3)
        
        self._draw_centered_text(draw, event['subtitle'], y_pos, fonts['subtitle'], colors['accent'])
        y_pos += self.section_spacing
        
        # === GREETING ===
        greeting = f"{texts['greeting_prefix']} {participant_name}{texts['greeting_suffix']}"
        self._draw_text(draw, greeting, self.padding, y_pos, fonts['heading'], colors['text'])
        y_pos += self.section_spacing
        
        # === INTRODUCTION ===
        intro_lines = texts['introduction']
        for line in intro_lines:
            self._draw_text(draw, line, self.padding, y_pos, fonts['body'], colors['text'])
            y_pos += self.line_spacing
        y_pos += self.section_spacing - self.line_spacing
        
        # === EVENT DETAILS BOX ===
        box_height = len(event['details']) * self.box_line_height + self.box_padding * 2
        box_left = self.padding
        box_right = self.width - self.padding
        
        draw.rectangle(
            [box_left, y_pos, box_right, y_pos + box_height],
            fill=colors['box_bg'],
            outline=colors['accent'],
            width=max(2, int(3 * self.scale))
        )
        
        box_y = y_pos + self.box_padding
        for detail in event['details']:
            self._draw_text(draw, detail, box_left + self.box_padding, box_y, 
                          fonts['body'], colors['text'])
            box_y += self.box_line_height
        
        y_pos += box_height + self.section_spacing
        
        # === AGENDA ===
        self._draw_centered_text(draw, texts['agenda_title'], y_pos, fonts['heading'], colors['accent'])
        y_pos += int(self.font_sizes['heading'] * 1.5)
        
        for i, item in enumerate(agenda, 1):
            agenda_text = f"{i}. {item}"
            self._draw_text(draw, agenda_text, self.padding * 1.3, y_pos, fonts['body'], colors['text'])
            y_pos += self.line_spacing
        
        y_pos += self.section_spacing - self.line_spacing
        
        # === THANK YOU ===
        self._draw_centered_text(draw, texts['thanks'], y_pos, fonts['body'], colors['text'])
        y_pos += self.section_spacing
        
        # === CLOSING ===
        self._draw_text(draw, texts['closing'], self.padding, y_pos, fonts['body'], colors['text'])
        y_pos += self.line_spacing
        self._draw_text(draw, texts['signature'], self.padding, y_pos, fonts['heading'], colors['accent'])
        
        # Save the card
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)
        
        filename = f"{participant_name.replace(' ', '_')}_invitation_{self.size_name}.png"
        filepath = os.path.join(output_folder, filename)
        img.save(filepath, quality=95, dpi=(300, 300))
        
        return filepath


def generate_all_invitations(participants, config, paper_size='A5', output_folder='output'):
    """
    Generate invitation cards for all participants with auto-fit height
    
    Args:
        participants: List of participant names
        config: Configuration dictionary with event details
        paper_size: Paper width preset or custom width
        output_folder: Output directory
    
    Returns:
        List of generated file paths
    """
    
    print(f"\n{'='*60}")
    print(f"Invitation Card Generator (Auto-Fit Height)")
    print(f"{'='*60}")
    print(f"Paper Width: {paper_size}")
    print(f"Height: Auto-calculated based on content")
    print(f"Participants: {len(participants)}")
    print(f"Output: {output_folder}/")
    print(f"{'='*60}\n")
    
    # Initialize generator
    generator = InvitationCardGenerator(paper_size)
    
    generated_files = []
    
    # Generate card for each participant
    for participant in participants:
        filepath = generator.generate_card(config, participant, output_folder)
        print(f"✓ Created invitation for {participant}")
        generated_files.append(filepath)
    
    # Show actual dimensions after generation
    if generated_files:
        from PIL import Image
        sample = Image.open(generated_files[0])
        print(f"\n{'='*60}")
        print(f"✓ Successfully generated {len(generated_files)} invitation cards!")
        print(f"📐 Actual size: {sample.width} × {sample.height} pixels")
        print(f"📁 Location: {output_folder}/")
        print(f"{'='*60}\n")
    
    return generated_files


if __name__ == "__main__":
    # This is just for testing the module
    # Use config.py to run the actual generation
    print("This is a module. Please run: python generate.py")
