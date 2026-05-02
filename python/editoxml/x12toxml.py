import pyx12.x12n_document
import pyx12.params
import os

def convert():
    input_file = "execution/samples/837_mult_claims.txt"
    output_file = "outputfile.xml"
    
    # Ensure the input exists to avoid obscure errors
    if not os.path.exists(input_file):
        print(f"Error: File {input_file} not found.")
        return

    # 1. Setup Parameters
    # We must explicitly tell it to output 'simple' XML
    param = pyx12.params.params()
    param.set('xmlout', 'simple') 

    try:
        # 2. Open the output file handle
        with open(output_file, 'w') as fd_xml:
            # 3. Call the primary document function
            # Arguments: (params, input_path, fd_997, fd_html, fd_xml)
            # Setting fd_997 and fd_html to None skips their generation
            pyx12.x12n_document.x12n_document(
                param, 
                input_file, 
                fd_997=None, 
                fd_html=None, 
                fd_xmldoc=fd_xml
            )
            
        print(f"Success! XML generated at {output_file}")
        
    except Exception as e:
        print(f"Conversion failed: {str(e)}")

if __name__ == "__main__":
    convert()