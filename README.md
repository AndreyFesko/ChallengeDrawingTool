<table>
 <tr>
   <td>Name</td>
   <td>Stmts</td>
   <td>Miss</td>
   <td>Cover</td>
  </tr>
  <tr>
   <td>draw.py</td>
   <td>82</td>
   <td>10</td>
   <td>88</td>
   </tr>
  </table>

<h1>Drawing Tool</h1>
In a nutshell, the program reads the input.txt, executes a set of commands from the file, step by step, and produces output.txt.<br>
At this time, the functionality of the program is quite limited but this might change in the future.<br>
At the moment, the program should support the following set of commands:<br><br>
<p>C w h</p>
<p>L x1 y1 x2 y2 </p>
<p>R x1 y1 x2 y2 </p>
<p>B x y c </p><br>
Create <b>Canvas</b>: Should create a new canvas of width w and height h.<br>
Create <b>Line</b>: Should create a new line from (x1,y1) to (x2,y2). Currently only horizontal or
vertical lines are supported. Horizontal and vertical lines will be drawn using the 'x'
character.<br>
Create <b>Rectangle</b>: Should create a new rectangle, whose upper left corner is (x1,y1) and
lower right corner is (x2,y2). Horizontal and vertical lines will be drawn using the 'x'
character.<br>
<b>Bucket Fill</b>: Should fill the entire area connected to (x,y) with "colour" c. The behavior of this
is the same as that of the "bucket fill" tool in paint programs.
