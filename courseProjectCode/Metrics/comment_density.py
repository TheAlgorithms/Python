

import os
import sys

def comment_density():
    
    
    # Path to data_structures directory 
    data_structures_path = os.path.join(os.path.dirname(__file__), '..', '..', 'data_structures')
    
    if not os.path.exists(data_structures_path):
        print(f"Error: data_structures directory not found at {data_structures_path}")
        return
    
    total_lines = 0
    comment_lines = 0
    blank_lines = 0
    files_processed = 0
    
   
    for root, dirs, files in os.walk(data_structures_path):
        for file in files:
            if file.endswith('.py'):
                file_path = os.path.join(root, file)
                
                try:
                    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                        lines = f.readlines()
                    
                    file_total = len(lines)
                    file_comments = 0
                    file_blanks = 0
                    
                    in_multiline_comment = False
                    multiline_delimiter = None
                    
                    for line in lines:
                        stripped_line = line.strip()
                        original_line = line
                        
                        if not stripped_line:
                            file_blanks += 1
                            continue
                        
                        # Check single line comments
                        if stripped_line.startswith('#'):
                            file_comments += 1
                            continue
                        
                        # Check multi-line comments
                        line_is_comment = False
                        temp_line = original_line
                        
                        while True:
                            if not in_multiline_comment:
                                # Look for start of multi-line comment
                                triple_double_pos = temp_line.find('"""')
                                triple_single_pos = temp_line.find("'''")
                                
                                if triple_double_pos != -1 and (triple_single_pos == -1 or triple_double_pos < triple_single_pos):
                                    in_multiline_comment = True
                                    multiline_delimiter = '"""'
                                    line_is_comment = True
                                    temp_line = temp_line[triple_double_pos + 3:]
                                elif triple_single_pos != -1:
                                    in_multiline_comment = True
                                    multiline_delimiter = "'''"
                                    line_is_comment = True
                                    temp_line = temp_line[triple_single_pos + 3:]
                                else:
                                    break
                            else:
                                
                                line_is_comment = True
                                end_pos = temp_line.find(multiline_delimiter)
                                if end_pos != -1:
                                    in_multiline_comment = False
                                    multiline_delimiter = None
                                    temp_line = temp_line[end_pos + 3:]
                                else:
                                    break
                        
                        if line_is_comment:
                            file_comments += 1
                    
                    total_lines += file_total
                    comment_lines += file_comments
                    blank_lines += file_blanks
                    files_processed += 1
                    
                except Exception as e:
                    continue
    
    code_lines = total_lines - blank_lines - comment_lines
    
    # Calculate comment density
    non_blank_lines = total_lines - blank_lines
    if non_blank_lines > 0:
        comment_density = (comment_lines / non_blank_lines) * 100
    else:
        comment_density = 0.0
    
    print(f"Code lines: {code_lines}")
    print(f"Comment lines: {comment_lines}")
    print(f"Comment density: {comment_density:.2f}%")

if __name__ == "__main__":
    comment_density()
