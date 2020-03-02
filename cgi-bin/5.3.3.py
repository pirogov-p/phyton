#<a href=http://hse.ru>Высшая школа экономики</a>
f = open('C:\\Users\\ppirogov\\phyton\\cgi-bin\\ttest.html', 'w')

print("<html>")
print("<body>")
print("<table>")
for a in range(1,11):
    print("<tr>")
    for b in range(1,11):
        print("<td>" + "<a href=http://"+ str(a*b) +".ru>"+ str(a*b) +"</a>" + "</td>")
    print("</tr>")
print("</table>")
print("</body>")
print("</html>")

f.write("<html>"+ '\n')
f.write("<body>"+ '\n')
f.write("<table>"+ '\n')
for a in range(1,11):
    f.write("<tr>"+ '\n')
    for b in range(1,11):
        f.write("<td>" + "<a href=http://"+ str(a*b) +".ru>"+ str(a*b) +"</a>" + "</td>"+ '\n')
    f.write("</tr>"+ '\n')
f.write("</table>"+ '\n')
f.write("</body>"+ '\n')
f.write("</html>")


f.close()