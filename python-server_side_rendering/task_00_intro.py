#!/usr/bin/python3
import os

def generate_invitations(template, attendees):
    """
    Generates personalized invitation files from a template.
    """
    # 1. Giriş tiplərini yoxla (Check input types)
    if not isinstance(template, str):
        print(f"Error: Invalid input type for template. Expected str, got {type(template).__name__}.")
        return

    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        print(f"Error: Invalid input type for attendees. Expected list of dictionaries.")
        return

    # 2. Boş girişləri yoxla (Handle empty inputs)
    if not template.strip():
        print("Template is empty, no output files generated.")
        return

    if not attendees:
        print("No data provided, no output files generated.")
        return

    # 3. Hər bir iştirakçı üçün emal et (Process each attendee)
    for index, attendee in enumerate(attendees, start=1):
        processed_template = template
        
        # Əsas açarlar (placeholders)
        keys = ["name", "event_title", "event_date", "event_location"]
        
        for key in keys:
            # Əgər dəyər yoxdursa (None) və ya açar lüğətdə yoxdursa "N/A" yaz
            value = attendee.get(key)
            if value is None:
                value = "N/A"
            
            # {name} kimi yerləri real dəyərlərlə dəyiş
            processed_template = processed_template.replace(f"{{{key}}}", str(value))
        
        # 4. Çıxış fayllarını yarat (Generate output files)
        filename = f"output_{index}.txt"
        
        # Faylın artıq mövcud olub-olmadığını yoxlamaq (isteğe bağlı amma yaxşı təcrübədir)
        try:
            with open(filename, 'w') as f:
                f.write(processed_template)
        except Exception as e:
            print(f"Error writing to {filename}: {e}")
