# Flowchart

Start
  |
Call max_depth(root)
  |
Is root None?
  |
  |-- Yes --> Return 0
  |
  |-- No
        |
        v
Calculate depth of Yes branch
        |
        v
Calculate depth of No branch
        |
        v
Compare Yes branch depth and No branch depth
        |
        v
Choose the larger depth
        |
        v
Add 1 for the current node
        |
        v
Return maximum depth
        |
        v
End
