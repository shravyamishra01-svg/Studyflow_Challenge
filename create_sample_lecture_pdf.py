"""Script to generate a realistic sample lecture PDF for testing and demo purposes."""

from pypdf import PdfWriter
from pypdf.generic import (
    DictionaryObject,
    NameObject,
    ArrayObject,
    NumberObject,
    DecodedStreamObject,
    ByteStringObject,
    create_string_object
)
import io

def generate_lecture_pdf(output_path: str = "sample_lecture_bst.pdf"):
    # Generate a pure standard PDF with embedded fonts and text stream
    # Minimal standard PDF structure
    pdf_content = b"""%PDF-1.4
1 0 obj
<< /Type /Catalog /Pages 2 0 R >>
endobj
2 0 obj
<< /Type /Pages /Kids [3 0 R 4 0 R 5 0 R] /Count 3 >>
endobj
3 0 obj
<< /Type /Page /Parent 2 0 R /MediaBox [0 0 612 792] /Resources << /Font << /F1 6 0 R >> >> /Contents 7 0 R >>
endobj
4 0 obj
<< /Type /Page /Parent 2 0 R /MediaBox [0 0 612 792] /Resources << /Font << /F1 6 0 R >> >> /Contents 8 0 R >>
endobj
5 0 obj
<< /Type /Page /Parent 2 0 R /MediaBox [0 0 612 792] /Resources << /Font << /F1 6 0 R >> >> /Contents 9 0 R >>
endobj
6 0 obj
<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica >>
endobj
7 0 obj
<< /Length 340 >>
stream
BT
/F1 14 Tf
50 720 Td
(CS 201: Data Structures and Algorithms) Tj
/F1 12 Tf
0 -30 Td
(Lecture 8: Binary Search Trees and Search Complexities) Tj
0 -30 Td
(1. Overview of Tree Structures:) Tj
0 -20 Td
(A Binary Tree is a hierarchical structure where each node has at most two children.) Tj
0 -20 Td
(Left child and Right child. The top node is called the Root.) Tj
0 -20 Td
(A leaf node has zero children.) Tj
ET
endstream
endobj
8 0 obj
<< /Length 380 >>
stream
BT
/F1 12 Tf
50 720 Td
(2. Binary Search Tree (BST) Invariant Property:) Tj
0 -25 Td
(For any node X: all keys in X's left subtree are strictly less than X.key.) Tj
0 -20 Td
(All keys in X's right subtree are strictly greater than X.key.) Tj
0 -30 Td
(3. Search and Insertion Complexity:) Tj
0 -20 Td
(Average case search time: T(n) = O(log n)) Tj
0 -20 Td
(Worst case search time on degenerate unbalanced tree: T(n) = O(n)) Tj
0 -20 Td
(Height of balanced tree: h = floor(log2(n))) Tj
ET
endstream
endobj
9 0 obj
<< /Length 360 >>
stream
BT
/F1 12 Tf
50 720 Td
(4. Tree Traversals:) Tj
0 -25 Td
(Inorder Traversal: Left, Root, Right. Produces sorted sequence for BST.) Tj
0 -20 Td
(Preorder Traversal: Root, Left, Right. Used to serialize or clone tree.) Tj
0 -20 Td
(Postorder Traversal: Left, Right, Root. Used for deleting tree bottom-up.) Tj
0 -30 Td
(5. Exam Key Takeaways:) Tj
0 -20 Td
(Always verify BST property holds for all descendants, not just immediate children.) Tj
ET
endstream
endobj
xref
0 10
0000000000 65535 f 
0000000009 00000 n 
0000000058 00000 n 
0000000133 00000 n 
0000000257 00000 n 
0000000381 00000 n 
0000000505 00000 n 
0000000574 00000 n 
0000000966 00000 n 
0000001398 00000 n 
trailer
<< /Size 10 /Root 1 0 R >>
startxref
1810
%%EOF"""
    with open(output_path, "wb") as f:
        f.write(pdf_content)
    print(f"Sample lecture PDF generated at: {output_path}")

if __name__ == "__main__":
    generate_lecture_pdf()
