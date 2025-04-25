class Solution:
    def compress(self, chars: List[str]) -> int:
        write = 0
        anchor = 0
        
        for read in range(len(chars)):
            # Check if we are at the end of a group
            if read == len(chars) - 1 or chars[read] != chars[read + 1]:
                chars[write] = chars[anchor]  # Write the character
                write += 1
                count = read - anchor + 1
                if count > 1:
                    for digit in str(count):
                        chars[write] = digit
                        write += 1
                anchor = read + 1  # Move anchor to next group
        
        return write