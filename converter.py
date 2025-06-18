import base64
import sys
import os

def convert_base64_to_jpeg(input_file, output_file=None):
    # Read the base64 data from file
    with open(input_file, 'r') as f:
        base64_data = f.read().strip()
    
    # Remove the data URL prefix if present
    if base64_data.startswith('data:image/jpeg;base64,'):
        base64_data = base64_data.replace('data:image/jpeg;base64,', '')
    
    try:
        # Decode base64 data
        image_data = base64.b64decode(base64_data)
        
        # If no output file specified, use input filename with .jpg extension
        if output_file is None:
            output_file = os.path.splitext(input_file)[0] + '.jpg'
        
        # Write the decoded data to a JPEG file
        with open(output_file, 'wb') as f:
            f.write(image_data)
        
        print(f"Successfully converted {input_file} to {output_file}")
        return True
    
    except Exception as e:
        print(f"Error converting file: {str(e)}")
        return False

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python base64_to_jpeg.py <input_file> [output_file]")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else None
    
    convert_base64_to_jpeg(input_file, output_file) 