import os

class X12Parser:
    def __init__(self, file_path):
        self.file_path = file_path

    def __call__(self):
        """
        Reads the file and returns the list of formatted segment strings.
        """
        if not os.path.exists(self.file_path):
            raise FileNotFoundError(f"No file found at {self.file_path}")
            
        with open(self.file_path, 'r') as f:
            # Read and remove any trailing newlines/whitespace
            raw_data = f.read().strip()
            
        return self.parser(raw_data)

    def parser(self, raw_data):
        """
        Core logic: Manual X12 parsing to ensure correct element splitting.
        """
        formatted_output = []
        
        # 1. Identify delimiters from the ISA segment
        # In X12, the 4th character is the element separator (e.g., '*')
        # The character at index 105 is usually the segment terminator (e.g., '~')
        if len(raw_data) < 106 or not raw_data.startswith('ISA'):
            return ["Error: Invalid X12 file format."]

        element_sep = raw_data[3]
        segment_sep = raw_data[105]

        # 2. Split into segments
        segments = raw_data.split(segment_sep)
        
        # Filter out empty strings from trailing terminators
        valid_segments = [s for s in segments if s.strip()]
        
        # 3. Add the summary count line
        formatted_output.append(f"Read {len(valid_segments)} segments")

        # 4. Process each segment
        for seg in valid_segments:
            parts = seg.split(element_sep)
            tag = parts[0].strip()
            elements = parts[1:]
            
            # Format: TAG: ['elem1', 'elem2', ...]
            formatted_output.append(f"  {tag}: {elements}")
            
        return formatted_output