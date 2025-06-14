print(chr(65))
# Converts to its ASCII value i.e. A

print(ord("A"))
# Converts to its integer value i.e. 65

'''
+------+-------+------------------+     +------+-------+------------------+     +------+-------+------------------+     +------+-------+------------------+
| Dec  | Char  | Description      |     | Dec  | Char  | Description      |     | Dec  | Char  | Description      |     | Dec  | Char  | Description      |
+------+-------+------------------+     +------+-------+------------------+     +------+-------+------------------+     +------+-------+------------------+
|  0   |  NUL  | Null             |     |  32  |   ' ' | Space            |     |  64  |   @   | At sign          |     |  96  |   `   | Backtick         |
|  1   |  SOH  | Start of Header  |     |  33  |   !   | Exclamation mark |     |  65  |   A   | Uppercase A      |     |  97  |   a   | Lowercase a      |
|  2   |  STX  | Start of Text    |     |  34  |   "   | Double quote     |     |  66  |   B   | Uppercase B      |     |  98  |   b   | Lowercase b      |
|  3   |  ETX  | End of Text      |     |  35  |   #   | Number sign      |     |  67  |   C   | Uppercase C      |     |  99  |   c   | Lowercase c      |
|  4   |  EOT  | End of Transmiss.|     |  36  |   $   | Dollar sign      |     |  68  |   D   | Uppercase D      |     | 100  |   d   | Lowercase d      |
|  5   |  ENQ  | Enquiry          |     |  37  |   %   | Percent sign     |     |  69  |   E   | Uppercase E      |     | 101  |   e   | Lowercase e      |
|  6   |  ACK  | Acknowledge      |     |  38  |   &   | Ampersand        |     |  70  |   F   | Uppercase F      |     | 102  |   f   | Lowercase f      |
|  7   |  BEL  | Bell             |     |  39  |   '   | Single quote     |     |  71  |   G   | Uppercase G      |     | 103  |   g   | Lowercase g      |
|  8   |  BS   | Backspace        |     |  40  |   (   | Left paren       |     |  72  |   H   | Uppercase H      |     | 104  |   h   | Lowercase h      |
|  9   |  TAB  | Horizontal Tab   |     |  41  |   )   | Right paren      |     |  73  |   I   | Uppercase I      |     | 105  |   i   | Lowercase i      |
| 10   |  LF   | Line Feed        |     |  42  |   *   | Asterisk         |     |  74  |   J   | Uppercase J      |     | 106  |   j   | Lowercase j      |
| 11   |  VT   | Vertical Tab     |     |  43  |   +   | Plus             |     |  75  |   K   | Uppercase K      |     | 107  |   k   | Lowercase k      |
| 12   |  FF   | Form Feed        |     |  44  |   ,   | Comma            |     |  76  |   L   | Uppercase L      |     | 108  |   l   | Lowercase l      |
| 13   |  CR   | Carriage Return  |     |  45  |   -   | Hyphen           |     |  77  |   M   | Uppercase M      |     | 109  |   m   | Lowercase m      |
| 14   |  SO   | Shift Out        |     |  46  |   .   | Period           |     |  78  |   N   | Uppercase N      |     | 110  |   n   | Lowercase n      |
| 15   |  SI   | Shift In         |     |  47  |   /   | Slash            |     |  79  |   O   | Uppercase O      |     | 111  |   o   | Lowercase o      |
| 16   |  DLE  | Data Link Escape |     |  48  |   0   | Digit 0          |     |  80  |   P   | Uppercase P      |     | 112  |   p   | Lowercase p      |
| 17   |  DC1  | Device Control 1 |     |  49  |   1   | Digit 1          |     |  81  |   Q   | Uppercase Q      |     | 113  |   q   | Lowercase q      |
| 18   |  DC2  | Device Control 2 |     |  50  |   2   | Digit 2          |     |  82  |   R   | Uppercase R      |     | 114  |   r   | Lowercase r      |
| 19   |  DC3  | Device Control 3 |     |  51  |   3   | Digit 3          |     |  83  |   S   | Uppercase S      |     | 115  |   s   | Lowercase s      |
| 20   |  DC4  | Device Control 4 |     |  52  |   4   | Digit 4          |     |  84  |   T   | Uppercase T      |     | 116  |   t   | Lowercase t      |
| 21   |  NAK  | Neg. Acknowledge |     |  53  |   5   | Digit 5          |     |  85  |   U   | Uppercase U      |     | 117  |   u   | Lowercase u      |
| 22   |  SYN  | Synchronous Idle |     |  54  |   6   | Digit 6          |     |  86  |   V   | Uppercase V      |     | 118  |   v   | Lowercase v      |
| 23   |  ETB  | End of Block     |     |  55  |   7   | Digit 7          |     |  87  |   W   | Uppercase W      |     | 119  |   w   | Lowercase w      |
| 24   |  CAN  | Cancel           |     |  56  |   8   | Digit 8          |     |  88  |   X   | Uppercase X      |     | 120  |   x   | Lowercase x      |
| 25   |  EM   | End of Medium    |     |  57  |   9   | Digit 9          |     |  89  |   Y   | Uppercase Y      |     | 121  |   y   | Lowercase y      |
| 26   |  SUB  | Substitute       |     |  58  |   :   | Colon            |     |  90  |   Z   | Uppercase Z      |     | 122  |   z   | Lowercase z      |
| 27   |  ESC  | Escape           |     |  59  |   ;   | Semicolon        |     |  91  |   [   | Left bracket     |     | 123  |   {   | Left brace       |
| 28   |  FS   | File Separator   |     |  60  |   <   | Less than        |     |  92  |   \   | Backslash        |     | 124  |   |   | Vertical bar     |
| 29   |  GS   | Group Separator  |     |  61  |   =   | Equals           |     |  93  |   ]   | Right bracket    |     | 125  |   }   | Right brace      |
| 30   |  RS   | Record Separator |     |  62  |   >   | Greater than     |     |  94  |   ^   | Caret            |     | 126  |   ~   | Tilde            |
| 31   |  US   | Unit Separator   |     |  63  |   ?   | Question mark    |     |  95  |   _   | Underscore       |     | 127  |  DEL  | Delete           |
+------+-------+------------------+     +------+-------+------------------+     +------+-------+------------------+     +------+-------+------------------+

'''