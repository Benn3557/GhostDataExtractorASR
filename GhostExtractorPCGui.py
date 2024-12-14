import os
import tkinter as tk
from tkinter import filedialog, messagebox

# Made By (Chatgpt) and (VoviBen)

def extract_data_between_occurrences(input_file, output_dir, custom_names, offsets):
    try:
        with open(input_file, 'rb') as f:
            data = f.read()
            start_sequence = b'GZ'
            inner_start_sequence = b'\x78\x9C'
            stop_sequence = b'\x00\x00\x00\x00'

            for custom_name, offset in zip(custom_names, offsets):
                # Check if "GZ" is present at the current offset
                if data[offset:offset + len(start_sequence)] != start_sequence:
                    print(f"Skipping offset {offset} because 'GZ' sequence not found for {custom_name}")
                    continue

                # Set the initial offset to 216 if the provided offset is lower
                current_offset = max(offset, 216)

                # Search for the start sequence from the current offset
                start = data.find(start_sequence, current_offset)
                if start == -1:
                    print(f"No start sequence found at or after offset {current_offset} for {custom_name}")
                    continue

                # Search for the inner start sequence after finding the initial start sequence
                inner_start = data.find(inner_start_sequence, start)
                if inner_start == -1:
                    print(f"No inner start sequence found after {start_sequence} at offset {start} for {custom_name}")
                    continue

                # Find the end sequence after the inner start sequence
                end = data.find(stop_sequence, inner_start)
                if end == -1:
                    print(f"No stop sequence found after offset {inner_start} for {custom_name}")
                    continue

                # Adjust end to include the stop sequence
                end += len(stop_sequence)

                # Extract data from the initial start sequence to the end
                extracted_data = data[start:end]
                output_file = os.path.join(output_dir, custom_name)

                with open(output_file, 'wb') as f_out:
                    f_out.write(extracted_data)

                print(f"Extracted data from {start} to {end} into {output_file}")

    except FileNotFoundError:
        print("Input file not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

def open_file_dialog():
    file_path = filedialog.askopenfilename(title="Select file", filetypes=(("ssr_save.bin", "*.bin*"), ("All files", "*.*")))
    if file_path:
        output_directory = "output"
        if not os.path.exists(output_directory):
            os.makedirs(output_directory)

        custom_names = [
            "9a531da2_billyhatcher_easy.lap.gz", 
            "9a531da2_seasidehill_easy.lap.gz", 
            "9a531da2_samba_easy.lap.gz", 
            "9a531da2_smb_easy.lap.gz", 
            "9a531da2_jetsetradio_easy.lap.gz", 
            "9a531da2_houseofthedead_easy.lap.gz", 
            "9a531da2_finalfortress_easy.lap.gz", 
            "9a531da2_casinopark_medium.lap.gz", 
            "9a531da2_billyhatcher_medium.lap.gz", 
            "9a531da2_seasidehill_medium.lap.gz", 
            "9a531da2_samba_medium.lap.gz", 
            "9a531da2_smb_medium.lap.gz", 
            "9a531da2_jetsetradio_medium.lap.gz", 
            "9a531da2_houseofthedead_medium.lap.gz", 
            "9a531da2_finalfortress_medium.lap.gz", 
            "9a531da2_casinopark_easy.lap.gz", 
            "9a531da2_billyhatcher_hard.lap.gz", 
            "9a531da2_seasidehill_hard.lap.gz", 
            "9a531da2_samba_hard.lap.gz", 
            "9a531da2_smb_hard.lap.gz", 
            "9a531da2_jetsetradio_hard.lap.gz", 
            "9a531da2_houseofthedead_hard.lap.gz", 
            "9a531da2_finalfortress_hard.lap.gz", 
            "9a531da2_casinopark_hard.lap.gz", 
        ]

        offsets = [
        61256,
        85840,
        110424,
        135008,
        159592,
        184176,
        208760,
        233344,
        257928,
        282512,
        307096,
        331680,
        356264,
        380848,
        405432,
        430016,
        454600,
        479184,
        503768,
        528352,
        552936,
        577520,
        602104,
        626688,
        ]

        extract_data_between_occurrences(file_path, output_directory, custom_names, offsets)
        messagebox.showinfo("Success", "Extraction completed successfully.")

def create_gui():
    root = tk.Tk()
    root.title("Ghost Extractor")
    root.geometry("250x150")

    label = tk.Label(root, text="Select a ssr_save.bin file :3")
    label.pack(pady=10)

    open_button = tk.Button(root, text="Open File", command=open_file_dialog)
    open_button.pack(pady=20)

    root.mainloop()

if __name__ == "__main__":
    create_gui()
