# Rotating a matrix in either direction 

\[
\begin{pmatrix}
a & b & c \\
d & e & f \\
g & h & i \\
\end{pmatrix}
\]

To rotate this matrix 90 degrees clockwise, follow these steps:
1. Transpose the matrix. This means converting rows into columns. The transposed matrix will be:
   \[
   \begin{pmatrix}
   a & d & g \\
   b & e & h \\
   c & f & i \\
   \end{pmatrix}
   \]

2. Swap columns. Swap the first column with the last, and so on. The rotated matrix will be:
   \[
   \begin{pmatrix}
   g & d & a \\
   h & e & b \\
   i & f & c \\
   \end{pmatrix}
   \]

To rotate the matrix 90 degrees counterclockwise, follow these steps:
1. Transpose the matrix (same as in the clockwise rotation).

2. Swap rows instead of columns. Swap the first row with the last, and so on. The rotated matrix will be:
   \[
   \begin{pmatrix}
   c & f & i \\
   b & e & h \\
   a & d & g \\
   \end{pmatrix}
   \]