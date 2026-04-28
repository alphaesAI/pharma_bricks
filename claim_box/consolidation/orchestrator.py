from claim_box.consolidation.parser import X12Parser

def run():
    # Using the available sample file
    input_file = "execution/samples/837_mult_claims.txt" 
    
    try:
        parser = X12Parser(input_file)
        results = parser()
        
        for line in results:
            print(line)
            
    except Exception as e:
        print(f"Orchestrator Error: {e}")

if __name__ == "__main__":
    run()