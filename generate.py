"""
Main script to generate invitation cards with auto-fit height
Run this file to create all invitations
"""

from invite import generate_all_invitations
from config import PARTICIPANTS, EVENT_CONFIG, PAPER_SIZE, OUTPUT_FOLDER

def main():
    """Generate invitation cards with auto-fit height based on config.py settings"""
    
    # Generate all invitations
    generated_files = generate_all_invitations(
        participants=PARTICIPANTS,
        config=EVENT_CONFIG,
        paper_size=PAPER_SIZE,
        output_folder=OUTPUT_FOLDER
    )
    
    print("\n📊 Summary:")
    print(f"   Total cards generated: {len(generated_files)}")
    print(f"   Paper width: {PAPER_SIZE}")
    print(f"   Height: Auto-calculated (no white space!)")
    print(f"   Saved to: {OUTPUT_FOLDER}/\n")

if __name__ == "__main__":
    main()
