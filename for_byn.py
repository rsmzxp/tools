"""
re 

([A,T,C,G]{25})[A,T,C,G,]+\s*([A,T,C,G]{25})[A,T,C,G,]+\s*([0-9]*)

"$1_$2"=>"$3",
"""