def segiempat():
	luas = 5 * 5
	return luas
print "<!DOCTYPE html>"
print
print """<html>
	<head>
		<title>Luas Segiempat</title>
	</head>
	<body>
		<form>
			<table>
				<tr>
					<td rowspan='8'>
					<img src='../segiempat.png' width='160' height='160'>
					</td>
					<td>
						<p><b><font size='5'>Bangun Geometri</font></b></p>
					</td>
				</tr>
				
				<tr>
					<td>Nama Bangun</td>
					<td>:</td>
					<td>Segiempat</td>
				</tr>
				
				<tr>
					<td>Dimensi</td>
					<td>:</td>
					<td>2D</td>
				</tr>
				
				<tr>
					<td>Rumus Luas</td>
					<td>:</td>
					<td>Sisi x Sisi</td>
				</tr>
				
				<tr>
					<td>Sisi</td>
					<td>:</td>
					<td>
					5
					</td>
				</tr>
				
    
				<tr>
					<td>Luas</td>
					<td>:</td>
					<td>"""
print segiempat()
print"""</td>
				</tr>
			</table>
		</form>
	</body>
</html>"""